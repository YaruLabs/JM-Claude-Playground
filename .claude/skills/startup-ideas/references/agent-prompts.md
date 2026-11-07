# Agent prompts for the startup-ideas pipeline

The skill hands these prompts to the Agent tool. Replace `<…>` placeholders. Every agent:
- works only from files and receipts;
- never invents URLs, quotes, prices or revenue;
- marks estimates with "est.";
- uses `python3 .claude/skills/startup-ideas/scripts/oppo.py search "<query>"` for web research, which is cached and budgeted, instead of free-form searching where possible.

## A. Clustering agent (stage 2)

> Read `<batch file(s)>` in `data/opportunities/work/`. Each line is one complaint written by a real person.
>
> Group the complaints into **problem clusters**: the same underlying job-to-be-done, the same kind of person, the same market. Rules:
> - Cluster by problem, not by product idea. Discard rows that are not complaints (ads, news, generic chat).
> - Give each cluster an `id` ("C" plus a short slug), a `label` of 4–8 words describing the *problem*, a `market` (TH/US/UK/GLOBAL) and a `segment`.
> - Add `keywords`: 3–8 search terms a sufferer would type, in the market's language (Thai for Thai locals).
> - For US money and finance clusters, add `cfpb_terms`: 1–3 single words.
> - List `pain_ids`. A cluster may have a single pain; recounting happens in code.
> - Merge into an existing cluster when it is the same problem. Read `data/opportunities/clusters.json` first.
>
> Write a JSON array to `data/opportunities/work/clusters_<date>.json`, then run
> `python3 .claude/skills/startup-ideas/scripts/oppo.py import-clusters <that file>`. Report the top 10 clusters by sufferers.

## B. Card-drafting agent (stage 5, the "scout")

> For each cluster id in `<ids>`:
> 1. Run `oppo.py card <id>`.
> 2. Fill `data/opportunities/cards/<id>.json` following `.claude/skills/startup-ideas/references/rubrics.md`.
>
> Fill these fields:
> - **money.incumbents:** at least 3 businesses or fixers that people already pay to solve this. Each needs a price or a revenue figure **and** an `evidence_url` you actually opened: a pricing page, a listing, a job ad paying a human, or a marketplace gig.
> - **money:** price, billing, gross_margin, months_retained_est and cac_est. These are estimates, so label your reasoning in `sources`.
> - **offer:** a one-line offer, a price point, a guarantee and a deposit amount.
> - **audience.statement:** "This is for … who want … it helps them get …".
> - **reach.channels:** named places the founder can post in, with URLs and estimated reach. Read `data/opportunities/founder_box.json`.
> - **agent_ops:** use the function-by-function breakdown in rubrics.md. Name every human-only task.
> - **risks:** answer every boolean. Use `null` only if you truly could not check.
> - **build:** mvp_days_est, next_test and next_test_cost_thb.
>
> Set `drafted_by: "scout"`. Do NOT set the gate or rung; code does that. Then run `oppo.py gate <ids>`.

## C. Panel review (stage 5b, blind)

The skill launches one agent per lens. The default is three: `hormozi-lens` (money), `levels-lens` (automation) and `godin-lens` (trust/reach). With `--full-panel` it launches all seven. Each lens reviews every card that passed or is incomplete. The reviewers did not draft the cards.

> Read your persona at `.claude/agents/<lens>.md` and adopt it. Then read every card in `data/opportunities/cards/` whose `gate.result` is PASS or INCOMPLETE.
>
> For each card:
> - Append `{"lens": "<lens>", "verdict": "go" | "fix" | "kill", "note": "<=40 words"}` to its `panel` array.
> - If you find a factual error (fake incumbent, wrong price, a free alternative the scout missed), fix that field, add your evidence URL to `sources`, and say so in your note.
> - Do not touch `gate`, `evidence_rung` or other lenses' entries.
>
> Then run `oppo.py gate`.

## D. Test-kit agent (stage 7, after the founder picks)

> For card `<id>`, build a reality-test kit in `data/opportunities/tests/<id>/`:
> 1. `index.html`: a one-page offer in the card's language (Thai and English for TH). It includes the one-liner, who it's for, what they get, the price, the guarantee, and a **deposit button** with placeholder `{{PAYMENT_LINK}}` (Stripe Payment Link, or Opn/PromptPay QR for Thailand).
>    - Make no fake testimonials, fake counts or fake urgency.
> 2. `posts.md`: 3 posts for each channel listed in `reach.channels`, written in the founder's voice for the founder to post personally. Add a DM template for 10 hand-reached sufferers drawn from the card's `top_quotes` platforms. Include no automated or bulk outreach.
> 3. `plan.md`:
>    - test window: 14 days
>    - thresholds: at least 100 reached and at least 3 deposits
>    - the ad cap: ฿5,000, and only if warm posts reach fewer than 300 people
>    - the daily logging command: `oppo.py test log <id> --reached N --visits N --deposits N ...`
>
> Tell the founder exactly which 3 things they must do by hand: create the payment link, post, and reply to DMs.

## E. Weekly review (stage 9)

> Run:
> - `oppo.py gate`
> - `oppo.py rank`
> - `oppo.py test eval <id>` for each active test
> - `oppo.py ledger stats <product> --weeks 4` for each live product
>
> Then write `data/opportunities/reports/weekly-<date>.md`, covering:
> - keep/kill verdicts due today;
> - the products below 80% agent share, with the human tasks to automate next;
> - which harvest sources produced the cards that reached L3 or above.
>
> Propose query changes to `references/queries.json` that would put more weight on the productive sources.
