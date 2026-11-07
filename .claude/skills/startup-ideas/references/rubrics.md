# Rubrics: evidence ladder, kill gate, agent-operability

Source: `docs/expert-debate/SYNTHESIS.md`. Seven panel lenses voted, and every rule below has majority support. Code enforces the ladder and gate in `scripts/oppo.py`, so agents never assign rungs or verdicts themselves.

## Evidence ladder (ranking; no averaged scores)

| Rung | Receipt (all must be linkable) |
|---|---|
| L0 Hypothesis | No receipts yet. The 1,050 legacy ideas in `data/ideas-*.csv` start here. |
| L1 Real pain | 15 or more distinct sufferers on 2 or more platforms within 90 days, counted in code from `pains.jsonl` |
| L2 Money moving | 3 or more incumbents or fixers, each with a price or revenue figure and an `evidence_url`. Or a CPC at or above the market threshold: TH $0.30, US $1.50, UK $1.20. |
| L3 Reached | The offer is in front of 100 or more of the target group, or 10 conversations are logged (`oppo.py test log`) |
| L4 Skin in the game | 3 or more deposits, pre-sales or paid pilots |
| L5 Paying customers | 5 or more paying customers, with an ops ledger running |
| L6 Durable | Customers retained at day 90 and a ledger agent share of 80% or more |

**Ranking order:** highest rung first. Ties are broken by gate result, then the cheapest next test, then recurring before one-off, then lower platform risk, then shorter payback.

## Kill gate (any one rule kills; code-enforced)

1. **No existing spend:** fewer than 3 valid incumbents.
2. **Unreachable:** named channels with URLs reach fewer than 100 people.
3. **A human or licence in every transaction,** or more than 5 on-site hours a week.
4. **Below the automation target:** estimated agent share under 75% (the founder's requirement is 80–90%).
5. **The money math fails:** CAC is more than 1/3 of 12-month gross LTV, or payback is over 6 months.
6. **Platform hostage:** one platform controls both acquisition and delivery, or the core data has no API and bans scraping.
7. **A free incumbent is good enough:** a bank app, LINE, the OS or a general AI assistant already does it.
8. **It needs fake trust:** bot posting, fake reviews, agent-run "community" or DM blasts.
9. **The reality test failed:** fewer than 3 deposits within 14 days. One offer rewrite is allowed.

**Soft flags** appear on the card but don't kill it: two-sided marketplace, one-off need priced as a subscription, thin pain (under 15 sufferers), 5 or more similar launches in 90 days, and MVP over 7 days.

**INCOMPLETE** means required fields are missing. Fix the card; don't guess.

## Agent-operability (pre-test estimate, then measured)

Fill `agent_ops.functions` for every function. For each one give `agent_pct` (0–100) and the human-only tasks.

| Function | Usually agent-run today | Usually human |
|---|---|---|
| acquisition | SEO pages, content drafts, ad variants, lead lists | Community posts as yourself, partnerships, sales calls |
| onboarding | Forms, document parsing, account setup, LINE/WhatsApp flows | KYC exceptions, high-touch B2B kickoff |
| delivery | Parsing, drafting, matching, monitoring, report generation | Licensed sign-off, judgement calls with liability, physical work |
| support | First-line answers, status updates, FAQs in Thai and English | Angry customers, refunds, disputes (trust moments) |
| billing | Payment links, PromptPay, dunning, receipts, e-Tax | Chargebacks, negotiated B2B terms |
| data_ops | Scraping, enrichment, dedup, alerts | Data partnerships, legal review of sources |
| content | Drafts, translations, social posts | Final voice, approvals |

`est_agent_share` is the time-weighted average across functions. It is an **estimate (est.)** used only by gate rule 4, never for ranking.

**Measured value.** During concierge delivery, log every task:

```
oppo.py ledger add <card_id> --task "<what>" --actor bot|human --minutes N [--rework]
```

Rework done by a human counts as human time.

**Pass mark:** an agent share of 80% or more by month 6, and founder time of 2–5 hours or fewer per product per week (`oppo.py ledger stats <id> --weeks 4`). Also check that referrals don't drop as automation rises.
