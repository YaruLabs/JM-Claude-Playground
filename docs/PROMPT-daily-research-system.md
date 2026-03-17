# Complete Prompt: Automated Daily Startup Idea Research System

## Instructions for AI Assistant

You are building an automated daily research system that generates 500 unique startup ideas (350 US market, 150 UK/Europe market). This system will run daily, discover pain points from free APIs, generate AI-powered startup ideas, score them using the LEAP framework, deduplicate against existing ideas, and append to CSV databases.

---

## Project Context

### Current State
The repository `/home/user/JM-Claude-Playground` contains:

| File | Records | Description |
|------|---------|-------------|
| `data/ideas-claude.csv` | 350 | AI-focused startup ideas (CLAUDE-001 to CLAUDE-350) |
| `data/ideas-directories.csv` | 100 | Directory/marketplace ideas (DIR-001 to DIR-100) |
| `data/ideas.csv` | 300 | Comprehensive version with 52 columns |
| `data/sources.json` | 104 | Research source database in 4 categories |

### CSV Schema (22 columns - MUST match exactly)
```
id, title, tagline, category, subcategory, problem, solution, target_audience,
business_model, pricing, leap_total, platform, tam, sam, pain_points,
tech_stack, ai_tools, mvp_features, phase, status, created_date, unique_data_capture
```

### LEAP Scoring Framework (1-5 scale)
- **L - Leverage**: Can AI do 90%+ of the work? (5 = fully automated)
- **E - Ease**: Can MVP be built in <2 weeks? (5 = 1-3 days)
- **A - Audience**: Is there existing demand? (5 = 10K+ monthly searches)
- **P - Platform**: Does it have distribution? (5 = ChatGPT/Chrome Store scale)
- **Minimum viable score**: 3.5/5 average
- **Hard requirement**: Ease must be >= 4

---

## System Architecture

