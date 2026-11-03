#!/usr/bin/env python3
"""
Comprehensive analysis of unique data capture opportunities.
Goes through ALL ideas and identifies genuine data moat potential.
"""

import csv

# Comprehensive mappings for startup ideas
STARTUP_DATA_CAPTURE = {
    # Consumer Protection (1-30)
    'CLAUDE-001': 'Hospital billing codes and error patterns, regional pricing benchmarks, successful dispute outcomes',
    'CLAUDE-002': 'Insurance claim values by type/insurer, adjuster tactics, settlement ranges, denial pattern recognition',
    'CLAUDE-003': 'Contractor quote data by trade/region, material costs, labor rates, scope gap patterns',
    'CLAUDE-004': 'Warranty denial patterns by company/product, successful dispute language, compliance rates',
    'CLAUDE-005': 'Veterinary pricing by procedure/clinic/region, unnecessary test patterns, treatment alternatives',
    'CLAUDE-006': 'Moving company pricing patterns, scam indicators, actual vs quoted cost variances',
    'CLAUDE-007': 'Gym cancellation processes by chain, successful cancellation tactics, retention script patterns',
    'CLAUDE-008': 'Subscription pricing across services, price increase patterns, cancellation difficulty scores',
    'CLAUDE-009': 'Retail price errors by store/category, scanner accuracy rates, successful claim patterns',
    'CLAUDE-010': 'Flight compensation outcomes by airline/route, successful claim language, denial patterns',
    'CLAUDE-011': 'Salary offers by role/company/location, negotiation success rates, counter-offer effectiveness',
    'CLAUDE-012': 'Freelancer rates by skill/experience/market, project pricing patterns, rate increase success',
    'CLAUDE-013': 'Debt settlement rates by creditor/debt age/amount, successful offer percentages',
    'CLAUDE-014': 'Property assessments vs sales data, appeal success rates by jurisdiction/argument type',
    'CLAUDE-015': 'Severance packages by company/tenure/role, negotiation leverage effectiveness',
    'CLAUDE-016': 'Real estate commission rates negotiated by market, agent pricing patterns',
    'CLAUDE-017': 'Wedding vendor pricing with/without wedding markup, discount patterns by vendor type',
    'CLAUDE-018': 'Creator deal values by platform/follower/engagement, brand budget benchmarks',
    'CLAUDE-019': 'B2B vendor pricing benchmarks by service/company size, negotiation outcomes',
    'CLAUDE-020': 'Appeal success rates by type/jurisdiction, winning argument patterns, effective templates',
    'CLAUDE-021': 'Tenant rights enforcement by jurisdiction, landlord violation patterns, dispute outcomes',
    'CLAUDE-022': 'Small claims outcomes by case type, evidence effectiveness, judge preference patterns',
    'CLAUDE-023': 'Credit bureau dispute outcomes, effective dispute language, error patterns by bureau',
    'CLAUDE-024': 'Eviction procedural errors by state, defense success rates, landlord mistake frequencies',
    'CLAUDE-025': 'Legal document errors by type/state, execution requirement violations',
    'CLAUDE-026': 'Data broker re-listing patterns, removal request effectiveness by broker',
    'CLAUDE-027': 'Unemployment appeal success by state/denial reason, effective argument patterns',
    'CLAUDE-028': 'Security deposit outcomes, landlord deduction patterns, penalty collection rates',
    'CLAUDE-029': 'Illegal lease clause prevalence by state, successful negotiation patterns',
    'CLAUDE-030': 'HOA fine dispute outcomes, rule enforcement patterns, board behavior data',

    # Life Transitions & Navigation (31-60)
    'CLAUDE-031': 'Franchise profitability data, FDD comparison benchmarks, franchisee outcome patterns',
    'CLAUDE-032': 'Used car pricing/issue patterns, dealer reliability scores, negotiation outcomes',
    'CLAUDE-033': 'Home inspection issue frequencies, repair cost benchmarks, red flag patterns',
    'CLAUDE-034': 'Co-founder agreement terms benchmarks, equity split patterns, dispute prevention clauses',
    'CLAUDE-035': 'Graduate program outcome data, career placement rates, ROI benchmarks',
    'CLAUDE-036': 'Patent prior art patterns, patentability indicators, prosecution outcome data',
    'CLAUDE-037': 'Small business insurance pricing by industry/size, coverage gap patterns',
    'CLAUDE-038': 'Disability claim success patterns, effective documentation, denial appeal outcomes',
    'CLAUDE-039': 'Medicare/Medicaid eligibility patterns, enrollment success rates',
    'CLAUDE-040': 'Social Security optimization patterns, claiming strategy outcomes',
    'CLAUDE-041': 'Divorce asset patterns, settlement benchmarks by state, mediation success rates',
    'CLAUDE-042': 'Elder care facility quality correlations, cost benchmarks, family satisfaction data',
    'CLAUDE-043': 'Inheritance tax patterns, estate planning effectiveness benchmarks',
    'CLAUDE-044': 'College admission patterns, essay effectiveness data, application success rates',
    'CLAUDE-045': 'Timeshare exit success rates by company, rescission pattern data',
    'CLAUDE-046': 'Home inspection issue frequencies by home type/age, severity benchmarks',
    'CLAUDE-047': 'New parent resource effectiveness, developmental milestone benchmarks',
    'CLAUDE-048': 'Estate administration complexity patterns, probate timeline benchmarks',
    'CLAUDE-049': 'Used car defect patterns by make/model/year, price manipulation indicators',
    'CLAUDE-050': 'School quality metrics beyond ratings, parent satisfaction correlations',

    # Community/Social Platforms (51-70)
    'CLAUDE-051': 'City livability data, cost of living benchmarks, community quality metrics',
    'CLAUDE-052': 'Mentorship matching effectiveness, relationship outcome data',
    'CLAUDE-053': 'Widow support resource effectiveness, grief timeline patterns',
    'CLAUDE-054': 'Remote work opportunity quality data, employer reliability scores',
    'CLAUDE-055': 'Empty nest transition patterns, activity effectiveness data',
    'CLAUDE-056': 'Introvert-friendly venue data, social anxiety accommodation ratings',
    'CLAUDE-057': 'New mom support resource effectiveness, postpartum pattern data',
    'CLAUDE-058': 'Divorce recovery resource effectiveness, rebuilding timeline patterns',
    'CLAUDE-059': 'Retiree activity effectiveness, community engagement patterns',
    'CLAUDE-060': 'Grief support resource effectiveness, recovery pattern data',

    # Professional Services (61-100)
    'CLAUDE-061': 'Expert witness effectiveness data, case outcome correlations',
    'CLAUDE-062': 'Insurance policy comparison data, coverage gap patterns',
    'CLAUDE-063': 'Contractor license verification patterns, compliance rates',
    'CLAUDE-064': 'Professional liability pricing benchmarks, claim pattern data',
    'CLAUDE-065': 'Compliance requirement patterns by industry, violation frequencies',

    # Business Tools (100-150)
    'CLAUDE-101': 'Startup metric benchmarks, growth pattern data',
    'CLAUDE-102': 'Investor pitch effectiveness data, funding success patterns',
    'CLAUDE-103': 'Business valuation benchmarks by industry/size',
    'CLAUDE-104': 'Customer acquisition cost benchmarks, conversion pattern data',
    'CLAUDE-105': 'Pricing optimization patterns, willingness-to-pay data',

    # Health & Wellness (150-200)
    'CLAUDE-151': 'Health provider quality metrics, outcome correlations',
    'CLAUDE-152': 'Treatment effectiveness data by condition/approach',
    'CLAUDE-153': 'Healthcare pricing benchmarks, negotiation success patterns',
    'CLAUDE-154': 'Insurance claim approval patterns, denial reason frequencies',
    'CLAUDE-155': 'Wellness program effectiveness data, health outcome correlations',

    # Education (200-250)
    'CLAUDE-201': 'Tutor effectiveness data by subject/approach',
    'CLAUDE-202': 'Learning resource effectiveness benchmarks',
    'CLAUDE-203': 'Skill development timeline data, mastery pattern analysis',
    'CLAUDE-204': 'Career training ROI data, job placement benchmarks',
    'CLAUDE-205': 'Educational content effectiveness ratings',

    # Real Estate (250-300)
    'CLAUDE-251': 'Property value prediction data, market trend patterns',
    'CLAUDE-252': 'Rental pricing benchmarks, landlord reliability data',
    'CLAUDE-253': 'Home improvement ROI data by project type/region',
    'CLAUDE-254': 'Property management quality benchmarks',
    'CLAUDE-255': 'Real estate agent performance data',

    # Finance (300-350)
    'CLAUDE-301': 'Investment performance benchmarks, strategy effectiveness data',
    'CLAUDE-302': 'Financial advisor quality metrics, fee comparison data',
    'CLAUDE-303': 'Loan approval patterns, interest rate benchmarks',
    'CLAUDE-304': 'Credit building effectiveness data, score improvement patterns',
    'CLAUDE-305': 'Tax optimization patterns, deduction effectiveness data',
}

