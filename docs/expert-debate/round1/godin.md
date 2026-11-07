# Round 1: Godin lens (Audience and Meaning)

_Lens inspired by Seth Godin's public writing. Paraphrase only, no quotes._

## 1. My one-line thesis
Don't hunt for ideas. Pick people you can reach and earn the trust of, then let their own words tell you what to build. Agents can run the work, but they can't make anyone trust you.

## 2. The system I'd build
1,050 ideas with 74% RECOMMENDED means nothing was chosen. Start from people, not ideas.

| Stage | Output | Human? |
|---|---|---|
| 0. Reach inventory: groups the founder already reaches (his students, LINE groups, expat FB groups) | 3–5 named groups, each with a channel and a count | **Founder picks** |
| 1. Listening: agents collect verbatim pain from Pantip, Reddit, HN, YouTube comments | A bank of quotes with links, clustered by problem | No |
| 2. Change card: "This is for ___ who want ___; it helps them get ___", plus who it's *not* for and why anyone would tell a friend | 10–15 cards | **Founder cuts to 3** |
| 3. Permission test: a Tally page plus a LINE OA, posted by hand under the founder's own name | Signups, forwards, deposits | **Founder posts and holds 10 conversations** |
| 4. Smallest build: Claude Code ships only to the people who asked | An MVP for 10–30 people | Light |
| 5. Learning loop: agents log support messages, refunds and referrals against the card | A weekly memo and a 30-day keep, narrow or quit decision; dead cards and reasons go back to stage 1 | **Founder decides** |

## 3. Minimum APIs
The most valuable data source is a permission list you own. Everything else is just listening.

| API | Unlocks | $/mo | Keep or cut |
|---|---|---|---|
| Tavily + Perplexity | Search and synthesis | Already paid | Keep |
| HN Algolia | Pain from builders and B2B buyers | $0 | Keep |
| Reddit API | Expat and global pain in verbatim text | $0 at low volume (unverified) | Keep |
| Pantip (no official API; slow, polite fetching) | Thai consumer pain in Thai | $0 (unverified) | Keep |
| YouTube Data API | Thai comment threads | $0 within quota (unverified) | Keep |
| Tally | Smoke-test pages; webhooks on the free plan | $0, or ~$29 | Keep |
| LINE Official Account | The Thai permission channel: ~300 free pushes, Basic ~฿1,280 for 15,000, replies free (third-party figures, unverified) | ฿0–1,280 | **Keep. This is the asset.** |
| Google Trends (pytrends, unofficial) | Relative Thai search interest | $0, fragile | Cut first |
| DBD DataWarehouse | Counts of Thai competitor registrations | $0 (unverified) | Optional |
| Paid social-listening or SEO suites | Volume | $100+ | Cut. Volume isn't trust. |

## 4. How to measure 80–90% agent-operable
Count hours, and also count **trust moments**.
- Map every customer touch in the first 60 days and label each one routine or trust-bearing.
- These stay human-only today:
  - the first reply to a worried person
  - refunds and disputes
  - anything regulated (visa, medical, legal)
  - Thai partner deals, where face matters
  - hosting a community
- To verify, run 30 days with real customers and track:
  - the share of touches closed with no human involved (target: 85% of routine touches)
  - founder hours spent on trust moments (target: under 3 a week)
  - whether referrals held steady
- If more automation means fewer referrals, the business isn't agent-operable. It's just cheaper while it shrinks.

## 5. Kill rules
1. **No reachable audience.** The founder can't put the page in front of 100 named-group members within 14 days, using channels he already has.
2. **Nobody tells anybody.** 10 conversations bring zero forwards or introductions.
3. **Fake trust.** It needs fake reviews, agent-run "community" accounts, cold DM blasts, or scrape-and-message.
4. **No skin in the game.** 10 conversations bring zero deposits or paid pilots.
5. **Not worth the Dip.** The founder wouldn't want to be the best in the world for this group. Quit before the sunk cost builds up.

## 6. Ranking (or why not)
Retire averaged scores. Rank by the highest rung reached on an **evidence ladder**:
1. Verbatim pain from at least 15 distinct people
2. A card the founder will sign his name to
3. 100 people reached by hand
4. 10 conversations
5. At least 3 deposits
6. At least 1 unprompted referral

Only real people move an idea up a rung, so it can't become theatre. Keep 3 ideas active at a time.

## 7. What I expect the other panelists to get wrong
- **Better spreadsheets.** Weighted scores built on more APIs are still opinions, just more precise ones.
- **Starting from TAM.** Big markets attract incumbents and agent-built clones.
- **Automating acquisition.** Agent outreach at volume is spam, and one screenshot in a Thai LINE group costs face you won't get back.
- **"Thais and expats" as one audience.** It's two audiences. Pick one.
- **Ignoring the founder.** The people he already teaches, professionals building with AI, are his most trusted reachable group. Nobody starts there.

_Checked: developers.line.biz/en/docs/messaging-api/pricing; sleekflow.io/blog/line-business-account-set-up; jetadmin.io/blog/tally-pricing (summarising tally.so/pricing)._
