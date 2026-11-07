#!/usr/bin/env python3
"""oppo: the startup-ideas opportunity pipeline (stdlib only).

Stages (see ../SKILL.md):
  init | harvest | export | import-clusters | signals | search | card | gate | rank
  | report | test | ledger | status | sources

All state lives in data/opportunities/ as git-friendly JSON/JSONL:
  founder_box.json, pains.jsonl, clusters.json, cards/<id>.json,
  tests.jsonl, ledger.jsonl, reports/, work/, .cache/ (gitignored)
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sources as S  # noqa: E402

SKILL = Path(__file__).resolve().parents[1]
DATA = S.DATA
CARDS, WORK, REPORTS = DATA / "cards", DATA / "work", DATA / "reports"
PAINS, CLUSTERS = DATA / "pains.jsonl", DATA / "clusters.json"
TESTS, LEDGER, BOX = DATA / "tests.jsonl", DATA / "ledger.jsonl", DATA / "founder_box.json"
TODAY = dt.date.today().isoformat()

# Evidence-ladder and gate thresholds (docs/expert-debate/SYNTHESIS.md)
MIN_SUFFERERS, MIN_PLATFORMS, WINDOW_DAYS = 15, 2, 90
MIN_INCUMBENTS = 3
CPC_MONEY = {"TH": 0.30, "US": 1.50, "UK": 1.20, "GLOBAL": 1.00}   # USD; L2 alt. receipt
MIN_REACH, MIN_DEPOSITS, TEST_DAYS = 100, 3, 14
MIN_AGENT_SHARE_EST, PASS_AGENT_SHARE = 0.75, 0.80
RUNGS = ["L0 Hypothesis", "L1 Real pain", "L2 Money moving", "L3 Reached",
         "L4 Skin in the game", "L5 Paying customers", "L6 Durable"]


# ------------------------------------------------------------------ io helpers

def jl_read(p):
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def jl_append(p, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def jread(p, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def jwrite(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(p):
    """Path for display: repo-relative when inside the repo."""
    try:
        return p.relative_to(S.ROOT)
    except ValueError:
        return p


def h(s, n=12):
    return hashlib.sha256(s.encode()).hexdigest()[:n]


# ---------------------------------------------------------------------- stages

def cmd_init(a):
    for d in (CARDS, WORK, REPORTS):
        d.mkdir(parents=True, exist_ok=True)
    gi = DATA / ".gitignore"
    if not gi.exists():
        gi.write_text(".cache/\nwork/\n")
    if not BOX.exists():
        jwrite(BOX, jread(SKILL / "references" / "founder_box.example.json", {}))
        print(f"created {rel(BOX)} — the founder fills this in once (stage 0)")
    print("ready:", rel(DATA))
    cmd_sources(a)


def cmd_sources(_a):
    av = S.available()
    for k, v in av.items():
        print(f"  {k:<11} {'ok' if v else 'missing key'}")


def cmd_harvest(a):
    """Stage 1: collect verbatim, sourced complaints into pains.jsonl."""
    q = jread(Path(a.queries) if a.queries else SKILL / "references" / "queries.json", {})
    av = S.available()
    seen = {r["url"] + "|" + r["text"][:80] for r in jl_read(PAINS)}
    new, skipped = [], set()
    markets = [m.upper() for m in a.market.split(",")] if a.market != "ALL" else None
    wanted = set(a.sources.split(",")) if a.sources else None
    for job in q.get("jobs", []):
        src, mk = job["source"], job.get("market", "GLOBAL")
        if job.get("enabled") is False or (wanted and src not in wanted) or (markets and mk not in markets):
            continue
        if not av.get(src):
            skipped.add(src)
            continue
        try:
            for term in job["queries"]:
                if src == "hn":
                    rows = S.hn(term, days=a.days, limit=a.limit)
                elif src == "tavily":
                    rows = S.tavily(term, domains=job.get("domains"), limit=min(a.limit, 20))
                elif src == "reddit":
                    rows = [r for sub in job["subreddits"] for r in S.reddit(term, sub, limit=a.limit)]
                elif src == "apify":
                    rows = S.apify(job["actor"], job["input"], platform=job.get("platform"))
                else:
                    continue
                for r in rows:
                    k = r["url"] + "|" + r["text"][:80]
                    if k in seen or not r.get("url"):
                        continue
                    seen.add(k)
                    r.update({"id": "P" + h(k), "market": mk, "segment": job.get("segment", ""),
                              "query": term, "author_hash": h(r.pop("author") or r["url"], 10),
                              "fetched": TODAY})
                    new.append(r)
        except (S.BudgetExceeded, RuntimeError) as e:
            print(f"  ! {src}: {e}", file=sys.stderr)
    jl_append(PAINS, new)
    print(f"harvested {len(new)} new pains (total {len(seen)})")
    if skipped:
        print("skipped (no key):", ", ".join(sorted(skipped)))


def cmd_export(a):
    """Stage 2a: write unclustered pains in batches for the clustering agent."""
    clustered = {pid for c in jread(CLUSTERS, []) for pid in c["pain_ids"]}
    todo = [p for p in jl_read(PAINS) if p["id"] not in clustered]
    WORK.mkdir(parents=True, exist_ok=True)
    files = []
    for i in range(0, len(todo), a.batch):
        f = WORK / f"pains_batch_{i // a.batch + 1:03d}.jsonl"
        f.write_text("")  # overwrite previous batch file of the same name
        jl_append(f, [{k: p[k] for k in ("id", "platform", "market", "lang", "text", "url")}
                      for p in todo[i:i + a.batch]])
        files.append(f)
    print(f"{len(todo)} unclustered pains -> {len(files)} batch file(s) in {rel(WORK)}")
    for f in files:
        print("  ", rel(f))


def cluster_stats(c, pains):
    rows = [pains[i] for i in c["pain_ids"] if i in pains]
    cutoff = time.time() - WINDOW_DAYS * 86400
    recent = [r for r in rows if not r.get("created") or r["created"] >= cutoff]
    return {"pains": len(rows), "sufferers": len({r["author_hash"] for r in recent}),
            "platforms": sorted({r["platform"] for r in recent}),
            "top_quotes": [{"text": r["text"][:280], "url": r["url"]} for r in rows[:5]]}


def cmd_import_clusters(a):
    """Stage 2b: merge the clustering agent's output and recount sufferers."""
    incoming = json.loads(Path(a.file).read_text(encoding="utf-8"))
    pains = {p["id"]: p for p in jl_read(PAINS)}
    cl = {c["id"]: c for c in jread(CLUSTERS, [])}
    for c in incoming:
        cid = c.get("id") or "C" + h(c["label"], 8)
        old = cl.get(cid, {})
        merged = sorted(set(old.get("pain_ids", [])) | {i for i in c["pain_ids"] if i in pains})
        cl[cid] = {**old, **{k: v for k, v in c.items() if k != "pain_ids"}, "id": cid, "pain_ids": merged}
        cl[cid]["stats"] = cluster_stats(cl[cid], pains)
    jwrite(CLUSTERS, sorted(cl.values(), key=lambda c: -c["stats"]["sufferers"]))
    print(f"{len(incoming)} clusters imported; {len(cl)} total")