# Directory ideas (already comprehensive in previous script)
DIRECTORY_DATA_CAPTURE = {
    'DIR-001': 'Landlord behavior patterns by address/company, maintenance response times, deposit return rates',
    'DIR-002': 'Veterinary pricing by procedure/clinic/region, crowdsourced cost benchmarks',
    'DIR-003': 'Contractor quality metrics with verified project photos, permit compliance rates',
    'DIR-004': 'Notary pricing by service type/location, availability patterns, specialty demand',
    'DIR-005': 'Daycare violation patterns, staff turnover rates, parent satisfaction correlations',
    'DIR-006': 'Senior care quality metrics, inspection correlations, family experience data',
    'DIR-007': 'Wedding vendor actual prices paid, quality vs cost correlations',
    'DIR-008': 'Funeral home pricing by service/region, transparency scores',
    'DIR-009': 'Emergency plumber pricing/availability patterns, response time benchmarks',
    'DIR-010': 'Groomer quality by breed specialty, pricing benchmarks',
    'DIR-011': 'Therapist effectiveness by specialty/approach, patient outcome data',
    'DIR-012': 'Lawyer specialty depth vs case outcomes, success rates by area',
    'DIR-013': 'Accountant industry expertise correlations with client outcomes',
    'DIR-014': 'Doctor communication quality vs patient outcomes, diagnostic accuracy',
    'DIR-015': 'Financial advisor fee structures vs returns, fiduciary compliance data',
    'DIR-016': 'AI tool effectiveness ratings by use case, user workflow patterns',
    'DIR-017': 'SaaS boilerplate quality metrics, launch success correlations',
    'DIR-018': 'No-code tool integration compatibility matrix, stack success patterns',
    'DIR-019': 'API reliability metrics, developer satisfaction data',
    'DIR-020': 'Remote job verification data, company remote culture scores',
    'DIR-021': 'Developer tool stack combinations, workflow efficiency patterns',
    'DIR-022': 'WordPress plugin performance benchmarks, conflict patterns',
    'DIR-023': 'Shopify app ROI data, actual conversion lift metrics',
    'DIR-024': 'Micro-SaaS valuation data, acquisition success patterns',
    'DIR-025': 'Chrome extension privacy audit data, permission risk scores',
    'DIR-026': 'Personal trainer effectiveness by specialty, outcome data',
    'DIR-027': 'Dietitian effectiveness by condition, treatment outcome data',
    'DIR-028': 'Sleep clinic diagnostic accuracy, treatment success rates',
    'DIR-029': 'Mental health app clinical evidence database',
    'DIR-030': 'Physical therapy outcomes by injury type/approach',
    'DIR-031': 'Addiction treatment outcome data, evidence-based markers',
    'DIR-032': 'Med spa provider outcomes, complication rates',
    'DIR-033': 'Freelancer tool proficiency vs project success correlations',
    'DIR-034': 'Influencer rate benchmarks by platform/niche/engagement',
    'DIR-035': 'Podcast guest-host matching success patterns',
    'DIR-036': 'Newsletter quality metrics, engagement benchmarks',
    'DIR-037': 'Course platform feature-to-success correlations',
    'DIR-038': 'Video editor style effectiveness by content type',
    'DIR-039': 'Ghostwriter expertise vs content performance',
    'DIR-040': 'Voice over characteristic preferences by use case',
    'DIR-041': 'Coliving space quality verification, community data',
    'DIR-042': 'ADU contractor permit success rates, pricing accuracy',
    'DIR-043': 'Property management response times, fee benchmarks',
    'DIR-044': 'STR manager performance metrics, revenue benchmarks',
    'DIR-045': 'Tiny home builder quality, delivery accuracy',
    'DIR-046': 'CRE broker transaction data by property type',
    'DIR-047': 'Homeschool curriculum effectiveness by learning style',
    'DIR-048': 'Tutor teaching style effectiveness by student type',
    'DIR-049': 'Coding bootcamp verified job outcomes, salary data',
    'DIR-050': 'Online degree employment outcomes, employer perception',
    'DIR-051': 'Professional certification ROI data, employer value ratings',
    'DIR-052': 'Apprenticeship completion/placement rates',
    'DIR-053': 'Restaurant supplier pricing/quality benchmarks',
    'DIR-054': 'Craft brewery style quality ratings',
    'DIR-055': 'Farmers market vendor availability/quality data',
    'DIR-056': 'Escape room completion rates, difficulty calibration',
    'DIR-057': 'Board game cafe library data, community patterns',
    'DIR-058': 'Dog-friendliness verification, accommodation quality',
    'DIR-059': 'Pickleball court availability, skill level data',
    'DIR-060': 'Community garden availability/waitlist data',
    'DIR-061': 'Repair cafe effectiveness data by item type',
    'DIR-062': 'E-waste recycler certification verification',
    'DIR-063': 'Church worship style/community data',
    'DIR-064': 'Support group effectiveness by specific situation',
    'DIR-065': 'Volunteer opportunity skill-match effectiveness',
    'DIR-066': 'Custom GPT effectiveness ratings by use case',
    'DIR-067': 'MCP server reliability data, capability verification',
    'DIR-068': 'Indie product quality metrics, founder transparency',
    'DIR-069': 'Prompt effectiveness data by task/model',
    'DIR-070': 'Dataset quality ratings, use case fit data',
    'DIR-071': 'Product longevity data, warranty honor rates',
    'DIR-072': 'Vintage dealer specialty inventory data',
    'DIR-073': 'Privacy tool effectiveness ratings',
    'DIR-074': 'Black-owned business verification, quality data',
    'DIR-075': 'Women-owned business certification verification',
    'DIR-076': 'Veteran-owned business verification data',
    'DIR-077': 'Wheelchair accessibility verification data',
    'DIR-078': 'LGBTQ+ friendliness verification, safety data',
    'DIR-079': 'Neurodivergent accommodation data',
    'DIR-080': 'Sober venue atmosphere/event data',
    'DIR-081': 'Cannabis strain effects data, user-reported outcomes',
    'DIR-082': 'Psychedelic therapy provider credentials/outcomes',
    'DIR-083': 'Concierge doctor pricing/service benchmarks',
    'DIR-084': 'Midwife birth outcome data by setting',
    'DIR-085': 'Functional medicine practitioner outcome data',
    'DIR-086': 'US manufacturer capability verification, MOQ accuracy',
    'DIR-087': 'Co-packer capability, minimum run accuracy',
    'DIR-088': 'White-label SaaS partnership terms database',
    'DIR-089': 'Startup service provider pricing/quality benchmarks',
    'DIR-090': 'Fractional executive engagement effectiveness',
    'DIR-091': 'Community center program effectiveness data',
    'DIR-092': 'Library of things inventory/availability data',
    'DIR-093': 'Makerspace equipment availability/quality data',
    'DIR-094': 'Coworking space amenity/vibe data',
    'DIR-095': 'Podcast studio equipment/quality data',
    'DIR-096': 'Video studio setup/quality data',
    'DIR-097': 'Photography location permit/access data',
    'DIR-098': 'Event venue realistic capacity data',
    'DIR-099': 'Retreat center type/capacity/quality data',
    'DIR-100': 'Wholesale buyer-maker matching data',
}


