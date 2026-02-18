# Fair Use Statement for Fragmented Aperture Antennas Book

**Location:** Place after title page, before Table of Contents
**Format:** Full page, prominent placement
**Updated:** February 18, 2026

---

# **Copyright Notice and Fair Use Statement**

## **Copyright and Permissions**

This book, *Fragmented Aperture Antennas*, is provided freely for educational and research purposes. It is not sold commercially and is distributed as an open educational resource to advance knowledge in the field of computational antenna design.

## **Use of Published Figures and Data**

This work includes figures, data, and results from previously published scientific papers to provide comprehensive documentation of the historical development and current state of fragmented aperture antenna technology. All such materials are used in accordance with established principles of fair use under U.S. Copyright Law (17 U.S.C. § 107) and international copyright conventions.

### **Fair Use Rationale**

The use of published materials in this work satisfies the four-factor test for fair use:

1. **Purpose and Character:** This book is a non-commercial, educational work that provides scholarly analysis and historical documentation of fragmented aperture antenna technology. Materials are used to illustrate technical concepts and validate scientific claims within a transformative educational context.

2. **Nature of the Work:** Materials used are factual, scientific, and technical in nature, consisting primarily of measurement data, simulation results, and engineering diagrams from published research papers.

3. **Amount and Substantiality:** Only a small number of figures (typically 2-4) are reproduced from any single publication, representing a minor portion of the original works and only what is necessary for educational purposes.

4. **Market Effect:** This non-commercial educational work does not compete with or substitute for the original publications. Indeed, proper citation and discussion are intended to increase awareness of and citations to the original research.

### **Good Faith Permission Efforts**

The author has made good faith efforts to contact authors and publishers of all referenced works to request permission for figure reproduction. Where permission has been explicitly granted, this is noted in the figure caption. Where permission could not be obtained after reasonable attempts, materials are included under fair use provisions as described above.

### **Attributions and Citations**

All reproduced figures, data, and materials are accompanied by:
- Complete bibliographic citations
- Explicit attribution to all original authors
- Copyright notices as specified by publishers
- DOI or other persistent identifiers where available

These attributions serve both to comply with academic standards and to direct readers to the original sources for complete context.

### **Compliance and Removal Requests**

The author respects the intellectual property rights of all researchers and publishers. If any copyright holder believes that material has been used inappropriately or wishes to request removal:

**Contact:** Dr. James G. Maloney
**Email:** [YOUR EMAIL ADDRESS]

Upon receiving a substantiated request, the author will promptly:
1. Review the concern in good faith
2. Remove or replace the material if appropriate
3. Provide revised versions of the book as necessary

This book is hosted on GitHub and other platforms to facilitate rapid updates in response to any concerns.

### **Author's Original Work**

Portions of this book reproduce figures and data from the author's own previously published papers. As the original creator of this content, the author retains rights to reuse this material regardless of publication agreements. These works include:

- Maloney, J. G., et al., "Switched fragmented aperture antennas," *IEEE Antennas and Propagation Society International Symposium*, 2000.
- Maloney, J. G., et al., "A Fragmented Aperture GPS Antenna," *IEEE International Symposium on Antennas and Propagation*, 2007.
- Maloney, J. G., et al., "Wide-scan phased arrays of fragmented aperture antennas," *Proc. AMTA*, 2011.
- Maloney, J. G., et al., "Genetic algorithm analysis of a 24-bit fragmented aperture phased array," *Proc. AMTA*, 2013.

### **Open Educational Resource**

This book is provided as an open educational resource to:
- Document the historical development of fragmented aperture technology
- Provide educational materials for students and researchers
- Advance scientific knowledge in computational antenna design
- Preserve technical knowledge for future generations

The work is distributed freely without charge and without commercial intent.

### **No Warranty**

This educational material is provided "as is" without warranty of any kind, either expressed or implied. The author has made reasonable efforts to ensure accuracy but makes no guarantees regarding the completeness or correctness of any information.

---

## **Acknowledgment of Copyright Holders**

The author gratefully acknowledges the following publishers and their contributions to scientific knowledge:

- **IEEE** (Institute of Electrical and Electronics Engineers)
- **IET** (Institution of Engineering and Technology)
- **Electromagnetics Academy**
- **AMTA** (Antenna Measurement Techniques Association)

And the many researchers whose work is cited throughout this book. Their contributions to the field of antenna engineering have made this comprehensive reference possible.

---

**Published:** [DATE]
**Version:** 1.0
**Last Updated:** [DATE]

This document will be updated to reflect any permission grants received after publication.

---

# **SEPARATE ACKNOWLEDGMENTS PAGE (to be updated as permissions arrive)**

## **Permissions Granted**

The author gratefully acknowledges the following researchers and institutions who graciously granted permission to reproduce figures from their published work:

### **Permissions Received:**

[TO BE UPDATED AS PERMISSIONS ARE RECEIVED - Leave blank initially]

*Example format:*
- **Professor Kamal Sarabandi** (University of Michigan) - Permission granted [DATE] for Figures 1, 2, 7 from Barani et al., "Fragmented Antenna Realization Using Coupled Small Radiating Elements," *IEEE Trans. Antennas Propag.*, vol. 66, no. 4, pp. 1725-1735, 2018.

### **Materials Used Under Fair Use:**

The following materials are used under fair use provisions (17 U.S.C. § 107) where permission could not be obtained after good faith attempts to contact authors:

[TO BE UPDATED - List specific figures and papers]

*Note: If any copyright holder listed above wishes to grant explicit permission retroactively, please contact the author.*

---

## **How to Update This Document**

As permissions are received:
1. Move the paper from "Fair Use" section to "Permissions Granted" section
2. Include date permission was granted
3. Note the contact who granted permission
4. Update the version number and "Last Updated" date
5. Commit changes to GitHub

---

## **Figure Caption Format**

### **For figures WITH permission:**
```
Figure X.Y: [Description]. Reproduced with permission from [Author(s)],
[Paper Title], [Journal/Conference], [Year]. ©[Year] IEEE/[Publisher].
```

### **For figures UNDER fair use:**
```
Figure X.Y: [Description]. From [Author(s)], [Paper Title],
[Journal/Conference], [Year]. Used under fair use (17 U.S.C. § 107)
for educational purposes. ©[Year] IEEE/[Publisher].
```

### **For YOUR OWN papers:**
```
Figure X.Y: [Description]. From Maloney et al., [Paper Title],
[Journal/Conference], [Year]. Author's original work.
```

---

## **LaTeX Implementation Notes**

Place this in your topLevel.tex file:

```latex
% After title page, before table of contents
\include{Chapters/copyrightNotice}  % Fair use statement
\include{Chapters/acknowledgments}  % Permissions acknowledgments
\tableofcontents
```

Create two new files:
- `Chapters/copyrightNotice.tex` - Fair use statement (static except for updates)
- `Chapters/acknowledgments.tex` - Permissions list (updated as received)

---

**END OF FAIR USE STATEMENT DOCUMENT**