def cmd_signals(a):
    """Stage 3: search volume + CPC (DataForSEO) and CFPB counts per cluster."""
    cls = jread(CLUSTERS, [])
    targets = [c for c in cls if a.all or c["id"] in a.ids]
    by_market = {}
    for c in targets:
        by_market.setdefault(c.get("market", "TH").upper(), []).append(c)
    for mk, group in by_market.items():
        kws = sorted({k for c in group for k in c.get("keywords", [])})
        if kws and S.available()["dataforseo"] and mk in S.LOCATIONS:
            try:
                vol = {r["keyword"]: r for r in S.keyword_volume(kws, mk)}
                for c in group:
                    rows = [vol[k] for k in c.get("keywords", []) if k in vol]
                    c.setdefault("signals", {})["keywords"] = rows
                    c["signals"]["max_cpc_usd"] = max([r["cpc_usd"] or 0 for r in rows] or [0])
                    c["signals"]["total_volume"] = sum(r["search_volume"] or 0 for r in rows)
            except (S.BudgetExceeded, RuntimeError) as e:
                print(f"  ! dataforseo: {e}", file=sys.stderr)
        if mk == "US":
            for c in group:
                for term in c.get("cfpb_terms", []):
                    c.setdefault("signals", {}).setdefault("cfpb", []).append(S.cfpb_count(term))
    jwrite(CLUSTERS, cls)
    print(f"signals updated for {len(targets)} cluster(s)")


