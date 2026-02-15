#!/usr/bin/env python3
"""
Refined script to add specific, thoughtful 'unique_data_capture' descriptions.
Focuses on ideas that truly have unique data moat potential.
"""

import csv

# Specific data capture opportunities by idea ID or title pattern
# Format: 'keyword_or_id': 'specific data capture description'

IDEA_DATA_CAPTURE = {
    # === CONSUMER PROTECTION - PRICING DATA ===
    'CLAUDE-001': 'Hospital billing codes, charge patterns, regional pricing benchmarks, error frequencies by hospital type',
    'CLAUDE-002': 'Insurance claim values, adjuster tactics, settlement ranges by claim type and insurer',
    'CLAUDE-003': 'Contractor quote data by trade/region, material costs, labor rates, scope gap patterns that lead to change orders',
    'CLAUDE-004': 'Warranty denial patterns by company, successful dispute language, compliance rates',
    'CLAUDE-005': 'Veterinary pricing by procedure/clinic/region, unnecessary test patterns, treatment alternatives',
    'CLAUDE-006': 'Moving company pricing patterns, scam indicator data, actual vs quoted cost differences',
    'CLAUDE-007': 'Gym cancellation processes by chain, successful cancellation tactics, retention script patterns',
    'CLAUDE-008': 'Subscription pricing across services, price increase patterns, churn triggers',
    'CLAUDE-009': 'Retail price errors by store/category, scanner accuracy rates, successful claim data',
    'CLAUDE-010': 'Flight delay/cancellation compensation outcomes by airline, successful claim language',

    # === FINANCIAL NEGOTIATION - COMPENSATION DATA ===
    'CLAUDE-011': 'Salary offers by role/company/location/experience, negotiation success rates, counter-offer outcomes',
    'CLAUDE-012': 'Freelancer rates by skill/experience/market, project pricing patterns, rate increase success',
    'CLAUDE-013': 'Debt settlement rates by creditor type/debt age/amount, successful offer percentages',
    'CLAUDE-014': 'Property tax assessments vs sales data, appeal success rates by jurisdiction',
    'CLAUDE-015': 'Severance packages by company/tenure/role, negotiation leverage effectiveness',
    'CLAUDE-016': 'Real estate commission rates actually negotiated, agent pricing by market',
    'CLAUDE-017': 'Wedding vendor pricing with/without wedding context, markup patterns by vendor type',
    'CLAUDE-018': 'Creator deal values by platform/follower count/engagement, brand budget ranges',
    'CLAUDE-019': 'B2B vendor pricing benchmarks by service type/company size, negotiation outcomes',
    'CLAUDE-020': 'Appeal success rates by type, winning argument patterns, effective letter language',

    # === LEGAL/RIGHTS - PROCESS DATA ===
    'CLAUDE-021': 'Tenant rights enforcement by jurisdiction, landlord violation patterns, successful dispute outcomes',
    'CLAUDE-022': 'Small claims case outcomes, effective evidence types, judge preferences by court',
    'CLAUDE-023': 'Credit bureau dispute outcomes, effective dispute language, error patterns by bureau',
    'CLAUDE-024': 'Eviction procedural errors by state, defense success rates, landlord mistake frequencies',
    'CLAUDE-025': 'Legal document errors by type/state, execution requirement violations',
    'CLAUDE-026': 'Data broker re-listing patterns, removal request effectiveness by broker',
    'CLAUDE-027': 'Unemployment appeal success rates by state/denial reason, effective argument patterns',
    'CLAUDE-028': 'Security deposit dispute outcomes, landlord deduction patterns, penalty collection rates',
    'CLAUDE-029': 'Illegal lease clause prevalence by state, negotiation success rates',
}

