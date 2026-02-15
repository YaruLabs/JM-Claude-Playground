#!/usr/bin/env python3
"""
Script to add 'unique_data_capture' column to CSV files.
Analyzes each idea to identify opportunities for unique data collection
that could make an AI better over time.
"""

import csv
import re

# Keywords and patterns that indicate data capture opportunities
DATA_CAPTURE_PATTERNS = {
    # Price/Cost Data Collection
    'price_data': {
        'keywords': ['price', 'cost', 'quote', 'bid', 'rate', 'fee', 'pricing', 'bill', 'charge', 'estimate', 'invoice'],
        'description': 'Pricing/cost data from real transactions'
    },
    'salary_data': {
        'keywords': ['salary', 'compensation', 'wage', 'pay', 'offer', 'severance'],
        'description': 'Compensation and salary data'
    },
    # Outcome/Success Data
    'outcome_data': {
        'keywords': ['success', 'outcome', 'result', 'win', 'settlement', 'resolved', 'appeal'],
        'description': 'Success/outcome data from real cases'
    },
    'negotiation_data': {
        'keywords': ['negotiat', 'counter', 'bargain'],
        'description': 'Negotiation tactics and outcomes'
    },
    # Review/Quality Data
    'review_data': {
        'keywords': ['review', 'rating', 'feedback', 'experience'],
        'description': 'Structured review and rating data'
    },
    # Document/Template Data
    'document_data': {
        'keywords': ['letter', 'template', 'document', 'contract', 'lease', 'agreement'],
        'description': 'Document templates and effectiveness data'
    },
    # Process/Procedure Data
    'procedure_data': {
        'keywords': ['process', 'procedure', 'cancel', 'dispute', 'claim', 'appeal'],
        'description': 'Process/procedure effectiveness data'
    },
    # Compliance/Error Data
    'error_data': {
        'keywords': ['error', 'mistake', 'violation', 'overcharge', 'fraud', 'scam'],
        'description': 'Error patterns and detection data'
    },
}

def analyze_idea_for_data_capture(row):
    """Analyze an idea and return its unique data capture opportunity description."""

    # Combine relevant fields for analysis
    title = row.get('title', '').lower()
    problem = row.get('problem', '').lower()
    solution = row.get('solution', '').lower()
    tagline = row.get('tagline', '').lower()

    combined_text = f"{title} {problem} {solution} {tagline}"

    opportunities = []

    # Check each pattern
    for pattern_name, pattern_info in DATA_CAPTURE_PATTERNS.items():
        for keyword in pattern_info['keywords']:
            if keyword in combined_text:
                opportunities.append(pattern_info['description'])
                break

    # Remove duplicates while preserving order
    seen = set()
    unique_opportunities = []
    for opp in opportunities:
        if opp not in seen:
            seen.add(opp)
            unique_opportunities.append(opp)

    # Now apply specific logic based on idea type
    specific_opportunity = get_specific_data_opportunity(row)
    if specific_opportunity:
        return specific_opportunity

    # Return combined opportunities or None
    if unique_opportunities:
        return "; ".join(unique_opportunities[:3])  # Limit to top 3

    return ""

def get_specific_data_opportunity(row):
    """Get specific data capture description based on idea characteristics."""

    title = row.get('title', '').lower()
    solution = row.get('solution', '').lower()
    problem = row.get('problem', '').lower()
    id_val = row.get('id', '')

    # Specific mappings for known high-value data capture ideas
    specific_mappings = {
        # Consumer Protection - Price/Cost Data
        'medical bill': 'Hospital billing codes, error patterns, regional pricing benchmarks, successful dispute outcomes',
        'vet bill': 'Veterinary procedure pricing by region/clinic, unnecessary test patterns, treatment cost benchmarks',
        'contractor bid': 'Contractor quote data, material costs by region, labor rates, scope gap patterns',
        'price': 'Real transaction pricing data enabling market-rate intelligence',
        'quote': 'Quote/estimate data with actual vs final cost comparisons',

        # Financial Negotiation - Compensation Data
        'salary': 'Salary offers by role/company/location, negotiation success rates, counter-offer outcomes',
        'freelance rate': 'Freelancer pricing by skill/experience/market, project scope patterns',
        'commission': 'Real estate commission rates negotiated, agent pricing patterns',
        'severance': 'Severance packages by company/tenure/role, negotiation leverage patterns',

        # Negotiation - Outcome Data
        'wedding vendor': 'Wedding vendor pricing with/without "wedding" markup, negotiation success rates',
        'influencer rate': 'Creator deal values by platform/follower count/engagement, brand budgets',
        'debt settlement': 'Settlement acceptance rates by creditor/debt age/amount, effective offer percentages',

        # Legal/Rights - Process Data
        'appeal': 'Appeal success rates by type/jurisdiction, winning argument patterns',
        'dispute': 'Dispute resolution outcomes, effective letter templates, response patterns',
        'eviction': 'Procedural error patterns, defense success rates, landlord mistake frequencies',
        'lease': 'Illegal clause prevalence by state, successful negotiation patterns',
        'credit dispute': 'Bureau response patterns, effective dispute language, error type frequencies',

        # Reviews/Ratings - Structured Quality Data
        'review': 'Structured quality metrics beyond star ratings, verified outcome data',
        'landlord review': 'Landlord behavior patterns, maintenance response times, deposit return rates',
        'doctor rating': 'Structured healthcare quality metrics, communication scores, outcome data',

        # Subscription/Cancellation - Process Data
        'subscription': 'Subscription pricing creep patterns, successful cancellation methods',
        'gym cancel': 'Gym cancellation process requirements by chain, successful cancellation patterns',

        # Travel/Claims - Outcome Data
        'airline compensation': 'Claim success rates by airline/route, denial pattern recognition',
        'insurance claim': 'Claim outcomes by type/insurer, successful counter-tactics',

        # Directory-Specific Data Capture
        'directory': 'Provider/business profiles with verified quality metrics and user reviews',
    }

    for keyword, opportunity in specific_mappings.items():
        if keyword in title or keyword in solution:
            return opportunity

    return None

def process_csv(input_path, output_path):
    """Process a CSV file and add the unique_data_capture column."""

    rows = []
    fieldnames = None

    # Read the CSV
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames.copy()

        # Add new column if not present
        if 'unique_data_capture' not in fieldnames:
            fieldnames.append('unique_data_capture')

        for row in reader:
            # Analyze for data capture opportunity
            data_capture = analyze_idea_for_data_capture(row)
            row['unique_data_capture'] = data_capture
            rows.append(row)

    # Write the updated CSV
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)

def main():
    # Process ideas-claude.csv
    ideas_count = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-claude.csv',
        '/home/user/JM-Claude-Playground/data/ideas-claude.csv'
    )
    print(f"Processed {ideas_count} ideas in ideas-claude.csv")

    # Process ideas-directories.csv
    dirs_count = process_csv(
        '/home/user/JM-Claude-Playground/data/ideas-directories.csv',
        '/home/user/JM-Claude-Playground/data/ideas-directories.csv'
    )
    print(f"Processed {dirs_count} directories in ideas-directories.csv")

if __name__ == '__main__':
    main()