def cmd_search(a):
    """Budgeted, cached research search for agents (competitor pricing, regulation)."""
    print(json.dumps(S.search(a.query, domains=a.domains.split(",") if a.domains else None, limit=a.limit),
                     ensure_ascii=False, indent=2))


def cmd_card(a):
    """Stage 5: create a card skeleton prefilled with cluster facts."""
    cl = {c["id"]: c for c in jread(CLUSTERS, [])}
    for cid in a.ids:
        c = cl[cid]
        p = CARDS / f"{cid}.json"
        if p.exists() and not a.force:
            print("exists:", rel(p))
            continue
        card = jread(SKILL / "references" / "card.template.json", {})
        card.update({"id": cid, "cluster_id": cid, "title": c.get("label", cid), "market": c.get("market", ""),
                     "created": TODAY, "updated": TODAY})
        card["pain"].update({k: c["stats"][k] for k in ("sufferers", "platforms", "top_quotes")})
        card["pain"]["window_days"] = WINDOW_DAYS
        sig = c.get("signals", {})
        card["money"].update({"cpc_usd": sig.get("max_cpc_usd"), "search_volume": sig.get("total_volume")})
        jwrite(p, card)
        print("created:", rel(p))


# ----------------------------------------------------------------- gate + rank

def valid_incumbents(card):
    return [i for i in card["money"].get("incumbents", [])
            if i.get("name") and i.get("evidence_url", "").startswith("http") and (i.get("price") or i.get("revenue"))]


def money_math(m):
    """Returns (ltv12, cac, payback_months, missing)."""
    need = ["price", "gross_margin", "months_retained_est", "cac_est"]
    missing = [k for k in need if m.get(k) in (None, "")]
    if missing:
        return None, None, None, missing
    price, margin, months, cac = (float(m[k]) for k in need)
    if m.get("billing") == "one_off":
        # one purchase: LTV is one sale's gross profit; payback is immediate if it covers CAC, else never
        ltv12 = price * margin
        payback = 0.0 if ltv12 >= cac else 99.0
    else:
        ltv12 = price * margin * min(12.0, months)
        payback = cac / max(price * margin, 1e-9)
    return round(ltv12, 2), cac, round(payback, 1), []


def gate(card):
    kills, flags, missing = [], [], []
    m, r, ops, reach = card["money"], card["risks"], card["agent_ops"], card["reach"]
    if len(valid_incumbents(card)) < MIN_INCUMBENTS:
        kills.append(f"no existing spend: {len(valid_incumbents(card))}/{MIN_INCUMBENTS} incumbents with price/revenue evidence")
    est_reach = sum(int(ch.get("est_reach") or 0) for ch in reach.get("channels", []) if ch.get("url"))
    if not reach.get("channels"):
        missing.append("reach.channels")
    elif est_reach < MIN_REACH:
        kills.append(f"unreachable: {est_reach} reachable via named channels < {MIN_REACH}")
    if ops.get("human_required_per_transaction") or float(ops.get("onsite_hours_week") or 0) > 5:
        kills.append("human or licence needed in every transaction / on-site presence")
    share = ops.get("est_agent_share")
    if share in (None, ""):
        missing.append("agent_ops.est_agent_share")
    elif float(share) < MIN_AGENT_SHARE_EST:
        kills.append(f"below automation target: est. agent share {float(share):.0%} < {MIN_AGENT_SHARE_EST:.0%}")
    ltv12, cac, payback, miss = money_math(m)
    if miss:
        missing += [f"money.{k}" for k in miss]
    else:
        card["money"].update({"ltv12": ltv12, "payback_months": payback})
        if cac > ltv12 / 3:
            kills.append(f"money math: CAC {cac:g} > LTV12/3 ({ltv12 / 3:.0f})")
        if payback > 6:
            kills.append(f"payback {payback} months > 6")
    for k, msg in (("platform_hostage", "platform hostage"), ("free_alternative_adequate", "free incumbent/AI already solves it"),
                   ("requires_fake_trust", "needs fake trust (bots, fake reviews, DM blasts)")):
        if r.get(k) is True:
            kills.append(msg)
        elif r.get(k) is None:
            missing.append(f"risks.{k}")
    if r.get("two_sided_marketplace"):
        flags.append("two-sided marketplace")
    if r.get("one_shot_priced_as_subscription"):
        flags.append("one-shot need priced as subscription")
    if int(card["pain"].get("sufferers") or 0) < MIN_SUFFERERS:
        flags.append(f"thin pain: {card['pain'].get('sufferers', 0)} sufferers < {MIN_SUFFERERS}")
    if int(r.get("crowded_launches_90d") or 0) >= 5:
        flags.append("crowded launch field")
    if float(card["build"].get("mvp_days_est") or 0) > 7:
        flags.append("MVP > 7 days")
    tests = test_totals(card["id"])
    if tests and tests["days"] >= TEST_DAYS and tests["deposits"] < MIN_DEPOSITS:
        kills.append(f"reality test failed: {tests['deposits']} deposits in {tests['days']} days")
    result = "KILL" if kills else ("INCOMPLETE" if missing else "PASS")
    card["gate"] = {"result": result, "kills": kills, "flags": flags, "missing": missing, "checked": TODAY}
    return card


