# Round 1: Hormozi lens (Offer and Money)

_A lens on Hormozi's public frameworks, not his words._

## 1. My one-line thesis
Stop scoring ideas and start pricing them. An idea counts only once a stranger pays a deposit, so the system's job is to test 50 ideas cheaply, not to rank 1,050 opinions.

## 2. The system I'd build
Each stage produces a number someone paid or bid, not one a model guessed.

| Stage | What agents do | Output | Human checkpoint |
|---|---|---|---|
| **S0 Problem mining** | Mine complaints from Pantip, Reddit, CFPB, 1-star app reviews and TikTok comments. Look for **existing spend** on agents, fixers and lawyers. | Problem cards with quote, URL and current spend | None |
| **S1 Money check** | Pull keyword volume and **CPC** (TH and US), top-5 competitor prices and whether ads are running. | Demand sheet with volume, CPC, price floor and price ceiling | None |
| **S2 Offer draft** | Write a one-line Grand Slam Offer (outcome, speed, done-for-you, guarantee, price). Compute implied CAC (CPC ÷ est. 2–3% conversion), LTV and payback. | Offer card with the unit economics shown | **H1, 15 min/week:** the founder picks the 10 offers they'd be proud to sell |
| **S3 Smoke test** | Build a Thai and English landing page with a refundable PromptPay/Stripe **deposit** button and a LINE OA CTA. Spend ฿3,000–5,000 (~$100–150) on Meta/TikTok ads over 5–7 days, plus 50 cold DMs. | CTR, CPL, deposit count and cost per deposit | **H2:** the founder approves spend and claims |
| **S4 Concierge delivery** | Serve the first 5–10 payers by hand plus agents, logging every task. | Task ledger (see §4) | **H3:** the founder does any task an agent can't yet do |
| **S5 Learn** | Feed real CPC→CPL→deposit rates back into S1/S2 estimates, including from killed tests. | Calibrated conversion priors | Monthly review |

Target: 10 smoke tests a month for about $1,500 of ad spend, expecting 2 to survive.

## 3. Minimum APIs

| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| Tavily + Perplexity (held) | Research, competitor prices | Sunk | Keep |
| **DataForSEO** ($50 minimum top-up, no expiry) | Volume and **CPC for TH and US**, plus SERPs. CPC is the cheapest willingness-to-pay proxy there is. | $10–30 usage (est.) | **Keep: #1 priority** |
| Google Ads Keyword Planner (via the founder's ads account) | Free CPC cross-check | $0 (unverified) | Keep |
| **Ad spend (Meta/TikTok)** | The only real demand test | $1,000–1,500 | **Keep: the real "API"** |
| Stripe / Opn (PromptPay) | Deposits, the strongest signal | % per transaction (unverified) | Keep |
| Apify | TikTok comments (~$1.70/1k results), Pantip and Ad Library scraping | $0–39 (Starter tier unverified) | **Cut first** |
| Meta Ad Library (public site) | Who is spending on ads. The official API covers only political ads and EU/UK delivery, not Thai commercial ads. | $0 | Keep the site, skip the API |
| HN Algolia, Reddit JSON, CFPB, data.go.th / DBD open data | Problem mining and competitor registrations | $0 | Keep |
| LINE OA free tier | TH lead capture and support | $0 (unverified) | Keep |

Excluding ad spend: under $75/mo.

## 4. How to measure 80–90% agent-operable
Log it, don't estimate it. In S4 every task goes in a ledger: `function | task | agent/human | minutes | escalations`.
- **Metric:** founder minutes per $1,000 MRR per month. Target 30 or less by customer 20.
- **Agent-operable %** = 1 − (human minutes ÷ total task minutes).
- **Human-only today:** approving ad spend, sales calls above ~$500, refunds and disputes, regulated sign-offs (legal, medical, visa, finance), partner deals, and anything needing a Thai ID or branch visit.
- **Rule:** if closing needs a sales call, it isn't agent-operable, however automated delivery is.

## 5. Kill rules
1. **Nobody pays today.** No competitor charges and nobody pays fixers? Kill it. A missing market is not a gap.
2. **The CAC math fails on paper.** Implied CAC above one-third of 12-month gross LTV. That kills most ฿99–199/month B2C ideas on paid ads.
3. **The smoke test fails.** Under 3 deposits on ฿5,000 of spend, or cost per lead above 3× plan. One offer rewrite allowed.
4. **Payback over 3 months** without upfront cash.
5. **A human is required at sale or at risk** (regulated sign-off, mandatory sales call).

## 6. Ranking
Drop LEAP averages. Rank on one number: **verified cost per deposit relative to price**, from the S3 test. Before testing, order the queue by **implied LTV:CAC from real CPC and competitor prices**, as a gate, never averaged. Scoring stops being theatre when every input is a number someone paid or bid. The H1 founder-fit veto is the only judgement call.

## 7. What I expect the other panelists to get wrong
- **They'll make research better and leave it as research.** Calibrated LLM judges are still opinions. A $150 ad test beats $150 of research.
- **They'll over-value moats** at $0 MRR. Cash first.
- **They'll chase the agent-operable goal into cheap B2C.** The ฿99/month top-20 apps (Parents Check-in, Queue Tracker) look automatable, but paid CAC kills them.
- **They'll skip pricing:** who pays, how much, how fast, and at what CAC.

Sources: [DataForSEO](https://dataforseo.com/pricing), [Ad Library API](https://www.shortsintel.com/guides/meta-ad-library-api), [TikTok APIs](https://www.socialcrawl.dev/blog/best-tiktok-data-apis-2026)
