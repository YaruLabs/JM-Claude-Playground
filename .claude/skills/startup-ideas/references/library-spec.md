# Idea library spec (for enrichment agents)

The public quiz site matches people to ideas by tags, with no AI call at request time. Your job is to turn researched ideas into **reader-facing entries with accurate tags**. A wrong tag sends a real person the wrong idea, so tag from what the idea says, not from what would be convenient.

You get a JSON array of ideas (fields from the v2 schema: problem, solution, pricing, competitors, demand_evidence, founder_feasibility, platform_distribution, mvp_features, review_notes …). For **each** idea, output one object with exactly these keys.

## Copy fields (plain English, written to the reader as "you")

Readers are employed professionals, many non-technical, about half in Thailand. Voice: direct, confident, practical. No hype ("insane", "game-changer"), no buzzwords, no promises of income. Use "build, ship, test, launch". Keep each field within its limit.

| Key | What | Limit |
|---|---|---|
| `id` | The idea's id, unchanged | |
| `name` | A clear product name, 2–5 words. Fix awkward legacy titles. | 40 chars |
| `one_liner` | What it is and who it's for, one sentence | 140 chars |
| `problem` | The pain, concretely: who, how often, what it costs them | 2 sentences |
| `why_it_works` | Why this is a real opportunity **now**. Use only facts already in the idea (demand evidence, what people already pay, what competitors miss). Keep "est." on estimates. Never add new numbers. | 3 sentences |
| `agent_plan` | Array of exactly 3 strings: concrete jobs AI agents do in this business (e.g. "Reads each uploaded bill and flags charges above the regional price list") | 20 words each |
| `human_part` | What you still do yourself. Be honest: licences, partnerships, sales calls, trust moments. | 1 sentence |
| `content_angle` | The content you could post to get customers: format, platform and an example topic | 1 sentence |
| `first_steps` | Array of exactly 3 strings: what to do in week one, cheapest test first | 18 words each |
| `price_hint` | The pricing in one short phrase, in the idea's local currency | 60 chars |
| `watch_out` | The biggest risk or open question, from review_notes / regulatory_notes / commoditization_risk | 1 sentence |

## Tags (the object `tags`; use only the listed values)

| Key | Values | How to decide |
|---|---|---|
| `markets` | array of `TH_LOCAL`, `TH_EXPAT`, `US`, `UK`, `GLOBAL` | Who the customers are. `GLOBAL` only if it is sold online to anyone. A TH idea for both groups gets both TH tags. EU-only ideas get `UK` only if UK customers can use it. |
| `portable` | `true` / `false` | Could a founder in another country run the same idea for their own market with modest changes? A Thai visa tool is `false`; a clinic price tracker is `true`. |
| `customer` | `consumer`, `small_business`, `professional` | Who pays. `professional` = clinics, law/accounting firms, agencies, larger companies. |
| `interests` | array of 1–3 from: `money`, `health`, `property`, `food`, `education`, `travel_expat`, `ecommerce`, `legal_paperwork`, `pets`, `mobility`, `creator`, `local_services`, `work_careers`, `family_care` | The subject area. |
| `channels` | array of 1–2 from: `content` (short video, posts), `seo` (search pages, directories), `community` (groups, forums, LINE/Facebook), `outbound` (direct sales, partnerships), `marketplace` (app stores, Shopify, LINE OA store) | How the first customers realistically arrive. |
| `tech` | `none`, `some`, `builder` | Minimum skill to ship v1 with AI coding tools. `none` = no-code/AI builders are enough; `some` = comfortable with automations and APIs; `builder` = real engineering (integrations, scraping at scale, payments logic). |
| `budget` | `1`, `2`, `3`, `4` | Money needed before first revenue. 1 = under $100 (฿3,500); 2 = up to $1,000; 3 = up to $5,000; 4 = more. Count licences, data, ads, legal. |
| `hours` | `1`, `2`, `3`, `4` | Minimum weekly hours to launch. 1 = under 5; 2 = 5–15; 3 = 15–30; 4 = full-time. |
| `goals` | array of 1–2 from: `side_income`, `replace_salary`, `scale`, `sellable_asset` | What it is best suited to. Directories and data sites are often `sellable_asset`; one-off consumer tools are `side_income`. |
| `backgrounds` | array of 1–3 from: `tech`, `marketing_content`, `sales_ops`, `finance_legal`, `health`, `property`, `hospitality`, `education`, `any` | Whose experience gives an edge. Use `any` if none is needed. |
| `agent_share` | integer 40–95 | Honest estimate of the share of ongoing work agents can do. Lower it for licensed sign-off, on-site work, sales calls, marketplaces needing supply recruitment. |
| `speed` | `weeks`, `months` | Time to a first paying customer if you work on it steadily. |
| `local_presence` | `true` / `false` | Do you need to be physically in the market (visits, local company, in-person partners)? |
| `thai_language` | `required`, `helpful`, `no` | For TH ideas serving Thai locals it is usually `required`. |

## Output

Write a JSON array, in input order, with `json.dump(..., ensure_ascii=False, indent=2)` from a Python script, to the output path in your task. Then validate it with:

```
python3 .claude/skills/startup-ideas/scripts/library.py check <your output file>
```

Fix every error it prints. Do not edit other files. Do not commit. Do no web research: everything you need is in the input.
