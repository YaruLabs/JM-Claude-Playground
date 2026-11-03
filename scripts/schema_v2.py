"""Idea schema v2: the single source of truth for every ideas CSV in data/.

Scores are integers 1-5:
  leap_l  Leverage  - how much of the core work AI does
  leap_e  Ease      - how fast a solo founder ships an MVP (5 = days, 1 = months+)
  leap_a  Audience  - evidence of existing demand / search volume
  leap_p  Platform  - built-in distribution channel
  moat_m  Moat      - proprietary, compounding data the product captures
  wtp_w   Willingness to pay - evidence buyers already pay for adjacent solutions
score_total = mean of the six, rounded to 2 dp.
"""

FIELDS = [
    "id", "title", "tagline", "market", "target_segment",
    "category", "subcategory", "problem", "solution", "target_audience",
    "business_model", "pricing",
    "leap_l", "leap_e", "leap_a", "leap_p", "moat_m", "wtp_w", "score_total", "score_justification",
    "platform_distribution", "tam_estimate", "tam_source", "competitors", "competitor_gap",
    "demand_evidence", "source_urls", "unique_data_capture",
    "commoditization_risk", "regulatory_notes", "founder_feasibility", "language",
    "payment_rails", "mvp_features", "tech_stack", "status",
    "review_notes", "created_date", "last_verified",
]

SCORE_FIELDS = ["leap_l", "leap_e", "leap_a", "leap_p", "moat_m", "wtp_w"]
MARKETS = {"US", "UK_EU", "TH", "GLOBAL"}
STATUSES = {"RECOMMENDED", "CAUTION", "OUTDATED", "SKIP"}
LANGUAGES = {"EN", "TH", "EN+TH"}

MIN_PROBLEM = 250
MIN_SOLUTION = 400
MIN_URLS = 3
GATE_TOTAL = 3.5
GATE_EASE = 3


def score_total(row):
    vals = [int(row[f]) for f in SCORE_FIELDS]
    return round(sum(vals) / len(vals), 2)
