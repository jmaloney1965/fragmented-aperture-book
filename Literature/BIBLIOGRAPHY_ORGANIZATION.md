# Bibliography Organization Summary
**Date**: February 18, 2026
**Status**: ✅ Complete - Ready for Chapter Integration

---

## What Was Done

From 165 IEEE Xplore papers, organized into **7 chapter-specific .bib files**:
- **134 unique papers** organized into 6 topic areas (kept)
- **9 non-RF papers** moved to reference file (deleted)
- **31 duplicates** removed (same paper appeared in multiple IEEE searches)

---

## Chapter-Specific Bibliography Files

### 📚 Core Work

#### 1. `fragmented_aperture_core.bib` (20 papers)
**Use in**: Chapters 1, 2, 3, 4, 6, 7

Essential fragmented aperture papers including:
- **Your publications** (Maloney et al.)
- **GTRI team work** (Landgren, Dykes, Howard, etc.)
- **External researchers** (Barani, Thors, Herscovici, etc.)

**Key papers**:
- Thors 2005 - GA for broadband fragmented apertures ⭐⭐⭐
- Maloney 2013 - 24-bit genetic algorithm design ⭐⭐⭐
- Maloney 2011 - Wide scan PCB fragmented array ⭐⭐⭐
- Barani 2018 - Coupled small radiating elements ⭐⭐⭐
- Landgren 2019 - Unbalanced feeds and power combiners ⭐⭐⭐

---

### 🤖 Modern Methods

#### 2. `ml_ai_optimization_methods.bib` (17 papers)
**Use in**: Chapter 3 (Improved Approach) or new Chapter 9

Modern optimization techniques for antenna design:
- **Machine Learning** (neural networks, deep learning)
- **Genetic Algorithms** (evolutionary optimization)
- **Topology Optimization** (level set, surrogate-assisted)
- **Reinforcement Learning** (RL-based design)

**Sample papers**:
- Chen 2026 - Surrogate-assisted level set topology opt
- Pang 2025 - Knowledge-guided ML for pixelated patch
- Wang 2024 - Pixelated patch with reinforcement learning
- Li 2025 - Inverse design with residual neural networks
- Kiesel 2015 - Optimization of pixelated antennas (GTRI)

**Recommendation**: Could become:
- Part of Ch 3 (modern GA/ML methods)
- OR new chapter: "Modern Computational Methods"

---

### 🔮 MetaMaterials

#### 3. `metamaterials_ch8.bib` (30 papers)
**Use in**: Chapter 8 (MetaMaterials and Antennas)

Papers on metasurfaces, RIS, and frequency selective surfaces:
- **Reconfigurable Intelligent Surfaces (RIS)**
- **Frequency Selective Surfaces (FSS)**
- **Metasurface antennas**
- **Reflectarrays and transmitarrays**

**Sample papers**:
- Lyu 2026 - Generative FSS with deep learning
- Banks 2025 - Pixelated metasurface with GA
- Chandrakapure 2024 - Automated metasurface with PSO
- Melouki 2022 - Fabry-Perot with pixelated PRS

**Note**: This collection supports your planned Ch 8 or could become a future book.

---

### ⚡ Reconfigurable

#### 4. `reconfigurable_ch5.bib` (13 papers)
**Use in**: Chapter 5 (Reconfigurable Fragmented Aperture Antennas)

Reconfigurable and tunable pixelated antennas:
- **Frequency reconfigurable** (switches, varactors, VO2)
- **MEMS-based reconfiguration**
- **Magnetically actuated pixels**
- **Beam steering**

**Key papers**:
- Lou 2025 - Frequency reconfig pixelated (VO2)
- Tang 2023 - Dual-port mmWave reconfigurable
- Wright 2018 - MEMS reconfigurable broadband patch
- Ali 2014 - MEMS reconfigurable pixel patch (CLAS)
- Kovitz 2011 - Micro-actuated pixel patch with PSO

---

### 📡 MIMO & Multiband (SAVED)

