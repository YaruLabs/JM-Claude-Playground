---
name: startup-ideas
description: Find and validate startup opportunities that can be ~80-90% run by AI agents, for Thailand/Bangkok (Thai locals and expats) and US/UK markets. Mines real complaints (HN, Pantip, ASEAN NOW, Reddit, reviews), counts sufferers, attaches money signals (CPC, paid incumbents), applies a code-enforced kill gate, ranks by an evidence ladder (no averaged scores), runs a blind expert-panel review, and builds deposit-based reality tests plus an ops ledger. Use when the user asks for startup ideas, opportunity scanning, "what should I build", idea validation, or the weekly opportunity review. Modes are scan, review, test <id>, ledger, and status.
---

# Startup Ideas: opportunity scanner (ideation system v3)

This skill replaces the LEAP 1–5 scoring. The design comes from a seven-lens expert debate (`docs/expert-debate/SYNTHESIS.md`) and rests on four rules:
- **Problem first.** Work from sourced, word-for-word complaints, not brainstorms.
- **Receipts, not scores.** Ideas are ranked by the evidence they have earned.
- **The generator never judges its own idea.**
- **Only deposits from real people count as validation.**

CLI: `python3 .claude/skills/startup-ideas/scripts/oppo.py <cmd>`. It uses only the Python standard library. All state lives in `data/opportunities/`.

Before acting, read `references/rubrics.md` for the ladder, gate and agent-ops rules, and `references/agent-prompts.md` for the subagent prompts.

## Modes

The user may give a mode: `/startup-ideas scan`, `review`, `test <card_id>`, `ledger <card_id>`, or `status`. With no mode, run `status` and recommend the next step.

### `scan`: the full automated pass (stages 0–5)

0. **Set up.** Run `oppo.py init`, which also shows which API keys are present.
   - If `founder_box.json` has no real `channels`, stop and ask the founder to fill it in. It takes about 30 minutes once a quarter. Without it, the reach rule and the founder-fit veto are guesses.
   - Missing keys are fine: `hn` and `cfpb` need none. Note what each missing key costs in coverage, and suggest the founder add keys to the repo-root `.env`, which is gitignored. Never print key values.
1. **Harvest.** Run `oppo.py harvest`, optionally with `--market TH` or `--sources hn,tavily`.
   - Every row is a real complaint with a URL. Per-run call budgets in `scripts/sources.py` cap spend.
   - Reddit's public JSON is blocked from cloud IPs, so use Reddit OAuth keys or the Tavily `reddit.com` domain jobs instead.
2. **Cluster.** Run `oppo.py export`. Then launch the **clustering agent** (prompt A), one agent per 2–3 batch files, in parallel when there are several. It runs `import-clusters`, and the code counts distinct sufferers and platforms over 90 days.
3. **Signals.** Run `oppo.py signals --all` for DataForSEO search volume and CPC by market, plus CFPB counts for US finance clusters.
4. **Shortlist.** Take clusters with 15 or more sufferers on 2 or more platforms, or the top 15 if fewer qualify, and skip anything already carded.
5. **Card.** Launch the **scout agent** (prompt B), one agent per about 5 clusters, to draft cards. Then run `oppo.py gate`.
   - **5b. Blind panel.** For PASS and INCOMPLETE cards, launch the panel review (prompt C) in parallel: `hormozi-lens`, `levels-lens` and `godin-lens` by default. Add `isenberg-lens`, `graham-lens`, `walling-lens` and `sanchez-lens` if the user says "full panel". Run `oppo.py gate` again afterwards.
6. **Report.** Run `oppo.py rank`. It writes `data/opportunities/reports/opportunities-<date>.md`. Present the PASS cards to the founder and ask for **the weekly pick: up to 5 cards to test** (a 15-minute human checkpoint).

### `test <card_id>`: reality test (stage 7)
- Launch the **test-kit agent** (prompt D). It builds a landing page with a deposit button placeholder, plus Thai and English posts for the founder to send personally.
- The founder must do three things by hand: create the payment link (Stripe Payment Link, or Opn/PromptPay), post, and reply to DMs.
- Log daily: `oppo.py test log <id> --reached N --visits N --conversations N --deposits N --revenue N`.
- Check with `oppo.py test eval <id>`. Day 14 with fewer than 3 deposits means KILL; one offer rewrite is allowed.

### `ledger <card_id>`: prove the 80–90% claim (stage 8)
- During concierge delivery, log every task: `oppo.py ledger add <id> --task "…" --actor bot|human --minutes N [--rework]`.
- Then run `oppo.py ledger stats <id> --weeks 4`. The target is an agent share of 80% or more by month 6, and 2–5 founder hours or fewer per week.
- For each human task, propose the agent or automation that would take it over next.

### `review`: weekly (stage 9)
- Run prompt E.
- Re-weight harvest sources by which ones produced L3-or-higher cards: edit `references/queries.json`, then show the diff to the founder.

### `status`
- Run `oppo.py status`, then recommend the single next action.

## Human checkpoints (everything else runs on agents, about 85%)

1. The founder box, once a quarter.
2. The weekly pick of up to 5 cards, with a founder-fit veto.
3. Creating payment links, posting publicly as yourself, and replying to DMs.
4. Trust moments: refunds, disputes, regulated sign-off.
5. Keep or kill at day 14 and day 30, and the retention check at day 90.

## Guardrails
- **Never fabricate.** URLs, quotes, prices, revenue and deposit counts must be real. Estimates are labelled "est." and never move a rung.
- **The ladder and gate are computed in code.** Agents must not hand-edit `gate`, `evidence_rung` or `rung_receipts`.
- **No fake trust in tests.** No bot posting, fake testimonials, fake scarcity or bulk DMs. The founder posts personally.
- **Regulated ideas** (legal, medical, financial advice) need a licensed partner named on the card, or the idea is killed.
- **Thailand ideas** must fill `risks.founder_feasibility`: Foreign Business Act status, BOI or a Thai partner, or offshore SaaS. They also need PDPA notes for any personal data.
- **Respect platform terms.** Scrape only through APIs or actors that permit it, and don't collect personal data beyond the complaint text and a hashed author.

## API stack (minimum set from the panel vote)

| Need | Source | Key | Cost |
|---|---|---|---|
| Forum and web pain, Pantip and ASEAN NOW via domain filter, competitor research | Tavily | `TAVILY_API_KEY` | 1,000 free credits/mo; $30 for 4,000 |
| Search volume and CPC for TH, US and UK (the money signal) | DataForSEO | `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD` | $50 minimum top-up, about $0.06–0.09 per 1,000 keywords |
| Reviews, TikTok and Pantip scraping, business-for-sale listings | Apify (optional) | `APIFY_TOKEN` | $5/mo free; Starter about $29 |
| Developer and SMB pain | HN Algolia | none | free |
| US complaint volume | CFPB | none | free (counts only) |
| Reddit (optional; free tier is non-commercial) | Reddit OAuth | `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | free tier, approval required |
| Deposits | Stripe or Opn (Omise) | (founder's dashboard) | transaction fees |

Perplexity and Google Trends are deliberately not used. Perplexity overlaps Tavily, and the Google Trends API is a gated alpha that returns relative values only.