def analyze_by_content(row):
    """Analyze idea content to determine data capture potential."""

    title = row.get('title', '').lower()
    problem = row.get('problem', '').lower()
    solution = row.get('solution', '').lower()
    combined = f"{title} {problem} {solution}"

    # Strong indicators of data capture potential
    strong_patterns = {
        'price': 'Pricing data and market rate benchmarks',
        'cost': 'Cost data and spending benchmarks',
        'rate': 'Rate/pricing comparison data',
        'bill': 'Billing data and charge pattern analysis',
        'quote': 'Quote/estimate data for market intelligence',
        'salary': 'Compensation data by role/company/location',
        'wage': 'Wage and compensation benchmarks',
        'review': 'Structured review and quality metrics',
        'rating': 'Rating data with quality correlations',
        'outcome': 'Outcome data for effectiveness analysis',
        'success': 'Success rate data and pattern analysis',
        'settlement': 'Settlement data and negotiation benchmarks',
        'benchmark': 'Benchmarking data for market comparison',
        'compare': 'Comparative data across providers/options',
        'crowdsourced': 'Crowdsourced user experience data',
        'verified': 'Verified quality and credential data',
        'track': 'Tracking data for pattern analysis',
    }

    for pattern, description in strong_patterns.items():
        if pattern in combined:
            return description

    # Check for directory-type data capture
    if 'directory' in combined or 'finder' in combined or 'find ' in combined:
        return 'Provider/business profiles with quality metrics'

    return ''


