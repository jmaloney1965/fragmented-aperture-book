# Paper Audit Plan — March 10, 2026

## Overview
Full audit of 127 papers in Literature/Papers/ against 10 chapters.
Four agents assessed all uncited papers. Results consolidated below.

## Housekeeping — Files to Remove
These are misfiled or irrelevant:
- `Allen2015_PhD_Microsphere_Photonics.pdf` — photonics PhD thesis, wrong domain
- `METU_TCA_Thesis.pdf` — space architecture thesis, misfiled
- `SaadFalcon2024_CFTR_ATP.pdf` — biophysics paper, wrong domain
- `SaadFalcon2024_Grassmannian_SAM.pdf` — duplicate of CFTR biophysics paper
- `SaadFalcon2024_MANGO_arXiv.pdf` — pure ML/computer vision, no EM connection
- `HorizPol_Omni_DGS.pdf` — conventional DGS patch, not pixelated/fragmented

## SKIP — Papers to Keep But Not Cite
These are in the library for reference but don't warrant citation:
- `Antenna_Design_5G_6G_IoT_MDPI.pdf` — edited collection cover, not a single paper
- `Behera2022_Microstrip_Evolutionary_Optimization.pdf` — shallow survey, no fragmented apertures
- `Ho2020_Denoising_Diffusion_Probabilistic_Models.pdf` — foundational ML, no EM (have Guo2025 which applies diffusion to EM)
- `Kingma2013_VAE_Auto_Encoding_Variational_Bayes.pdf` — foundational ML, no EM
- `SohlDickstein2015_Deep_Unsupervised_Nonequilibrium_Thermodynamics.pdf` — foundational diffusion, no EM
- `Lee2004_TEM_Horn_Design.pdf` — TEM horn design, not fragmented
- `Liu2005_PBG_DGS_Harmonic_Suppression.pdf` — PBG/DGS, tangential only
- `Sung2003_DGS_Harmonics_Reduction.pdf` — DGS harmonic suppression, not fragmented
- `Tayli2016_Physical_Bounds_Ground_Plane.pdf` — theoretical Q-bounds, not fragmented
- `Oskooi2010_MEEP_FDTD.pdf` — MEEP FDTD tool (already cited in Ch 9 as Oskooi2010Meep)
- `ElBadawe2016_True_Metasurface_APS.pdf` — conference version, redundant with journal

## Phase 1: CITE-only additions (no figures needed)
Quick wins — add citation + brief text. Grouped by chapter.

### Ch 5 (Reconfigurable)
- [ ] `Chen2025_REMAA_arXiv.pdf` — Reconfigurable pixel antenna arrays for MIMO, beamforming
- [ ] `Han2026_AngularSensing_arXiv.pdf` — HRPA for angle-of-arrival sensing
- [ ] `Shen2025_AntennaCoding_arXiv.pdf` — Antenna coding with pixel switch states

### Ch 6 (Wideband Arrays)
- [ ] `Dang2025_TCDA_Frontiers.pdf` — Low-profile wideband TCDA, competing technology
- [ ] `Doane2013_TCDA_Integrated_Balun.pdf` — TCDA with Marchand balun, 7.35:1 BW
- [ ] `Hosseini2023_TCDA_Metasurface.pdf` — TCDA with metasurface superstrate analysis

### Ch 9 (Recent Innovations / ML-AI)
- [ ] `Koziel2024_Reduced_Dimensionality.pdf` — ML surrogates with reduced-dimensionality
- [ ] `Koziel2024_Versatile_Unsupervised.pdf` — Unsupervised automated antenna design
- [ ] `LowProfile_DualBand_Pixelated_IoT_2022.pdf` — Pixelated DGS for IoT
- [ ] `Multiband_Antenna_ImageSegmentation_2025.pdf` — Logo-to-antenna via pixelation
- [ ] `Tang2023_Dual_Port_mmW_Pixel.pdf` — Dual-port mmWave pixel reconfigurable (already cited in Ch 4)
- [ ] `Genetic_Wire_Antenna_Designs.pdf` — Altshuler 1997, foundational GA antenna
- [ ] `Genetic_Wire_Antenna_SelfResonant.pdf` — Altshuler 2002, GA small antennas near Q limits
- [ ] `Genetic_Representation_Significance.pdf` — GA representation study for wire antennas
- [ ] `Genetic_Antenna_MultiFreq_DielectricPowder.pdf` — GA multi-freq wire antenna in dielectric

### Ch 10 (Other EM Structures)
- [ ] `ElBadawe2016_True_Metasurface_Antenna.pdf` — True metasurface antenna (ERR array) — **NOTE: previously confirmed NOT pixelated/fragmented; session notes say "don't use in Ch 10". Verify before adding.**

## Phase 2: FIGURE extractions + citations
Papers where we should extract key figures and add substantive text.

