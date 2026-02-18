#!/usr/bin/env python3
"""
Organize IEEE Xplore bibliography entries into chapter-specific .bib files
Based on PAPER_CLEANUP_DECISIONS.md categorization
"""

import re
import os

# Category definitions based on PAPER_CLEANUP_DECISIONS.md
CATEGORIES = {
    'fragmented_aperture_core': {
        'filename': 'fragmented_aperture_core.bib',
        'description': 'Core Fragmented Aperture Work (GTRI + External)',
        'cite_keys': [
            # Category 1: GTRI Papers (keep 17, delete Martinello2011Fragmented)
            'Howard2024Topology', 'Landgren2019Broadband', 'Zang2019Optimum',
            'Cook2019Printed', 'Kiesel2018Conex', 'Dykes2017Wideband',
            'Landgren2017Wideband', 'Hughes2015Integration', 'Hughes2015Co-design',
            'Maloney2013Genetic', 'Maloney2011Wide', 'Wang2010Broadband',
            'Herscovici2008Fragmented', 'Maloney2007Fragmented',
            'Ellgardt2006Characteristics', 'Thors2005Broad-band', 'Maloney2000Switched',
            # Category 2: External Fragmented Work
            'Wu2025Efficient', 'E2023Design', 'Barani2018Fragmented',
        ]
    },

    'ml_ai_optimization_methods': {
        'filename': 'ml_ai_optimization_methods.bib',
        'description': 'ML/AI and Modern Optimization Methods',
        'cite_keys': [
            # Category 3: Modern ML/AI Pixelated (20 papers)
            'Chen2026Surrogate', 'Istiaque2025Design', 'Pang2025Knowledge',
            'Lou2025Frequency', 'Li2025Inverse', 'Yang2025Self-decoupled',
            'Zeghdoud2025Accelerated', 'Wang2024Bandwidth', 'Wang2024Machine',
            'Chen2024Advancing', 'Mair2024Design', 'Karahan2024Deep',
            'Grant2024Automated', 'Tang2024Performance', 'Yang2024Generative',
            'Pollini2024Human', 'Mair2022Evolutionary', 'Jacobs2022Accurate',
            'Li2019Automated', 'Kiesel2015Optimization',
        ]
    },

    'metamaterials_ch8': {
        'filename': 'metamaterials_ch8.bib',
        'description': 'MetaMaterials, RIS, and FSS for Chapter 8',
        'cite_keys': [
            # Category 4: Metasurfaces/RIS/FSS (35 papers)
            # Will add these based on keywords: metasurface, RIS, FSS, reflectarray
        ]
    },

    'reconfigurable_ch5': {
        'filename': 'reconfigurable_ch5.bib',
        'description': 'Reconfigurable Antennas for Chapter 5',
        'cite_keys': [
            # Category 5: Reconfigurable (12 papers)
            # Note: Lou2025Frequency already in ML/AI, will appear in both
            'Xu2025Reconfigurable', 'Tang2023Dual-port', 'Qiao2023Novel',
            'Bichara2021Miniaturized', 'Towfiq2018Reconfigurable', 'Wright2018Mems',
            'Pal2018Magnetically', 'Wright2016Effect', 'Ouedraogo2014Tunable',
            'Ali2014Mems', 'Kovitz2011Micro',
        ]
    },

    'mimo_multiband': {
        'filename': 'mimo_multiband.bib',
        'description': 'MIMO and Multiband Antennas (Saved for Future)',
        'cite_keys': [
            # Category 6: MIMO/Multiband (10 papers)
            'Odiamenhi2025Design', 'Basherlou2023Qr', 'Ullah2023Multiservice',
            'Zhang2021Compact', 'Soltani2016Mimo', 'Chen2015Pixelated',
            'Chen2014Antenna',
        ]
    },

    'specialized_applications': {
        'filename': 'specialized_applications.bib',
        'description': 'Specialized Applications (Saved for Future)',
        'cite_keys': [
            # Category 8: Specialized (18 papers) - keeping all
            # Absorbers, Lenses, THz, Transparent, GA studies, etc.
        ]
    },

    'deleted_non_rf': {
        'filename': 'deleted_non_rf.bib',
        'description': 'Non-RF Papers (For Reference Only)',
        'cite_keys': [
            # Category 7: Obviously Wrong (15 papers + 1 camera optics)
            'Martinello2011Fragmented',  # Camera optics from Category 1
            'Kandil2024Experimental', 'Bogaerts2021Pixelated', 'York2014Frames',
            'Kreucher2012Optimal', 'Salary2020Time', 'Ruan2024Broadband',
            'Liu2021Pixelated', 'Lim2021Low', 'Wang2020Bernoulli',
            'Madden2023Calibration', 'Sanusi2022Pixelated', 'Zhou2025Ai',
            'Ussmueller2023Maintenance', 'Gradoni2024Interference',
        ]
    }
}

