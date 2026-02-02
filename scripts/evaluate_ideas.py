#!/usr/bin/env python3
"""
Startup Ideas Reviewer
Evaluates 300 ideas for non-technical solopreneurs with <$5K budget
"""

import csv
import json

# Evaluation criteria
def evaluate_idea(idea_id, title, tagline, category):
    """
    Returns evaluation dict with:
    - status: RECOMMENDED / CAUTION / SKIP
    - viability_score: 1-5
    - technical_grade: A/B/C/D
    - domain_barrier: None/Low/Medium/High
    - monetization: Strong/Moderate/Weak/Unlikely
    - ai_wrapper_test: Pass/Fail
    - duplicate_of: None or ID of similar idea
    - review_notes: explanation
    """

    # This will be filled in by the AI evaluation
    return {}

# Known duplicates/overlaps to flag
DUPLICATES = {
    "IDEA-165": "IDEA-067",  # MeetingCost2 -> MeetingCost
    "IDEA-234": "IDEA-125",  # TeamRetro2 -> TeamRetro
    "IDEA-271": "IDEA-136",  # SocialProof2 -> SocialProof
    "IDEA-204": "IDEA-077",  # GlossaryGen -> GlossaryAI
    "IDEA-244": "IDEA-076",  # InvoiceChase -> InvoiceRemind
    "IDEA-283": "IDEA-092",  # DevPortfolio -> PortfolioAI
    "IDEA-211": "IDEA-101",  # ContractRenew -> ContractAlert (similar)
    "IDEA-265": "IDEA-037",  # BugReport2 -> BugReportAI
    "IDEA-246": "IDEA-038",  # ReleaseNote -> ChangelogAI (similar)
    "IDEA-247": "IDEA-172",  # MeetAgenda -> AgendaAI
    "IDEA-240": "IDEA-193",  # EmailCleanup -> EmailClean
}

# Ideas that are just ChatGPT wrappers (FAIL ai_wrapper_test)
CHATGPT_WRAPPERS = [
    "IDEA-011",  # ReplyGPT - ChatGPT writes emails
    "IDEA-012",  # SummaryTab - ChatGPT summarizes
    "IDEA-019",  # DataStory - ChatGPT does this
    "IDEA-021",  # PolicyWriter - ChatGPT does this
    "IDEA-034",  # JobDescAI - ChatGPT does this
    "IDEA-035",  # SOPWriter - ChatGPT does this
    "IDEA-039",  # ErrorExplain - ChatGPT does this
    "IDEA-040",  # RegexHelper - ChatGPT does this
    "IDEA-080",  # OneLiner - ChatGPT does this
    "IDEA-095",  # GiftIdea - ChatGPT does this
    "IDEA-115",  # CourseOutline - ChatGPT does this
    "IDEA-130",  # StartupName - many free tools
    "IDEA-139",  # BlogOutline - ChatGPT does this
    "IDEA-152",  # SocialBio - ChatGPT does this
    "IDEA-154",  # MeetingNo - ChatGPT does this
    "IDEA-162",  # PRHeadline - ChatGPT does this
    "IDEA-164",  # ContentIdea - ChatGPT does this
    "IDEA-185",  # HashtagGen - many free tools
    "IDEA-188",  # SurveyQ - ChatGPT does this
    "IDEA-191",  # LandingCopy - ChatGPT does this
    "IDEA-201",  # TweetThread - ChatGPT does this
    "IDEA-213",  # PodQuestion - ChatGPT does this
    "IDEA-221",  # CustomerInt - ChatGPT does this
    "IDEA-223",  # VideoHook - ChatGPT does this
    "IDEA-260",  # EventName - ChatGPT does this
    "IDEA-266",  # QuizMaker - ChatGPT does this
    "IDEA-267",  # LeadMagnet - ChatGPT does this
    "IDEA-281",  # BlogTitle - ChatGPT does this
]

