# LEAP Framework - Startup Idea Evaluation Guide

## Overview

The LEAP framework is a systematic approach to evaluating startup ideas specifically designed for solo founders building AI-powered products. It emphasizes speed-to-market, AI leverage, and platform distribution.

## The Four Pillars

### L - Leverage (Can AI do 90% of the heavy lifting?)

**Definition:** Measures how much of the core value creation can be automated by AI, making it feasible for a solo founder to deliver enterprise-level value.

**Key Question:** Is this a genuine AI-powered tool or just an API wrapper?

**Scoring Guide:**

| Score | Description | Examples |
|-------|-------------|----------|
| **5** | AI handles everything - user just provides input | Content generator, code assistant, data analyzer |
| **4** | AI handles 80%+ with minimal human intervention | Semi-automated workflow tools |
| **3** | AI handles 50-80%, significant human work still needed | AI-assisted tools requiring expert review |
| **2** | AI handles less than 50%, mostly human-driven | Manual processes with AI suggestions |
| **1** | Minimal AI involvement, mostly traditional software | Standard CRUD apps with no AI |

**What High Leverage Looks Like:**
- The AI generates the core deliverable (content, analysis, recommendations)
- User's role is to provide input and approve/edit output
- Can handle 100x more volume than a human doing it manually
- The "wrapper" adds genuine value through prompts, UX, and workflows

**Red Flags:**
- "We use AI for [one small feature]"
- Requires extensive human review for every output
- AI is bolted on rather than central to value proposition

---

### E - Ease (Can MVP be built in < 2 weeks?)

**Definition:** Measures how quickly a solo founder can build a working MVP using vibe coding tools (Claude Code, Cursor, Lovable, etc.).

**Key Question:** Can I ship something valuable in two weeks or less?

**Scoring Guide:**

| Score | Time to MVP | Complexity Level |
|-------|-------------|------------------|
| **5** | 1-3 days | Landing page + single core feature |
| **4** | 1 week | 3-5 features, simple integrations |
| **3** | 2 weeks | Full MVP with payment, auth, core workflows |
| **2** | 1 month | Complex integrations, multiple APIs |
| **1** | 2+ months | Custom ML models, significant infrastructure |

**What High Ease Looks Like:**
- Can use existing APIs (OpenAI, Anthropic, etc.) vs training custom models
- Standard tech stack (Next.js, Supabase, Vercel)
- No complex compliance requirements (HIPAA, SOC2, etc.)
- No hardware or physical product components

**Recommended Tech Stacks by Ease Score:**

**Score 5 (Days):**
- Lovable.dev + OpenAI API
- Bolt.new + Supabase
- v0 + Vercel

**Score 4 (1 week):**
- Next.js + Supabase + OpenAI API
- Cursor + Claude Code

**Score 3 (2 weeks):**
- Full-stack with Stripe, Auth, Database
- Multiple API integrations

**Red Flags:**
- Requires custom ML model training
- Complex regulatory compliance needed
- Hardware or IoT components
- Enterprise-grade security requirements upfront

---

### A - Audience (Is there existing search volume/demand?)

**Definition:** Measures whether people are actively searching for solutions to this problem. The goal is to ride existing demand, not create new demand through "education" marketing.

**Key Question:** Are people already searching for this, or do I have to convince them they need it?

**Scoring Guide:**

| Score | Monthly Search Volume | Demand Signal |
|-------|----------------------|---------------|
| **5** | 10,000+ searches/mo | Strong existing demand, active communities |
| **4** | 5,000-10,000 | Good demand with growing trends |
| **3** | 1,000-5,000 | Moderate demand, niche audience |
| **2** | 500-1,000 | Limited demand, may need education |
| **1** | <500 | Minimal search volume, speculative |

**What High Audience Looks Like:**
- Primary keyword has 1,000+ monthly searches
- People are searching for "[category] software" or "[competitor] alternative"
- Active Reddit/forum discussions about this problem
- Existing competitors (proves market exists)
- Commercial intent keywords (CPC > $1)

**Demand Validation Methods:**
1. Google Keyword Planner - Monthly search volume
2. Semrush/Ahrefs - Keyword difficulty and trends
3. Reddit - Pain point posts with high engagement
4. G2/Capterra - Review volume for competitors
5. Google Trends - Trend direction (growing vs declining)

**Red Flags:**
- No one is searching for solutions to this problem
- "I'll need to educate the market"
- Only competitor mentions are from 3+ years ago
- Declining search trends

---

### P - Platform (Does it leverage a platform multiplier?)

**Definition:** Measures whether the product can be distributed through an existing platform with built-in discovery (ChatGPT App Store, Chrome Store, Shopify, etc.) rather than relying solely on cold outbound marketing.

**Key Question:** Can I tap into an existing distribution channel with millions of users?

**Scoring Guide:**

| Score | Platform Fit | Distribution Potential |
|-------|-------------|----------------------|
| **5** | Perfect fit for major platform (ChatGPT Apps, Chrome) | 100M+ potential reach |
| **4** | Good fit for platform (Slack, Shopify, Notion) | 10M+ potential reach |
| **3** | Possible platform play with some work | 1M+ potential reach |
| **2** | Weak platform fit, mostly direct marketing | Limited platform discovery |
| **1** | No platform, 100% outbound marketing | Zero platform distribution |

**Platform Options (Ranked by Reach):**

