# Round 1: Walling lens (Durability)

_A lens on Rob Walling's public frameworks. No quotes._

## 1. My one-line thesis
Rank markets and retention, not ideas. Find B2B niches with existing spend, get there in steps (a one-time product first, SaaS second), and learn which early signals predicted *retained* revenue.

The current top 40 is full of one-shot consumer rescues (100% churn by design) and two-sided marketplaces (TH-020, TH-036, TH-091, TH-094), the worst bootstrapper base rates. LEAP has no churn or platform-risk axis, so it can't see either.

## 2. The system I'd build
| Stage | Output | Human? |
|---|---|---|
| 0. Founder-fit file | `founder.yaml`: languages, existing channels, hours, banned domains | **H1**, once |
| 1. Market sourcing: find *existing spend* (paid incumbents on G2/app listings, job posts for the manual role, DBD firm counts) | Market cards, each with ≥3 spend links | No |
| 2. Pain mining inside surviving markets: 1–2★ incumbent reviews, Reddit/HN/Pantip | Problem cards with verbatim quotes and URLs. No ideas yet | No |
| 3. Kill gate (section 5, binary) | Pass, or kill with the rule that killed it | No |
| 4. Durability card from a separate reviewer agent, blind to the generator | Churn profile (one-shot / seasonal / workflow-embedded), main channel, top platform dependency, expansion path, stair-step (1 = one-time, 2 = SaaS) | No |
| 5. Ops map (section 4) | Human-minutes per customer per month | No |
| 6. Pick | Founder picks 3 from a shortlist of at most 10 | **H2** |
| 7. Validate: agents build a landing page and run outreach in ONE channel; founder does 5 calls per idea | Pre-sales, LOIs, reply rates | **H3** |
| 8. Day-30 go/kill against pre-set thresholds | Decision plus an outcome row | **H4** |
| 9. Learning loop: freeze stage-4 signals at scoring time, join to outcomes (paid? still paying at day 90?) | Signal-to-outcome table, reviewed quarterly | Read-only |

The first agent-run business should be a one-time or productized B2B tool sold through a single channel. Recurring SaaS comes after that.

## 3. Minimum APIs
| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| Tavily (held) | Web search and extraction for spend evidence | Existing | Keep |
| Perplexity (held) | Synthesized answers | Existing | **Cut first.** Overlaps Tavily and leans on vendor blogs |
| HN Algolia | B2B pain, "who pays for X" threads | Free | Keep |
| Apify | Scrapers for Pantip, Reddit, TikTok comments, G2/app reviews | ~$19–29 Starter (cut to $19 reported Sep 2026; check) | Keep |
| DataForSEO | Keyword volume incl. Thai, SERP competition | Pay-as-you-go, $50 minimum top-up; ~$0.18 per 1k-keyword task (third-party figure) | Keep. SEO is the channel bootstrappers most often win with |
| App Store RSS reviews | Incumbent complaints | Free | Keep |
| DBD DataWarehouse / data.go.th | Thai firm counts by TSIC = TAM floor | Free (API access unverified) | Keep for TH |
| CFPB, Companies House | US/UK pain and firm counts | Free | Keep |

Under ~$80/mo beyond the keys held. Treat LINE as a platform *risk* to score, not a research source.

## 4. How to measure 80–90% agent-operable
- **List the tasks.** For each function (acquisition, onboarding, delivery, support, billing, churn-saves, data ops), list the tasks at 100 customers. Tag each A (agent), A+R (agent drafts, human approves) or H (human-only).
- **Use one metric.** Human-minutes per customer per month (HMCM). The 80–90% target means HMCM ≤ ~10% of a manual operator's.
- **Verify it.** The founder logs every intervention during the pilot. Re-measure monthly.
- **Human-only today:** high-ACV sales, refund and dispute judgment, regulated advice, Thai government and partner relationships, onsite work, saving at-risk accounts.

Durability caveat: a business at 90% automation with 8% monthly churn is an acquisition treadmill, and acquisition is the hardest function to automate. Rate it below a business at 80% automation with 2% churn.

## 5. Kill rules
1. **No existing spend.** Nobody pays a tool, agency or employee for this today.
2. **One-shot need priced as a subscription.** One-time pricing is allowed only as a step-1 product with an SEO channel.
3. **Needs a two-sided marketplace or network effects** to deliver value on day one.
4. **One platform controls both acquisition and delivery** (LINE-only, TikTok-only, one marketplace).
5. **No single channel** reaches 100 qualified buyers in 30 days. W=1 is also an instant kill.

## 6. Ranking
Don't average anything. Gate first, then sort by an **evidence ladder**:

pre-sale > LOI or pilot > qualified reply > waitlist > search volume > complaint

Break ties with the churn bucket, then platform risk. Freeze every score when it's made. After about 20 validations, drop any signal that didn't predict 90-day retention. A score no outcome can falsify is theatre.

## 7. What I expect the other panelists to get wrong
- **Levels lens:** fast consumer launches. Consumer churn and willingness to pay are poor, and the founder can't run five of them.
- **Hormozi lens:** service-heavy "grand slam" offers inflate HMCM, and a one-time offer isn't recurring revenue.
- **Graham lens:** "do things that don't scale" is right for validation, but it breaks the 80–90% goal if it's never unwound.
- **Godin and Isenberg lenses:** audience- and community-first approaches add platform dependence and lag before any spend is proven.
- **Sanchez lens:** boring markets with real spend, which I agree with. But buying businesses brings staff and physical operations agents can't run.
- **Everyone:** treating agent-operability as the goal when retention is the binding constraint.