# Ideas requiring technical co-founder (Grade D)
NEEDS_TECHNICAL_COFOUNDER = [
    "IDEA-003",  # ComplianceBot - complex compliance logic
    "IDEA-013",  # CodeReviewBot - complex GitHub integration
    "IDEA-044",  # InventoryAlert - complex inventory systems
    "IDEA-083",  # Notifyr - push notification infrastructure
    "IDEA-084",  # AuditLog - security-critical infrastructure
    "IDEA-090",  # GitBranch - complex git tooling
    "IDEA-103",  # ChurnPredict - ML/data science
    "IDEA-142",  # TechDebt - complex codebase analysis
    "IDEA-147",  # MetricAlert - anomaly detection ML
    "IDEA-173",  # RepoDoc - complex code parsing
    "IDEA-190",  # DiscordBot - bot infrastructure
    "IDEA-196",  # LeadScore - ML scoring
    "IDEA-198",  # APIKey - security scanning
    "IDEA-206",  # BugPriority - ML prioritization
    "IDEA-207",  # CustomerTag - ML segmentation
    "IDEA-217",  # TeamPulse - sentiment analysis ML
    "IDEA-227",  # SprintPlan - complex Jira integration
    "IDEA-231",  # SOCReport - compliance complexity
    "IDEA-237",  # CodeSnippet - IDE integration
    "IDEA-252",  # SiteStatus - monitoring infrastructure
    "IDEA-288",  # SlackBot - bot infrastructure
    "IDEA-289",  # MeetingRec - video processing
]

# Ideas requiring domain expertise (High barrier)
NEEDS_DOMAIN_EXPERTISE = [
    "IDEA-003",  # ComplianceBot - SOC2/ISO knowledge
    "IDEA-045",  # TutorBot - education expertise
    "IDEA-047",  # GymPlan - fitness certification helpful
    "IDEA-048",  # PetCareAI - vet advice is risky
    "IDEA-049",  # RentalReview - legal review risky
    "IDEA-104",  # GrantFinder - nonprofit expertise
    "IDEA-141",  # VCIntro - VC network needed
    "IDEA-148",  # OfferLetter - HR/legal expertise
    "IDEA-181",  # StartupPitch - fundraising expertise
    "IDEA-216",  # RiskFlag - legal expertise
    "IDEA-220",  # NDAGen - legal expertise
    "IDEA-231",  # SOCReport - compliance expertise
    "IDEA-238",  # GrantWrite - grant writing expertise
    "IDEA-253",  # CareerPath - career counseling
    "IDEA-274",  # CopyrightCheck - trademark expertise
    "IDEA-299",  # TaxEstimate - tax expertise risky
]

# Consumer apps that are hard to monetize
CONSUMER_HARD_TO_MONETIZE = [
    "IDEA-055",  # HabitScore - consumer habit app
    "IDEA-093",  # CancelFlow - consumer utility
    "IDEA-094",  # ParkingSpot - consumer utility
    "IDEA-095",  # GiftIdea - consumer utility
    "IDEA-096",  # PlantCare - consumer utility
    "IDEA-097",  # MealPlan - consumer utility
    "IDEA-098",  # MovingList - consumer utility
    "IDEA-099",  # BabyTrack - consumer utility
    "IDEA-100",  # DogWalk - marketplace (very hard)
    "IDEA-219",  # RecipeScale - consumer utility
    "IDEA-229",  # ReviewSum - consumer utility
    "IDEA-232",  # LocalEvent - consumer utility
]

print("Evaluation criteria loaded")
print(f"Duplicates flagged: {len(DUPLICATES)}")
print(f"ChatGPT wrappers: {len(CHATGPT_WRAPPERS)}")
print(f"Needs technical cofounder: {len(NEEDS_TECHNICAL_COFOUNDER)}")
print(f"Needs domain expertise: {len(NEEDS_DOMAIN_EXPERTISE)}")
print(f"Consumer hard to monetize: {len(CONSUMER_HARD_TO_MONETIZE)}")
