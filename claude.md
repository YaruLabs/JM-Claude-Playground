# Startup Ideation System - LEAP Framework

## Project Overview
This project generates 300 high-quality, AI-buildable startup ideas for solo founders using the LEAP framework. Each idea is validated through market research, keyword analysis, and pain point discovery.

## LEAP Framework Definition

| Metric | Definition | Target | Scoring (1-5) |
|--------|------------|--------|---------------|
| **L - Leverage** | Can AI do 90% of the heavy lifting? Is this a tool vs wrapper? | High | 5 = AI handles everything, 1 = Heavy manual work |
| **E - Ease** | Can the MVP be built in < 2 weeks? | High | 5 = Days, 3 = 2 weeks, 1 = Months |
| **A - Audience** | Is there existing search volume/demand? No "education" marketing needed | High | 5 = 10K+ searches, 3 = 1K+, 1 = <500 |
| **P - Platform** | Does it leverage a platform multiplier? (App Store, OpenAI Store, Chrome, etc.) | High | 5 = Strong platform fit, 1 = No platform |

### LEAP Score Calculation
```
LEAP Score = (L + E + A + P) / 4
Minimum viable score: 3.5/5 for inclusion
Target score: 4.0+/5 for top-tier ideas
```

## Validation Gate (Ghost Test)
Before any idea is marked "production ready":
1. Create landing page or mock listing
2. Run $200-$1500 in ads
3. **Pass criteria:**
   - CTR >= 2%
   - Waitlist Conversion >= 10%
4. If criteria not met, idea is killed or pivoted

## Project Structure

```
/startup-ideation-system/
├── claude.md                    # This file - project configuration
├── PLAN.md                      # Detailed implementation plan
├── CHECKLIST.md                 # Phase checklist and status
├── /data/
│   ├── ideas.csv                # Main spreadsheet with 300 ideas
│   ├── sources.json             # 100+ research sources database
│   ├── pain-points.json         # Collected pain expressions
│   └── keywords.json            # Keyword research data
├── /docs/
│   ├── LEAP-framework.md        # Framework documentation
│   ├── research-methodology.md  # How ideas are sourced
│   └── vibe-coding-guide.md     # Implementation guidance
└── /phases/
    ├── phase-1-research/        # Source collection
    ├── phase-2-first-10/        # Initial 10 ideas
    ├── phase-3-next-40/         # Ideas 11-50
    ├── phase-4-next-50/         # Ideas 51-100
    ├── phase-5-next-50/         # Ideas 101-150
    └── phase-6-final-150/       # Ideas 151-300
```

## Idea Schema (Spreadsheet Columns)

Each startup idea includes:

### Core Fields
- `id`: Unique identifier (IDEA-001 to IDEA-300)
- `title`: Short, memorable name
- `tagline`: One-sentence pitch
- `category`: Primary category
- `subcategory`: Specific niche

### Description Fields
- `problem`: The pain point being solved (2-3 sentences)
- `solution`: How the product solves it (2-3 sentences)
- `target_audience`: Specific who this is for
- `unique_value`: Why this beats alternatives
- `business_model`: How it makes money (subscription, freemium, etc.)
- `pricing_suggestion`: Recommended price point

### LEAP Evaluation
- `leap_leverage`: Score 1-5 with justification
- `leap_ease`: Score 1-5 with justification
- `leap_audience`: Score 1-5 with justification
- `leap_platform`: Score 1-5 with justification
- `leap_total`: Average score
- `platform_target`: Which platform (OpenAI Store, Chrome, iOS, etc.)

### Market Research
- `search_volume_primary`: Monthly searches for main keyword
- `keyword_difficulty`: 0-100 scale
- `competitor_count`: Number of direct competitors
- `competitor_gaps`: What competitors are missing
- `tam_estimate`: Total addressable market
- `sam_estimate`: Serviceable addressable market

### Pain Point Evidence
- `pain_expressions`: Array of verbatim quotes from users
- `pain_sources`: Where pain points were found
- `pain_frequency`: How often problem is mentioned
- `pain_intensity`: Emotional intensity (low/medium/high)

### Source Links
- `source_reddit`: Reddit threads/posts
- `source_reviews`: G2/Capterra reviews
- `source_forums`: Forum discussions
- `source_market`: Market research links

### Keyword Research
- `keyword_primary`: Main target keyword
- `keyword_secondary`: Supporting keywords (array)
- `keyword_longtail`: Long-tail opportunities (array)
- `keyword_questions`: Question-based keywords (array)

