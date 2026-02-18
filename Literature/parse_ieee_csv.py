#!/usr/bin/env python3
"""
Parse IEEE Xplore CSV export files and generate BibTeX entries
"""
import csv
import re
import sys
from pathlib import Path

def clean_field(text):
    """Clean and format field text"""
    if not text:
        return ""
    # Remove quotes and extra whitespace
    text = text.strip().strip('"')
    return text

def format_authors(authors_str):
    """Convert 'First Last; First Last' to BibTeX format"""
    if not authors_str:
        return ""
    authors = [a.strip() for a in authors_str.split(';')]
    return " and ".join(authors)

def generate_cite_key(authors, year, title):
    """Generate BibTeX citation key"""
    # Get first author's last name
    if not authors:
        first_author = "Unknown"
    else:
        first_author = authors.split(';')[0].strip().split()[-1]

    # Get first significant word from title (skip articles)
    skip_words = {'a', 'an', 'the', 'on', 'for', 'of', 'in'}
    title_words = [w for w in title.lower().split() if w not in skip_words and len(w) > 3]
    title_word = title_words[0].capitalize() if title_words else "Paper"

    return f"{first_author}{year}{title_word}"

def csv_to_bibtex(csv_file, output_file, filter_keywords=None):
    """Convert IEEE Xplore CSV to BibTeX format"""
    entries = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            title = clean_field(row.get('Document Title', ''))
            authors = clean_field(row.get('Authors', ''))
            year = clean_field(row.get('Publication Year', ''))
            pub_title = clean_field(row.get('Publication Title', ''))
            volume = clean_field(row.get('Volume', ''))
            issue = clean_field(row.get('Issue', ''))
            start_page = clean_field(row.get('Start Page', ''))
            end_page = clean_field(row.get('End Page', ''))
            doi = clean_field(row.get('DOI', ''))
            abstract = clean_field(row.get('Abstract', ''))
            keywords = clean_field(row.get('Author Keywords', ''))

            # Skip if no title or year
            if not title or not year:
                continue

            # Filter by keywords if specified
            if filter_keywords:
                text_to_search = f"{title} {abstract} {keywords}".lower()
                if not any(kw.lower() in text_to_search for kw in filter_keywords):
                    continue

            # Determine entry type
            if 'conference' in pub_title.lower() or 'symposium' in pub_title.lower() or 'proceedings' in pub_title.lower():
                entry_type = 'inproceedings'
                pub_field = 'booktitle'
            else:
                entry_type = 'article'
                pub_field = 'journal'

            # Generate citation key
            cite_key = generate_cite_key(authors, year, title)

            # Build BibTeX entry
            bibtex = f"@{entry_type}{{{cite_key},\n"
            bibtex += f"  author    = {{{format_authors(authors)}}},\n"
            bibtex += f"  title     = {{{title}}},\n"
            if pub_title:
                bibtex += f"  {pub_field}  = {{{pub_title}}},\n"
            bibtex += f"  year      = {{{year}}},\n"
            if volume:
                bibtex += f"  volume    = {{{volume}}},\n"
            if issue:
                bibtex += f"  number    = {{{issue}}},\n"
            if start_page:
                pages = f"{start_page}--{end_page}" if end_page else start_page
                bibtex += f"  pages     = {{{pages}}},\n"
            if doi:
                bibtex += f"  doi       = {{{doi}}},\n"
            bibtex += "}\n"

            entries.append({
                'bibtex': bibtex,
                'cite_key': cite_key,
                'year': int(year) if year.isdigit() else 0,
                'title': title,
                'authors': authors,
                'abstract': abstract[:200] + '...' if len(abstract) > 200 else abstract
            })

    # Sort by year (newest first)
    entries.sort(key=lambda x: x['year'], reverse=True)

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("% Generated from IEEE Xplore CSV export\n")
        f.write(f"% Total entries: {len(entries)}\n")
        f.write(f"% Source: {csv_file}\n\n")
        for entry in entries:
            f.write(entry['bibtex'] + '\n')

    return entries

if __name__ == "__main__":
    lit_dir = Path(__file__).parent
    csv_files = list(lit_dir.glob("export*.csv"))

    print(f"Found {len(csv_files)} CSV files to process")

    # Process each CSV
    for csv_file in csv_files:
        output_file = csv_file.with_suffix('.bib')
        print(f"\nProcessing {csv_file.name}...")

        # Detect search type from first entry
        filter_kw = None
        if 'fragmented aperture' in open(csv_file).read(5000).lower():
            filter_kw = ['fragmented aperture', 'fragmented antenna']

        entries = csv_to_bibtex(csv_file, output_file, filter_keywords=filter_kw)
        print(f"  Generated {len(entries)} BibTeX entries -> {output_file.name}")

        # Show first 5
        print(f"  Recent papers:")
        for entry in entries[:5]:
            print(f"    [{entry['year']}] {entry['title']}")

    print("\n✓ Done! BibTeX files created in Literature/ directory")