### High-Level Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DAILY RESEARCH ORCHESTRATOR                         │
│                     (Python cron job / systemd timer)                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 1: DATA COLLECTION                             │
├───────────────┬───────────────┬───────────────┬───────────────┬─────────────┤
│  Reddit API   │   HN API      │ Product Hunt  │  GitHub API   │ Google      │
│  (PRAW)       │  (No auth)    │  (GraphQL)    │  (Token)      │ Trends      │
│  60 req/min   │  No limit     │  Free tier    │  5K/hr        │ (pytrends)  │
└───────────────┴───────────────┴───────────────┴───────────────┴─────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 2: PAIN POINT EXTRACTION                       │
│              (Tavily Search API + Perplexity Pro for research)               │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 3: IDEA GENERATION                             │
│                         (Claude API / Anthropic)                             │
│         - US Market Ideas (350 total target)                                 │
│         - UK/Europe Market Ideas (150 total target)                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 4: SCORING & VALIDATION                        │
├───────────────────────────────────┬─────────────────────────────────────────┤
│     LEAP Scoring (AI-automated)   │      Deduplication Engine               │
│     L: Leverage (AI capability)   │      (Against 450+ existing ideas)      │
│     E: Ease (build complexity)    │      (Semantic similarity check)        │
│     A: Audience (search volume)   │      (Title/problem matching)           │
│     P: Platform (distribution)    │                                         │
└───────────────────────────────────┴─────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 5: OUTPUT & STORAGE                            │
├───────────────────────────────────┬─────────────────────────────────────────┤
│   CSV Export (22-column schema)   │       Daily Run Reports                 │
│   Append to existing ideas.csv    │       Metrics & Statistics              │
└───────────────────────────────────┴─────────────────────────────────────────┘
```

---

## File Structure to Create

```
/home/user/JM-Claude-Playground/
├── automation/                          # NEW: Daily automation system
│   ├── __init__.py
│   ├── config.py                        # Configuration and API keys
│   ├── orchestrator.py                  # Main daily job orchestrator
│   ├── scheduler.py                     # APScheduler or systemd config
│   │
│   ├── collectors/                      # Data collection modules
│   │   ├── __init__.py
│   │   ├── reddit_collector.py
│   │   ├── hn_collector.py
│   │   ├── producthunt_collector.py
│   │   ├── github_collector.py
│   │   ├── trends_collector.py
│   │   └── base_collector.py
│   │
│   ├── processors/                      # Data processing modules
│   │   ├── __init__.py
│   │   ├── pain_extractor.py            # Extract pain points from raw data
│   │   ├── market_researcher.py         # Tavily/Perplexity research
│   │   └── trend_analyzer.py
│   │
│   ├── generators/                      # Idea generation modules
│   │   ├── __init__.py
│   │   ├── claude_generator.py          # Claude API integration
│   │   ├── leap_scorer.py               # LEAP scoring automation
│   │   ├── deduplicator.py              # Deduplication engine
│   │   └── prompts/
│   │       ├── us_market.txt
│   │       └── uk_eu_market.txt
│   │
│   ├── outputs/                         # Output management
│   │   ├── __init__.py
│   │   ├── csv_manager.py               # CSV read/write operations
│   │   ├── report_generator.py          # Daily run reports
│   │   └── validator.py                 # Final validation checks
│   │
│   └── utils/                           # Shared utilities
│       ├── __init__.py
│       ├── rate_limiter.py
│       ├── logger.py
│       └── cache.py
│
├── data/                                # EXISTING: Data storage
│   ├── ideas-claude.csv                 # Existing 350 ideas
│   ├── ideas-directories.csv            # Existing 100 directory ideas
│   ├── sources.json                     # 104 data sources config
│   ├── daily_runs/                      # NEW: Daily run archives
│   │   └── YYYY-MM-DD/
│   │       ├── raw_data.json
│   │       ├── pain_points.json
│   │       ├── candidates.json
│   │       ├── approved.csv
│   │       └── run_report.md
│   └── embeddings/                      # NEW: Cached embeddings
│       └── existing_ideas.pkl
│
├── scripts/                             # EXISTING: Utility scripts
│   ├── evaluate_ideas.py
│   └── run_daily.py                     # NEW: CLI entry point
│
├── tests/                               # NEW: Test suite
│   ├── test_collectors.py
│   ├── test_generators.py
│   ├── test_deduplication.py
│   └── fixtures/
│
├── requirements.txt                     # NEW: Dependencies
├── .env.example                         # NEW: Environment template
└── README.md                            # UPDATE: Setup instructions
```

---

## API Specifications

### 1. Reddit API (PRAW)

```python
# Target subreddits from sources.json
subreddits = [
    "Entrepreneur", "SaaS", "startups", "smallbusiness",
    "webdev", "marketing", "freelance", "sideproject",
    "EntrepreneurRideAlong", "microsaas", "nocode", "indiehackers"
]

# Search queries (from sources.json pain_types)
queries = [
    "frustrating", "looking for tool", "I wish", "waste of time",
    "feature request", "missing from", "alternative to",
    "struggle with", "advice needed", "automate"
]

# Parameters
time_filter = "week"  # or "day" for more frequent runs
sort = "hot"
limit = 100  # per subreddit
```

### 2. Hacker News API (No auth required)

```python
# Endpoints
base_url = "https://hacker-news.firebaseio.com/v0"

endpoints = [
    "/topstories.json",     # Top 500 story IDs
    "/askstories.json",     # Ask HN stories
    "/showstories.json",    # Show HN stories
]

# Filter for pain points
keywords = ["wish", "looking for", "frustrating", "problem", "need"]
```

### 3. Google Trends (pytrends)

```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

# Geographic focus
geo_us = "US"
geo_uk = "GB"
geo_eu = ["DE", "FR", "NL", "ES"]

# Trending topics
trending = pytrends.trending_searches(pn='united_states')
rising = pytrends.related_queries(kw_list, geo=geo)
```

### 4. Product Hunt API (GraphQL)

```python
url = "https://api.producthunt.com/v2/api/graphql"

query = """
query {
  posts(first: 50, order: VOTES) {
    edges {
      node {
        name
        tagline
        votesCount
        commentsCount
        topics { name }
        makers { name }
      }
    }
  }
}
"""
```

### 5. Tavily Search API

```python
from tavily import TavilyClient

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