def test_totals(cid):
    rows = [t for t in jl_read(TESTS) if t["card_id"] == cid]
    if not rows:
        return None
    days = (dt.date.fromisoformat(max(t["date"] for t in rows)) - dt.date.fromisoformat(min(t["date"] for t in rows))).days + 1
    tot = {k: sum(float(t.get(k) or 0) for t in rows)
           for k in ("reached", "visits", "spend", "conversations", "deposits", "revenue", "paying_customers")}
    tot.update(days=days, retained_day90=any(t.get("retained_day90") for t in rows))
    return tot


def ledger_stats(product, weeks=None):
    rows = [r for r in jl_read(LEDGER) if r["product"] == product]
    if weeks:
        cutoff = (dt.date.today() - dt.timedelta(weeks=weeks)).isoformat()
        rows = [r for r in rows if r["date"] >= cutoff]
    bot = sum(r["minutes"] for r in rows if r["actor"] == "bot" and not r.get("rework"))
    human = sum(r["minutes"] for r in rows if r["actor"] == "human" or r.get("rework"))
    days = 1
    if rows:
        first, last = min(r["date"] for r in rows), max(r["date"] for r in rows)
        days = (dt.date.fromisoformat(last) - dt.date.fromisoformat(first)).days + 1
    weeks_span = max(days / 7, 1)
    return {"entries": len(rows), "agent_share": round(bot / (bot + human), 3) if bot + human else None,
            "founder_hours_per_week": round(human / 60 / weeks_span, 2)}


def rung(card):
    """Highest evidence rung with receipts. Never uses model-judged scores."""
    receipts, level = {}, 0
    p, m = card["pain"], card["money"]
    if int(p.get("sufferers") or 0) >= MIN_SUFFERERS and len(p.get("platforms") or []) >= MIN_PLATFORMS:
        level, receipts["L1"] = 1, f"{p['sufferers']} sufferers on {len(p['platforms'])} platforms"
    else:
        return 0, receipts
    inc = valid_incumbents(card)
    cpc_ok = (m.get("cpc_usd") or 0) >= CPC_MONEY.get((card.get("market") or "GLOBAL").upper(), 1.0)
    if len(inc) >= MIN_INCUMBENTS or cpc_ok:
        level, receipts["L2"] = 2, f"{len(inc)} paid incumbents" + (f"; CPC ${m['cpc_usd']}" if cpc_ok else "")
    else:
        return level, receipts
    t = test_totals(card["id"]) or {}
    if (t.get("reached") or 0) >= MIN_REACH or (t.get("conversations") or 0) >= 10:
        level, receipts["L3"] = 3, f"reached {t.get('reached', 0):g}, {t.get('conversations', 0):g} conversations"
    else:
        return level, receipts
    if (t.get("deposits") or 0) >= MIN_DEPOSITS:
        level, receipts["L4"] = 4, f"{t['deposits']:g} deposits"
    else:
        return level, receipts
    ls = ledger_stats(card["id"])
    if (t.get("paying_customers") or 0) >= 5 and ls["entries"]:
        level, receipts["L5"] = 5, f"{t['paying_customers']:g} paying; ledger {ls['entries']} entries"
    else:
        return level, receipts
    if t.get("retained_day90") and (ls["agent_share"] or 0) >= PASS_AGENT_SHARE:
        level, receipts["L6"] = 6, f"retained day 90; agent share {ls['agent_share']:.0%}"
    return level, receipts