### Vibe Coding Path
- `tech_stack`: Recommended technologies
- `ai_tools`: Claude Code, Cursor, etc.
- `mvp_features`: Core features for MVP (3-5 items)
- `week_1_plan`: What to build in week 1
- `week_2_plan`: What to build in week 2
- `no_code_alternative`: Bubble, Lovable, etc. option
- `security_notes`: Important security considerations

### Metadata
- `phase`: Which phase it was created in
- `status`: draft/validated/approved
- `created_date`: When idea was generated
- `validation_status`: ghost_test_pending/passed/failed

## Research Sources Categories

### Pain Point Discovery (25+ sources)
- Reddit communities (r/Entrepreneur, r/SaaS, r/startups, etc.)
- Q&A platforms (Quora, Stack Exchange)
- Review platforms (G2 1-3 star reviews, Capterra)
- Job platforms (Upwork recurring jobs, Fiverr gigs)

### Keyword & SEO Research (25+ sources)
- AnswerThePublic, AlsoAsked
- Semrush, Ahrefs, Ubersuggest
- Google Trends, Exploding Topics
- Search Console data

### Market Intelligence (25+ sources)
- Crunchbase, AngelList, Product Hunt
- Statista, IBISWorld industry reports
- IndieHackers success stories
- BigIdeasDB, StartupIdeasDB

### Platform & Vibe Coding (25+ sources)
- OpenAI GPT Store, ChatGPT Apps
- Chrome Extension Store
- App Store/Play Store trends
- Cursor, Claude Code, Lovable docs

## Phase Deliverables

### Phase 1: Research & Setup
- [ ] 100+ sources compiled and categorized
- [ ] LEAP framework documented
- [ ] Data schema finalized
- [ ] Spreadsheet template created

### Phase 2: First 10 Ideas (Proof of Concept)
- [ ] 10 fully documented ideas
- [ ] Each scores 3.5+ on LEAP
- [ ] Complete pain point evidence
- [ ] Full keyword research
- [ ] Vibe coding paths defined

### Phase 3-6: Scale to 300
- Phase 3: Ideas 11-50 (40 ideas)
- Phase 4: Ideas 51-100 (50 ideas)
- Phase 5: Ideas 101-150 (50 ideas)
- Phase 6: Ideas 151-300 (150 ideas)

## Quality Gates

### Minimum Requirements per Idea
- Pain expressions: 5+ verbatim quotes
- Source links: 8+ valid URLs
- Primary keyword: 500+ monthly searches
- LEAP total score: 3.5+/5
- MVP buildable: < 2 weeks
- AI leverage: 90%+ automatable

### Category Distribution Target
- AI/ML Tools: 20% (60 ideas)
- SaaS/Productivity: 18% (54 ideas)
- Creator Economy: 12% (36 ideas)
- B2B Services: 15% (45 ideas)
- Developer Tools: 10% (30 ideas)
- Vertical SaaS: 15% (45 ideas)
- Emerging/Other: 10% (30 ideas)

## Commands and Workflows

### Generating Ideas
1. Mine pain points from sources
2. Cluster similar problems
3. Evaluate against LEAP framework
4. Research keywords and market
5. Design vibe coding path
6. Compile into spreadsheet

### Validating Ideas (Ghost Test)
1. Create Carrd/Webflow landing page
2. Set up Meta/Google ads ($200-$1500)
3. Track CTR and conversions
4. Pass: CTR >= 2%, Conversion >= 10%
5. Mark status accordingly

## Important Notes

- All ideas must be grounded in real market research
- No speculative or "wouldn't it be cool if" ideas
- Every claim needs a source link
- Focus on problems people are ALREADY paying to solve
- Prioritize platform multipliers (ChatGPT Store, Chrome, etc.)
- Solo founder feasibility is mandatory

---

## Key Learnings & Constraints (Updated Phase 3+)

### Solopreneur Feasibility Requirements

Every idea MUST be achievable by a normal solopreneur with:
- **Time**: Can build MVP in evenings/weekends over 1-2 weeks
- **Skills**: Basic web dev or willingness to learn vibe coding
- **Budget**: < $100/month in tools and hosting
- **No specialized knowledge**: Shouldn't require domain expertise (medical, legal licenses, etc.)

### Ease Score Requirements (CRITICAL)

**All ideas must have Ease score of 4-5:**

