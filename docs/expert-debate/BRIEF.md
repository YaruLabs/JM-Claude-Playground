# Expert Panel Brief: Designing the Best Ideation System

_Shared by all seven panelists. Date: 2026-11-07._

## Who the founder is
- A solo founder running a small AI-focused company (Yaru Labs). Based in, and marketing to, **Thailand/Bangkok**, covering both Thai locals and expats. Also open to **US/UK/global** markets.
- Builds with AI coding agents (Claude Code), so a working MVP can ship in days.
- **Already holds API keys for Tavily and Perplexity.** Has a modest budget and wants the minimum number of paid APIs.
- **Goal:** find businesses that can be **~80–90% operated by AI agents** once running (acquisition, onboarding, delivery, support, billing, data ops), so one person can run several of them.

## What we built so far, and why it's not good enough
The repo (`data/`, `docs/`) holds about 1,050 ideas scored with "LEAP v2": six 1–5 scores (Leverage, Ease, Audience, Platform, Moat, Willingness to pay), averaged, with a gate at a mean of 3.5 or more. Audit findings (`docs/AUDIT-2026-11.md`, `docs/IDEAS-SUMMARY-2026-11.md`):
1. **The scores are opinions.** Model-judged numbers have no link to real outcomes.
2. **The generators scored their own ideas.**
   - New ideas: 74% RECOMMENDED.
   - Legacy ideas re-scored by a separate reviewer: about 3%.
3. **The scores barely separate ideas.** Almost all new ideas land at 3.3–3.9.
4. **Averaging hides fatal flaws.** An idea with W=1 can still pass.
5. **Research was thin.** A shared web-search budget ran out. Reddit and Pantip were mostly unreachable, so many sources are vendor blogs, and every TAM is an estimate.
6. **The process was idea-first, not problem-first.** Agents brainstormed and then looked for support, and dedup was done afterwards by title.
7. **There's no learning loop.** No idea ever met a customer.
8. **Founder fit was ignored.**

## The questions for the panel
1. **System design.** Design the end-to-end ideation system you would trust, from sourcing to filtering, ranking, validation and learning. It should be mostly automated (agents and scripts) with a few human checkpoints. Be specific about the stages, what each stage outputs, and where humans step in.
2. **Minimum APIs.** List the **smallest set of APIs/data sources** that gives agents materially better research than "web search only".
   - For each, say what it unlocks, the rough monthly cost, and what you'd cut first.
   - Include free, no-key sources (e.g. HN Algolia, CFPB, government open data).
   - Consider Thailand-specific needs: Pantip, LINE, TikTok, Thai-language search volume, the DBD business registry.
3. **Measuring "80–90% agent-operable".** How should the system estimate and verify how much of a business agents can run? Which functions are human-only today?
4. **Kill criteria.** Your top 3–5 instant-kill rules.
5. **Ranking.** If you keep any scoring at all, what is it, and how do you stop it becoming theatre?

## Rules of the debate
- Argue from **your own lens and skill** (see your persona file in `.claude/agents/`).
- Be concrete: name tools, sources, numbers and channels. Mark anything unverified "(unverified)".
- You may use **at most 4 web searches/fetches**, mainly to check API availability or pricing.
- Never put invented quotes in a real person's mouth. You are a *lens*, not the person.