DIRECTORY_DATA_CAPTURE = {
    # === LOCAL SERVICES - PRICING & REVIEW DATA ===
    'DIR-001': 'Landlord behavior patterns by address/management company, maintenance response times, deposit return rates',
    'DIR-002': 'Veterinary pricing by procedure/clinic/region, crowdsourced cost benchmarks',
    'DIR-003': 'Contractor quality metrics with project photos, permit compliance rates, scope accuracy',
    'DIR-004': 'Notary pricing by service type/location, availability patterns, specialty expertise',
    'DIR-005': 'Daycare violation patterns, staff turnover rates, parent satisfaction correlations',
    'DIR-006': 'Senior care facility quality metrics, inspection correlations, actual family experiences',
    'DIR-007': 'Wedding vendor actual prices paid, quality vs cost correlations, booking patterns',
    'DIR-008': 'Funeral home pricing by service/region, markup patterns, family satisfaction',
    'DIR-009': 'Emergency plumber pricing/availability patterns, response time benchmarks',
    'DIR-010': 'Groomer quality by breed specialty, pricing benchmarks, certification value',

    # === PROFESSIONAL SERVICES ===
    'DIR-011': 'Therapist effectiveness by specialty/approach, patient outcome correlations',
    'DIR-012': 'Lawyer specialty depth vs outcomes, case success rates by practice area',
    'DIR-013': 'Accountant industry expertise correlations with client outcomes',
    'DIR-014': 'Doctor communication quality vs patient outcomes, diagnostic accuracy patterns',
    'DIR-015': 'Financial advisor fee structures vs client returns, fiduciary compliance',

    # === TECH ===
    'DIR-016': 'AI tool effectiveness ratings by use case, user workflow patterns',
    'DIR-017': 'SaaS boilerplate quality metrics, launch success correlations',
    'DIR-018': 'No-code tool integration compatibility matrix, stack success patterns',
    'DIR-019': 'API reliability metrics, developer satisfaction, implementation patterns',
    'DIR-020': 'Remote job verification data, company remote culture authenticity',
    'DIR-021': 'Developer tool stack combinations, workflow efficiency patterns',
    'DIR-022': 'WordPress plugin performance benchmarks, conflict patterns, support quality',
    'DIR-023': 'Shopify app ROI data by store type/size, actual conversion lift metrics',
    'DIR-024': 'Micro-SaaS valuation data, MRR verification, acquisition success patterns',
    'DIR-025': 'Chrome extension privacy audit data, permission risk assessments',

    # === HEALTH ===
    'DIR-026': 'Personal trainer effectiveness by specialty, client outcome correlations',
    'DIR-027': 'Dietitian effectiveness by condition specialty, treatment outcome data',
    'DIR-028': 'Sleep clinic diagnostic accuracy, treatment success rates',
    'DIR-029': 'Mental health app clinical evidence database, effectiveness ratings',
    'DIR-030': 'Physical therapy outcomes by injury type/approach, recovery patterns',
    'DIR-031': 'Addiction treatment outcome data, evidence-based treatment markers',
    'DIR-032': 'Med spa provider credentials vs outcomes, complication rates',

    # === CREATOR ===
    'DIR-033': 'Freelancer tool proficiency correlations with project success',
    'DIR-034': 'Influencer rate benchmarks by platform/niche/engagement, deal value database',
    'DIR-035': 'Podcast guest-host matching success patterns, booking outcomes',
    'DIR-036': 'Newsletter quality metrics, subscriber growth patterns, engagement benchmarks',
    'DIR-037': 'Course platform feature-to-creator-success correlations',
    'DIR-038': 'Video editor style effectiveness by content type, turnaround benchmarks',
    'DIR-039': 'Ghostwriter industry expertise vs content performance',
    'DIR-040': 'Voice over characteristic preferences by project type',

    # === REAL ESTATE ===
    'DIR-041': 'Coliving space wifi/amenity quality verification, community vibe data',
    'DIR-042': 'ADU contractor permit success rates, actual vs quoted pricing',
    'DIR-043': 'Property management response time data, fee structure benchmarks',
    'DIR-044': 'STR manager performance metrics, occupancy/revenue benchmarks',
    'DIR-045': 'Tiny home builder quality metrics, delivery time accuracy',
    'DIR-046': 'CRE broker transaction data by property type/market',

    # === EDUCATION ===
    'DIR-047': 'Homeschool curriculum effectiveness by learning style, parent satisfaction',
    'DIR-048': 'Tutor teaching style effectiveness by student type, outcome correlations',
    'DIR-049': 'Coding bootcamp verified job outcomes, salary data, employer acceptance',
    'DIR-050': 'Online degree employment outcomes, employer perception data',
    'DIR-051': 'Professional certification ROI data, employer value ratings',
    'DIR-052': 'Apprenticeship program completion/placement rates',

    # === LIFESTYLE ===
    'DIR-053': 'Restaurant supplier pricing/quality benchmarks',
    'DIR-054': 'Craft brewery style quality ratings, taproom experience data',
    'DIR-055': 'Farmers market vendor availability patterns, product quality',
    'DIR-056': 'Escape room verified completion rates, difficulty calibration',
    'DIR-057': 'Board game cafe game library data, community event patterns',
    'DIR-058': 'Dog-friendliness verification data, accommodation quality',
    'DIR-059': 'Pickleball court availability patterns, skill level distribution',

    # === NICHE ===
    'DIR-066': 'Custom GPT effectiveness ratings, use case success patterns',
    'DIR-067': 'MCP server reliability data, capability verification',
    'DIR-068': 'Indie product quality metrics, founder transparency data',
    'DIR-069': 'Prompt effectiveness data by task/model, community refinements',
    'DIR-070': 'Dataset quality ratings, preprocessing notes, use case fit',
    'DIR-071': 'Product longevity data, warranty honor rates, durability metrics',

    # === SOCIAL IMPACT ===
    'DIR-074': 'Black-owned business verification data, community ratings',
    'DIR-075': 'Women-owned business certification verification, capability data',
    'DIR-076': 'Veteran-owned business verification, capability matching data',
    'DIR-077': 'Wheelchair accessibility verification data, real user experiences',
    'DIR-078': 'LGBTQ+ friendliness verification, community safety data',
    'DIR-079': 'Neurodivergent accommodation data, sensory information',

    # === B2B ===
    'DIR-086': 'US manufacturer capability verification, MOQ accuracy, quality data',
    'DIR-087': 'Co-packer capability verification, minimum run accuracy',
    'DIR-088': 'White-label SaaS partnership terms database, agency success patterns',
    'DIR-089': 'Startup service provider pricing/quality benchmarks, founder ratings',
    'DIR-090': 'Fractional executive availability, engagement model effectiveness',
}

