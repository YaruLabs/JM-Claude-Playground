# Round 1: Isenberg lens (Opportunity Scout and Distribution)

_A lens on Greg Isenberg's public frameworks, not the person. No quotes are his._

## 1. My one-line thesis
Rank **audiences with a repeated pain that someone already pays a human to fix**, not ideas. A waitlist number beats any 1–5 score.

## 2. The system I'd build
A holding-company loop: 3–5 bets a month, 14 days each, then double down on winners.

| Stage | Who | Output |
|---|---|---|
| 0. Channel inventory | **Human, once** | The crowds Yaru can reach free today: Bangkok expat FB groups, Thai TikTok, LINE OA, X followers. |
| 1. Pain harvest | Agents | "Pain cards" (verbatim quote, URL, date, platform) from r/Thailand, r/Bangkok, r/expats, Pantip (Sinthorn, Chan rooms), TikTok comments, 1–2★ incumbent app reviews and Google autocomplete ("วิธี…", "how to … thailand"). |
| 2. Cluster | Agents | Embedding dedup into problem dossiers. Promotion needs **≥15 independent cards on ≥2 platforms in 90 days**. |
| 3. Wedge check | Agents | Who already pays a human for this (Fastwork/Upwork gigs, agencies, FB ads), plus Thai and English search volume and a named first-100 path. |
| 4. Pick | **Human, 15 min/week** | Up to 5 dossiers. Founder fit is applied here. |
| 5. 72-hour smoke test | Agents build, **human posts** | A landing page, LINE OA waitlist and PromptPay/Stripe pre-order. The agent drafts the post and the founder posts it as himself. |
| 6. Concierge 5 | Agents + human | 5 paying customers, with every human minute logged by function. |
| 7. Learn | Script | An outcomes table that re-weights sources: which subreddit or Pantip room produced the winners. |

Run the 1,050 legacy ideas backwards through Stages 1–3 instead of re-scoring them.

## 3. Minimum APIs

| API | Unlocks | ~$/mo | Keep/cut |
|---|---|---|---|
| Tavily (held) | Search and extract | $0 extra | Keep |
| Perplexity (held) | Synthesis | $0 extra | **Cut first** (overlaps Tavily) |
| Apify, pay-per-result | TikTok comments (listed at ~$0.20–1.00 per 1k), Pantip, public FB groups, Maps and app reviews, Fastwork/Upwork gigs | $30–50 | **Keep: the one real add** |
| Reddit OAuth | 100 QPM free | $0 | Keep. It is non-commercial only and approval is slow; a reported 2026–27 sunset is unverified. Apify is the fallback. |
| DataForSEO search volume | Thai-language demand at $0.06 per 1,000-keyword task, $50 top-up (unverified against pricing page) | $5–10 | Keep |
| Google autocomplete | Free long-tail pain phrasing | $0 | Keep (unofficial endpoint) |
| google-play-scraper / iTunes RSS | Incumbent complaints | $0 | Keep |
| DBD DataWarehouse | Registered firms by TSIC code, as a B2B target list | $0 | Keep for Thai B2B |
| HN Algolia, CFPB | Global B2B and US consumer pain | $0 | Keep; low value for Thailand |
| LINE Messaging API | Smoke-test channel (quota unverified) | $0 | Keep |
| Ahrefs, Semrush, SparkToro | Dashboards | $100+ | Cut |

New spend is about **$40–60/mo**.

## 4. How to measure 80–90% agent-operable
Measure it during the build; don't guess it up front.
- **Before launch:** agents dry-run each function (acquisition, onboarding, delivery, support, billing, data ops) on 10 synthetic cases and flag every step a human touches.
- **During Concierge 5:** log human minutes per customer per function. Operability = 1 − (human minutes ÷ the minutes a human-run competitor spends). Fastwork gig price ÷ hourly rate gives the benchmark.
- **Pass:** at most 20% by customer 5, trending down. The headline metric is human minutes per ฿10k MRR.
- **Human-only today:**
  - Trusted community posting, since bots get banned from FB groups and Pantip.
  - Licensed advice (legal, medical, visa) and signatures.
  - In-person work.
  - B2B sales calls above about ฿5k/mo.
  - Large payment disputes.
  - Creator deals.

## 5. Kill rules
1. **No crowd:** you can't name 3 free-to-post places with at least 1,000 target buyers.
2. **No paid substitute:** if nobody pays a human today, nobody will pay an agent.
3. **Thin pain:** fewer than 15 independent complaints across 2 or more platforms in 90 days.
4. **Dead smoke test:** a push reaching about 2,000 people gets fewer than 20 sign-ups or fewer than 3 pre-payments in 7 days. These thresholds are my heuristics, to be tuned by outcomes.
5. **Human sink or free giant:** customer 5 still needs more than 30% human minutes or a licence, or LINE, Google or a bank app ships it free.

## 6. Ranking
Drop the composite score and use an **evidence ladder**:
- L0: a hunch.
- L1: at least 15 pain cards.
- L2: a paid substitute found.
- L3: the waitlist threshold hit.
- L4: at least 3 pre-sales.
- L5: 5 paying customers with at most 20% human minutes.

Rank by rung, then by cheapest next test. To keep it from becoming theatre:
- Every rung needs a URL, a screenshot or a receipt.
- No agent may promote an idea it generated.

## 7. What I expect the other panelists to get wrong
- **Pipeline builders:** a 10-stage scoring engine with $300/mo of APIs that never meets a customer. A better rubric is still a spreadsheet.
- **Automation purists:** they'll pick back-office workflows with no channel. Fully automated with zero distribution is still zero.
- **TAM people:** 30k reachable Bangkok expats beat a $4B TAM you can't reach.
- **Thai specialists:** full Pantip/LINE crawling is a ToS risk. Sample it instead.
- **Everyone:** they'll underweight the founder's own audience. Build or borrow distribution first.
