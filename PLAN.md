# Startup Ideation System - Detailed Implementation Plan

## Executive Summary

This plan outlines the systematic generation of **300 high-quality, AI-buildable startup ideas** for solo founders using the **LEAP framework**. Each idea is grounded in real market research, validated pain points, keyword data, and includes a practical "vibe coding" implementation path.

---

## Table of Contents

1. [LEAP Framework Deep Dive](#1-leap-framework-deep-dive)
2. [Research Methodology](#2-research-methodology)
3. [Phase 1: Research & System Setup](#3-phase-1-research--system-setup)
4. [Phase 2: First 10 Ideas (Proof of Concept)](#4-phase-2-first-10-ideas)
5. [Phase 3-6: Scaling to 300](#5-phases-3-6-scaling-to-300)
6. [Quality Assurance](#6-quality-assurance)
7. [Deliverables Checklist](#7-deliverables-checklist)
8. [Sources Database](#8-sources-database)
9. [Risk Mitigation](#9-risk-mitigation)

---

## 1. LEAP Framework Deep Dive

### 1.1 Framework Definition

| Dimension | Question | What "High" Means | Scoring Guide |
|-----------|----------|-------------------|---------------|
| **L - Leverage** | Can AI do 90% of the heavy lifting? | The product is primarily AI-powered, not just an API wrapper. AI generates core value. | 5: Full AI automation<br>4: 80%+ AI<br>3: 50-80% AI<br>2: <50% AI<br>1: Minimal AI |
| **E - Ease** | Can MVP be built in < 2 weeks? | Using vibe coding (Claude Code, Cursor), a working MVP ships fast. | 5: 1-3 days<br>4: 1 week<br>3: 2 weeks<br>2: 1 month<br>1: 2+ months |
| **A - Audience** | Existing search volume/demand? | People are actively searching for this solution. No "education" marketing. | 5: 10K+ searches/mo<br>4: 5K-10K<br>3: 1K-5K<br>2: 500-1K<br>1: <500 |
| **P - Platform** | Platform multiplier available? | Can distribute via ChatGPT Store, Chrome Store, App Stores, etc. | 5: Perfect platform fit<br>4: Good fit<br>3: Possible fit<br>2: Weak fit<br>1: No platform |

### 1.2 LEAP Score Calculation

```
LEAP Score = (L + E + A + P) / 4

Thresholds:
- 4.5-5.0: Exceptional - Top priority ideas
- 4.0-4.4: Strong - High confidence ideas
- 3.5-3.9: Viable - Worth pursuing with caveats
- <3.5: Rejected - Does not meet minimum bar
```

### 1.3 Platform Multiplier Options (for P score)

| Platform | Audience Size | Discovery Mechanism | Best For |
|----------|--------------|---------------------|----------|
| **ChatGPT App Store** | 800M+ weekly users | In-chat recommendations, search | AI agents, productivity tools |
| **Chrome Extension Store** | 3B+ Chrome users | Search, recommendations | Browser utilities, productivity |
| **OpenAI GPT Store** | 200M+ ChatGPT users | Categories, featured | Custom GPTs, niche assistants |
| **Slack App Directory** | 30M+ daily users | Workspace admins | B2B productivity, integrations |
| **Shopify App Store** | 4M+ merchants | App store search | E-commerce tools |
| **iOS/Android App Store** | 1.5B+/3B+ users | ASO, ads | Consumer apps |
| **Notion Templates** | 100M+ users | Template gallery | Productivity templates |
| **Zapier/Make Integrations** | 10M+ users | Integration directory | Automation connectors |

### 1.4 Validation Gate (Ghost Test)

Before committing significant development time:

**Setup:**
1. Create landing page (Carrd, Webflow, or Framer - 2-4 hours)
2. Write compelling copy targeting pain point
3. Add email capture for waitlist
4. Create simple Meta or Google ad ($200-$1500 budget)

**Metrics to Track:**
- **CTR (Click-Through Rate)**: Ad clicks / impressions
- **Waitlist Conversion**: Email signups / landing page visitors

**Pass/Fail Criteria:**
| Metric | Pass | Fail |
|--------|------|------|
| CTR | >= 2% | < 2% |
| Waitlist Conversion | >= 10% | < 10% |

**Outcome:**
- **Both pass**: Proceed with development
- **One fails**: Iterate on messaging/positioning
- **Both fail**: Kill or pivot the idea

---

## 2. Research Methodology

### 2.1 Pain Point Discovery Framework

```
Source Type → Extraction Method → Validation → Documentation

Reddit/Forums → Search pain keywords → Count mentions → Verbatim quotes
G2/Capterra → Mine 1-3 star reviews → Cluster themes → Feature gaps
Upwork/Fiverr → Analyze recurring jobs → Frequency check → Job descriptions
Google → "How to" queries → Search volume → Question keywords
```

### 2.2 Pain Point Keywords to Search

```
Frustration signals:
- "I hate when..."
- "Why can't I just..."
- "So frustrated with..."
- "Waste of time"
- "Looking for a tool that..."
- "Does anyone know a solution for..."
- "Can't believe there isn't..."
- "I spend hours every week..."

Solution-seeking signals:
- "[tool name] alternative"
- "Best way to..."
- "How to automate..."
- "[competitor] vs"
- "Tired of [process]"
```

### 2.3 Keyword Research Process

**Step 1: Seed Keywords**
- Problem terms: "how to [solve problem]"
- Solution terms: "[category] software/tool"
- Alternative terms: "[competitor] alternative"
- Pain terms: verbatim phrases from research

**Step 2: Expansion Tools**
- AnswerThePublic: Question variations
- AlsoAsked: Related query chains
- Semrush/Ahrefs: Competitor keyword gaps
- Google Autocomplete: Real-time suggestions

**Step 3: Metrics to Capture**
| Metric | Source | Threshold |
|--------|--------|-----------|
| Monthly search volume | Semrush/Ahrefs | 500+ minimum |
| Keyword difficulty | Semrush/Ahrefs | <50 preferred |
| CPC (commercial intent) | Google Ads | >$1 = buying intent |
| Search trend | Google Trends | Stable or growing |

### 2.4 Competitive Analysis Process

For each idea, analyze 3-5 existing solutions:

**Data to Collect:**
- Pricing tiers and structure
- Core features vs premium features
- G2/Capterra average rating
- Common complaints (1-3 star reviews)
- What's missing (feature requests)

**Gap Identification:**
- Price gaps: Too expensive for small users
- Feature gaps: Missing integrations or capabilities
- UX gaps: Poor onboarding or complexity
- Support gaps: Slow response, limited docs
- AI gaps: No AI features or poor AI implementation

---

## 3. Phase 1: Research & System Setup

**Duration:** 1-2 weeks
**Goal:** Compile 100+ sources, finalize framework, create templates

### 3.1 Source Collection (100+ Sources)

#### Category 1: Pain Point Discovery (25+ sources)

| Source | Type | URL | How to Use |
|--------|------|-----|------------|
| r/Entrepreneur | Reddit | reddit.com/r/Entrepreneur | Search frustration keywords |
| r/SaaS | Reddit | reddit.com/r/SaaS | Feature requests, complaints |
| r/startups | Reddit | reddit.com/r/startups | Founder pain points |
| r/smallbusiness | Reddit | reddit.com/r/smallbusiness | SMB problems |
| r/webdev | Reddit | reddit.com/r/webdev | Developer tool gaps |
| r/marketing | Reddit | reddit.com/r/marketing | Marketing tool needs |
| r/freelance | Reddit | reddit.com/r/freelance | Freelancer problems |
| Indie Hackers | Forum | indiehackers.com | Validated problems |
| Hacker News | Forum | news.ycombinator.com | Tech community needs |
| Quora | Q&A | quora.com | Question-based problems |
| Stack Overflow | Q&A | stackoverflow.com | Developer tool gaps |
| G2 Reviews | Reviews | g2.com | 1-3 star review mining |
| Capterra Reviews | Reviews | capterra.com | Feature complaints |
| TrustRadius | Reviews | trustradius.com | Enterprise feedback |
| Product Hunt | Community | producthunt.com | Shipping gaps |
| Upwork Jobs | Jobs | upwork.com | Recurring manual tasks |
| Fiverr Gigs | Jobs | fiverr.com | Service automation opps |
| Twitter/X | Social | twitter.com | Real-time complaints |
| LinkedIn | Social | linkedin.com | B2B pain points |
| YouTube Comments | Social | youtube.com | Tutorial requests |

#### Category 2: Keyword & SEO Research (25+ sources)

| Tool | Type | URL | Key Features |
|------|------|-----|--------------|
| AnswerThePublic | Questions | answerthepublic.com | Question keyword discovery |
| AlsoAsked | Questions | alsoasked.com | PAA chain mapping |
| Semrush | Full SEO | semrush.com | Volume, difficulty, gaps |
| Ahrefs | Full SEO | ahrefs.com | Backlinks, keywords |
| Ubersuggest | Free SEO | ubersuggest.com | Free keyword data |
| Keywords Everywhere | Browser ext | keywordseverywhere.com | Quick volume checks |
| Google Trends | Trends | trends.google.com | Trend direction |
| Exploding Topics | Trends | explodingtopics.com | Emerging opportunities |
| Glimpse | Trends | meetglimpse.com | Trend prediction |
| SparkToro | Audience | sparktoro.com | Audience research |
| Google Search Console | Own data | search.google.com/search-console | Actual query data |
| Google Autocomplete | Free | google.com | Real-time suggestions |
| Reddit Keyword Tool | Reddit | keywordtool.io/reddit | Reddit search volume |

#### Category 3: Market Intelligence (25+ sources)

| Source | Type | URL | Data Available |
|--------|------|-----|----------------|
| Crunchbase | Startups | crunchbase.com | Funding, competitors |
| AngelList | Startups | angel.co | Startup trends |
| Product Hunt | Launches | producthunt.com | New product trends |
| IndieHackers | Revenue | indiehackers.com | MRR data |
| Statista | Reports | statista.com | Market size |
| IBISWorld | Reports | ibisworld.com | Industry reports |
| CB Insights | Research | cbinsights.com | Trend analysis |
| BigIdeasDB | Ideas | bigideasdb.com | Validated problems |
| StartupIdeasDB | Ideas | startupideasdb.com | AI-scored ideas |
| GummySearch | Reddit | gummysearch.com | Reddit analysis |
| PainOnSocial | Pain points | painonsocial.com | Social pain mining |
| TechCrunch | News | techcrunch.com | Funding trends |
| The Hustle | Newsletter | thehustle.co | Business trends |

#### Category 4: Platform & Vibe Coding (25+ sources)

| Resource | Type | URL | Purpose |
|----------|------|-----|---------|
| ChatGPT App Store | Platform | chat.openai.com | App discovery |
| OpenAI GPT Store | Platform | chat.openai.com/gpts | GPT opportunities |
| Chrome Web Store | Platform | chrome.google.com/webstore | Extension ideas |
| Slack App Directory | Platform | slack.com/apps | B2B integrations |
| Shopify App Store | Platform | apps.shopify.com | E-commerce tools |
| Claude Code Docs | Tool | docs.anthropic.com | Vibe coding guide |
| Cursor Docs | Tool | cursor.com | AI IDE usage |
| Lovable | No-code | lovable.dev | No-code building |
| Bubble | No-code | bubble.io | Visual development |
| Replit | Tool | replit.com | Quick prototyping |
| v0 by Vercel | Tool | v0.dev | UI generation |
| Bolt | Tool | bolt.new | Full-stack gen |
| Supabase | Backend | supabase.com | Quick backend |
| Firebase | Backend | firebase.google.com | Serverless |
| Vercel | Deploy | vercel.com | Easy deployment |

### 3.2 Deliverables

- [x] claude.md - Project configuration
- [ ] PLAN.md - This document
- [ ] CHECKLIST.md - Phase tracking
- [ ] /data/sources.json - Categorized sources
- [ ] /data/ideas-template.csv - Spreadsheet structure
- [ ] /docs/LEAP-framework.md - Scoring guide
- [ ] /docs/research-methodology.md - How-to guide

---

## 4. Phase 2: First 10 Ideas

**Duration:** 1-2 weeks
**Goal:** Prove the system works with 10 fully-documented ideas

### 4.1 Category Distribution for First 10

| Category | Count | Rationale |
|----------|-------|-----------|
| AI Tools | 2 | Highest LEAP potential |
| SaaS/Productivity | 2 | Proven business model |
| Creator Economy | 2 | Large accessible audience |
| B2B Services | 2 | Higher ticket potential |
| Developer Tools | 2 | Technical founder fit |

### 4.2 Process per Idea (4-6 hours each)

```
Hour 1: Pain Point Mining
├── Search 5+ subreddits for related problems
├── Find 5+ verbatim pain expressions
├── Document sources with URLs

Hour 2: Competitive Analysis
├── Identify 3-5 existing solutions
├── Read 10+ G2/Capterra reviews
├── Document gaps and complaints

Hour 3: Keyword Research
├── Find primary keyword (500+ volume)
├── Find 5+ secondary keywords
├── Find 10+ long-tail keywords
├── Document question keywords

Hour 4: LEAP Evaluation
├── Score Leverage (1-5) with justification
├── Score Ease (1-5) with justification
├── Score Audience (1-5) with justification
├── Score Platform (1-5) with justification
├── Calculate total score (must be 3.5+)

Hour 5: Vibe Coding Path
├── Define 3-5 MVP features
├── Select tech stack
├── Write week 1 plan
├── Write week 2 plan
├── Note no-code alternative

Hour 6: Documentation
├── Write problem statement (2-3 sentences)
├── Write solution description (2-3 sentences)
├── Define target audience
├── Define business model and pricing
├── Compile all into spreadsheet row
```

### 4.3 Quality Criteria (Phase 2)

| Requirement | Minimum | Target |
|-------------|---------|--------|
| Pain expressions | 5+ | 10+ |
| Source links | 8+ | 15+ |
| Primary keyword volume | 500+ | 2,000+ |
| LEAP score | 3.5+ | 4.0+ |
| Competitors analyzed | 3+ | 5+ |
| MVP features defined | 3+ | 5+ |

### 4.4 First 10 Ideas - Target Categories

1. **AI Writing Assistant for [Niche]** - Category: AI Tools
2. **[Industry] Compliance Automation** - Category: B2B Services
3. **Content Repurposing Tool** - Category: Creator Economy
4. **API Wrapper for [Service]** - Category: Developer Tools
5. **[Profession] Client Portal** - Category: SaaS
6. **Social Proof Aggregator** - Category: Marketing
7. **Micro-SaaS for [Vertical]** - Category: Vertical SaaS
8. **AI Chatbot for [Industry]** - Category: AI Tools
9. **Freelancer Workflow Tool** - Category: Creator Economy
10. **Integration Connector** - Category: Developer Tools

---

## 5. Phases 3-6: Scaling to 300

### 5.1 Phase 3: Ideas 11-50 (40 ideas)

**Duration:** 3-4 weeks
**Approach:** Parallel processing with refined workflow

**Category Distribution:**
| Category | Count |
|----------|-------|
| AI/ML Tools | 8 |
| SaaS/Productivity | 8 |
| Creator Economy | 6 |
| B2B Services | 6 |
| Developer Tools | 4 |
| E-commerce | 4 |
| Vertical SaaS | 4 |

### 5.2 Phase 4: Ideas 51-100 (50 ideas)

**Duration:** 3-4 weeks
**Approach:** Expand into underserved niches

**Focus Areas:**
- Industry-specific SaaS (legal, healthcare, real estate)
- Local business tools
- Compliance/regulatory automation
- Emerging tech (spatial computing, voice-first)

### 5.3 Phase 5: Ideas 101-150 (50 ideas)

**Duration:** 3-4 weeks
**Approach:** Enhanced detail and validation

**Quality Uplift:**
- 10+ pain expressions per idea
- 15+ source links per idea
- Full competitive landscape
- Detailed financial model sketch

### 5.4 Phase 6: Ideas 151-300 (150 ideas)

**Duration:** 6-8 weeks
**Approach:** Final sprint with full automation

**Completion Tasks:**
- Generate 200+ candidates
- Filter to final 150
- Cross-check all source links
- Final LEAP calibration
- Complete spreadsheet export

---

## 6. Quality Assurance

### 6.1 Per-Idea Checklist

```
[ ] Problem clearly defined with real pain evidence
[ ] 5+ verbatim pain expressions documented
[ ] 8+ source links (all valid and relevant)
[ ] Primary keyword has 500+ monthly searches
[ ] LEAP score calculated with justifications
[ ] LEAP total >= 3.5
[ ] 3-5 competitors analyzed
[ ] Gap/opportunity clearly identified
[ ] Tech stack appropriate for solo founder
[ ] MVP buildable in < 2 weeks
[ ] Week-by-week plan documented
[ ] Business model and pricing defined
[ ] Platform multiplier identified (if applicable)
```

### 6.2 Batch Review Process

After each batch of 10 ideas:
1. Cross-check all URLs are valid
2. Verify keyword data accuracy
3. Ensure LEAP scores are consistent
4. Check for duplicate or overlapping ideas
5. Validate category distribution

---

## 7. Deliverables Checklist

### Phase 1 Deliverables
- [ ] 100+ research sources compiled
- [ ] LEAP framework documentation
- [ ] Spreadsheet template created
- [ ] Research methodology documented
- [ ] Project structure established

### Phase 2 Deliverables
- [ ] 10 complete startup ideas
- [ ] All ideas score 3.5+ on LEAP
- [ ] 50+ pain expressions collected
- [ ] 80+ source links documented
- [ ] 100+ keywords researched
- [ ] 10 vibe coding paths defined

### Phase 3-6 Deliverables
- [ ] Additional 290 startup ideas
- [ ] 2,000+ total pain expressions
- [ ] 3,000+ total source links
- [ ] 3,000+ total keywords
- [ ] Complete searchable spreadsheet
- [ ] Category distribution achieved

---

## 8. Sources Database

See `/data/sources.json` for the complete categorized database of 100+ research sources.

---

## 9. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Source link rot | High | Medium | Archive quotes, use Wayback Machine |
| Keyword data staleness | Medium | Medium | Refresh quarterly |
| Duplicate ideas | Medium | Low | Deduplication checks per batch |
| LEAP score inconsistency | Medium | Medium | Calibration reviews |
| Quality dilution at scale | Medium | High | Maintain strict thresholds |
| Market shifts | Low | Medium | Add "timing sensitivity" flag |

---

## Appendix A: Spreadsheet Column Reference

```csv
id,title,tagline,category,subcategory,problem,solution,target_audience,unique_value,business_model,pricing_suggestion,leap_leverage,leap_leverage_justification,leap_ease,leap_ease_justification,leap_audience,leap_audience_justification,leap_platform,leap_platform_justification,leap_total,platform_target,search_volume_primary,keyword_difficulty,competitor_count,competitor_gaps,tam_estimate,sam_estimate,pain_expressions,pain_sources,pain_frequency,pain_intensity,source_reddit,source_reviews,source_forums,source_market,keyword_primary,keyword_secondary,keyword_longtail,keyword_questions,tech_stack,ai_tools,mvp_features,week_1_plan,week_2_plan,no_code_alternative,security_notes,phase,status,created_date,validation_status
```

---

## Appendix B: Research Queries Library

### Reddit Search Queries
```
site:reddit.com "I hate" [category] software
site:reddit.com "looking for" [category] tool
site:reddit.com "frustrating" [process]
site:reddit.com "waste of time" [task]
site:reddit.com "[competitor] alternative"
site:reddit.com "does anyone know" [category]
```

### G2/Capterra Review Queries
```
site:g2.com [category] reviews
site:capterra.com [category] reviews
"1 star" [category] software
"missing features" [category]
"wish it had" [category]
```

### Question-Based Queries
```
"how to automate" [task]
"best way to" [process]
"is there a tool for" [need]
"how do I" [problem]
```

---

*This plan is a living document. Updates will be made as the project progresses.*