| Score | Meaning | Acceptable? |
|-------|---------|-------------|
| 5 | Build in 1-3 days | ✅ Yes |
| 4 | Build in 1 week | ✅ Yes |
| 3 | Build in 2 weeks | ⚠️ Only if exceptional |
| 2 | Build in 1 month | ❌ No |
| 1 | Build in 2+ months | ❌ No |

### Tech Stack Constraints

**ALLOWED (vibe-codeable):**
- Next.js + Supabase + Vercel (standard stack)
- Chrome extensions with Plasmo/WXT
- Shopify/Slack apps with their SDKs
- Claude/OpenAI API for AI features
- Simple mobile with Expo/React Native
- No-code: Bubble, Lovable, Softr + Airtable

**NOT ALLOWED:**
- Custom ML model training
- Complex infrastructure (Kubernetes, microservices)
- Hardware or IoT components
- Blockchain/Web3 (complex and regulated)
- Anything requiring enterprise sales cycle
- Regulated industries requiring licenses

### Duplicate Prevention Rules

**Before adding any idea, verify it doesn't overlap with existing ideas:**

1. Check title isn't similar to existing idea
2. Check core problem/solution isn't already covered
3. If similar niche, ensure differentiation is substantial
4. Different audience for same tool = OK (e.g., CRM for realtors vs CRM for coaches)
5. Same audience with different tool = OK (e.g., email tool vs social tool for creators)

### Ideas Already Covered (DO NOT DUPLICATE)

**AI Tools (covered):**
- Meeting transcription/notes (MeetingMind)
- Email summarization (InboxDigest)
- Email reply writing (ReplyGPT)
- Webpage summarization (SummaryTab)
- Code review automation (CodeReviewBot)
- ChatGPT history export (ChatExport)
- Meeting prep/briefing (MeetingPrep)
- Screenshot data extraction (ScreenshotAI)
- Brand voice content (BrandVoice)
- Competitor monitoring (CompetitorWatch)

**SaaS/Productivity (covered):**
- Data insights from spreadsheets (DataStory)
- Form building (FormGenius)
- HR policy generation (PolicyWriter)
- AI invoicing (InvoiceMagic)
- Meeting scheduling (ScheduleGenius)
- Customer feedback aggregation (FeedbackLoop)
- Employee onboarding (OnboardFlow)
- Pitch deck review (PitchPolish)

**Creator Economy (covered):**
- Podcast repurposing (ClipGenius)
- Testimonial collection (ProofPilot)
- Content calendar planning (ContentCal)
- Twitter thread generation (ThreadMaster)
- YouTube thumbnail testing (ThumbnailTest)
- Newsletter writing (NewsletterGrow)
- LinkedIn content (LinkedInGhost)
- Quote graphics (QuoteGraphic)

**B2B Services (covered):**
- SOC 2 compliance (ComplianceBot)
- Accountant client portal (ClientSync)
- Review response writing (ReviewReply)
- Job description writing (JobDescAI)
- SOP generation (SOPWriter)
- Cold email writing (ColdEmailAI)

**Developer Tools (covered):**
- API documentation (DocuAPI)
- Freelancer proposals (ProposalPro)
- Bug report formatting (BugReportAI)
- Changelog generation (ChangelogAI)
- Error message explanation (ErrorExplain)
- Regex generation (RegexHelper)

**E-commerce (covered):**
- Product descriptions Shopify (ShopifyDescribe)
- Review request automation (ReviewBoost)
- Abandoned cart recovery (AbandonedWin)
- Inventory prediction (InventoryAlert)

**Vertical SaaS (covered):**
- Real estate CRM (AgentCRM)
- Freelancer contracts (LegalDraft)
- AI tutoring (TutorBot)
- Restaurant menus (MenuMaker)
- Workout planning (GymPlan)
- Pet health triage (PetCareAI)
- Lease review for renters (RentalReview)
- Wedding planning (WeddingPlan)

---

## Progress Tracking

### Completed
- [x] Phase 1: Research & Setup (104 sources)
- [x] Phase 2: Ideas 1-10 (10 ideas, avg LEAP 4.125)
- [x] Phase 3: Ideas 11-50 (40 ideas, all Ease 4-5)

### In Progress
- [ ] Phase 4: Ideas 51-100 (50 ideas)

### Pending
- [ ] Phase 5: Ideas 101-150 (50 ideas)
- [ ] Phase 6: Ideas 151-300 (150 ideas)
