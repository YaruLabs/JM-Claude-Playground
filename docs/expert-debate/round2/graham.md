# Round 2: Graham lens (Problem Quality)

_A lens that reasons from Paul Graham's public essays. Not the person. Paraphrase only._

## 1. Where I've been persuaded

- **Walling** is right that "do things that don't scale" breaks the 80–90% goal if nobody ever unwinds it. I'll add an unwind date: the concierge phase ends at month 6, and the ops ledger has to show human minutes per customer falling every month. I'll also take his churn bucket as a tie-breaker. A one-shot rescue is a shallow well even when the pain is sharp.
- **Sanchez** says pain shows anger and incumbent revenue shows payment. That sharpens my "paid workaround" rung. A complaint with no money nearby is L1 at most.
- **Isenberg** says no agent may promote an idea it generated. That is the cleanest fix for the 74%-vs-3% gap, and I adopt it word for word as a system rule. His requirement of at least 2 platforms also guards against one loud subreddit.
- **Godin** says Thais and expats are two audiences. He's right, and the founder's own students are the deepest well nobody else can reach.
- **Levels** has a fair point that "talk to users" can rot into weeks of interviews. So I'm adding a clock: 10 conversations in 14 days, and each one ends with a price.

## 2. Where I still disagree, and why

- **Hormozi:** a ฿5,000 Meta test measures copy and targeting, not urgency. Deep wells are small and hard to target, which is why they are open. His CAC-on-paper kill rule would have killed most good startups at their start, because nobody's early users came from paid ads. Ads come after you know who is desperate, not as the way you find out.
- **Levels:** a bot posting to subreddits, Pantip and LINE OpenChat is spam. Godin and Isenberg both warn that it gets you banned and costs face. The "≥300 visits" kill also mixes up traffic with need. Ten named sufferers tell you more than 300 anonymous visits.
- **Sanchez:** treating HN as an anti-signal gets it backwards for this founder. He builds with agents in 2026, so he is living in the future, and builder forums are where he will notice what's missing. Buying a business also needs capital and runs into foreign-ownership limits before it teaches us anything about problems.
- **Walling:** a blind reviewer's durability card is still a model's opinion, written before any customer exists. Freeze it and score it against outcomes, as he suggests, but give it no gating power until that has been done.
- **Everyone with 10 tests a month:** filtering can't recover signal the generator never had. Four well-chosen problems a month, each tested properly, beat ten shallow ones.

## 3. The one thing the final system must not lose

**Every idea traces back to a named person with a real problem, ideally one the founder has felt himself.** The unit of work is a problem card with verbatim quotes, links and a workaround someone already pays for. It is never an idea title. If a stage can create a row that has no sufferer attached, the system will drift back into sitcom ideas within a month, however good the APIs are. Agents harvest and count. Humans choose, talk and charge. Only payment moves a problem up the ladder.

```json
{"apis_ranked": ["Tavily", "Reddit API", "HN Algolia", "DataForSEO", "Stripe/Opn", "CFPB API"], "apis_cut": ["Perplexity", "Apify", "Google Trends", "Meta Ad Library"], "max_monthly_api_budget_usd": 50, "stages": ["Founder vantage inventory", "Pain harvest (verbatim, no ideas)", "Cluster and count distinct sufferers", "Well test (urgency and paid workaround)", "Human pick (max 5/week)", "Concierge to 10 named sufferers", "Build crappy v1 if 3 of 10 pay", "Learning loop on sources and ops ledger"], "ranking_method": "Sort by highest evidence-ladder rung reached (sufferers, paid workaround, conversations, payments), each rung requiring a link or receipt, then by recency, with ties to the founder's vantage point.", "agent_operable_metric": "Agent share of logged task minutes from the concierge ops ledger, with rework counted as human time, required to trend down monthly and reach 80%+ by month 6.", "kill_rules": ["No verbatim sufferer: traces only to a brainstorm", "No paid workaround: nobody spends money or hours on it today", "Founder cannot reach 10 named sufferers by hand within 14 days", "Fewer than 3 of 10 pay or pre-commit to the concierge version", "A free incumbent (bank app, LINE, OS, general assistant) already solves it adequately"], "human_checkpoints": ["Quarterly vantage inventory", "Weekly problem pick (max 5)", "Founder sends outreach and holds the 10 conversations", "Build-or-kill decision after concierge", "Month-6 operability unwind review"], "ideas_tested_per_month": 4}
```
