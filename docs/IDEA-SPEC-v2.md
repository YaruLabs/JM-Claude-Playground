# Idea Spec v2 (for generation and review agents)

Every new idea is a JSON object with **exactly** the keys in `scripts/schema_v2.py` `FIELDS`, written as a JSON array to the staging file named in your task. Write valid JSON with `json.dump(..., ensure_ascii=False, indent=2)` from a Python script. Do not hand-write JSON containing unescaped quotes.

## Field rules

| Field | Rule |
|---|---|
| id | The id given in your task (e.g. `TH-001`, `GL-026`, `DIR-226`) |
| title | 2–5 words, Title Case, spaces (no camelCase) |
| tagline | One line, under 110 chars, concrete |
| market | `US`, `UK_EU`, `TH`, or `GLOBAL` |
| target_segment | Who it is marketed to, e.g. `Thai locals`, `Expats in Thailand`, `Both`, `US consumers`, `UK SMBs` |
| category / subcategory | Short labels |
| problem | **≥250 chars, 3+ sentences.** Written for a human browsing a directory. Specific: who hurts, how often, what it costs, why current options fail. Cite numbers only if you found them; mark unverified ones "est." |
| solution | **≥400 chars, 4+ sentences.** Exactly what the product does, the key features, and why it beats the alternatives |
| target_audience | Concrete segments separated by `;` |
| business_model | e.g. `Subscription`, `Freemium + per-report`, `Marketplace commission` |
| pricing | Real price points in **local currency** (THB for TH, USD for US, GBP/EUR for UK_EU) |
| leap_l, leap_e, leap_a, leap_p, moat_m, wtp_w | **Integers 1–5** (see the schema docstring) |
| score_total | Mean of the six, 2 dp |
| score_justification | One short clause per score, e.g. `L5 AI parses bills; E4 OCR+LLM, 1 wk; A4 ...; P3 ...; M4 ...; W4 ...` |
| platform_distribution | The real channel: LINE OA, TikTok, Facebook groups, Pantip, Google Maps/SEO, Chrome Web Store, Shopify App Store, ChatGPT apps, App Store, etc. |
| tam_estimate | e.g. `$450M (est.)` or `฿12B` |
| tam_source | URL or `bottom-up: N users × price`. Never blank |
| competitors | ≥2 named competitors or substitutes, `;` separated |
| competitor_gap | What they miss |
| demand_evidence | 1–3 sentences: the actual signal you found (thread, trend, statistic) |
| source_urls | **≥3 real URLs you actually opened or saw in search results**, separated by ` \| `. At least one must be a demand signal (forum/review thread, trend, government or industry data). Never invent URLs |
| unique_data_capture | The specific proprietary dataset this product accumulates and why it compounds (or `None meaningful`) |
| commoditization_risk | `Low`/`Medium`/`High` plus a reason: could a general AI assistant, OS feature, bank app or incumbent do this in 2026? |
| regulatory_notes | Licensing, liability, PDPA/GDPR/HIPAA, UPL (legal-advice) risk, etc. `None notable` if none |
| founder_feasibility | Can a solo founder run it? For TH, whether a foreigner can operate it (Foreign Business Act, Thai partner, BOI, or fine as an offshore SaaS) |
| language | `EN`, `TH`, or `EN+TH` |
| payment_rails | e.g. `Stripe`, `PromptPay QR + cards (Omise/2C2P)`, `TrueMoney`, `App Store IAP` |
| mvp_features | 4–6 features, `;` separated |
| tech_stack | Model-agnostic, e.g. `Next.js + Supabase + LLM API (Claude/GPT) + OCR`. Do not write "GPT-4" |
| status | `RECOMMENDED` if score_total ≥3.5 and leap_e ≥3 and commoditization risk is not High; else `CAUTION` |
| review_notes | Biggest risk or open question, one sentence |
| created_date / last_verified | `2026-11-03` |

## Quality bar
- Research first using WebSearch/WebFetch: real complaint threads, real competitors, real statistics.
- No duplicates. Check `data/staging/corpus_titles.tsv` (925 existing ideas). Don't repeat an existing concept, even under a new name, unless it is a genuinely different market adaptation and you say so in review_notes.
- Avoid 2026 dead ends: generic prompt libraries, GPT/AI-tool directories, thin ChatGPT wrappers, things Apple/Google/banks now ship free.
- Prefer ideas where proprietary data compounds (high moat_m) and buyers already pay (high wtp_w).

## Review mode (auditing legacy ideas)

Legacy rows use old fields and old scales. For each legacy idea, write one review object to the staging file named in your task. A review object has these keys:

```
id, status, leap_l, leap_e, leap_a, leap_p, moat_m, wtp_w, score_justification,
unique_data_capture, commoditization_risk, regulatory_notes, competitors, competitor_gap,
source_urls, founder_feasibility, review_notes, duplicate_of, fix
```

**Scores.** Re-judge every score on the 1–5 rubric. Do not just rescale the old numbers.

**status:**
- `RECOMMENDED`: still a good 2026 bet.
- `CAUTION`: viable, but a real risk such as heavy competition or regulation.
- `OUTDATED`: the premise is gone. A free incumbent or a general AI assistant now does it well, the regulation it relied on changed, or the market/vendor named is dead. Say which in `review_notes`.
- `SKIP`: a duplicate of another idea, or a bad idea such as unlicensed legal or medical advice, or an unworkable business. Set `duplicate_of` to the other idea's id when it is a duplicate.

The gates still apply: RECOMMENDED needs the mean score ≥ 3.5 and E ≥ 3.

**source_urls:** at least 1 real URL, ideally 2–3, supporting your verdict (competitor homepage, demand thread, regulation page).

**unique_data_capture:** rewrite it so it names the specific dataset. No generic filler such as "Rate/pricing comparison data".

**fix:** an object holding replacement text, only for fields that are wrong. Allowed keys: `tagline`, `problem`, `solution`, `target_audience`, `business_model`, `pricing`. Use it when:
- A field is corrupted. Some legacy rows have shifted columns: `pricing` holding audience text, `problem` holding several merged fields with commas, or `target_audience` holding a search phrase.
- A field has stale facts.
- A non-SKIP idea's `problem` is under 250 characters or its `solution` is under 400. Rewrite these to meet the bar.

If nothing needs fixing, use `{}`.
