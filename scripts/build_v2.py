#!/usr/bin/env python3
"""Build the four v2 idea CSVs from data/staging/.

Inputs (data/staging/):
  claude_legacy_{1,2,3}.json  + review_claude_{1,2,3}.json  -> data/ideas-claude.csv
  dir_legacy.json + review_dir_{1,2}.json + dir_226_250.json -> data/ideas-directories.csv
  th_*.json                                                  -> data/ideas-thailand.csv
  gl_*.json                                                  -> data/ideas-global-2026.csv

Legacy rows keep their id/title/category; scores, status and kill-check fields come
from the 2026-11 review; `fix` replaces corrupted or thin text fields.
Run: python3 scripts/build_v2.py && python3 scripts/validate_ideas.py
"""
import csv
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from schema_v2 import FIELDS, SCORE_FIELDS, score_total

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
TODAY = "2026-11-03"
FIX_KEYS = {"tagline", "problem", "solution", "target_audience", "business_model", "pricing"}


def load(name):
    with open(STAGING / name, encoding="utf-8") as f:
        return json.load(f)


def load_many(pattern):
    out = []
    for p in sorted(glob.glob(str(STAGING / pattern))):
        out.extend(json.load(open(p, encoding="utf-8")))
    return out


def modern_stack(s):
    s = s or ""
    s = re.sub(r"\bGPT-4o?\b|\bOpenAI\b", "LLM API (Claude/GPT)", s)
    s = re.sub(r"(LLM API \(Claude/GPT\))(\s*\+\s*LLM API \(Claude/GPT\))+", r"\1", s)
    return s or "Next.js + Supabase + LLM API (Claude/GPT)"


def fix_date(d):
    # v1 stamped many rows 2024-01-15 although they were written in early 2026.
    if not d or d.startswith("2024") or d.startswith("2025"):
        return "2026-02-01"
    return d


def legacy_to_v2(old, rev, kind):
    fix = {k: v for k, v in (rev.get("fix") or {}).items() if k in FIX_KEYS and v}
    g = lambda k: fix.get(k, old.get(k, "")) or ""
    row = {f: "" for f in FIELDS}
    row.update({
        "id": old["id"], "title": old["title"], "tagline": g("tagline"),
        "market": "US", "category": old.get("category", ""), "subcategory": old.get("subcategory", ""),
        "problem": g("problem"), "solution": g("solution"), "target_audience": g("target_audience"),
        "business_model": g("business_model"), "pricing": g("pricing"),
        "platform_distribution": old.get("platform", ""),
        "tam_estimate": f"{old.get('tam', '')} (v1 est.)".strip() if old.get("tam") else "",
        "tam_source": "v1 estimate (unverified)",
        "demand_evidence": "v1 search phrases (unverified): " + old.get("pain_points", "") if old.get("pain_points") else "",
        "language": "EN", "payment_rails": "Stripe",
        "mvp_features": old.get("mvp_features", ""),
        "created_date": fix_date(old.get("created_date", "")), "last_verified": TODAY,
    })
    row["target_segment"] = (row["target_audience"].split(";")[0].strip() or "US consumers")[:80]
    if kind == "DIR":
        if old.get("monetization") and "monetization" not in row["business_model"].lower():
            row["business_model"] = f"{row['business_model']} ({old['monetization']})" if row["business_model"] else old["monetization"]
        row["tech_stack"] = "Next.js + Supabase + Postgres full-text search + LLM API (Claude/GPT) for listing enrichment"
    else:
        row["tech_stack"] = modern_stack(old.get("tech_stack", ""))
    for k in ("status", "score_justification", "unique_data_capture", "commoditization_risk",
              "regulatory_notes", "competitors", "competitor_gap", "source_urls",
              "founder_feasibility", "review_notes"):
        v = rev.get(k, "")
        if isinstance(v, list):
            v = (" | " if k == "source_urls" else "; ").join(map(str, v))
        row[k] = str(v or "")
    for f in SCORE_FIELDS:
        row[f] = str(int(rev[f]))
    row["score_total"] = f"{score_total(row):.2f}"
    if rev.get("duplicate_of"):
        note = f"Duplicate of {rev['duplicate_of']}."
        if note not in row["review_notes"]:
            row["review_notes"] = (note + " " + row["review_notes"]).strip()
    return row


def normalize_new(r):
    row = {f: "" for f in FIELDS}
    for f in FIELDS:
        v = r.get(f, "")
        if isinstance(v, list):
            v = (" | " if f == "source_urls" else "; ").join(map(str, v))
        row[f] = str(v) if v is not None else ""
    for f in SCORE_FIELDS:
        row[f] = str(int(float(row[f])))
    row["score_total"] = f"{score_total(row):.2f}"
    row["created_date"] = row["created_date"] or TODAY
    row["last_verified"] = row["last_verified"] or TODAY
    return row


def write(rel, rows):
    rows.sort(key=lambda r: (r["id"].rsplit("-", 1)[0], int(r["id"].rsplit("-", 1)[1])))
    with open(ROOT / rel, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {rel}: {len(rows)} rows")


def build_legacy(legacy, reviews, kind):
    rev = {r["id"]: r for r in reviews}
    missing = [o["id"] for o in legacy if o["id"] not in rev]
    if missing:
        sys.exit(f"{kind}: no review for {len(missing)} ids, e.g. {missing[:5]}")
    return [legacy_to_v2(o, rev[o["id"]], kind) for o in legacy]


def main():
    claude = load_many("claude_legacy_[123].json")
    write("data/ideas-claude.csv", build_legacy(claude, load_many("review_claude_*.json"), "CLAUDE"))

    dirs = build_legacy(load("dir_legacy.json"), load_many("review_dir_*.json"), "DIR")
    dirs += [normalize_new(r) for r in load("dir_226_250.json")]
    write("data/ideas-directories.csv", dirs)

    write("data/ideas-thailand.csv", [normalize_new(r) for r in load_many("th_*.json")])
    write("data/ideas-global-2026.csv", [normalize_new(r) for r in load_many("gl_*.json")])


if __name__ == "__main__":
    main()
