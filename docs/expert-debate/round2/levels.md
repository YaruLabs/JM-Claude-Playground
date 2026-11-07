# Round 2: Levels lens (Automation and Shipping), rebuttal

_A lens on Pieter Levels' public approach. Not the person. No quotes._

## 1. Where I've been persuaded

- **Godin and Isenberg, on bot posting.** My S4 had a bot posting to Pantip, subreddits and LINE OpenChat. They're right: bots get banned there, and one screenshot in a Thai group burns trust. The new rule: the agent drafts and the founder posts as himself. That adds 10 minutes a test, which is fine.
- **Hormozi, on CPC.** I was already pulling DataForSEO for volume. CPC comes in the same call for free and is the cheapest willingness-to-pay proxy. His CAC check on paper (CAC above a third of 12-month LTV means kill) also catches the ฿99/month ideas before any ads run.
- **Walling, on churn.** "Revenue per human hour" alone flatters one-shot products that churn 100%. Revenue now counts only if it is still there at day 90, or I'm just measuring how fast the page converts.
- **Graham and Walling, on timing the operability gate.** Requiring 80–90% on day 1 picks shallow products. I'll measure in weeks 3–6 and apply the bar at month 3, not at idea stage.
- **Isenberg's rule** that no agent promotes an idea it generated goes straight into code.

## 2. Where I still disagree, and why

- **Sanchez: buying businesses.** That means ฿1–5M of cash, staff, premises and Foreign Business Act limits. A "2-week shadow run" needs a business you already own. It's a good research lens (1-star Maps clusters, DBD revenue filings), but as a track it's the opposite of solo with robots. Calling HN an anti-signal is half right: crowded is a kill rule, but not a reason to stop reading it.
- **Graham and Godin: 10 conversations before anything ships.** Run them in parallel with a live payment link, not as a gate before it. A page with a price takes 72 hours and asks the question better than an interview does. Godin's "not worth the Dip" can't be coded or measured. And 3 active ideas is too few when most tests fail.
- **Hormozi: $1,500/mo of ads plus 50 cold DMs.** Cold DMs are spam (Godin is right about that), and polishing a Grand Slam Offer before the first visit is backwards. Use ฿1,500–3,000 per test and polish only what sells.
- **Walling: B2B and recurring first.** Productized one-off reports at ฿290–990 with an SEO channel can be fully robotic. Keep his churn tag, but don't make B2B a gate. "5 founder calls per idea" doesn't scale across 8 tests a month.
- **Everyone's 7–10-stage tables.** We all converged on evidence ladders, which is good. But every extra stage is a place for agents to write more paragraphs. Ladders need receipts, not essays.

## 3. The one thing the final system must not lose

**Speed to a payment link, measured by a ledger that runs on cron.** One VPS, SQLite and Python on cron. Every test goes from a complaint with a URL to a live page with a price in 72 hours or less, and every live product writes an `ops_ledger` row (function, actor, minutes) automatically. If the system starts spending more founder hours on research and review than on launches, it has turned back into LEAP with more APIs. Ship, measure, kill, repeat.

```json
{"apis_ranked": ["Stripe/Opn", "DataForSEO", "Tavily", "HN Algolia", "Reddit API", "Apify"], "apis_cut": ["Perplexity", "Google Trends", "Ahrefs/Semrush/SparkToro", "Meta Ad Library API (use the public site instead)", "TikTok Research API"], "max_monthly_api_budget_usd": 75, "stages": ["Nightly complaint mining (sourced rows only)", "Cluster and demand facts (volume, CPC, paid competitor)", "Kill gate as code", "Founder pick and fit veto", "72-hour smoke test with payment link, posted by the founder", "14-day measurement", "Concierge MVP with ops ledger", "Learn: re-weight sources by payers and day-90 retention"], "ranking_method": "Before launch, order the queue by cheapest and fastest test after it passes the binary kill gate; after launch, rank by day-90 retained revenue per logged human hour.", "agent_operable_metric": "From the auto-logged ops_ledger in weeks 3-6, the bot share of task minutes (rework counts as human time), with a pass at under 2 founder hours per week per product by month 3.", "kill_rules": ["No payment within 14 days after 300 or more targeted visits", "MVP can't ship in 7 days on a boring stack", "Every transaction needs a human or a licence", "No channel the founder owns or can buy cheaply, and the CAC math fails on paper (CAC above a third of 12-month LTV)", "Hostage platform: the core data bans scraping and has no API, or one platform can switch the product off"], "human_checkpoints": ["Weekly 15-min founder pick and fit veto", "Approve price and copy, and post the launch himself", "Hold the trust moments: first replies, refunds, disputes", "Confirm keep or kill at day 14 and month 3"], "ideas_tested_per_month": 8}
```