def process_csv(input_path, data_capture_map):
    """Process CSV and add specific data capture descriptions."""

    rows = []
    fieldnames = None

    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)

        # Ensure unique_data_capture is in fieldnames
        if 'unique_data_capture' not in fieldnames:
            fieldnames.append('unique_data_capture')

        for row in reader:
            idea_id = row.get('id', '')
            title = row.get('title', '').lower()

            # Check for specific mapping by ID
            if idea_id in data_capture_map:
                row['unique_data_capture'] = data_capture_map[idea_id]
            else:
                # Check for patterns in title for ideas not explicitly mapped
                capture = analyze_by_title(title, row)
                row['unique_data_capture'] = capture

            rows.append(row)

    # Write back
    with open(input_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)

def analyze_by_title(title, row):
    """Analyze by title patterns for unmapped ideas."""

    solution = row.get('solution', '').lower()

    # Price/cost data
    if any(w in title for w in ['price', 'cost', 'bill', 'quote', 'rate', 'fee']):
        return 'Pricing and cost benchmarking data'

    # Review/rating data
    if any(w in title for w in ['review', 'rating', 'finder', 'directory']):
        return 'Structured quality and review data'

    # Negotiation data
    if any(w in title for w in ['negotiat', 'deal', 'contract']):
        return 'Negotiation outcome and tactic data'

    # Process/procedure data
    if any(w in title for w in ['cancel', 'dispute', 'appeal', 'claim']):
        return 'Process effectiveness and outcome data'

    # Document/template data
    if any(w in title for w in ['letter', 'template', 'document']):
        return 'Document template effectiveness data'

    # Check solution for indicators
    if 'crowdsourced' in solution or 'user-reported' in solution:
        return 'Crowdsourced user data and experiences'

    if 'benchmark' in solution or 'compare' in solution:
        return 'Comparative benchmarking data'

    return ''

def main():
    # Process ideas-claude.csv
    count1 = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-claude.csv',
        IDEA_DATA_CAPTURE
    )
    print(f"Processed {count1} ideas in ideas-claude.csv")

    # Process ideas-directories.csv
    count2 = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-directories.csv',
        DIRECTORY_DATA_CAPTURE
    )
    print(f"Processed {count2} directories in ideas-directories.csv")

    # Print statistics
    print("\n=== Data Capture Statistics ===")

    for filepath, name in [
        ('/home/user/JM-Claude-Playground/data/ideas-claude.csv', 'Startup Ideas'),
        ('/home/user/JM-Claude-Playground/data/ideas-directories.csv', 'Directory Ideas')
    ]:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            with_capture = sum(1 for r in rows if r.get('unique_data_capture'))
            print(f"\n{name}: {with_capture}/{len(rows)} have data capture opportunities")

            # Show sample
            print("Sample entries:")
            for i, r in enumerate(rows[:5]):
                capture = r.get('unique_data_capture', '')[:60] or 'None'
                print(f"  {r['id']}: {capture}...")

if __name__ == '__main__':
    main()
