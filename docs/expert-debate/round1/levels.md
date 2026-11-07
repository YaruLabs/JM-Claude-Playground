# Round 1: Levels lens (Automation and Shipping)

## 1. My one-line thesis
You have 1,050 ideas and zero customers. Build a **launch factory**, not an ideation system. It turns a real complaint into a live page with a payment link in 72 hours, and then money decides. The only score is revenue per human hour.

## 2. The system I'd build
The stack is one VPS (~$6–12/mo, unverified), SQLite, Python on cron, and Claude Code as the builder. No rubric UI.

| Stage | Output | Human? |
|---|---|---|
| **S1 Complaint mining (nightly).** Pull HN Algolia, Reddit JSON, Pantip, TikTok comments, 1–2★ app reviews and CFPB. Cluster by *problem*. | `problems` rows, each with a raw quote, URL, language and count. A row with no source is dropped. | No |
| **S2 Demand facts.** DataForSEO volume (TH and EN), Trends, Meta Ad Library | Three facts, not 1–5 opinions: searches/mo, whether anyone advertises it, and whether a paid competitor exists | No |
| **S3 Kill gate.** Section 5 rules as code | 5–10 survivors a week | **Yes, 15 min/week.** Founder-fit veto. |
| **S4 Smoke test.** Claude Code ships one page with the offer, price and a Stripe or PromptPay link. A bot posts it to X, the subreddit, Pantip and LINE OpenChat, plus ~฿1,500 of Meta ads. | A live URL and a spend log | **Yes, 5 min.** He approves price and copy. |
| **S5 Measure for 14 days.** Cron pulls Stripe, analytics and ad spend | Visits, payments, CAC | No |
| **S6 Keep or kill.** ≥3 payments or ≥฿3,000 in preorders means a 7-day MVP. Otherwise the page is archived. | A decision row with the kill reason | **Yes, 10 min.** He confirms. |
| **S7 Learn.** Write outcomes back to the sources and channels | Payers per 100 problems mined, by source | No |

About 1–2 founder hours a week, 2–4 tests at once.

## 3. Minimum APIs

| API | Unlocks | $/mo | Keep or cut |
|---|---|---|---|
| HN Algolia, Reddit JSON | Complaint text | Free. Reddit often blocks cloud IPs (unverified). | Keep |
| Tavily (held) | Search and extraction | Free at 1,000 credits; $30 for 4,000 | Keep |
| Perplexity Sonar (held) | Answers with citations | ~$5–20 (unverified) | **Cut first.** It overlaps Tavily plus Claude. |
| DataForSEO Keywords | Real Google volume, **Thai keywords included** | $50 minimum top-up, ~$0.06 per task of 1,000 keywords (live-mode rate unverified). About $5 of real use. | Keep. Biggest upgrade. |
| Apify (TikTok, Pantip, reviews) | Thai social demand that search misses | ~$0.25–2 per 1,000 TikTok results, by actor. Cap at $10–49 (unverified). | Keep, capped. Cut second. |
| Meta Ad Library, pytrends | Whether anyone already pays for ads; interest trend in TH | Free. Pytrends is unofficial and breaks. | Keep |
| CFPB, data.go.th, DBD open data | Regulated pain; Thai firm counts by category | Free (DBD API unverified) | Keep |
| Stripe and Omise/PromptPay | **The validation API** | % of revenue | Never cut |

Total: **~$20–100/mo**.

## 4. How to measure 80–90% agent-operable
Don't estimate it. **Log it.** Each live product writes an `ops_ledger` row with the function, the actor (bot or human) and the minutes spent. The functions are acquisition, onboarding, delivery, support, billing, data ops and content.
- **Pre-launch:** an agent tags every task as one of: scripted, agent plus review, or human-only. That is a hypothesis, nothing more.
- **Verified:** bot share of minutes, measured in weeks 3–6.
- **Pass:** under 2 human hours a week per product (my threshold). If it still needs an hour a day after week 4, it is a job, not a robot business.

**Human-only today:**
- Licensed sign-off (medical, legal, immigration)
- Bank and KYC onboarding
- Disputes that need judgment
- B2B and Thai relationship selling
- Anything physical
- Early community trust
- Kill decisions

## 5. Kill rules
1. **No money in 14 days** after ≥300 targeted visits.
2. **The MVP can't ship in 7 days** on a boring stack.
3. **Each transaction needs a human or a licence.** Inspector and chaperone marketplaces fail this rule.
4. **No channel the founder owns or can buy cheaply.** Outbound sales only means kill.
5. **Hostage platform.** The core data bans scraping and has no API, or one platform (LINE, TikTok or a bank feed) can switch the product off.

## 6. Ranking (or why not)
No scores before launch. LEAP was theatre: the generators graded their own homework, so everything landed at 3.3–3.9.
- **Pre-launch:** order the queue by cheapest, fastest test, meaning build hours plus ad spend.
- **Post-launch:** rank by revenue per human hour from the ledger.


## 7. What I expect the other panelists to get wrong
- **Graham lens:** "talk to users" will become weeks of interviews. A payment link is a better interview.
- **Hormozi lens:** offer engineering before a single visit. Polish what already sells.
- **Walling lens:** it will push recurring SaaS. One-off ฿290 reports can be fully robotic and profitable.
- **Sanchez lens:** buying boring businesses means staff, premises and Thai foreign-ownership limits. That is the opposite of agent-operable.
- **Godin and Isenberg lenses:** community costs human hours. Price them.
- **Everyone:** 15 APIs and a new weighted rubric. More research is procrastination with citations.
