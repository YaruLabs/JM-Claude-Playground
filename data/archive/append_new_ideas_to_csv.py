"""
Script to append new directory ideas (DIR-176 to DIR-200) to the existing CSV file.
"""

import csv
from new_directory_ideas_176_200 import new_directory_ideas

# CSV headers in the correct order
headers = [
    "id", "title", "tagline", "category", "subcategory", "problem", "solution",
    "target_audience", "business_model", "pricing", "leap_l", "leap_e", "leap_a",
    "leap_p", "leap_total", "platform", "tam", "pain_points", "mvp_features",
    "monetization", "phase", "status", "created_date"
]

def write_new_ideas_to_csv(output_file="ideas-directories-new.csv"):
    """Write just the new ideas to a new CSV file."""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for idea in new_directory_ideas:
            writer.writerow(idea)
    print(f"Wrote {len(new_directory_ideas)} ideas to {output_file}")

def append_to_existing_csv(existing_file="ideas-directories.csv", output_file="ideas-directories-combined.csv"):
    """Read existing CSV and append new ideas."""
    # Read existing data
    existing_ideas = []
    with open(existing_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        existing_ideas = list(reader)

    print(f"Read {len(existing_ideas)} existing ideas from {existing_file}")

    # Combine
    all_ideas = existing_ideas + new_directory_ideas

    # Write combined file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for idea in all_ideas:
            writer.writerow(idea)

    print(f"Wrote {len(all_ideas)} total ideas to {output_file}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--append":
        append_to_existing_csv()
    else:
        write_new_ideas_to_csv()
        print("\nTo append to existing CSV, run: python append_new_ideas_to_csv.py --append")
