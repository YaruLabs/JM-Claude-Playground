#!/usr/bin/env python3
"""Validate every v2 ideas CSV in data/. Exit code 1 on any error.

Usage: python3 scripts/validate_ideas.py [files...]
"""
import csv
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from schema_v2 import (FIELDS, SCORE_FIELDS, MARKETS, STATUSES, LANGUAGES, MIN_PROBLEM,
                       MIN_SOLUTION, MIN_URLS, GATE_TOTAL, GATE_EASE, score_total)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ["data/ideas-claude.csv", "data/ideas-directories.csv",
           "data/ideas-thailand.csv", "data/ideas-global-2026.csv"]
EXPECTED_ROWS = {"data/ideas-thailand.csv": 100, "data/ideas-global-2026.csv": 100}
# Legacy sets were not originally sourced; their URL/length rules apply only to non-SKIP rows we re-verified.
NEW_SETS = {"data/ideas-thailand.csv", "data/ideas-global-2026.csv"}


def urls(s):
    return [u for u in re.split(r"\s*\|\s*", s or "") if u.startswith("http")]


def check_file(rel, errors, warnings, all_titles):
    path = ROOT / rel
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            errors.append(f"{rel}: header mismatch: missing={set(FIELDS)-set(reader.fieldnames or [])} extra={set(reader.fieldnames or [])-set(FIELDS)}")
            return
        rows = list(reader)
    if rel in EXPECTED_ROWS and len(rows) != EXPECTED_ROWS[rel]:
        errors.append(f"{rel}: expected {EXPECTED_ROWS[rel]} rows, got {len(rows)}")
    seen = set()
    strict = rel in NEW_SETS
    for r in rows:
        i = r["id"]
        if i in seen:
            errors.append(f"{rel}:{i} duplicate id")
        seen.add(i)
        for k in ("title", "problem", "solution", "status", "market"):
            if not r[k].strip():
                errors.append(f"{rel}:{i} empty {k}")
        if r["status"] not in STATUSES:
            errors.append(f"{rel}:{i} bad status {r['status']}")
        if r["market"] not in MARKETS:
            errors.append(f"{rel}:{i} bad market {r['market']}")
        if r["language"] and r["language"] not in LANGUAGES:
            errors.append(f"{rel}:{i} bad language {r['language']}")
        try:
            vals = [int(r[f]) for f in SCORE_FIELDS]
            if any(v < 1 or v > 5 for v in vals):
                errors.append(f"{rel}:{i} score out of range {vals}")
            elif abs(float(r["score_total"]) - score_total(r)) > 0.011:
                errors.append(f"{rel}:{i} score_total {r['score_total']} != {score_total(r)}")
        except ValueError:
            errors.append(f"{rel}:{i} non-integer score")
            continue
        if r["status"] == "RECOMMENDED" and (score_total(r) < GATE_TOTAL or int(r["leap_e"]) < GATE_EASE):
            errors.append(f"{rel}:{i} RECOMMENDED but fails gates ({score_total(r)}, E{r['leap_e']})")
        if r["status"] == "SKIP":
            continue
        msgs = errors if strict else warnings
        if len(r["problem"]) < MIN_PROBLEM:
            msgs.append(f"{rel}:{i} problem {len(r['problem'])} chars < {MIN_PROBLEM}")
        if len(r["solution"]) < MIN_SOLUTION:
            msgs.append(f"{rel}:{i} solution {len(r['solution'])} chars < {MIN_SOLUTION}")
        # New ideas need >=3 sources; re-reviewed legacy ideas need >=1 supporting the verdict (IDEA-SPEC-v2 review mode).
        min_urls = MIN_URLS if strict else 1
        if len(urls(r["source_urls"])) < min_urls:
            msgs.append(f"{rel}:{i} only {len(urls(r['source_urls']))} source URLs")
        if strict:
            for k in ("competitors", "founder_feasibility", "unique_data_capture", "pricing", "tam_source"):
                if not r[k].strip():
                    errors.append(f"{rel}:{i} empty {k}")
            if r["market"] == "TH" and not re.search(r"฿|THB|baht", r["pricing"], re.I):
                errors.append(f"{rel}:{i} TH idea without THB pricing")
        all_titles.append((rel, i, r["title"]))


def fuzzy_dupes(all_titles, errors):
    norm = [(rel, i, re.sub(r"[^a-z0-9 ]", "", t.lower())) for rel, i, t in all_titles]
    for a in range(len(norm)):
        for b in range(a + 1, len(norm)):
            if difflib.SequenceMatcher(None, norm[a][2], norm[b][2]).ratio() > 0.9:
                errors.append(f"near-duplicate titles (non-SKIP): {norm[a][0]}:{norm[a][1]} '{all_titles[a][2]}' ~ {norm[b][0]}:{norm[b][1]} '{all_titles[b][2]}'")


def main():
    files = sys.argv[1:] or [f for f in DEFAULT if (ROOT / f).exists()]
    errors, warnings, titles = [], [], []
    for rel in files:
        check_file(rel, errors, warnings, titles)
    fuzzy_dupes(titles, errors)
    for w in warnings[:40]:
        print("WARN ", w)
    if len(warnings) > 40:
        print(f"WARN  ... {len(warnings) - 40} more warnings")
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(files)} files, {len(titles)} active ideas, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
