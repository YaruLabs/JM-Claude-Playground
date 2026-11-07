# Round 1: Sanchez lens (Contrarian and Cash Flow)

_A lens inspired by Codie Sanchez's public "boring businesses" and buy-vs-build ideas. These are not her words._

## 1. My one-line thesis
Stop generating ideas. Find businesses that already make money and do it badly, then choose between **buying one and agent-ifying it** or **building the agent-native version and taking its customers**. If no incumbent is earning money, there is no market yet.

## 2. The system I'd build

| Stage | What agents do | Output | Human? |
|---|---|---|---|
| 0. Founder box | One-time form: cash available to deploy (build budget vs. a ฿1–5M / $50–250k acquisition), hours per week, languages, licences, Foreign Business Act constraints | `founder.yaml` that every later stage reads | **Yes, once** |
| 1. Money-signal sourcing | Pull four streams: (a) businesses-for-sale listings (BizBuySell, Flippa, Acquire.com, Thai "เซ้งกิจการ" transfer posts); (b) 1-star Google Maps review clusters by category and city; (c) DBD registry counts and filed revenue by TSIC code; (d) CFPB complaints for the US | `signals.csv`: segment, number of firms, median revenue, asking multiples, complaint themes | No |
| 2. Incumbent card | Cluster signals into problems. Each card **must name 3 incumbents with evidence of revenue** (DBD filings, listing P&L, published price lists) and their top complaint themes | `incumbents/<segment>.md` | No |
| 3. Buy vs. build | For each card, model both tracks: owner earnings, asking multiple, payback, and margin after agents replace staff hours, set against build cost plus CAC to steal 50 customers | Two-column P&L with a source on every number | No |
| 4. Pick 5 | Founder reads the 10 best cards and keeps 5 | Shortlist | **Yes, 30 min per month** |
| 5. Reality contact | Buy track: agent sends outreach to brokers and owners, requests P&Ls, and books calls. Build track: LINE OA or landing-page pre-sale, plus 10 incumbent customers reached via review authors and FB groups | Reply rates, real P&Ls, deposits | **Yes: calls and any money moving** |
| 6. Learning log | Every outcome (ask multiple, reply rate, price objection, deposit or none) is written back. Monthly, the agent re-weights which signal streams predicted real traction | `outcomes.csv` that feeds stage 1 | No |

The key difference from LEAP is that **no stage creates an idea from nothing**. Every row is anchored to an existing business with cash flow.

## 3. Minimum APIs

| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| Tavily (already held) | General search and extraction for incumbent pricing pages | $0 extra | Keep |
| Perplexity (already held) | Synthesised answers | $0 extra | **Cut first.** It overlaps Tavily and summaries without sources are opinions again |
| Apify (Google Maps reviews and business listings) | 1-star clusters per category and city (TH and US), plus BizBuySell/Flippa listings with asking price and cash flow | ~$30–50 for the plan. Official Compass review actor is ~$0.35–0.50 per 1k reviews; BizBuySell scrapers are ~$2–4 per 1k listings. Check ToS | **Keep.** This is the single most valuable addition |
| DBD Open Data / DataWarehouse+ | Thai firm counts, registration dates and filed revenue by industry, i.e. who is earning money | Free. Endpoint `openapi.dbd.go.th` (unverified); the DataWarehouse+ web export is manual | Keep |
| CFPB Complaint DB | Free US complaint clusters by product and company | Free, no key | Keep (US only) |
| Google Trends (unofficial pytrends) | Thai-language demand direction | Free, brittle | Keep, low weight |
| HN Algolia / Reddit | What builders are excited about | Free | **Use as an anti-signal.** Crowded on HN means skip |

Total new spend is **about $30–50/mo**. I would not buy SEO suites, TikTok APIs or paid social listening until a shortlist exists.

## 4. Measuring "80–90% agent-operable"
A percentage of tasks is the wrong unit. Measure **owner-hours per week, weighted by dollars**.
1. **Task inventory from a real business**, not imagination. Build it from seller interviews, job posts and the incumbent's SOPs: every recurring task, hours per week and the cost of the person doing it.
2. Classify each task: agent-now, agent-plus-human-approval, contractor (physical), or owner-only.
3. **Score** = 1 minus (owner-only hours divided by total hours), weighted by labour cost. The target is **≤5 owner-hours per week per business**.
4. **Verify with a 2-week shadow run.** Agents perform the tasks in parallel with the current operator, and we log every intervention. The claim is only accepted if the logged interventions fit inside 5 hours.

These remain human-only today: physical delivery (repairs, cleaning, inspections), licensed sign-offs, Thai government counter visits and bank KYC, cash handling, large-account relationship sales, and escalated disputes and refunds.

The contrarian point is that physical businesses with agent-run back offices (booking, quoting, billing, reviews, LINE support) and contractor-run delivery can reach the 5-hour target. Pure software clones of incumbents rarely build a moat.

## 5. Kill rules
1. **No incumbent making money.** If we can't name 3 paying competitors with revenue evidence, kill.
2. **Payback too long.** Kill if build payback is over 18 months, or if the asking multiple at post-agent margins gives buy payback over 3 years.
3. **Nobody has paid yet.** Kill if no customer has ever paid anyone for this outcome through an existing rail (PromptPay, card or invoice).
4. **Owner has to be there.** Kill if the founder must be physically present more than 5 hours a week, or if the business needs a licence or majority Thai ownership he can't structure.
5. **Crowd rule.** Kill if 5 or more launches in the last 90 days appear on Product Hunt, HN or X. Someone smarter and better funded is already there.

## 6. Ranking
Retire the 1–5 scores. Rank on **three real numbers**, each with a cited source:
- projected month-12 owner earnings;
- payback in months;
- owner-hours per week.

A field without a source stays blank, and blank rows sort last. That is the anti-theatre rule. Once stage 5 runs, real data such as reply rates, actual P&Ls and deposits **overwrite the estimates**. A model can't give a 4/5 to a number that came off a seller's bank statement.

## 7. What I expect the other panelists to get wrong
- **They'll still start from ideas.** The brainstorming will be better sourced, but it is still building from zero while ageing owners sell cash-flowing businesses at 2–3x SDE (seller's discretionary earnings, unverified range for small Main Street deals).
- **They'll measure pain instead of payment.** Reddit and Pantip complaints show where people are angry. Incumbent revenue shows where people pay.
- **They'll over-buy APIs.** Social listening and SEO tools add cost before there is any signal worth listening to.
- **They'll read "80–90%" as a software metric.** The founder's constraint is his own hours, not a percentage of automated tasks.
- **They'll never price the buy option.** That is the most underpriced move a solo founder with agents has.

Sources checked: Apify Store listings for the Compass Google Maps reviews actor and BizBuySell scrapers (prices vary by actor); DBD DataWarehouse+ references, which disagree on whether an official free API exists.