#### 5. `mimo_multiband.bib` (9 papers)
**Use in**: Future work, Chapter 6, or Chapter 9

MIMO and multiband pixelated designs:
- **MIMO antennas** for wireless systems
- **Dual-band and multi-band** designs
- **Self-decoupling techniques**
- **IoT applications**

**Note**: Not core to current book focus, but saved for:
- Potential Chapter 9 (Reconfigurable Arrays)
- Future applications chapter
- Reference material

---

### 🔬 Specialized Applications (SAVED)

#### 6. `specialized_applications.bib` (36 papers)
**Use in**: Background reading, future chapters

Specialized topics including:
- **Absorbers and RCS reduction** (5 papers)
- **Lens antennas** (3 papers)
- **Terahertz and mmWave** (4 papers)
- **Transparent antennas** (2 papers)
- **Additional GA studies** (4 papers)
- **Various applications** (18 papers)

**Note**: Saved for future reference, not core to current book.

---

### 🗑️ Deleted Non-RF (REFERENCE ONLY)

#### 7. `deleted_non_rf.bib` (9 papers)
**Not for use** - kept only for documentation

Papers that are NOT RF antennas:
- Camera optics (Martinello 2011)
- Optical sensors and LiDAR
- Neural recording systems
- Sensor networks
- Power amplifiers

**Why saved**: In case you ever wonder "what happened to paper X?"

---

## How to Use These Files

### In Your LaTeX Chapters

Each chapter uses the `chapterbib` package for per-chapter bibliographies.

**Example for Chapter 3** (Improved Approach):
```latex
\bibliography{../Literature/fragmented_aperture_core,%
              ../Literature/ml_ai_optimization_methods}
\bibliographystyle{IEEEtran}

% Then cite papers:
\cite{Thors2005Broad-band}  % GA for fragmented apertures
\cite{Chen2026Surrogate}     % Modern topology optimization
```

**Example for Chapter 5** (Reconfigurable):
```latex
\bibliography{../Literature/fragmented_aperture_core,%
              ../Literature/reconfigurable_ch5}
\bibliographystyle{IEEEtran}
```

**Example for Chapter 8** (MetaMaterials):
```latex
\bibliography{../Literature/metamaterials_ch8}
\bibliographystyle{IEEEtran}
```

---

## Recommended Chapter-to-Bibliography Mapping

| Chapter | Primary .bib Files | Secondary .bib Files |
|---------|-------------------|---------------------|
| **Ch 1: Introduction** | `fragmented_aperture_core` | — |
| **Ch 2: Original Approach** | `fragmented_aperture_core` | — |
| **Ch 3: Improved Approach** | `fragmented_aperture_core`<br>`ml_ai_optimization_methods` | — |
| **Ch 4: Sample Design** | `fragmented_aperture_core` | — |
| **Ch 5: Reconfigurable** | `reconfigurable_ch5` | `fragmented_aperture_core` |
| **Ch 6: Fragmented Arrays** | `fragmented_aperture_core` | `mimo_multiband` (optional) |
| **Ch 7: Wideband Arrays** | `fragmented_aperture_core` | — |
| **Ch 8: MetaMaterials** | `metamaterials_ch8` | `ml_ai_optimization_methods` |
| **Ch 9: Reconfig Arrays** *(missing)* | `reconfigurable_ch5`<br>`fragmented_aperture_core` | `mimo_multiband` |
| **Appendix A: Modeling** | `fragmented_aperture_core` | — |

---

## Statistics

### Papers by Topic Area

| Topic | Count | % of Total |
|-------|-------|-----------|
| **Core Fragmented Aperture** | 20 | 15% |
| **ML/AI Optimization** | 17 | 13% |
| **MetaMaterials/RIS** | 30 | 22% |
| **Reconfigurable** | 13 | 10% |
| **MIMO/Multiband** | 9 | 7% |
| **Specialized Apps** | 36 | 27% |
| **Non-RF (deleted)** | 9 | 7% |
| **TOTAL UNIQUE** | **134** | **100%** |

