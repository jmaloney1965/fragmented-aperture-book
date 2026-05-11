"""Re-render the 24-bit optimizer master comparison figure at book scale,
same layout as the 20-bit version."""
import os
import numpy as np
import matplotlib.pyplot as plt

NPZ = os.path.expanduser(
    '~/Library/CloudStorage/GoogleDrive-jmaloney65@gmail.com/My Drive/ai_design/'
    'exhaustive20/results/book_figures/part4_master_24bit_v4/master_results.npz')

OUT_DIR = os.path.expanduser(
    '~/github-clones/fragmented-aperture-book/images/appendixB')
OUT_PDF = os.path.join(OUT_DIR, 'master_comparison_24bit_book.pdf')

BANDS = ['0.5-0.8', '0.8-1.2', '1.2-1.6', '1.6-2.0',
         '2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']

METHODS = [
    ('hc',   'HC',      'tab:blue'),
    ('ss',   'SS-GA',   'tab:green'),
    ('sshc', 'SS+HC',   'tab:olive'),
    ('mem',  'Memetic', 'tab:red'),
]

EPS_STRICT = 0.01

data = np.load(NPZ, allow_pickle=True)

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

FIG_W, FIG_H = 4.79, 5.4
fig, (axA, axB) = plt.subplots(2, 1, figsize=(FIG_W, FIG_H), constrained_layout=True)
x = np.arange(len(BANDS))
W = 0.20
offsets = np.linspace(-1.5*W, 1.5*W, len(METHODS))

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

for off, (key, lbl, color) in zip(offsets, METHODS):
    vals = np.array([r[f'{key}_strict_pct'] for r in rows])
    axB.bar(x + off, vals, W, color=color, label=lbl,
            edgecolor='black', linewidth=0.3)
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

print('\nPer-band summary (24-bit):')
print(f'{"Band":<10} {"BFfit":>8} | ' + ' | '.join(
    f'{lbl:>6} G/S' for _, lbl, _ in METHODS))
for r in rows:
    parts = [f'{r["band"]:<10} {r["bf_fit"]:8.4f} |']
    for key, _, _ in METHODS:
        parts.append(f'{r[f"{key}_med"]:6.0f}/{r[f"{key}_strict_pct"]:4.1f}')
    print(' '.join(parts))