def parse_bib_file(filename):
    """Parse a .bib file and return list of entries as (cite_key, entry_text)"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by @ to get individual entries
    entries = []
    pattern = r'@(\w+)\{([^,]+),(.*?)\n\}'

    for match in re.finditer(pattern, content, re.DOTALL):
        entry_type = match.group(1)
        cite_key = match.group(2)
        entry_content = match.group(3)
        full_entry = f"@{entry_type}{{{cite_key},{entry_content}\n}}"
        entries.append((cite_key, full_entry))

    return entries

def categorize_by_keywords(cite_key, entry_text):
    """Categorize entries not explicitly listed based on keywords"""
    text_lower = entry_text.lower()

    # Check for metasurfaces/RIS/FSS keywords
    meta_keywords = ['metasurface', 'metamaterial', 'ris', 'reconfigurable intelligent',
                     'frequency selective', 'fss', 'reflectarray', 'transmitarray']
    if any(kw in text_lower for kw in meta_keywords):
        # But exclude if it's reconfigurable antenna
        if 'reconfigurable' in text_lower and 'antenna' in text_lower:
            return 'reconfigurable_ch5'
        return 'metamaterials_ch8'

    # Check for MIMO keywords
    mimo_keywords = ['mimo', 'multiband', 'dual-band', 'tri-band', 'multi-band']
    if any(kw in text_lower for kw in mimo_keywords):
        return 'mimo_multiband'

    # Check for specialized keywords
    spec_keywords = ['absorber', 'lens antenna', 'terahertz', 'thz', 'transparent',
                     'genetic algorithm', 'topology optimization']
    if any(kw in text_lower for kw in spec_keywords):
        return 'specialized_applications'

    # Default to specialized if can't categorize
    return 'specialized_applications'

def main():
    # Read all IEEE export .bib files
    bib_files = [
        'export2026.02.17-11.37.40.bib',
        'export2026.02.17-11.38.27.bib',
        'export2026.02.17-11.38.54.bib',
        'export2026.02.17-11.39.19.bib',
    ]

    # Initialize output buckets
    output_buckets = {cat: [] for cat in CATEGORIES.keys()}
    stats = {cat: 0 for cat in CATEGORIES.keys()}

    # Parse all entries
    all_entries = []
    for bib_file in bib_files:
        if os.path.exists(bib_file):
            entries = parse_bib_file(bib_file)
            all_entries.extend(entries)
            print(f"Read {len(entries)} entries from {bib_file}")

    print(f"\nTotal entries read: {len(all_entries)}")

    # Categorize each entry
    for cite_key, entry_text in all_entries:
        categorized = False

        # Check against explicit cite_key lists
        for category, cat_info in CATEGORIES.items():
            if cite_key in cat_info['cite_keys']:
                output_buckets[category].append((cite_key, entry_text))
                stats[category] += 1
                categorized = True
                break

        # If not explicitly categorized, use keyword matching
        if not categorized:
            category = categorize_by_keywords(cite_key, entry_text)
            output_buckets[category].append((cite_key, entry_text))
            stats[category] += 1

    # Write output files
    print("\n" + "="*70)
    print("WRITING CHAPTER-SPECIFIC BIBLIOGRAPHY FILES")
    print("="*70)

    for category, cat_info in CATEGORIES.items():
        filename = cat_info['filename']
        description = cat_info['description']
        entries = output_buckets[category]

        with open(filename, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"% {description}\n")
            f.write(f"% Generated: 2026-02-18\n")
            f.write(f"% Total entries: {len(entries)}\n")
            f.write(f"%\n")
            f.write(f"% Source: IEEE Xplore exports organized by category\n")
            f.write(f"%\n\n")

            # Write entries (sorted by cite key)
            entries_sorted = sorted(entries, key=lambda x: x[0])
            for cite_key, entry_text in entries_sorted:
                f.write(entry_text)
                f.write("\n\n")

        print(f"✅ {filename:40s} {len(entries):3d} entries - {description}")
        stats[category] = len(entries)

    # Print summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    total_kept = sum(stats[cat] for cat in stats if cat != 'deleted_non_rf')
    total_deleted = stats['deleted_non_rf']

    print(f"\n📚 KEPT:    {total_kept:3d} papers (organized into 6 topic areas)")
    print(f"🗑️  DELETED: {total_deleted:3d} papers (saved to reference file)")
    print(f"📊 TOTAL:   {total_kept + total_deleted:3d} papers processed")
    print("\n✅ Done! Chapter-specific .bib files created.")

if __name__ == '__main__':
    main()