### Ch 3 (Improved Approach)
- [ ] `Mair2022_Evolutionary_5G_IoT.pdf` — Cross-shaped pixel optimization for IoT
- [ ] `Mair2024_IFA_ScientificReports.pdf` — Einstein Hat tile pixels for IFA
- [ ] `Mair2024_Pixel_Size_Symmetry.pdf` — Pixel size/symmetry effects on gain
- [ ] `Li2019_Automated_Pixelated_Topology.pdf` — Multi-objective BPSO pixelated design (already cited in Ch 3)
- [ ] `Merulla2008_Fragmented_Wire_Antenna.pdf` — Wire-based fragmented antenna, fabricated

### Ch 4 (Advanced Fragmented)
- [ ] `Cook2019_3DPrinted_Fragmented.pdf` — 3D-printed voxel fragmented antenna, GTRI, 3:1 BW RHCP
- [ ] `MaloneyBaker_GPS_CRPA_ModelMeasurements.pdf` — Miniaturized GPS CRPA array

### Ch 5/8 (Reconfigurable)
- [ ] `Kiesel2017_Cylindrical_Reconfigurable.pdf` — Cylindrical switched pixel antennas
- [ ] `Lou2025_VO2_Frequency_Reconfig.pdf` — VO2 phase-change reconfigurable pixels (already cited in Ch 5)

### Ch 6/7 (Wideband / Wide-Scan Arrays)
- [ ] `Thors2005_Broadband_Fragmented_GA.pdf` — GA fragmented phased array elements (already cited)
- [ ] `Ellgardt2006_Broadband_WideScan.pdf` — Wide-scan fragmented array, manufacturing issues
- [ ] `Zang2019_Fragmented_Aperture_Array.pdf` — 3-10 GHz fragmented array (already cited)
- [ ] `Landgren2017_mmWave_Unbalanced.pdf` — mmWave fragmented element 18-40 GHz
- [ ] `Landgren2017_Unbalanced_Feed_ITC.pdf` — Balun-free fragmented array
- [ ] `Maloney2011_WideScan_PCB_FragArray.pdf` — 33:1 BW validation, PCB fabrication

### Ch 9 (Recent Innovations)
- [ ] `Dou2024_Surrogate_Parallel_AGA_Antenna.pdf` — Surrogate + adaptive GA pixelated optimization
- [ ] `Wang2024_Bandwidth_RL_Pixelated.pdf` — Reinforcement learning for pixel antenna (already cited in Ch 3)
- [ ] `Zeghdoud2025_GA_Fuzzy_ML_Optimization.pdf` — Fuzzy+ML GA acceleration (already cited in Ch 3)
- [ ] `Kiesel2018_CONEX_CARAMEL.pdf` — VHF fragmented array in Conex container, deployed system
- [ ] `Li2025_Inverse_Design_ResNet.pdf` — ResNet inverse design of pixelated antennas (already cited in Ch 9)

### Ch 10 (Other EM Structures)
- [ ] `Efficient_Pixelated_Rectenna_2024.pdf` — Pixelated rectenna, 37% RF-DC efficiency
- [ ] `Ethier2014_Reflectarray_Fragmented.pdf` — Reflectarray with fragmented elements
- [ ] `ElBadawe2017_Metasurface_DC_Conversion.pdf` — Metasurface energy harvester (see NOTE above re: ElBadawe)
- [ ] `Cheng2021_LowRCS_FSS_MA_Antenna.pdf` — FSS + metamaterial absorber for RCS reduction
- [ ] `Hughes2015_CoDesign_Photodiode_Array.pdf` — Fragmented array + photodiode integration
- [ ] `Hughes2015_XBand_Photodiode_Integration.pdf` — X-band fragmented array + PD

### Author's own papers (Ch 2/3/5/7) — highest priority
- [ ] `Maloney2000_Switched_Fragmented_Aperture.pdf` — Original switched FA paper
- [ ] `Maloney2001_Patent_US6323809_Fragmented_Aperture.pdf` — Original patent
- [ ] `Maloney2013_Genetic_24bit_Evaluation.pdf` — Exhaustive 2^24 design space search

## Execution Order
1. **Phase 1** first (cite-only, fast, ~30 min)
2. **Phase 2A** — Author's own papers (Maloney2000, Maloney2013, MaloneyBaker, Cook2019, Kiesel2018) — these are the most important
3. **Phase 2B** — Ch 9 ML/AI papers (Dou2024, Wang2024, etc.)
4. **Phase 2C** — Ch 10 papers (Efficient_Pixelated_Rectenna, Ethier2014, Cheng2021, Hughes2015×2)
5. **Phase 2D** — Ch 3 papers (Mair2022, Mair2024_IFA, Merulla2008)
6. **Phase 2E** — Ch 6/7 papers (Ellgardt2006, Landgren2017×2, Maloney2011)
7. Rebuild PDF, update memory

## Status Tracking
- [x] Phase 1 complete
- [x] Phase 2A complete
- [x] Phase 2B complete
- [x] Phase 2C complete (ElBadawe2017 + Cheng2021 skipped per author; rectenna PDF truncated, text-only)
- [x] Phase 2D complete (Mar 11 — 13 figs: Mair2022, Mair2024×2, Li2019, Merulla2008)
- [x] Phase 2E complete (Mar 11 — 2 figs: Ellgardt2006; Maloney2011+Landgren already in book)
- [x] PDF rebuilt (322 pages)
- [x] Memory updated