def load_cards():
    return [jread(p, {}) for p in sorted(CARDS.glob("*.json"))]


def cmd_gate(a):
    clusters = {c["id"]: c for c in jread(CLUSTERS, [])}
    for card in load_cards():
        if a.ids and card["id"] not in a.ids:
            continue
        # Pain counts always come from code-computed cluster stats, never from hand edits.
        cl = clusters.get(card.get("cluster_id"))
        if cl:
            card["pain"].update({k: cl["stats"][k] for k in ("sufferers", "platforms")})
        card = gate(card)
        card["evidence_rung"], card["rung_receipts"] = rung(card)
        card["updated"] = TODAY
        jwrite(CARDS / f"{card['id']}.json", card)
        g = card["gate"]
        print(f"{card['id']:<12} {g['result']:<10} {RUNGS[card['evidence_rung']]:<20} "
              + "; ".join(g["kills"] or [f"missing: {', '.join(g['missing'])}" if g["missing"] else ""]))


def sort_key(card):
    churn = {"subscription": 0, "usage": 0, "one_off": 1}.get(card["money"].get("billing"), 1)
    return (-card.get("evidence_rung", 0), {"PASS": 0, "INCOMPLETE": 1, "KILL": 2}[card["gate"]["result"]],
            float(card["build"].get("next_test_cost_thb") or 1e9), churn,
            1 if card["risks"].get("platform_hostage") else 0, float(card["money"].get("payback_months") or 99))


