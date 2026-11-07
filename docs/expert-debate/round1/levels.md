# Round 1: Levels lens (Automation and Shipping)

_A lens inspired by Pieter Levels' public approach. Not the person, and no quotes from him._

## 1. My one-line thesis
You already have 1,050 ideas and zero customers. Stop building an ideation system and build a **launch factory**: a cron-driven pipeline that turns a real complaint into a live page with a payment link inside 72 hours, then lets money decide. The only score that counts is THB or USD per human hour.

## 2. The system I'd build
One cheap VPS (about $6–12/mo (unverified)), SQLite, Python scripts on cron, and Claude Code as the builder. No dashboards, no rubric UI.

| Stage | What runs | Output | Human? |
|---|---|---|---|
| **S1 Complaint mining** (nightly cron) | Scripts pull HN Algolia, Reddit JSON, Pantip (via Apify or direct fetch), TikTok comments (Apify), app-store 1–2★ reviews and CFPB complaints. Agents cluster these by problem, **not** by idea title. | A `problems` table holding the raw quote, URL, date, language and count. A problem with no link to real text is dropped. | No |
| **S2 Demand check** | DataForSEO search volume (TH plus EN), Google Trends, Meta Ad Library (are people already paying to advertise this?) | Each problem gets three facts: monthly searches, whether anyone is advertising, and an existing paid competitor (yes/no). These are facts, not 1–5 opinions. | No |
| **S3 Kill gate** | The five rules in section 5 run as code, pass or fail. | A shortlist of about 5–10 a week | **Yes, 15 min/week.** The founder vetoes anything he would hate running (founder fit, as a gut check). |
| **S4 Ship the smoke test** | Claude Code builds a one-page site with the offer, price and a Stripe or PromptPay link (or a preorder or waitlist with a deposit). A bot posts it to X, the relevant subreddit or Pantip room, a LINE OpenChat or a Facebook group, and runs ~฿1,500 ($40) of Meta ads. | A live URL and a spend log | **Yes.** He approves the price and copy (5 min each). |
| **S5 Measure for 14 days** | A cron pulls Stripe, Plausible or Umami and ad spend into SQLite. | Visits, signups, **payments**, CAC | No |
| **S6 Keep or kill** | Code applies the rule: ≥3 payments (or ≥฿3,000 preorders) means build the MVP in 7 days. Anything less is killed and the page archived. | A decision row, plus the reason it was killed | **Yes, 10 min.** He confirms. |
| **S7 Learn** | Each kill reason and conversion rate is written back. S1 and S2 learn which sources and channels produced payers. | A source-level table: payments per 100 problems mined | No |

The founder spends about 1–2 hours a week in total. He runs 2–4 tests at once, so that is 100+ launches a year. Most will die, which is how it is meant to work.

## 3. Minimum APIs

| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| HN Algolia | Searchable complaints and "Ask HN" pain posts | Free | Keep |
| Reddit public JSON | Complaint mining (often blocked from cloud IPs, so run it from the VPS with a user agent) | Free (unverified reliability) | Keep |
| Tavily (already held) | General search and extraction for agents | Free at 1,000 credits/mo; Project plan $30 for 4,000 | Keep |
| Perplexity Sonar (already held) | Synthesised answers with citations | ~$5–20 at low volume (unverified) | **Cut first.** It overlaps with Tavily plus Claude. |
| DataForSEO Keywords | Real Google search volume, **including Thai-language keywords** | Pay-as-you-go from a $50 top-up; ~$0.06 per task of up to 1,000 keywords (the price is for the standard endpoint, live mode unverified). That works out to about $5/mo of real use. | Keep. It is the single biggest upgrade over opinions. |
| Apify (TikTok, Pantip, app reviews) | Thai social demand that web search can't see | Free $5 credit, then ~$0.25–2 per 1,000 TikTok results depending on the actor. ~$10–49/mo (unverified plan price) | Keep, but capped |
| Meta Ad Library | Shows whether someone already pays to acquire these customers | Free (unverified API access in TH) | Keep |
| Google Trends (pytrends) | Direction of interest, with Thailand as a geo | Free (unofficial, breaks) | Keep, accepting that it breaks |
| CFPB complaints, data.go.th, DBD open data | Regulated pain in the US, and Thai business-registry counts by category | Free (DBD API access unverified) | Keep |
| Stripe and Omise/PromptPay | **The validation API.** | % of revenue only | Keep. This is non-negotiable. |

Total: **about $20–100/mo**. If the budget gets cut, the order is: Perplexity, then paid Apify (fall back to manual TikTok checks), then the Tavily paid plan.

## 4. How to measure 80–90% agent-operable
Don't estimate it. **Log it.** Every live product writes to an `ops_ledger` table with these fields: function (acquisition, onboarding, delivery, support, billing, data ops or content), actor (bot or human) and minutes. The ledger works like this:
- **Pre-launch**, an agent fills in a function-by-function sheet and marks each task as one of: scriptable today, agent with review, or human-only. This is only a hypothesis.
- **Verification:** the number is `bot_events / all_events`, weighted by minutes, measured during weeks 3–6 after launch.
- **Pass:** a weekly cap of under 2 human hours per product at ~฿50k MRR (I chose this threshold myself). If a product needs more than about 1 hour a day after week 4, it is a job, not a robot business.

**Human-only today:**
- Licensed advice: medical, legal and immigration sign-off.
- Bank, KYC and payment-provider onboarding.
- Chargebacks and disputes that need judgment.
- B2B sales calls and Thai relationship selling.
- Anything physical: inspections, chaperones, deliveries.
- Getting LINE OA approval and building the first community trust.
- Deciding what to kill.

## 5. Kill rules
1. **No money in 14 days.** If a live page with a price and real traffic (≥300 targeted visits) gets zero payments or deposits, kill it.
2. **The MVP can't ship in 7 days** with Claude Code on a boring stack.
3. **Each transaction needs a human or a licence.** That rules out every marketplace built on chaperones or inspectors, and every service where a professional has to sign.
4. **No channel he already owns or can buy cheaply.** If the only route to customers is outbound sales or partnerships, kill it.
5. **Fatal platform dependency.** Kill it if its core data source bans scraping and has no API, or if one platform holds the product hostage (LINE, TikTok or a bank feed).

## 6. Ranking (or why not)
Pre-launch, **no scores at all.** LEAP was theatre: the generators graded their own homework, and the scores sat between 3.3 and 3.9. Order the queue by **cheapest and fastest test first**: hours to build the smoke test plus ad spend needed. Post-launch, rank by **revenue per human hour** from the ledger. Those are two numbers that come from reality, and nobody gets to average them.

## 7. What I expect the other panelists to get wrong
- **Graham lens:** "talk to users" and the well-versus-shallow test are right, but they will turn into weeks of interviews. A payment link is a better interview.
- **Hormozi lens:** grand-slam offer engineering before anyone has visited the page. Offer polish is for round two, once something sells.
- **Walling lens:** it will push recurring SaaS and retention modelling. Plenty of one-off ฿290 reports print money and are fully robotic.
- **Sanchez lens:** buying boring businesses means staff, premises and Thai foreign-ownership limits. That is the opposite of 80–90% agent-operable.
- **Godin and Isenberg leans:** community-building is real, but it is human-hours-heavy. Someone has to price that time.
- **Everyone:** proposing 15 APIs and a new weighted rubric. More research is just procrastination with citations.
