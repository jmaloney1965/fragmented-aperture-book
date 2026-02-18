#!/usr/bin/env python3
"""Remove duplicate entries from .bib files"""

import re
import glob

def deduplicate_bib_file(filename):
    """Remove duplicate entries from a .bib file"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into header and entries
    lines = content.split('\n')
    header = []
    for i, line in enumerate(lines):
        if line.startswith('@'):
            break
        header.append(line)

    # Parse entries
    pattern = r'(@\w+\{[^,]+,.*?\n\})'
    entries = re.findall(pattern, content, re.DOTALL)

    # Deduplicate by cite key
    seen = set()
    unique_entries = []
    duplicates = 0

    for entry in entries:
        cite_key_match = re.search(r'@\w+\{([^,]+),', entry)
        if cite_key_match:
            cite_key = cite_key_match.group(1)
            if cite_key not in seen:
                seen.add(cite_key)
                unique_entries.append(entry)
            else:
                duplicates += 1

    # Update header with correct count
    header_text = '\n'.join(header)
    header_text = re.sub(r'% Total entries: \d+', f'% Total entries: {len(unique_entries)}', header_text)

    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header_text)
        if not header_text.endswith('\n'):
            f.write('\n')
        for entry in unique_entries:
            f.write(entry)
            f.write('\n\n')

    return len(unique_entries), duplicates

# Process all .bib files (except exports and master)
bib_files = [
    'fragmented_aperture_core.bib',
    'ml_ai_optimization_methods.bib',
    'metamaterials_ch8.bib',
    'reconfigurable_ch5.bib',
    'mimo_multiband.bib',
    'specialized_applications.bib',
    'deleted_non_rf.bib',
]

print("Deduplicating .bib files...")
print("="*70)

total_kept = 0
total_removed = 0

for filename in bib_files:
    unique, dups = deduplicate_bib_file(filename)
    total_kept += unique
    total_removed += dups
    status = f"✅ {filename:40s} {unique:3d} unique ({dups} duplicates removed)"
    print(status)

print("="*70)
print(f"Total unique entries: {total_kept}")
print(f"Total duplicates removed: {total_removed}")
print("✅ Done!")
