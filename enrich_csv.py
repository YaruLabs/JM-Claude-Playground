#!/usr/bin/env python3
"""
Master script to enrich ideas-claude.csv with researched data.
Reads enrichment data from batch files and applies to CSV.
"""
import csv
import importlib
import sys
import os

def load_enrichments():
    """Load all enrichment batch modules and combine."""
    all_enrichments = {}
    batch_dir = os.path.join(os.path.dirname(__file__), 'data', 'enrichments')
    sys.path.insert(0, batch_dir)

    batch_files = sorted([f for f in os.listdir(batch_dir) if f.startswith('batch_') and f.endswith('.py')])

    for batch_file in batch_files:
        module_name = batch_file[:-3]  # Remove .py
        print(f"Loading {batch_file}...")
        mod = importlib.import_module(module_name)
        all_enrichments.update(mod.ENRICHMENTS)

    return all_enrichments

def enrich_csv(input_path, output_path, enrichments):
    """Read CSV, apply enrichments, write updated CSV."""
    rows = []
    with open(input_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(dict(row))

    enriched_count = 0
    fields_filled = 0

    for row in rows:
        idea_id = row['id']
        if idea_id in enrichments:
            enriched_count += 1
            updates = enrichments[idea_id]
            for field, value in updates.items():
                if field in row:
                    current = row[field].strip() if row[field] else ''
                    # Only fill if empty or if the current value is clearly wrong
                    # (e.g., it's a duplicate of another field)
                    if not current or current == row.get('tagline', '').strip() or current == row.get('title', '').strip() or len(current) < 10:
                        row[field] = value
                        fields_filled += 1
                    elif field == 'solution' and len(current) < 80:
                        # Replace short solutions with better ones
                        row[field] = value
                        fields_filled += 1
                    elif field == 'problem' and len(current) < 80:
                        row[field] = value
                        fields_filled += 1

    # Write enriched CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nEnrichment complete:")
    print(f"  Ideas enriched: {enriched_count}/{len(rows)}")
    print(f"  Fields filled: {fields_filled}")
    print(f"  Output: {output_path}")

def validate_csv(path):
    """Validate the enriched CSV."""
    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"\nValidation of {path}:")
    print(f"  Total rows: {len(rows)}")

    fields_to_check = ['solution', 'target_audience', 'platform', 'pricing', 'tam', 'business_model', 'pain_points', 'mvp_features']
    for field in fields_to_check:
        empty = sum(1 for r in rows if not r.get(field, '').strip() or len(r.get(field, '').strip()) < 10)
        pct = empty / len(rows) * 100
        print(f"  {field}: {len(rows)-empty}/{len(rows)} filled ({100-pct:.0f}%)")

    # Check solution lengths
    short_solutions = sum(1 for r in rows if len(r.get('solution', '').strip()) < 80)
    print(f"\n  Solutions < 80 chars: {short_solutions}/{len(rows)}")

if __name__ == '__main__':
    input_csv = os.path.join(os.path.dirname(__file__), 'data', 'ideas-claude.csv')
    output_csv = os.path.join(os.path.dirname(__file__), 'data', 'ideas-claude-enriched.csv')

    enrichments = load_enrichments()
    print(f"Loaded {len(enrichments)} enrichment entries")

    enrich_csv(input_csv, output_csv, enrichments)
    validate_csv(output_csv)
