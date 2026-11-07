# Expert Panel Synthesis: The Ideation System v3

_Moderator's synthesis of a two-round debate between seven panel lenses: Isenberg, Hormozi, Godin, Graham, Levels, Walling and Sanchez. Each lens is built from that person's public frameworks; none is the real person. Full papers are in `round1/` and rebuttals with structured votes are in `round2/`. Date: 2026-11-07._

## Verdict in one paragraph

Kill LEAP and every averaged score.

The panel voted 7–0 for a **problem-first, evidence-ladder system**:
1. Agents harvest real complaints, quoted word for word with links.
2. They count the distinct people who have the problem and attach money signals: what people pay today, ad CPC, competitors' prices.
3. A **binary kill gate written as code** removes ideas that fail.
4. A reviewer who did not generate the idea writes a short card.
5. The founder spends 15 minutes a week picking which ideas get tested.
6. A test only counts when real people put down **deposits**. The founder posts the offer by hand; agents never do.
7. Ideas that pass are run by hand first ("concierge"), with every task logged in an **ops ledger**. The ledger proves or disproves the "80–90% agent-operable" claim with logged minutes rather than estimates.
8. Results feed back: sources that produced payers get more weight.

## What all seven agreed on

| Topic | Consensus |
|---|---|
| Scoring | No 1–5 scores or averages. Rank by the **highest evidence rung reached**, and each rung needs a link or receipt. Of the seven, 5 voted for the ladder. Hormozi orders by paper LTV:CAC before the test and by cost per deposit after it. Levels orders by cheapest test before launch and by revenue per human hour after it. Both reject averages. |
| Sourcing | **Problem-first.** Store sourced, word-for-word complaints, not brainstormed ideas. Graham, Isenberg and Levels: "sourced rows only". |
| Who judges | **The generator never scores its own idea.** A blind reviewer writes the card. |
| Kill rule 1 (7/7) | **No existing spend.** Nobody pays a human, a tool or an incumbent for this today. |
| Kill rule 2 (7/7) | **Reality test fails.** Fewer than 3 deposits or payments within 14 days. The threshold is about 300 targeted visits, ฿5,000 of ad spend, or 10 hand-reached buyers. |
| Agent-operability | **Measured, not estimated.** It comes from an ops ledger kept during concierge delivery. Rework counts as human time. The target is an agent share of task minutes of at least 80% by month 6, and 2–5 founder hours or fewer per product per week. |
| Human checkpoints | A one-time "founder box" (who can I reach?). A weekly 15-minute pick with a founder-fit veto. The founder posts publicly and handles trust moments (refunds, disputes). Keep-or-kill at day 14/30. Retention check at day 90. |
| APIs to cut | **Perplexity (7/7):** it overlaps with Tavily plus Claude. **Google Trends (7/7):** the official API is still a gated alpha, and its values are relative, not absolute. Ahrefs, Semrush and SparkToro are cut as overkill. |

## Minimum API stack (vote tally and moderator check)

