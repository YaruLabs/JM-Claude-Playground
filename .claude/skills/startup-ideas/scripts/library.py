#!/usr/bin/env python3
"""Build the public idea library that the quiz site and `/startup-ideas quiz` match against.

  select   pick library candidates from the v2 CSVs -> data/library/in/chunk_NN.json
  check    validate an enrichment file against references/library-spec.md
  build    merge data/library/enriched/*.json + CSV facts -> web/data/ideas.json

Stdlib only.
"""
import csv
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LIB = ROOT / "data" / "library"
OUT = ROOT / "web" / "data" / "ideas.json"
CSVS = ["data/ideas-thailand.csv", "data/ideas-global-2026.csv", "data/ideas-claude.csv", "data/ideas-directories.csv"]
NEW = {"data/ideas-thailand.csv", "data/ideas-global-2026.csv"}
MIN_LEGACY_CAUTION = 3.33
CHUNK = 25

AGENT_FIELDS = ["id", "title", "tagline", "market", "target_segment", "category", "subcategory", "problem", "solution",
                "target_audience", "business_model", "pricing", "platform_distribution", "competitors", "competitor_gap",
                "demand_evidence", "unique_data_capture", "commoditization_risk", "regulatory_notes",
                "founder_feasibility", "language", "mvp_features", "review_notes", "score_justification"]

COPY = {"name": 40, "one_liner": 140, "problem": 400, "why_it_works": 600, "human_part": 260,
        "content_angle": 300, "price_hint": 60, "watch_out": 300}
LISTS3 = {"agent_plan": 160, "first_steps": 150}
ENUMS = {
    "markets": ({"TH_LOCAL", "TH_EXPAT", "US", "UK", "GLOBAL"}, 1, 5),
    "interests": ({"money", "health", "property", "food", "education", "travel_expat", "ecommerce", "legal_paperwork",
                   "pets", "mobility", "creator", "local_services", "work_careers", "family_care"}, 1, 3),
    "channels": ({"content", "seo", "community", "outbound", "marketplace"}, 1, 2),
    "goals": ({"side_income", "replace_salary", "scale", "sellable_asset"}, 1, 2),
    "backgrounds": ({"tech", "marketing_content", "sales_ops", "finance_legal", "health", "property", "hospitality",
                     "education", "any"}, 1, 3),
}
SINGLES = {"customer": {"consumer", "small_business", "professional"}, "tech": {"none", "some", "builder"},
           "speed": {"weeks", "months"}, "thai_language": {"required", "helpful", "no"}}
BANNED = ["game-changer", "game changer", "insane", "mind-blowing", "revolutionize", "synergy", "disrupt", "get rich"]


def candidates():
    rows = []
    for rel in CSVS:
        with open(ROOT / rel, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                ok = r["status"] == "RECOMMENDED" or (
                    r["status"] == "CAUTION" and (rel in NEW or float(r["score_total"]) >= MIN_LEGACY_CAUTION))
                if ok:
                    r["_set"] = "new" if rel in NEW else "legacy"
                    rows.append(r)
    return rows


def cmd_select():
    rows = candidates()
    d = LIB / "in"
    d.mkdir(parents=True, exist_ok=True)
    for old in d.glob("chunk_*.json"):
        old.unlink()
    for i in range(0, len(rows), CHUNK):
        part = [{k: r[k] for k in AGENT_FIELDS} for r in rows[i:i + CHUNK]]
        (d / f"chunk_{i // CHUNK + 1:02d}.json").write_text(json.dumps(part, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} candidates -> {len(list(d.glob('chunk_*.json')))} chunks in {d.relative_to(ROOT)}")


def check_entry(e):
    errs, i = [], e.get("id", "?")
    for k, n in COPY.items():
        v = e.get(k)
        if not isinstance(v, str) or not v.strip():
            errs.append(f"{i}: missing {k}")
        elif len(v) > n:
            errs.append(f"{i}: {k} is {len(v)} chars (max {n})")
    for k, n in LISTS3.items():
        v = e.get(k)
        if not (isinstance(v, list) and len(v) == 3 and all(isinstance(x, str) and 0 < len(x) <= n for x in v)):
            errs.append(f"{i}: {k} must be 3 strings of at most {n} chars")
    t = e.get("tags")
    if not isinstance(t, dict):
        return errs + [f"{i}: missing tags"]
    for k, (allowed, lo, hi) in ENUMS.items():
        v = t.get(k)
        if not (isinstance(v, list) and lo <= len(v) <= hi and set(v) <= allowed):
            errs.append(f"{i}: tags.{k} invalid: {v}")
    for k, allowed in SINGLES.items():
        if t.get(k) not in allowed:
            errs.append(f"{i}: tags.{k} invalid: {t.get(k)}")
    for k in ("budget", "hours"):
        if t.get(k) not in (1, 2, 3, 4):
            errs.append(f"{i}: tags.{k} must be 1-4")
    if not (isinstance(t.get("agent_share"), int) and 40 <= t["agent_share"] <= 95):
        errs.append(f"{i}: tags.agent_share must be an integer 40-95")
    for k in ("portable", "local_presence"):
        if not isinstance(t.get(k), bool):
            errs.append(f"{i}: tags.{k} must be true/false")
    text = json.dumps(e, ensure_ascii=False).lower()
    errs += [f"{i}: banned phrase '{b}'" for b in BANNED if b in text]
    return errs


def cmd_check(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    errs = [m for e in data for m in check_entry(e)]
    ids = [e.get("id") for e in data]
    if len(ids) != len(set(ids)):
        errs.append("duplicate ids")
    src = LIB / "in" / Path(path).name.replace("enriched_", "chunk_")
    if src.exists():
        want = [r["id"] for r in json.loads(src.read_text(encoding="utf-8"))]
        if ids != want:
            errs.append(f"ids do not match {src.name}: missing {sorted(set(want) - set(ids))[:5]} extra {sorted(set(ids) - set(want))[:5]}")
    print("\n".join(errs[:60]) if errs else "ok")
    print(f"{len(data)} entries, {len(errs)} errors")
    return 1 if errs else 0


def cmd_build():
    facts = {r["id"]: r for r in candidates()}
    cur = json.loads((LIB / "curation.json").read_text(encoding="utf-8")) if (LIB / "curation.json").exists() else {}
    drop, overrides = cur.get("drop", {}), cur.get("tag_overrides", {})
    out, errs = [], []
    for p in sorted(glob.glob(str(LIB / "enriched" / "enriched_*.json"))):
        for e in json.loads(Path(p).read_text(encoding="utf-8")):
            r = facts.get(e.get("id"))
            if not r or e["id"] in drop:
                continue
            e["tags"].update(overrides.get(e["id"], {}))
            bad = check_entry(e)
            if bad:
                errs += bad
                continue
            urls = [u for u in (x.strip() for x in r["source_urls"].split("|")) if u.startswith("http")]
            out.append({**{k: e[k] for k in ["id", *COPY, *LISTS3, "tags"]},
                        "competitors": r["competitors"], "sources": urls[:4],
                        "quality": {"status": r["status"], "score": float(r["score_total"]), "set": r["_set"],
                                    "verified": r["last_verified"]}})
    missing = sorted(set(facts) - {o["id"] for o in out} - set(drop))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out)} ideas; {len(drop)} held back by curation; {len(missing)} candidates not yet enriched; {len(errs)} entries rejected")
    for m in errs[:20]:
        print("  !", m)
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"select": cmd_select, "build": cmd_build}.get(cmd, lambda: cmd_check(sys.argv[2]) if cmd == "check" else print(__doc__))() or 0)