def process_csv(filepath, explicit_mappings):
    """Process CSV and add data capture column."""

    rows = []
    fieldnames = None

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)

        if 'unique_data_capture' not in fieldnames:
            fieldnames.append('unique_data_capture')

        for row in reader:
            idea_id = row.get('id', '')

            # Use explicit mapping if available
            if idea_id in explicit_mappings:
                row['unique_data_capture'] = explicit_mappings[idea_id]
            else:
                # Fall back to content analysis
                row['unique_data_capture'] = analyze_by_content(row)

            rows.append(row)

    # Write back
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    return rows


def main():
    print("Processing ideas-claude.csv...")
    startup_rows = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-claude.csv',
        STARTUP_DATA_CAPTURE
    )

    print("Processing ideas-directories.csv...")
    dir_rows = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-directories.csv',
        DIRECTORY_DATA_CAPTURE
    )

    # Statistics
    startup_with_capture = sum(1 for r in startup_rows if r.get('unique_data_capture'))
    dir_with_capture = sum(1 for r in dir_rows if r.get('unique_data_capture'))

    print(f"\n=== Results ===")
    print(f"Startup Ideas: {startup_with_capture}/{len(startup_rows)} have data capture opportunities")
    print(f"Directory Ideas: {dir_with_capture}/{len(dir_rows)} have data capture opportunities")

    # Show high-value examples
    print(f"\n=== High-Value Data Capture Examples ===")
    print("\nStartup Ideas:")
    for r in startup_rows[:15]:
        if r.get('unique_data_capture'):
            print(f"  {r['id']}: {r['title'][:30]:30} | {r['unique_data_capture'][:50]}...")

    print("\nDirectory Ideas:")
    for r in dir_rows[:15]:
        if r.get('unique_data_capture'):
            print(f"  {r['id']}: {r['title'][:30]:30} | {r['unique_data_capture'][:50]}...")


if __name__ == '__main__':
    main()
