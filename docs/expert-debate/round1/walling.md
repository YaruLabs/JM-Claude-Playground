# Round 1: Walling lens (Durability)

_A lens based on Rob Walling's public frameworks. It is not the person, and nothing here quotes him._

## 1. My one-line thesis
Rank markets and retention, not ideas. Build a system that finds B2B niches where people already pay, gets there in steps (a one-time product first, then a subscription), and learns which early signals actually predicted paying, retained customers.

Look at the current top 40. Many entries are one-shot consumer rescues: refunds, appeals, parking charges. That is 100% churn by design. Others are two-sided marketplaces (TH-020, TH-036, TH-094, TH-091), which have the worst base rates for bootstrappers. LEAP has no churn or platform-risk axis, so it can't see either problem.

## 2. The system I'd build
| Stage | What runs | Output | Human? |
|---|---|---|---|
| 0. Founder-fit file | One-off interview | `founder.yaml`: languages, networks, channels the founder already has, hours per week, banned domains (e.g. regulated advice) | **H1**, once |
| 1. Market sourcing | Agents look for *existing spend*: paid incumbents (G2/Capterra, Shopify/LINE app listings), job posts for the manual role, DBD counts of businesses in the vertical | Market cards, each with ≥3 links proving spend | No |
| 2. Pain mining | Only inside surviving markets: 1–2★ reviews of incumbents, Reddit/HN/Pantip threads | Problem cards with verbatim quotes and URLs. No idea text yet | No |
| 3. Kill gate | Section 5 rules, binary | Pass or kill, with the rule that killed it | No |
| 4. Durability card | Separate reviewer agent, blind to the generator | Churn profile (one-shot / seasonal / workflow-embedded), main channel, biggest platform dependency, expansion path, step (1 = one-time, 2 = SaaS) | No |
| 5. Ops map | Task inventory per function (section 4) | Human-minutes per customer per month | No |
| 6. Pick | Founder picks 3 from a shortlist of at most 10 | Validation plan | **H2** |
| 7. Validate | Agents build a landing page and run outreach in ONE channel. Founder does 5 calls per idea | Pre-sales, LOIs, reply rates | **H3** |
| 8. Go/kill | Day-30 review against pre-set thresholds | Decision plus an outcome row | **H4** |
| 9. Learning loop | Freeze every stage-4 signal at scoring time, then join to outcomes (paid? still paying at 90 days?) | Signal-to-outcome table, reviewed quarterly | Read-only |

Stair-step: the founder's *first* agent-run business should be a one-time or productized B2B tool sold through a single channel. Recurring SaaS comes after that.

## 3. Minimum APIs
| API | Unlocks | Rough $/mo | Keep or cut |
|---|---|---|---|
| Tavily (held) | General web plus extraction for spend evidence | Existing | Keep |
| Perplexity (held) | Synthesized answers | Existing | **Cut first.** It overlaps Tavily and its citations drift toward vendor blogs |
| HN Algolia | Founder and B2B pain, "who pays for X" threads | Free | Keep |
| Apify | Scrapers for Pantip, Reddit, TikTok comments, G2/app-store reviews | ~$19–29 Starter (reported cut to $19 in Sep 2026; check) | Keep. This is what makes Pantip and Reddit reachable |
| DataForSEO | Keyword volume incl. Thai (Google Ads data), SERP competitor checks | Pay-as-you-go, $50 minimum top-up that doesn't expire; volume ≈ $0.18 per 1k-keyword task (third-party figure) | Keep. SEO is the channel most bootstrappers win with |
| Apple App Store RSS reviews | Incumbent complaints | Free | Keep |
| DBD DataWarehouse / data.go.th | Count of Thai firms by TSIC code = real TAM floor | Free (bulk/API access unverified) | Keep for TH |
| CFPB complaints, Companies House | US/UK pain and firm counts | Free | Keep |
| Google Trends (unofficial) | Seasonality, so seasonal churn can be flagged | Free | Nice to have |

Total: under ~$80/mo on top of the keys you already hold. Skip LINE/TikTok official APIs at this stage. LINE is a *delivery* platform risk to score, not a research source.

## 4. How to measure 80–90% agent-operable
- **List the tasks.** For each function (acquisition, onboarding, delivery, support, billing, retention/churn-saves, data ops), list the tasks at 100 customers. Tag each one A (agent end-to-end), A+R (agent drafts, human approves) or H (human-only).
- **Use one metric.** Human-minutes per customer per month (HMCM), and multiply by the expected customer count. 80–90% means HMCM ≤ ~10% of what a manual operator would need.
- **Verify, don't estimate.** In the pilot, the founder logs every intervention. Re-measure monthly.
- **Human-only today:** high-ACV sales calls, refund and dispute judgment, regulated advice (legal, medical, immigration), Thai government and partner relationships, onsite work, and saving at-risk accounts.

Durability caveat: acquisition is the hardest function to automate. A business at 90% automation with 8% monthly churn runs on an acquisition treadmill. Score it as lower automation than one at 80% with 2% churn.

## 5. Kill rules
1. **No existing spend.** Nobody pays a tool, agency or employee for this today.
2. **Structural churn without the right pricing.** The need is one-shot, but it is priced as a subscription. (One-shot sold as one-time is allowed only as a step-1 product with an SEO channel.)
3. **Two-sided marketplace or network effect** needed for value on day one.
4. **One platform controls both acquisition and delivery.** Examples: LINE-only or TikTok-only, or a single marketplace that can delist you.
5. **No single channel** where agents can reach 100 qualified buyers within 30 days. W=1 is also an instant kill.

## 6. Ranking
Keep it, but don't average anything. Gate first, then sort by an **evidence ladder**:

pre-sale > LOI or pilot > qualified reply > waitlist > search volume > complaint

Break ties with the churn bucket, then platform risk. Every score is frozen when it's made, and any signal that fails to predict 90-day retention after about 20 validations gets dropped. A score no outcome can falsify is just theatre.

## 7. What I expect the other panelists to get wrong
- **Levels lens:** will favor fast consumer launches and building in public. Consumer base rates for churn and willingness to pay are poor, and the founder can't run five of them.
- **Hormozi lens:** strong on offers, but services-heavy offers wreck HMCM, and one-time "grand slam" offers aren't recurring revenue.
- **Graham lens:** "do things that don't scale" is right for validation, but it fails the 80–90% goal if it's never unwound.
- **Godin and Isenberg lenses:** audience- and community-first approaches add platform dependence and lag without proving spend.
- **Sanchez lens (expected):** marketplace-shaped ideas.
- **Everyone:** treating "agent-operable" as the goal when retention is the real constraint.