def cmd_rank(a):
    cards = [c for c in load_cards() if c.get("gate")]
    cards.sort(key=sort_key)
    lines = [f"# Opportunities — {TODAY}", "",
             "_Ranked by evidence rung (receipts only), then gate result, cheapest next test, churn type, "
             "platform risk, payback. No averaged scores. Generated by `oppo.py rank`._", "",
             "| # | Card | Title | Mkt | Rung | Gate | Agent est. | Next test ฿ | Flags / kills |",
             "|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(cards, 1):
        g = c["gate"]
        note = "; ".join(g["kills"] or g["flags"] or ([f"missing {len(g['missing'])} fields"] if g["missing"] else []))
        share = c["agent_ops"].get("est_agent_share")
        lines.append(f"| {i} | {c['id']} | {c['title']} | {c.get('market', '')} | {RUNGS[c.get('evidence_rung', 0)]} | "
                     f"{g['result']} | {f'{float(share):.0%}' if share not in (None, '') else '?'} | "
                     f"{c['build'].get('next_test_cost_thb') or '?'} | {note.replace('|', '/')} |")
    passed = [c for c in cards if c["gate"]["result"] == "PASS"]
    lines += ["", f"**{len(passed)} PASS** of {len(cards)} gated cards. The founder picks up to 5 PASS cards for a "
              f"reality test this week (`oppo.py test start <id>`)."]
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / f"opportunities-{TODAY}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:4 + min(len(cards), a.top) + 2]))
    print("\nwrote", rel(out))


def cmd_test(a):
    if a.action == "log":
        row = {"card_id": a.id, "date": a.date or TODAY, "channel": a.channel or "", "reached": a.reached,
               "visits": a.visits, "spend": a.spend, "conversations": a.conversations, "deposits": a.deposits,
               "revenue": a.revenue, "paying_customers": a.paying, "retained_day90": a.retained, "notes": a.notes or ""}
        jl_append(TESTS, [row])
        print("logged:", row)
    t = test_totals(a.id)
    if not t:
        print("no test rows yet for", a.id)
        return
    verdict = ("KEEP (passed reality test)" if t["deposits"] >= MIN_DEPOSITS else
               f"KILL (fewer than {MIN_DEPOSITS} deposits in {t['days']} days; one offer rewrite allowed)"
               if t["days"] >= TEST_DAYS else f"RUNNING (day {t['days']} of {TEST_DAYS})")
    print(json.dumps(t, indent=2), "\nverdict:", verdict)


def cmd_ledger(a):
    if a.action == "add":
        row = {"product": a.product, "date": a.date or TODAY, "task": a.task, "actor": a.actor,
               "minutes": a.minutes, "rework": a.rework}
        jl_append(LEDGER, [row])
        print("logged:", row)
    s = ledger_stats(a.product, weeks=a.weeks)
    ok = (s["agent_share"] or 0) >= PASS_AGENT_SHARE
    print(json.dumps(s, indent=2), f"\n{'PASS' if ok else 'BELOW'} 80% agent-operable target")


def cmd_status(_a):
    cards = load_cards()
    res = {}
    for c in cards:
        k = c.get("gate", {}).get("result", "UNGATED")
        res[k] = res.get(k, 0) + 1
    print(f"pains: {len(jl_read(PAINS))}  clusters: {len(jread(CLUSTERS, []))}  cards: {len(cards)} {res}  "
          f"test rows: {len(jl_read(TESTS))}  ledger rows: {len(jl_read(LEDGER))}")
    real = [c for c in jread(BOX, {}).get("channels", []) if c.get("url") and not c.get("name", "").startswith("Example")]
    print("founder box:", f"{len(real)} real channel(s)" if real else "NOT FILLED — founder must complete stage 0")
    cmd_sources(_a)


def main():
    ap = argparse.ArgumentParser(prog="oppo", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("init")
    sp.add_parser("sources")
    sp.add_parser("status")
    p = sp.add_parser("harvest")
    p.add_argument("--sources", help="comma list: hn,tavily,reddit,apify (default: all with keys)")
    p.add_argument("--market", default="ALL", help="TH,US,UK,GLOBAL or ALL")
    p.add_argument("--days", type=int, default=90)
    p.add_argument("--limit", type=int, default=30)
    p.add_argument("--queries", help="alternate queries.json")
    p = sp.add_parser("export")
    p.add_argument("--batch", type=int, default=200)
    p = sp.add_parser("import-clusters")
    p.add_argument("file")
    p = sp.add_parser("signals")
    p.add_argument("ids", nargs="*")
    p.add_argument("--all", action="store_true")
    p = sp.add_parser("search")
    p.add_argument("query")
    p.add_argument("--domains")
    p.add_argument("--limit", type=int, default=8)
    p = sp.add_parser("card")
    p.add_argument("ids", nargs="+")
    p.add_argument("--force", action="store_true")
    p = sp.add_parser("gate")
    p.add_argument("ids", nargs="*")
    p = sp.add_parser("rank")
    p.add_argument("--top", type=int, default=25)
    p = sp.add_parser("test")
    p.add_argument("action", choices=["log", "eval"])
    p.add_argument("id")
    for f in ("reached", "visits", "spend", "conversations", "deposits", "revenue", "paying"):
        p.add_argument(f"--{f}", type=float, default=0)
    p.add_argument("--retained", action="store_true")
    p.add_argument("--channel")
    p.add_argument("--date")
    p.add_argument("--notes")
    p = sp.add_parser("ledger")
    p.add_argument("action", choices=["add", "stats"])
    p.add_argument("product")
    p.add_argument("--task", default="")
    p.add_argument("--actor", choices=["bot", "human"], default="bot")
    p.add_argument("--minutes", type=float, default=0)
    p.add_argument("--rework", action="store_true")
    p.add_argument("--date")
    p.add_argument("--weeks", type=int)
    a = ap.parse_args()
    {"init": cmd_init, "sources": cmd_sources, "status": cmd_status, "harvest": cmd_harvest, "export": cmd_export,
     "import-clusters": cmd_import_clusters, "signals": cmd_signals, "search": cmd_search, "card": cmd_card,
     "gate": cmd_gate, "rank": cmd_rank, "test": cmd_test, "ledger": cmd_ledger}[a.cmd](a)


if __name__ == "__main__":
    main()