response = client.search(
    query="[pain point] startup opportunity",
    search_depth="advanced",
    include_domains=["reddit.com", "news.ycombinator.com", "g2.com"],
    max_results=10
)
```

### 6. Claude API for Idea Generation

```python
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
You are a startup idea researcher specializing in AI-first, solo-founder buildable products.

For each pain point provided, generate a startup idea following this EXACT schema:
- id: Will be assigned by system
- title: Short, memorable product name (2-4 words)
- tagline: One-sentence value proposition (under 80 chars)
- category: One of [AI Tools, SaaS/Productivity, Creator Economy, B2B Services, Developer Tools, E-commerce, Vertical SaaS, Consumer Protection, Financial Negotiation, Legal/Rights]
- subcategory: Specific niche within category
- problem: 2-3 sentences describing the pain point with specifics
- solution: 2-3 sentences on how the product solves it, with AI mechanism
- target_audience: Specific who (not generic)
- business_model: Freemium/Subscription/Per-use/Success Fee
- pricing: Specific price points with tiers
- leap_l, leap_e, leap_a, leap_p: Scores 1-5 with justifications
- platform: Web/Mobile/Chrome Extension/etc
- tam, sam: Market size estimates
- pain_points: 3-5 verbatim expressions from research
- tech_stack: Recommended stack (Next.js + Supabase + OpenAI typical)
- ai_tools: Which AI tools to use
- mvp_features: 3-5 core features for MVP
- unique_data_capture: What proprietary data the product could collect

