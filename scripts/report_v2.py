#!/usr/bin/env python3
"""Generate docs/AUDIT-2026-11.md and docs/IDEAS-SUMMARY-2026-11.md from the v2 CSVs.

Run after build_v2.py:  python3 scripts/report_v2.py
"""
import collections
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETS = [
    ("Thailand (TH)", "data/ideas-thailand.csv"),
    ("Global 2026 (GL)", "data/ideas-global-2026.csv"),
    ("Legacy AI ideas (CLAUDE)", "data/ideas-claude.csv"),
    ("Legacy directories (DIR)", "data/ideas-directories.csv"),
]
ORDER = ["RECOMMENDED", "CAUTION", "OUTDATED", "SKIP"]


def rows(rel):
    with open(ROOT / rel, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def esc(s, n=None):
    s = " ".join((s or "").split()).replace("|", "/")
    return s if n is None or len(s) <= n else s[: n - 1] + "…"


def status_table(data):
    out = ["| Set | Ideas | " + " | ".join(ORDER) + " |", "|---|---|" + "---|" * len(ORDER)]
    for name, rs in data:
        c = collections.Counter(r["status"] for r in rs)
        out.append(f"| {name} | {len(rs)} | " + " | ".join(str(c.get(s, 0)) for s in ORDER) + " |")
    return "\n".join(out)


def top(rs, n=20):
    act = [r for r in rs if r["status"] in ("RECOMMENDED", "CAUTION")]
    act.sort(key=lambda r: (-float(r["score_total"]), -int(r["wtp_w"]), -int(r["moat_m"])))
    out = ["| # | ID | Title | Score | L/E/A/P/M/W | Status | Pricing |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(act[:n], 1):
        sc = "/".join(r[k] for k in ("leap_l", "leap_e", "leap_a", "leap_p", "moat_m", "wtp_w"))
        out.append(f"| {i} | {r['id']} | {esc(r['title'])} | {r['score_total']} | {sc} | {r['status']} | {esc(r['pricing'], 70)} |")
    return "\n".join(out)


def verdict_table(rs, statuses):
    out = ["| ID | Title | Status | Score | Reason |", "|---|---|---|---|---|"]
    for r in rs:
        if r["status"] in statuses:
            out.append(f"| {r['id']} | {esc(r['title'])} | {r['status']} | {r['score_total']} | {esc(r['review_notes'], 220)} |")
    return "\n".join(out)


def categories(rs):
    c = collections.Counter(r["category"] for r in rs)
    return ", ".join(f"{k} ({v})" for k, v in c.most_common())


def segments(rs):
    c = collections.Counter(r["target_segment"] for r in rs)
    return ", ".join(f"{k} ({v})" for k, v in c.most_common(8))


AUDIT_HEAD = """# Audit 2026-11: what v1 got wrong and what we changed

_Generated in part by `scripts/report_v2.py`. Last verified 2026-11-03._

## 1. Defects found in v1

| # | Problem | What we did |
|---|---|---|
| 1 | **Corrupted CSV rows.** About 115 of the 350 rows in `ideas-claude.csv` had shifted columns, e.g. `pricing` holding the target audience (CLAUDE-001) or `problem` holding several merged fields (CLAUDE-013, 023-030, 131-199). | Every row was re-reviewed. A `fix` object rewrote the corrupted `problem`, `solution`, `target_audience`, `pricing` and `tagline` fields. The corrupted file is in `data/archive/`. |
| 2 | **Three incompatible score scales.** The doc used 1-5, `ideas-claude.csv` used totals out of 400, and the DIR files scored each pillar 1-100. | Framework v2 has six integer scores from 1 to 5: LEAP plus **M**oat and **W**illingness to pay. `score_total` is their mean. All 850 ideas were re-scored by judgement, not by rescaling. |
| 3 | **Generic `unique_data_capture`.** It was keyword-filled: 108 blank, and about 60 read "Rate/pricing comparison data". | Rewritten per idea to name a specific dataset, and scored as M. |
| 4 | **Directory batches never merged or deduplicated.** 175 ideas sat in loose `.py` files, DIR-226 to 250 were never saved, and duplicate clusters went unmarked. | Everything is in one `ideas-directories.csv` (300 ids). DIR-226 to 250 were regenerated with sources. Duplicates are marked `SKIP` with "Duplicate of …" and keep their ids. |
| 5 | **No evidence per idea.** TAMs and statistics were asserted without sources (e.g. "80% of hospital bills have errors"). | New ideas need at least 3 real URLs, at least 2 named competitors and "est." on unverified numbers. Legacy ideas need at least 1 URL supporting the verdict. v1 TAMs are kept but labelled `v1 estimate (unverified)`. |
| 6 | **Stale stack and dates.** 348 rows said "GPT-4", and 218 rows were dated 2024-01-15 although written in 2026. | The tech stack is now model-agnostic ("LLM API (Claude/GPT)"). The bad dates became 2026-02-01, and `last_verified` is 2026-11-03. |
| 7 | **Outdated research sources.** GummySearch (closed Nov 2025), MicroAcquire (now Acquire.com), Codeium (now Windsurf), the X API (too expensive), Google CSE "search entire web" (unavailable for new engines). | `data/sources.json` v2 retires or renames them and adds 22 Thailand sources and 10 free government-data sources. |
| 8 | **No 2026 reality check.** Many ideas are now done by general AI assistants or free incumbents, rely on rules that changed, or carry unauthorized-practice-of-law or medical-advice risk. | Every idea has `commoditization_risk`, `regulatory_notes` and `founder_feasibility`, plus a status of RECOMMENDED, CAUTION, OUTDATED or SKIP. |
| 9 | **Repo clutter.** A corrupted CSV, loose batch files at the root, misnamed files and three overlapping data-capture scripts. | Moved to `data/archive/`. A single `scripts/validate_ideas.py` replaces the ad-hoc scripts. |
| 10 | **South-East Asia ideas tagged as US.** CLAUDE-201 to 250 are SG/MY/ID/PH/VN ideas with local pricing. | Tagged `market=GLOBAL` with local wallet payment rails. Titles like "Cloud KitchenSEA" were split. |

## 2. Regulatory and market changes that drove verdicts

These facts were checked against official or primary pages during the audit unless marked _(from memory, not re-verified)_.

- **FTC "click-to-cancel" rule:** vacated by the 8th Circuit in July 2025 _(from memory, not re-verified)_. This kills the regulatory tailwind behind CLAUDE-007 Gym Cancel.
- **FTC CARS rule (auto dealers):** vacated by the 5th Circuit on 27 Jan 2025. **CFPB BNPL interpretive rule:** withdrawn in 2025. **FTC junk-fees rule:** in force since 12 May 2025, but only for live-event tickets and short-term lodging.
- **US home energy credits:** IRS 25D (residential clean energy) and 25C ended for property placed in service after 31 Dec 2025. The 30C home EV-charger credit covers property placed in service through 30 Jun 2026. This changes the solar, geothermal and charger ideas.
- **Student loans:** the SAVE plan ended. The Repayment Assistance Plan starts 1 Jul 2026.
- **ACA:** the enhanced premium tax credits expired after 2025, so the 400% FPL subsidy cliff is back. From tax year 2026, repayment of excess advance credits is no longer capped.
- **Medicaid:** work requirements from 1 Jan 2027. Some lawfully present immigrants lost eligibility on 1 Oct 2026.
- **California DROP:** a free, one-click data-broker deletion platform, live since 1 Jan 2026. Brokers must process requests from 1 Aug 2026. This makes paid data-broker removal (CLAUDE-026) OUTDATED for Californians.
- **ChatGPT Health:** launched 7 Jan 2026. Consumer lab-result and symptom explainers are now commoditized.
- **AI, GPT, MCP and prompt directories:** owned by There's An AI For That, Futurepedia, the ChatGPT app directory, the official MCP Registry, Glama and Smithery. All OUTDATED.
- **Thailand:**
  - Visa-exempt stays drop from 60 to 30 days from 15 Sep 2026, with at most two land-border entries a year (TAT and Thai embassies).
  - From 31 Aug 2026, DTV applicants must apply in their country of citizenship or legal residence and supply a criminal-record certificate. Embassy and agent sources agree, but "residence" and when the record is required are not consistently defined.
  - Foreign-income remittance tax (Por.161/2566) applies from 2024. Relief for income remitted the following year was _not_ confirmed as enacted.
- **UK and EU:**
  - Renters' Rights Act: Royal Assent 27 Oct 2025.
  - Making Tax Digital for income tax: over £50k from Apr 2026, over £30k from Apr 2027, over £20k from Apr 2028.
  - Private Parking Code of Practice: laid 20 Oct 2026, not yet in force.
  - EU €3 duty on low-value parcels from 1 Jul 2026.
  - EUDR: 30 Dec 2026 for large and medium operators, 30 Jun 2027 for micro and small.
  - Poland KSeF timing for micro-businesses and the EU AI Act Article 4 amendment date: sources conflict.

## 3. Research limits (be aware)

- All agents shared one web-search budget, which ran out early. The three TH/GL generation batches that finished first got about 30-45 searches each. The audit agents ran almost none, and verified by opening about 700 competitor, regulator and news pages directly instead.
- Some legacy `source_urls` are homepages of well-known incumbents that were not opened in this session.
- Pantip, Reddit and Facebook-group threads were rarely reachable (Reddit blocks fetches), so demand evidence leans on government data, the CFPB complaint database, news and forums such as ASEAN NOW, BiggerPockets and MSE.
- **URL spot-check:** a random 10% of new-set URLs (80 of 801) were requested. 71 returned 200, 6 returned 403 (bot protection on live sites), 2 timed out (the bangkokbank.com PDF host returned 503) and 1 was a 404. That is 96% reachable. The 404 (an FTC page in GL-041) was replaced.
- All TAMs in the new sets are bottom-up estimates marked "(est.)".

## 4. Status counts after the audit

{status}

## 5. Duplicate clusters resolved

- **Directories:**
  - Climbing gym: DIR-113 kept; 136 and 165 SKIP.
  - Land surveyor: DIR-107 kept; 299 SKIP.
  - Expert witness: DIR-108 kept; 192 SKIP.
  - Flight school: DIR-115 kept; 278 SKIP.
  - EV charging: DIR-128 kept; 285 SKIP.
  - Sign-language interpreters: DIR-110 kept; 195 SKIP.
  - Translators: DIR-109 kept; 145 SKIP.
  - Adult sports: DIR-119 kept; 139 SKIP.
  - Hot springs: DIR-180 kept; 212 SKIP.
  - Dark-sky sites: DIR-181 kept; 211 SKIP.
  - Estate sales: DIR-177 kept; 222 SKIP.
  - Farriers: DIR-158 kept; 291 SKIP.
  - Landlord reviews: DIR-001 kept; 043 SKIP.
  - Studios: DIR-095 kept; 096 SKIP.
  - Ceramics: DIR-117 kept; 143 SKIP.
  - The DIR-230 regeneration was a duplicate of DIR-146, so it was replaced with Cost Segregation Firms.
- **CLAUDE ideas:** 50+ duplicates of each other or of IDEA, DIR and CLAUDE ideas elsewhere in the corpus. See the SKIP rows below; each names its original.
- **New sets:** before merging, 7 new ideas that duplicated another new idea were replaced: TH-093, TH-095, TH-097, GL-066, GL-071, GL-074 and GL-075. Ideas that adapt an existing legacy concept for Thailand or the UK are kept, and their `review_notes` say so.

## 6. Per-idea verdicts: legacy CLAUDE ideas (OUTDATED and SKIP)

{claude_bad}

## 7. Per-idea verdicts: legacy directories (OUTDATED and SKIP)

{dir_bad}

## 8. Legacy ideas still worth building (RECOMMENDED)

{legacy_good}
"""

SUMMARY_HEAD = """# Ideas Summary 2026-11

_Generated by `scripts/report_v2.py` from the v2 CSVs. Framework: `docs/LEAP-framework.md` (v2 box) and `docs/IDEA-SPEC-v2.md`. Audit: `docs/AUDIT-2026-11.md`._

## What changed since v1

- **200 new, sourced ideas:**
  - `data/ideas-thailand.csv`: 100 ideas marketable to Thai locals and to expats in Bangkok and Thailand, with THB pricing, LINE/TikTok/Pantip distribution, PromptPay rails and Foreign Business Act notes.
  - `data/ideas-global-2026.csv`: 100 AI-first solo-founder ideas, 70 US and 30 UK/EU.
- **850 legacy ideas re-audited.** About two-thirds of the v1 consumer AI ideas are now OUTDATED or SKIP, because general AI assistants, free incumbents or rule changes cover them.
- **One schema** (`scripts/schema_v2.py`) for all four files, enforced by `scripts/validate_ideas.py`.
- **Six 1-5 scores: L, E, A, P, M and W.** RECOMMENDED requires a mean of at least 3.5, E of at least 3, and commoditization risk below High.
- **Lessons applied to the new sets:**
  - Go after paperwork that has deadlines and money attached: denials, deposits, refunds, compliance filings and appeals.
  - Prefer markets where buyers already pay (high W), and products whose data compounds (high M). Examples: dispute outcomes by reason code, real price paid by clinic, juristic-office response times by building.
  - Avoid thin chat wrappers, AI or prompt directories, and anything a bank app or OS ships free.

## Status counts

{status}

## Thailand: top 20

{th_top}

**Categories:** {th_cat}

**Target segments:** {th_seg}

## Global 2026: top 20

{gl_top}

**Categories:** {gl_cat}

**Markets:** {gl_mkt}

## Legacy CLAUDE: best surviving ideas

{cl_top}

## Legacy directories: best surviving ideas

{dir_top}

## How to use these files

- Filter on `status=RECOMMENDED` and sort by `score_total`, then by `wtp_w`.
- Before building, re-check the items in `review_notes`. Many name the single open question that would kill the idea, such as an unconfirmed regulation date.
- For Thailand ideas, read `founder_feasibility` first. Most run legally as offshore SaaS. Marketplaces that take commissions locally need a Thai company (51% Thai or BOI).
"""


def main():
    data = [(name, rows(rel)) for name, rel in SETS]
    th, gl, cl, di = (rs for _, rs in data)
    status = status_table(data)
    legacy_good = verdict_table(cl + di, {"RECOMMENDED"})
    (ROOT / "docs/AUDIT-2026-11.md").write_text(AUDIT_HEAD.format(
        status=status,
        claude_bad=verdict_table(cl, {"OUTDATED", "SKIP"}),
        dir_bad=verdict_table(di, {"OUTDATED", "SKIP"}),
        legacy_good=legacy_good), encoding="utf-8")
    mk = collections.Counter(r["market"] for r in gl)
    (ROOT / "docs/IDEAS-SUMMARY-2026-11.md").write_text(SUMMARY_HEAD.format(
        status=status, th_top=top(th), th_cat=categories(th), th_seg=segments(th),
        gl_top=top(gl), gl_cat=categories(gl), gl_mkt=", ".join(f"{k} ({v})" for k, v in mk.items()),
        cl_top=top(cl, 10), dir_top=top(di, 10)), encoding="utf-8")
    print("wrote docs/AUDIT-2026-11.md, docs/IDEAS-SUMMARY-2026-11.md")


if __name__ == "__main__":
    main()
