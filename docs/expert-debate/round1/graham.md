# Round 1: Graham lens (Problem Quality)

_A lens that reasons from Paul Graham's public essays. Not the person. No quotes, only paraphrase._

## 1. My one-line thesis
Stop generating ideas. Harvest problems that named people already pay to work around, starting from the founder's own Bangkok vantage point. Only paying humans can promote a problem, never model scores.

The 1,050-idea backlog is mostly sitcom ideas: plausible, and wanted by no one in particular. The 74% vs 3% gap shows the scores measure the writer's enthusiasm. The unit of work should be a **problem card** with verbatim evidence.

## 2. The system I'd build

| Stage | Who | Output |
|---|---|---|
| 0. Vantage inventory (quarterly) | **Human** | Schleps the founder has hit (visa, bank KYC, LINE OA admin, Thai invoicing, agent tooling), plus who he can message today. This seeds the queries. |
| 1. Pain harvest | Agents | `pains.jsonl`: verbatim quote, URL, date, author type, money or deadline at stake. **No ideas allowed.** |
| 2. Cluster and count | Script | `problems.csv`: distinct sufferers, recency, **workarounds seen** (spreadsheets, paid fixers, agents). |
| 3. Well test | Agent and script | Keep a cluster only with urgency evidence: money lost, a deadline, repeat posters, or a paid bad workaround. Breadth counts for nothing. |
| 4. Checkpoint A | **Human** | Pick at most 5 problems a week that the founder understands or can reach. |
| 5. Things that don't scale | Agent drafts, human sends | Contact 10 named sufferers by hand. Solve the problem as a paid concierge, with Claude behind the curtain. Log every task (§4). |
| 6. Checkpoint B | **Human** | Build the crappy v1 only if at least 3 of 10 paid or pre-committed. Otherwise kill it and record why. |
| 7. Learning loop | Script | Track which sources and queries led to payment, and shift harvest budget monthly toward them. |

## 3. Minimum APIs

| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| Tavily (have) | `site:` harvesting of Pantip, Reddit and forums | Existing | **Keep.** Workhorse |
| Perplexity (have) | Synthesis, "why now" checks | Existing | **Cut first.** Overlaps Tavily and invites brainstorming |
| HN Algolia | Builder pain, "Ask HN: how do you handle X" | Free | Keep |
| Reddit Data API | Verbatim consumer and SMB pain | Free for approved non-commercial use; approval slow; future unclear (unverified) | Keep while free; fall back to Tavily |
| CFPB complaints, UK FOS decisions | Money disputes with a paper trail | Free | Keep (US/UK) |
| DataForSEO search volume | Thai and English volume for Thailand | About $0.05–0.06 per task of up to 1,000 keywords; under $20/mo here (minimum deposit unverified) | Keep, the one paid addition |
| DBD DataWarehouse | Count Thai firms by type, and whether anyone already sells the fix | Free web; no official API (unverified) | Low priority |
| Pantip | Best Thai complaint source | No API; reach it through Tavily | Keep |
| LINE / TikTok | Mostly closed; TikTok's research API is academic-only (unverified) | n/a | **Cut** as research sources. Use them to *recruit* in stage 5 |

New spend is about $20–50/mo. Complaints are free to read.

## 4. How to measure 80–90% agent-operable
Don't estimate it. Measure it. During the concierge phase, `ops_log` records each task's function, minutes, and who did it: agent, human, or human fixing the agent. Over 4 weeks:

- **Agent share = agent minutes ÷ total minutes**, with rework counted as human time.
- Human minutes per customer should fall week over week.

Human-only today: first B2B sales, regulated sign-off (lawyers, licensed brokers, OIC filings), physical presence, escalated disputes and refunds, and Thai banking and KYC.

A warning: a day-1 gate at 80–90% selects for shallow, crowded self-serve products. Deep wells often start human-heavy, so apply the bar at month 6.

## 5. Kill rules
1. **No verbatim sufferer.** The idea traces only to a brainstorm.
2. **No workaround.** Nobody spends money or hours on it now.
3. **Can't reach 10 sufferers in 2 weeks.** That means no distribution and no founder fit.
4. **Free incumbent.** A bank app, LINE, the OS or a general assistant already solves it adequately.
5. **0 of 10 pay for the concierge version.**

## 6. Ranking (or why not)
Retire averaged scores. Rank on an **evidence ladder** whose rungs are facts:

- L0: hypothesis
- L1: at least 5 distinct verbatim sufferers in the last 12 months
- L2: a paid workaround observed
- L3: at least 5 conversations held
- L4: at least 3 people paid

Sort by rung, then by how recent the evidence is. Promotion past L2 needs a link or a receipt. Ties go to the founder's vantage point. A confident paragraph can't inflate any rung.

## 7. What I expect the other panelists to get wrong
- **Rescoring with more decimals.** Weighted rubrics and LLM judges are still opinions.
- **TAM-first thinking.** It favours shallow wide markets over a few desperate users.
- **Automating before learning.** An idea-to-ads pipeline optimises clicks, not need.
- **API maximalism.** The bottleneck is conversations, not data.
- **"Generate 200, filter to 5."** Filtering can't recover signal the generator never had.
