"""Re-render the 20-bit optimizer master comparison figure at book scale
for Appendix B of the Fragmented Aperture Antennas book.

Source data: master_results.npz (per-band bootstrap and per-trial fitness
arrays for HC / GA / SS-GA / SS+HC / Memetic).

Book scale: 4.79-inch text-width, two panels stacked vertically (a wide-by-
short side-by-side layout works at PIERS two-column but reads tiny in the
book single-column).

Panel A: Good Enough (0.5 dB) bootstrap-median evals, log y-axis.
Panel B: Strict (0.01 dB) per-band reach rate (% of trials).

Output: images/appendixB/master_comparison_20bit_book.{pdf,png}
"""
import os
import numpy as np
import matplotlib.pyplot as plt

NPZ = os.path.expanduser(
    '~/Library/CloudStorage/GoogleDrive-jmaloney65@gmail.com/My Drive/ai_design/'
    'exhaustive20/results/book_figures/part4_master_20bit_v4/master_results.npz')

OUT_DIR = os.path.expanduser(
    '~/github-clones/fragmented-aperture-book/images/appendixB')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PDF = os.path.join(OUT_DIR, 'master_comparison_20bit_book.pdf')

BANDS = ['0.5-0.8', '0.8-1.2', '1.2-1.6', '1.6-2.0',
         '2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']

# Plot 4 methods (pure GA omitted from the figure; HC / SS / SS+HC / Memetic).
METHODS = [
    ('hc',   'HC',      'tab:blue'),
    ('ss',   'SS-GA',   'tab:green'),
    ('sshc', 'SS+HC',   'tab:olive'),
    ('mem',  'Memetic', 'tab:red'),
]

EPS_STRICT = 0.01  # dB

data = np.load(NPZ, allow_pickle=True)


def gather():
    """Return per-band, per-method (good_med, strict_pct)."""
    rows = []
    for band in BANDS:
        bf_fit = float(data[f'{band}_bf_fit'])
        row = {'band': band, 'bf_fit': bf_fit}
        for key, _, _ in METHODS:
            fits = data[f'{band}_{key}_fits']
            boot = data[f'{band}_{key}_boot']
            row[f'{key}_med'] = float(np.median(boot))
            row[f'{key}_strict_pct'] = 100.0 * float(
                np.mean(np.abs(fits - bf_fit) <= EPS_STRICT))
        rows.append(row)
    return rows


rows = gather()

# Book column width 4.79 in; total height ~5.4 in (two panels ~2.3 in each).
FIG_W, FIG_H = 4.79, 5.4
fig, (axA, axB) = plt.subplots(2, 1, figsize=(FIG_W, FIG_H), constrained_layout=True)

x = np.arange(len(BANDS))
W = 0.20  # bar width
offsets = np.linspace(-1.5*W, 1.5*W, len(METHODS))

# Panel A: Good Enough bootstrap-median evals (log axis)
for off, (key, lbl, color) in zip(offsets, METHODS):
    vals = np.array([r[f'{key}_med'] for r in rows])
    axA.bar(x + off, vals, W, color=color, label=lbl,
            edgecolor='black', linewidth=0.3)
axA.set_yscale('log')
axA.set_xticks(x)
axA.set_xticklabels(BANDS, rotation=20, fontsize=7.5)
axA.set_ylabel('Bootstrap-median evals to 0.5 dB target', fontsize=8.5)
axA.tick_params(axis='y', labelsize=7.5)
axA.grid(True, alpha=0.25, axis='y', zorder=0, which='both')
axA.set_axisbelow(True)
axA.set_title('(A) Good Enough (0.5 dB): bootstrap-median evals',
              fontsize=9, pad=4)
axA.legend(fontsize=7, loc='upper left', ncol=4, columnspacing=0.8,
           handlelength=1.0, framealpha=0.92)

# Panel B: Strict reach rate (% of trials), linear axis 0-100
for off, (key, lbl, color) in zip(offsets, METHODS):
    vals = np.array([r[f'{key}_strict_pct'] for r in rows])
    axB.bar(x + off, vals, W, color=color, label=lbl,
            edgecolor='black', linewidth=0.3)
    # Annotate Memetic bars (the only ones that reach meaningful values)
    if key == 'mem':
        for xi, v in zip(x + off, vals):
            if v >= 1.0:
                axB.text(xi, v + 1.5, f'{v:.0f}', ha='center',
                         fontsize=6.5, color='black')
axB.set_xticks(x)
axB.set_xticklabels(BANDS, rotation=20, fontsize=7.5)
axB.set_xlabel('Reference band (GHz)', fontsize=8.5)
axB.set_ylabel('Strict reach rate (% of trials)', fontsize=8.5)
axB.set_ylim(0, 110)
axB.tick_params(axis='y', labelsize=7.5)
axB.grid(True, alpha=0.25, axis='y', zorder=0)
axB.set_axisbelow(True)
axB.set_title('(B) Strict (0.01 dB basin recovery): per-band reach %',
              fontsize=9, pad=4)

fig.savefig(OUT_PDF, bbox_inches='tight')
fig.savefig(OUT_PDF.replace('.pdf', '.png'), bbox_inches='tight', dpi=220)
print(f'Saved {OUT_PDF}')

# Print summary table for the record
print()
print('Per-band summary:')
print(f'{"Band":<10} {"BFfit":>8} | ' + ' | '.join(
    f'{lbl:>6} G/S' for _, lbl, _ in METHODS))
for r in rows:
    parts = [f'{r["band"]:<10} {r["bf_fit"]:8.4f} |']
    for key, _, _ in METHODS:
        parts.append(f'{r[f"{key}_med"]:6.0f}/{r[f"{key}_strict_pct"]:4.1f}')
    print(' '.join(parts))