CRITICAL CONSTRAINTS:
- LEAP total must be >= 3.5
- Ease must be >= 4 (buildable in 1 week with vibe coding)
- Must leverage AI for 80%+ of core functionality
- Must have platform distribution opportunity
- Must not be a simple ChatGPT wrapper
"""

def generate_ideas(pain_points: list, market: str = "US") -> list:
    market_context = {
        "US": "Focus on American market dynamics, USD pricing, US regulations",
        "UK_EU": "Focus on UK/European market, GBP/EUR pricing, GDPR compliance, EU regulations"
    }

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT + f"\n\nMARKET FOCUS: {market_context[market]}",
        messages=[{
            "role": "user",
            "content": f"Generate startup ideas for these pain points:\n\n{json.dumps(pain_points, indent=2)}"
        }]
    )

    return parse_ideas_from_response(response.content)
```

---

## LEAP Scoring Automation

```python
def calculate_leap_score(idea: dict, market_data: dict) -> dict:
    """
    Automated LEAP scoring with justifications.
    Returns scores and detailed reasoning.
    """

    scores = {}

    # L - Leverage (AI capability)
    ai_indicators = [
        "AI generates", "AI analyzes", "AI automates",
        "automated", "instant", "automatically"
    ]
    solution = idea.get("solution", "").lower()
    ai_score = sum(1 for ind in ai_indicators if ind in solution)
    scores["leap_l"] = min(5, max(1, ai_score + 2))
    scores["leap_l_justification"] = f"AI handles {'90%+' if scores['leap_l'] >= 4 else '50-80%'} of core functionality"

    # E - Ease (build complexity)
    complex_indicators = ["ML model", "custom training", "hardware", "blockchain", "compliance"]
    complexity = sum(1 for ind in complex_indicators if ind in solution)
    scores["leap_e"] = 5 - complexity
    scores["leap_e_justification"] = "Standard vibe coding stack" if scores["leap_e"] >= 4 else "Requires specialized development"

    # A - Audience (search volume from Google Trends / Tavily research)
    search_volume = market_data.get("search_volume", 0)
    if search_volume >= 10000:
        scores["leap_a"] = 5
    elif search_volume >= 5000:
        scores["leap_a"] = 4
    elif search_volume >= 1000:
        scores["leap_a"] = 3
    elif search_volume >= 500:
        scores["leap_a"] = 2
    else:
        scores["leap_a"] = 1
    scores["leap_a_justification"] = f"{search_volume}+ monthly searches for primary keyword"

    # P - Platform (distribution opportunity)
    platform_keywords = {
        5: ["ChatGPT", "Chrome Extension", "GPT Store"],
        4: ["Slack", "Shopify", "Notion"],
        3: ["Web", "Mobile"],
        2: ["Desktop"],
        1: []
    }
    platform = idea.get("platform", "")
    for score, keywords in platform_keywords.items():
        if any(kw in platform for kw in keywords):
            scores["leap_p"] = score
            break
    else:
        scores["leap_p"] = 2
    scores["leap_p_justification"] = f"Distributable via {platform}"

    # Calculate total
    scores["leap_total"] = round(
        (scores["leap_l"] + scores["leap_e"] + scores["leap_a"] + scores["leap_p"]) / 4,
        2
    )

    return scores
```

---

## Deduplication Engine

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class IdeaDeduplicator:
    def __init__(self, existing_ideas_csv: str):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.existing_ideas = self._load_existing(existing_ideas_csv)
        self.existing_embeddings = self._compute_embeddings()

    def _load_existing(self, csv_path: str) -> list:
        """Load existing ideas from CSV."""
        ideas = []
        for path in [csv_path, csv_path.replace('claude', 'directories')]:
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                ideas.extend(list(reader))
        return ideas

    def _compute_embeddings(self) -> np.ndarray:
        """Compute embeddings for existing ideas."""
        texts = [
            f"{idea['title']} {idea['tagline']} {idea['problem']}"
            for idea in self.existing_ideas
        ]
        return self.model.encode(texts)

    def is_duplicate(self, new_idea: dict, threshold: float = 0.85) -> tuple[bool, str]:
        """
        Check if idea is duplicate of existing.
        Returns (is_duplicate, similar_idea_id or None).
        """

        # Layer 1: Exact title match
        new_title = new_idea['title'].lower().strip()
        for existing in self.existing_ideas:
            if existing['title'].lower().strip() == new_title:
                return True, existing['id']

        # Layer 2: Semantic similarity
        new_text = f"{new_idea['title']} {new_idea['tagline']} {new_idea['problem']}"
        new_embedding = self.model.encode([new_text])

        similarities = cosine_similarity(new_embedding, self.existing_embeddings)[0]
        max_similarity_idx = np.argmax(similarities)
        max_similarity = similarities[max_similarity_idx]

        if max_similarity > threshold:
            return True, self.existing_ideas[max_similarity_idx]['id']

        # Layer 3: Category + subcategory + audience overlap
        for existing in self.existing_ideas:
            if (existing['category'] == new_idea['category'] and
                existing['subcategory'] == new_idea['subcategory'] and
                self._audience_overlap(existing, new_idea) > 0.7):
                return True, existing['id']

        return False, None

    def _audience_overlap(self, idea1: dict, idea2: dict) -> float:
        """Calculate audience overlap score."""
        aud1 = set(idea1.get('target_audience', '').lower().split())
        aud2 = set(idea2.get('target_audience', '').lower().split())
        if not aud1 or not aud2:
            return 0.0
        return len(aud1 & aud2) / len(aud1 | aud2)
```

---

## Geographic Market Configuration

### US Market (350 ideas)

```python
US_MARKET_CONFIG = {
    "currency": "USD",
    "pricing_examples": "$9/mo, $29/mo, $99/mo",
    "legal_frameworks": ["Magnuson-Moss", "FTC", "state AG"],
    "platforms": ["ChatGPT Store", "Chrome Web Store", "Slack", "Shopify"],
    "pain_sources": [
        "r/Entrepreneur", "r/smallbusiness", "r/startups",
        "Hacker News", "Product Hunt"
    ],
    "cultural_keywords": [
        "solopreneur", "side hustle", "bootstrap",
        "Series A", "YC", "venture"
    ],
    "categories_emphasis": [
        "Consumer Protection (medical bills, insurance)",
        "Financial Negotiation (salary, debt)",
        "Legal/Rights (tenant, consumer)"
    ]
}
```

### UK/Europe Market (150 ideas)

```python
UK_EU_MARKET_CONFIG = {
    "currencies": {"UK": "GBP", "EU": "EUR"},
    "pricing_examples": "£9/mo, €19/mo, €49/mo",
    "legal_frameworks": ["GDPR", "Consumer Rights Act 2015", "EU Consumer Rights Directive"],
    "platforms": ["Chrome Web Store", "Slack", "Shopify (EU)", "Notion"],
    "pain_sources": [
        "r/UKPersonalFinance", "r/UKJobs", "r/AskUK",
        "r/germany", "r/france", "r/europe",
        "Product Hunt (EU launches)"
    ],
    "cultural_keywords": [
        "VAT", "GDPR compliant", "UK-based",
        "EU market", "cross-border"
    ],
    "unique_opportunities": [
        "Brexit compliance tools",
        "EU VAT automation",
        "GDPR consent management",
        "UK pension analysis",
        "EU employment rights",
        "Multi-currency SaaS"
    ],
    "categories_emphasis": [
        "GDPR/Privacy compliance",
        "Cross-border e-commerce",
        "Employment rights (different per country)",
        "Healthcare navigation (NHS, EU systems)"
    ]
}
```

---

## Validation Rules

```python
VALIDATION_RULES = {
    "min_leap_total": 3.5,
    "min_ease": 4,
    "min_search_volume": 500,
    "max_build_time_weeks": 2,
    "required_fields": [
        "title", "tagline", "problem", "solution",
        "target_audience", "business_model", "pricing"
    ],
    "prohibited_patterns": [
        "blockchain", "crypto", "NFT",  # Complex/regulated
        "medical diagnosis", "legal advice",  # Liability
        "hardware", "IoT",  # Not software-only
    ]
}

def validate_idea(idea: dict) -> tuple[bool, list]:
    """
    Validate idea against rules.
    Returns (is_valid, list_of_issues).
    """
    issues = []

    if idea.get("leap_total", 0) < VALIDATION_RULES["min_leap_total"]:
        issues.append(f"LEAP score {idea['leap_total']} below minimum {VALIDATION_RULES['min_leap_total']}")

    if idea.get("leap_e", 0) < VALIDATION_RULES["min_ease"]:
        issues.append(f"Ease score {idea['leap_e']} too low for solo founder")

    for field in VALIDATION_RULES["required_fields"]:
        if not idea.get(field):
            issues.append(f"Missing required field: {field}")

    combined_text = f"{idea.get('solution', '')} {idea.get('tech_stack', '')}".lower()
    for pattern in VALIDATION_RULES["prohibited_patterns"]:
        if pattern in combined_text:
            issues.append(f"Contains prohibited pattern: {pattern}")

    return len(issues) == 0, issues
```

---

## Dependencies (requirements.txt)

```
# API Clients
anthropic>=0.18.0
praw>=7.7.0
pytrends>=4.9.0
tavily-python>=0.3.0
requests>=2.31.0

# Data Processing
pandas>=2.0.0
numpy>=1.24.0

# ML / NLP
sentence-transformers>=2.2.0
scikit-learn>=1.3.0

# Scheduling
apscheduler>=3.10.0

# Utilities
python-dotenv>=1.0.0
pydantic>=2.0.0
rich>=13.0.0
loguru>=0.7.0

# Testing
pytest>=7.0.0
pytest-asyncio>=0.21.0
```

---

## Environment Variables (.env.example)

```bash
# API Keys (Required)
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...

# API Keys (Optional but recommended)
REDDIT_CLIENT_ID=...
REDDIT_CLIENT_SECRET=...
REDDIT_USER_AGENT=StartupIdeaResearcher/1.0
GITHUB_TOKEN=ghp_...

# Configuration
DAILY_RUN_TIME=06:00
TARGET_IDEAS_US=25
TARGET_IDEAS_UK_EU=10
MIN_LEAP_SCORE=3.5
DEDUP_THRESHOLD=0.85

# Storage
DATA_DIR=/home/user/JM-Claude-Playground/data
OUTPUT_CSV=ideas-claude.csv
```

---

## Daily Pipeline Execution

```python
# automation/orchestrator.py

class DailyOrchestrator:
    def run_daily(self, target_us: int = 25, target_uk_eu: int = 10):
        """Execute daily research pipeline."""

        # Stage 1: Collect data from all sources
        raw_data = {
            "reddit": self.reddit_collector.fetch_all(),
            "hn": self.hn_collector.fetch_top_and_ask(),
            "producthunt": self.ph_collector.fetch_recent(),
            "github": self.github_collector.fetch_trending(),
            "trends": self.trends_collector.fetch_rising()
        }

        # Stage 2: Extract pain points
        pain_points = self.pain_extractor.extract(raw_data)

        # Stage 3: Generate ideas (3x target for filtering)
        us_candidates = self.claude_generator.generate(
            pain_points[:60], market="US", count=target_us * 3
        )
        uk_eu_candidates = self.claude_generator.generate(
            pain_points[60:], market="UK_EU", count=target_uk_eu * 3
        )

        # Stage 4: Score and validate
        scored_us = [self.leap_scorer.score(idea) for idea in us_candidates]
        scored_uk_eu = [self.leap_scorer.score(idea) for idea in uk_eu_candidates]

        # Stage 5: Filter by LEAP minimum
        valid_us = [i for i in scored_us if i["leap_total"] >= 3.5 and i["leap_e"] >= 4]
        valid_uk_eu = [i for i in scored_uk_eu if i["leap_total"] >= 3.5 and i["leap_e"] >= 4]

        # Stage 6: Deduplicate
        unique_us = [i for i in valid_us if not self.deduplicator.is_duplicate(i)[0]]
        unique_uk_eu = [i for i in valid_uk_eu if not self.deduplicator.is_duplicate(i)[0]]

        # Stage 7: Select top ideas
        final_us = sorted(unique_us, key=lambda x: x["leap_total"], reverse=True)[:target_us]
        final_uk_eu = sorted(unique_uk_eu, key=lambda x: x["leap_total"], reverse=True)[:target_uk_eu]

        # Stage 8: Append to CSV
        self.csv_manager.append(final_us + final_uk_eu)

        # Stage 9: Generate report
        return self.report_generator.create_daily_report(
            raw_data, pain_points, final_us, final_uk_eu
        )
```

---

## Critical Files Reference

These existing files MUST be read and understood:

1. **`/home/user/JM-Claude-Playground/data/sources.json`** - Contains all 104 data sources with extraction methods, search queries, and pain type classifications

2. **`/home/user/JM-Claude-Playground/data/ideas-claude.csv`** - The 350 existing ideas with full 22-column schema (for deduplication)

3. **`/home/user/JM-Claude-Playground/docs/LEAP-framework.md`** - Complete LEAP scoring documentation

4. **`/home/user/JM-Claude-Playground/scripts/evaluate_ideas.py`** - Contains DUPLICATES, CHATGPT_WRAPPERS, and NEEDS_TECHNICAL_COFOUNDER lists (patterns to avoid)

5. **`/home/user/JM-Claude-Playground/enrich_csv.py`** - Pattern for loading enrichments and updating CSV files

---

## Implementation Order

1. **Foundation** - Project structure, config, logging
2. **Reddit Collector** - Highest-value source first
3. **Remaining Collectors** - HN, Product Hunt, GitHub, Trends
4. **Pain Extractor** - Process raw data into pain points
5. **Claude Generator** - Idea generation from pain points
6. **LEAP Scorer** - Automated scoring
7. **Deduplicator** - Semantic similarity checking
8. **CSV Manager** - Schema-compliant output
9. **Orchestrator** - Pipeline coordination
10. **Scheduler** - Daily automation

---

## Verification

After implementation, verify:

1. Run `python scripts/run_daily.py --dry-run` - Should complete without errors
2. Check output CSV matches 22-column schema exactly
3. Verify LEAP scores are >= 3.5 for all ideas
4. Verify Ease scores are >= 4 for all ideas
5. Run deduplication against existing 450 ideas - should find no matches
6. Generate 5 test ideas and manually verify quality