### Papers by Year

**Most recent** (2024-2026): ~45 papers
**Recent** (2018-2023): ~55 papers
**Foundational** (2000-2017): ~34 papers

---

## What's Next

### Immediate (This Week):

1. ✅ **DONE**: Organize 165 papers into chapter-specific .bib files
2. ✅ **DONE**: Remove duplicates (31 removed)
3. ✅ **DONE**: Delete non-RF papers (9 moved to reference)
4. ⏳ **TODO**: Review downloaded PDFs (Thors 2005, Pringle 2004, etc.)
5. ⏳ **TODO**: Add citations to existing chapters

### Near-Term (Next 2 Weeks):

6. Read top 10-15 essential papers thoroughly
7. Integrate citations into Ch 1-7
8. Identify gaps in Ch 3 (modern methods)
9. Plan Ch 8 (MetaMaterials) structure
10. Plan Ch 9 (Reconfigurable Arrays) - currently missing

### Long-Term:

11. Update `master_bibliography.bib` with all 134 entries
12. Download remaining paywalled papers (if needed)
13. Create citation summary tables per chapter
14. Write missing sections referencing new papers

---

## Key Files in Literature Folder

```
Literature/
├── fragmented_aperture_core.bib           (20 entries) ⭐ CORE
├── ml_ai_optimization_methods.bib         (17 entries) ⭐ NEW
├── metamaterials_ch8.bib                  (30 entries) ⭐ CH 8
├── reconfigurable_ch5.bib                 (13 entries) ⭐ CH 5
├── mimo_multiband.bib                     (9 entries)  💾 SAVED
├── specialized_applications.bib           (36 entries) 💾 SAVED
├── deleted_non_rf.bib                     (9 entries)  🗑️ REFERENCE
│
├── master_bibliography.bib                (32 entries from web search)
│
├── export2026.02.17-11.37.40.bib         (18 entries - raw IEEE export)
├── export2026.02.17-11.38.27.bib         (20 entries - raw IEEE export)
├── export2026.02.17-11.38.54.bib         (14 entries - raw IEEE export)
├── export2026.02.17-11.39.19.bib         (113 entries - raw IEEE export)
│
├── IEEE_Papers/                           (8 PDFs downloaded)
│   ├── Thors2005_Broadband_Fragmented_GA.pdf ⭐⭐⭐
│   ├── Pringle2004_Reconfigurable_Switched_Links.pdf ⭐⭐⭐
│   ├── Barani2018_Fragmented_Coupled_Elements.pdf ⭐⭐
│   └── ... (5 more)
│
├── Open_Access/                           (8 PDFs downloaded)
│   ├── Landgren2017_Unbalanced_Feed_Design.pdf ⭐⭐⭐
│   ├── Evolutionary_Optimisation_Pixelated_IFA_2024.pdf ⭐⭐
│   └── ... (6 more)
│
└── Documentation/
    ├── PAPER_CLEANUP_DECISIONS.md         (original categorization)
    ├── BIBLIOGRAPHY_ORGANIZATION.md       (this file)
    ├── SOURCES_SUMMARY.md                 (all sources found)
    └── DOWNLOADED_PAPERS.md               (PDF inventory)
```

---

## Success! 🎉

**134 papers** organized and ready for integration into your book!

**Core collection**: 20 essential fragmented aperture papers
**Modern methods**: 17 ML/AI optimization papers
**Specialty topics**: 97 papers on metasurfaces, reconfigurable, MIMO, etc.
**Saved for future**: 45 papers (MIMO + specialized apps)

**Next step**: Start integrating citations into your chapters!

---

**Questions or need help?**
- Want to see which papers are in a specific category? Read the .bib file
- Want to add more papers? Add them to the appropriate .bib file
- Want to move papers between categories? Edit the .bib files manually or rerun `organize_bibliography.py`
- Want chapter-specific citation counts? I can generate that!

---

✅ **Bibliography cleanup and organization: COMPLETE!**
