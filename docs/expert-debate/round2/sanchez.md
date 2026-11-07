# Round 2: Sanchez lens (Contrarian and Cash Flow)

_A lens inspired by Codie Sanchez's public "boring businesses" ideas. These are not her words._

## 1. Where I've been persuaded

- **Levels and Walling on buying.** They're right that a Thai laundromat or clinic comes with staff, premises and Foreign Business Act limits. I'm demoting the buy track. In months 1–6 it covers **asset-light deals only**: online businesses on Acquire.com/Flippa, or service books with contractor delivery. Physical acquisitions wait until one agent-run business is producing cash.
- **Hormozi on CPC.** CPC is the cheapest price someone has actually bid. It belongs on my incumbent card next to filed revenue. His deposit rule also beats my looser rule that "someone paid through a rail".
- **Graham on timing.** Apply the 80–90% bar at month 6, not on day 1. Deep, profitable wells often start out human-heavy. My ≤5 owner-hours target becomes a month-6 test, measured from a real ledger.
- **Walling on churn.** A business with 8% monthly churn is an acquisition treadmill. I'm adding a churn bucket to the card. One-shot rescues get valued as one-shot cash, not as MRR.
- **Isenberg's "someone already pays a human"** is my incumbent rule in different words. We agree, so take the stricter version: name the payer and show the price.

## 2. Where I still disagree, and why

- **Godin, Graham and Isenberg start the ladder at complaints.** Fifteen angry Pantip posts tell you about anger, not cash. Rung zero should be **evidence that money is already moving**: an incumbent's DBD-filed revenue, a listing P&L, a Fastwork gig price or a CPC. Without that, a complaint is noise. HN and Reddit buzz still work best as an anti-signal: if builders are crowding in, skip.
- **Levels' bot posting to Pantip, subreddits and LINE OpenChat.** Godin is right that this burns face. It also gets accounts banned, which hits the one free channel. Agents can draft posts, but a human posts them.
- **Hormozi's $1,500/month ad budget across 10 tests.** Paid-ad smoke tests favour consumer offers, which are exactly the ones his own CAC rule kills. B2B incumbents' customers can be reached for free through review authors and DBD target lists. Spend ฿5k on a test only once the card shows a payback of 6 months or less.
- **Walling's "buying brings staff agents can't run".** That's true of the front line, but the back office (booking, billing, reviews, LINE support) is where owners bleed hours. In a contractor-delivered business, that back office is the moat a software clone doesn't have. I'm not dropping the buy option. I'm keeping it small and putting it later.
- **Everyone on ranking.** An evidence ladder tells you an idea is *real*. It doesn't tell you it's *worth it*. Between ideas on the same rung, break the tie with **payback months and owner-hours per week**, both sourced.

## 3. The one thing the final system must not lose

**Every card is anchored to someone already making money doing it badly, and the cash math is shown.** Without that anchor, the new system turns into LEAP again: verbatim quotes in place of scores, but still idea-first and still building from zero. Each card needs to show three named incumbents with revenue evidence, a price someone pays today, and a payback figure. If a card has no anchor, the agents don't work on it. And for every winner, keep one column asking whether we could buy this cheaper than we could build it.

```json
{"apis_ranked": ["Tavily", "Apify", "DataForSEO", "DBD open data", "Stripe/Opn", "CFPB API"], "apis_cut": ["Perplexity", "Google Trends", "Meta Ad Library", "Reddit API", "paid SEO and social-listening suites"], "max_monthly_api_budget_usd": 80, "stages": ["Founder box", "Money-signal sourcing (listings, 1-star clusters, DBD, CPC)", "Incumbent card with 3 revenue-evidenced incumbents", "Binary kill gate", "Buy-vs-build P&L with payback", "Founder pick", "Reality contact: pre-sale deposits or concierge, broker calls for asset-light buys", "Ops ledger and outcome re-weighting"], "ranking_method": "Gate first, sort by highest evidence rung reached (money moving > deposit > paid concierge), then break ties by sourced payback months and owner-hours per week, with real P&Ls and deposits overwriting estimates.", "agent_operable_metric": "Owner-hours per week per business from a logged ops ledger (rework counts as human time), target 5 or fewer by month 6.", "kill_rules": ["No money already moving: fewer than 3 named incumbents or paid substitutes with revenue or price evidence", "Payback over 6 months to build, or over 3 years to buy at post-agent margins", "Zero deposits or paid concierge customers from 10 reached buyers", "Owner must be present: more than 5 on-site hours a week, or a licence or Thai-majority structure he can't arrange", "Crowd rule: 5 or more similar launches on Product Hunt, HN or X in the last 90 days"], "human_checkpoints": ["Founder box (once)", "Weekly founder pick of up to 5 cards", "Founder posts, takes calls and approves any money moving", "Day-30 keep, narrow or kill decision", "Month-6 operability review"], "ideas_tested_per_month": 4}
```