| # | Source | Votes | What it unlocks | Cost (checked 2026-11-07) |
|---|---|---|---|---|
| 1 | **Tavily** (key already held) | 7/7 | Web, news and forum search, including domain-filtered search of Pantip, ASEAN NOW and Reddit pages. Also page extraction. | Free 1,000 credits a month. Project plan $30/mo for 4,000 credits. [help.tavily.com](https://help.tavily.com/articles/8816424538-pricing) |
| 2 | **DataForSEO** | 7/7 | Google Ads search volume, CPC and competition for **Thailand (location 2764), US and UK**. CPC is the cheapest proxy for "money moving". | Pay as you go with a $50 minimum top-up and no monthly fee. Search volume about $0.06–0.09 per task of up to 1,000 keywords. [dataforseo.com/keyword-planner-api](https://dataforseo.com/keyword-planner-api) |
| 3 | **Stripe or Opn (Omise)** | 7/7 | Deposit and payment links (PromptPay, cards) for the reality test. It is the only signal the panel fully trusts. | Transaction fees only |
| 4 | **Apify** | 5/7 | Scrapers for Google Maps 1-star reviews, TikTok comments, app reviews, Pantip, and business-for-sale listings (BizBuySell, Flippa). | Free $5 credit a month. Starter about $29/mo; third-party sources disagree ($19–49). [costbench](https://costbench.com/software/web-scraping/apify/free-plan/) |
| 5 | **HN Algolia** | 5/7 | Search of HN stories and comments. | Free, no key. Verified working from this environment. |
| 6 | **Reddit** | 4/7 | Subreddit pain mining. | The free OAuth tier is non-commercial only, and new apps need manual approval. Commercial pricing is unclear: third-party sources range from $0.24 per 1,000 calls to $12k/yr or more. The public JSON returns **403** from this environment. **Use Tavily or Apify for Reddit content until the founder has approved OAuth.** |
| – | **CFPB complaint API** | 2/7 | Free, no-key US complaint **counts** by product, issue and company. | Free. Verified: the 2026 API returns counts and metadata but **not complaint text**. |
| – | **DBD open data** (Thailand) | 2/7 | Business registrations by sector, used for incumbents and acquisition targets. | Free. Whether an API exists is unverified; use the DBD DataWarehouse site. |
| – | **LINE OA** | 2/7 | The founder's owned channel for Thai tests and a contact list the founder owns. Godin's lens calls this the main asset. | Free tier, then paid plans (unverified) |

**Minimum viable stack: 3 paid sources plus the free ones.**
- Paid: Tavily (already held), DataForSEO and Apify.
- Free: HN Algolia, CFPB and DBD.
- Payments: Stripe/Opn for deposits.

The budget votes ranged from $50 to $80/mo (median $75). Realistic monthly spend is **$30–60**: about $30 for Tavily, $5–15 drawn from the DataForSEO deposit, and $0–29 for Apify.

## The pipeline (merged from the seven votes)

| # | Stage | Who | Output |
|---|---|---|---|
| 0 | **Founder box** (once a quarter) | Human, 30 min | Reachable groups and channels, skills, markets, budget, hard constraints |
| 1 | **Pain harvest** (nightly) | Script | `pains.jsonl`: one sourced, word-for-word complaint per row (url, date, platform, market, language) |
| 2 | **Cluster and count** | Agent | Problem clusters with distinct-sufferer counts across 2 or more platforms in 90 days |
| 3 | **Money signals** | Script plus agent | CPC and search volume; 3 or more incumbents or paid workarounds, each with price or revenue evidence |
| 4 | **Kill gate as code** | Script | Pass or kill with reasons (rules below) |
| 5 | **Blind card and panel review** | A different agent, then the expert lenses | An opportunity card (template below) |
| 6 | **Founder pick** (weekly) | Human, 15 min | Up to 5 cards picked, with a founder-fit veto |
| 7 | **Reality test** (72-hour build, 14-day window) | Agent builds, human posts | Landing page with a deposit link, plus Thai/English posts the founder sends personally |
| 8 | **Concierge plus ops ledger** | Human plus agents | Task log: actor (bot or human), minutes, rework |
| 9 | **Learn** | Script | Keep or kill at day 14/30, retention at day 90. Sources are re-weighted by which produced payers. |

**How automated the system is.**
- Stages 1–5 and 9 run fully on agents.
- Stage 7 is mostly agents: they build the page and draft the posts, and the human approves and posts.
- Human time is about 30–60 minutes a week plus trust moments. By time spent, that is roughly **85% agent-run**.

## The evidence ladder (replaces scores)

| Rung | Name | Receipt required |
|---|---|---|
| L0 | Hypothesis | None. It cannot go higher without a receipt. |
| L1 | Real pain | 15 or more distinct word-for-word sufferers on 2 or more platforms within 90 days, with links |
| L2 | Money moving | 3 or more incumbents, fixers or paid workarounds with price or revenue evidence, **or** CPC above a market threshold |
| L3 | Reached | The offer put in front of 100 or more of the target group, or 10 conversations held |
| L4 | Skin in the game | 3 or more deposits, pre-sales or paid pilots |
| L5 | Paying customers | 5 or more paying concierge customers, plus an ops ledger running |
| L6 | Durable | Retained at day 90, and agent share of 80% or more in the ledger |

**Ranking order.**
1. Highest rung reached.
2. Ties: the cheapest next test.
3. Then the churn type (recurring beats one-off).
4. Then platform risk.
5. Then payback in months.

No averages anywhere.

## Kill rules (the gate)

**Hard rules** (any one kills the idea):
1. **No existing spend.** Fewer than 3 named incumbents, fixers or paid workarounds. _(7/7)_
2. **Unreachable.** The founder can't put the offer in front of 100 or more of the target group within 14–30 days using channels they have or can buy cheaply. _(5/7)_
3. **A human or licence in every transaction,** or the owner must be on site. This would make 80–90% agent operation impossible. _(4/7)_
4. **The money math fails on paper.** Implied CAC is more than 1/3 of the churn-adjusted 12-month gross LTV, or payback is over 6 months to build or over 3 years to buy. _(4/7)_
5. **Platform hostage.** One platform controls both how customers are found and how the product is delivered, or the core data bans scraping and offers no API. _(3/7)_
6. **Free incumbent.** A bank app, LINE, the OS or a general AI assistant already solves it adequately. _(carried over from the v2 audit, plus Graham)_
7. **It needs fake trust,** such as bot posting, fake reviews, agent-run "community" or cold DM blasts. _(Godin)_

**After the reality test:** fewer than 3 deposits within 14 days kills the idea. One offer rewrite is allowed. _(7/7)_

**Soft flags** (shown on the card; they don't kill):
- A two-sided marketplace (Walling).
- A one-off need priced as a subscription (Walling).
- Thin pain, with fewer than 15 complaints (Isenberg).
- A crowded launch field, with 5 or more similar launches in the last 90 days (Sanchez).
- An MVP that would take more than 7 days (Levels).

## Measuring "80–90% agent-operable"

1. **Before the test (screen only).** The card breaks the business into acquisition, onboarding, delivery, support, billing, data ops and content. Each function gets an agent percentage and the human-only tasks are named. Rule 3 kills the idea if a human is needed in every transaction. The estimate is labelled *est.* and is never used for ranking.
2. **During concierge (the real measure).** Log every task in the ops ledger as {date, product, task, actor = bot or human, minutes, rework}. Rework done by a human counts as human time.
3. **Pass mark:**
   - An agent share of task minutes of 80% or more by month 6.
   - Founder time of 2–5 hours or fewer per product per week.
   - Referrals that do not fall as automation rises (Godin's guard against automation that destroys trust).

## Where the panel still disagrees (founder's call)

| Question | Positions |
|---|---|
| Tests per month | **8:** Levels and Hormozi (volume wins). **3–4:** Godin, Graham, Isenberg, Walling and Sanchez (depth and trust). **Default in the skill: 4.** |
| Paid ads in tests | Hormozi and Levels: buy targeted traffic (฿3–5k per test). Godin and Graham: founder-posted, hand-reached only. **Default: warm and community posts first, then a capped paid test if those reach fewer than 300 people.** |
| Build vs buy | Sanchez: always compare with buying an existing cash-flowing business and automating it. The skill adds an optional buy-vs-build section to the card. |
| B2B vs consumer | Walling: prefer B2B recurring and avoid one-off consumer rescues. Shown as a soft flag and a tie-breaker, not a kill. |
| Reddit API | Kept for its signal value. Use it via Tavily or Apify until commercial OAuth terms are clear. |

## What this means for the existing 1,050 ideas

They become **L0 hypotheses**. They are not thrown away; they seed the harvest queries. The new system re-earns every idea through receipts. The `/startup-ideas` skill implements this design (`.claude/skills/startup-ideas/`).