| Platform | Audience Size | Best For | Discovery |
|----------|--------------|----------|-----------|
| ChatGPT App Store | 800M+ weekly | AI agents, productivity | In-chat recommendations |
| Chrome Extension Store | 3B+ Chrome users | Browser utilities | Search, featured |
| OpenAI GPT Store | 200M+ users | Custom GPTs | Categories, search |
| Slack App Directory | 30M+ daily | B2B tools | Workspace admins |
| Shopify App Store | 4M+ merchants | E-commerce | App store search |
| Notion Templates | 100M+ users | Productivity | Template gallery |
| Zapier Integrations | 10M+ users | Automation | Integration directory |
| Figma Community | 4M+ designers | Design tools | Community search |

**What High Platform Looks Like:**
- Natural fit for platform's use case
- Can be discovered through platform search/browse
- Platform's audience aligns with target customer
- Platform provides built-in trust (reviews, installs count)

**Red Flags:**
- Product doesn't fit any existing platform
- Would be awkward/forced to put on platform
- Target audience doesn't use that platform
- Platform has saturated category

---

## LEAP Score Calculation

### Formula
```
LEAP Score = (L + E + A + P) / 4
```

### Thresholds

| Score Range | Rating | Recommendation |
|-------------|--------|----------------|
| **4.5 - 5.0** | Exceptional | Top priority - pursue immediately |
| **4.0 - 4.4** | Strong | High confidence - develop with priority |
| **3.5 - 3.9** | Viable | Worth pursuing with noted caveats |
| **3.0 - 3.4** | Marginal | Consider pivoting or strengthening weak areas |
| **< 3.0** | Reject | Does not meet minimum bar |

### Minimum Viable Score: 3.5

Ideas scoring below 3.5 should be rejected or significantly pivoted before inclusion.

---

## Validation Gate: The Ghost Test

Before committing significant development time to any idea, run a "Ghost Test":

### Setup (2-4 hours)
1. Create landing page (Carrd, Webflow, or Framer)
2. Write compelling copy targeting the pain point
3. Add email capture for waitlist
4. Create simple Meta or Google ad ($200-$1500 budget)

### Metrics to Track
- **CTR (Click-Through Rate):** Ad clicks / impressions
- **Waitlist Conversion:** Email signups / landing page visitors

### Pass/Fail Criteria

| Metric | Pass | Fail |
|--------|------|------|
| CTR | >= 2% | < 2% |
| Waitlist Conversion | >= 10% | < 10% |

### Decision Matrix

| CTR | Conversion | Action |
|-----|------------|--------|
| Pass | Pass | **Proceed with development** |
| Pass | Fail | Iterate on landing page messaging |
| Fail | Pass | Iterate on ad creative/targeting |
| Fail | Fail | **Kill or significantly pivot the idea** |

---

## Scoring Examples

### Example 1: AI Resume Writer for Tech Professionals

| Dimension | Score | Justification |
|-----------|-------|---------------|
| L - Leverage | 5 | AI generates entire resume from job posting + profile |
| E - Ease | 5 | Can build with Claude API + Next.js in 3-4 days |
| A - Audience | 4 | "AI resume writer" has 6,500 monthly searches |
| P - Platform | 4 | Good fit for ChatGPT App Store |
| **Total** | **4.5** | **Exceptional - pursue immediately** |

### Example 2: Local Restaurant Inventory Management

| Dimension | Score | Justification |
|-----------|-------|---------------|
| L - Leverage | 2 | AI helps with predictions but heavy manual input |
| E - Ease | 2 | Requires POS integrations, inventory scanning |
| A - Audience | 3 | 2,100 monthly searches, established market |
| P - Platform | 2 | No clear platform play |
| **Total** | **2.25** | **Reject - doesn't meet criteria** |

### Example 3: Chrome Extension for Email Summarization

| Dimension | Score | Justification |
|-----------|-------|---------------|
| L - Leverage | 5 | AI summarizes entire email threads automatically |
| E - Ease | 4 | Chrome extension + Claude API, 1 week build |
| A - Audience | 4 | "Email summarizer" has 5,400 monthly searches |
| P - Platform | 5 | Perfect fit for Chrome Web Store (3B users) |
| **Total** | **4.5** | **Exceptional - pursue immediately** |

---

## Common Pitfalls to Avoid

### 1. "Wrapper Syndrome"
Just wrapping an API without adding value. The wrapper must provide:
- Better UX than calling the API directly
- Domain-specific prompts and workflows
- Integrations that matter to the audience

### 2. "Education Market"
Building for a problem people don't know they have. Signs:
- No search volume for the problem
- Have to explain why they need it
- "Once they see it, they'll love it"

### 3. "Platform Forcing"
Forcing a product onto a platform where it doesn't fit naturally.
- Ask: "Would this feel native on this platform?"
- If it would be awkward, find a better distribution channel

### 4. "Over-Engineering"
Building more than needed for validation.
- MVP should prove value, not be production-ready
- Vibe code the core feature, polish later

---

## Quick Reference Checklist

Before adding an idea to the database, confirm:

- [ ] **Leverage:** Can AI do 90%+ of the work?
- [ ] **Ease:** Can I build MVP in 2 weeks or less?
- [ ] **Audience:** Is there 1,000+ monthly searches?
- [ ] **Platform:** Is there a natural distribution channel?
- [ ] **Score:** Does it score 3.5+ overall?
- [ ] **Pain:** Are there 5+ verbatim pain expressions?
- [ ] **Sources:** Are there 8+ valid source links?

If any answer is "No," the idea needs refinement before inclusion.
