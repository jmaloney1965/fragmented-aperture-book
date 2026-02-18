# Fair Use Implementation Guide
**Created:** February 18, 2026

---

## 📋 What Was Created

**Three new files:**

1. **`Literature/FAIR_USE_STATEMENT.md`**
   - Reference document with full text
   - Planning and tracking resource
   - Not compiled into book directly

2. **`Chapters/copyrightNotice.tex`**
   - LaTeX version ready to compile
   - Place early in book (after title, before TOC)
   - Static content (rarely changes)

3. **`Chapters/permissionsAcknowledgments.tex`**
   - Dynamic content (updates as permissions arrive)
   - Template with instructions included
   - Place after copyright notice

---

## 🔧 How to Integrate Into Your Book

### **Step 1: Add to topLevel.tex**

Open `/Users/jim.maloney/Book/Chapters/topLevel.tex` and add these lines after the title page but before `\tableofcontents`:

```latex
% Title page, dedication, etc. (existing content)

% ADD THESE TWO LINES:
\include{Chapters/copyrightNotice}
\include{Chapters/permissionsAcknowledgments}

% Then your existing table of contents
\tableofcontents
\listoffigures
\listoftables
```

### **Step 2: Add Your Email**

Edit `Chapters/copyrightNotice.tex` and replace:
```latex
\textbf{Email:} [YOUR EMAIL ADDRESS]
```

With your actual email:
```latex
\textbf{Email:} your.email@example.com
```

### **Step 3: Compile and Verify**

```bash
cd /Users/jim.maloney/Book/Chapters
pdflatex topLevel.tex
```

Verify the copyright notice appears early in the PDF.

---

## 📝 How to Update When Permissions Arrive

### **When Someone Grants Permission:**

**1. Edit `Chapters/permissionsAcknowledgments.tex`**

Find the section that says:
```latex
\textit{[This section will be updated as permissions are received...]}
```

Replace with:
```latex
\noindent\textbf{Professor Kamal Sarabandi} (University of Michigan)\\
Permission granted February 22, 2026 for Figures 1, 2, 7 from Barani et al.,
``Fragmented Antenna Realization Using Coupled Small Radiating Elements,''
\textit{IEEE Trans. Antennas Propag.}, vol. 66, no. 4, pp. 1725--1735, 2018.

\vspace{0.5em}
```

**2. Update the date at top of file:**
```latex
% Last updated: February 22, 2026
```

**3. Recompile the book:**
```bash
cd /Users/jim.maloney/Book/Chapters
pdflatex topLevel.tex
```

**4. Commit to git:**
```bash
git add Chapters/permissionsAcknowledgments.tex
git commit -m "Add permission acknowledgment: Sarabandi (UMich) - Barani2018"
git push
```

**5. Update tracking log:**

Also update `Literature/PERMISSION_TRACKING_LOG.md`:
- Change status from "AWAITING RESPONSE" to "GRANTED"
- Add grant date
- Update success metrics

---

## 📊 Figure Caption Formats

### **For Figures WITH Permission:**

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{images/barani2018_fig1.pdf}
\caption{Proposed fragmented antenna concept showing coupled elements on robotic flyers.
Reproduced with permission from N. Barani, J. F. Harvey, and K. Sarabandi,
``Fragmented Antenna Realization Using Coupled Small Radiating Elements,''
\textit{IEEE Trans. Antennas Propag.}, vol. 66, no. 4, pp. 1725--1735, 2018.
\copyright~2018 IEEE.}
\label{fig:barani_concept}
\end{figure}
```

### **For Figures UNDER Fair Use:**

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{images/thors2005_fig9.pdf}
\caption{Final optimized design showing reflection coefficients and unit cell geometry.
From B. Thors, H. Steyskal, and H. Holter, ``Broad-Band Fragmented Aperture Phased
Array Element Design Using Genetic Algorithms,'' \textit{IEEE Trans. Antennas Propag.},
vol. 53, no. 10, pp. 3280--3287, 2005. Used under fair use (17 U.S.C. \S~107) for
educational purposes. \copyright~2005 IEEE.}
\label{fig:thors_final}
\end{figure}
```

### **For YOUR OWN Figures:**

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{images/maloney2011_fig3.pdf}
\caption{Wide-scan performance of fragmented aperture array showing VSWR across scan angles.
From J. G. Maloney et al., ``Wide-scan phased arrays of fragmented aperture antennas,''
\textit{Proc. AMTA}, 2011. Author's original work.}
\label{fig:maloney_widescan}
\end{figure}
```

---

## ✅ Checklist for Each Permission Received

- [ ] Update `Chapters/permissionsAcknowledgments.tex`
- [ ] Update date at top of file
- [ ] Update figure captions (from "fair use" to "reproduced with permission")
- [ ] Recompile book
- [ ] Update `Literature/PERMISSION_TRACKING_LOG.md`
- [ ] Commit changes to git
- [ ] Push to GitHub
- [ ] Send thank-you email to researcher

---

## 📅 Workflow Summary

### **Initial Setup (Do Once):**
1. ✅ Add your email to `copyrightNotice.tex`
2. ✅ Add includes to `topLevel.tex`
3. ✅ Compile and verify
4. ✅ Commit to git

### **As Permissions Arrive (Repeat):**
1. Update `permissionsAcknowledgments.tex`
2. Update figure captions throughout book
3. Recompile
4. Update tracking documents
5. Commit and push
6. Thank the researcher

### **Final Publication:**
1. Review all permissions granted vs. fair use
2. Verify all figure captions are correct
3. Ensure all attributions are complete
4. Final compile and PDF check
5. Tag release in git

---

## 🎯 Quick Commands

### **Compile the book:**
```bash
cd /Users/jim.maloney/Book/Chapters
pdflatex topLevel.tex
bibtex topLevel
pdflatex topLevel.tex
pdflatex topLevel.tex
```

### **Check what needs permissions:**
```bash
cd /Users/jim.maloney/Book/Literature
grep "AWAITING" PERMISSION_TRACKING_LOG.md
```

### **Commit a permission update:**
```bash
git add Chapters/permissionsAcknowledgments.tex
git add Literature/PERMISSION_TRACKING_LOG.md
git commit -m "Add permission: [Author] - [Paper]"
git push
```

---

## 📧 Email Response Templates

### **When Permission is Granted:**

```
Dear [Researcher],

Thank you so much for granting permission to use Figures [X, Y, Z]
from your [YEAR] paper in my book on Fragmented Aperture Antennas.

I will provide full attribution in both the figure captions and the
acknowledgments section, and your work will be properly cited
throughout the relevant chapters.

Your contribution to the field and your willingness to support this
educational effort are deeply appreciated.

Best regards,
Jim Maloney
```

### **When Permission is Denied (ask for alternative):**

```
Dear [Researcher],

Thank you for your response. I understand your position regarding
figure permissions.

Would you be comfortable with me:
1. Recreating similar figures using my own simulation data?
2. Citing your work without reproducing figures?
3. Using a reduced number of figures?

I want to respect your wishes while still acknowledging your important
contributions to the field.

Best regards,
Jim Maloney
```

---

## 🔍 Fair Use Decision Tree

```
START: Need to use a figure from external paper

├─ Did you get explicit permission?
│  ├─ YES → Use it! Mark as "Reproduced with permission"
│  └─ NO → Continue below
│
├─ Did you make good faith attempts to contact authors?
│  ├─ NO → Try to contact them first
│  └─ YES → Continue below
│
├─ Is it critical to your educational argument?
│  ├─ NO → Consider omitting or recreating
│  └─ YES → Continue below
│
├─ Is it a small portion of the original work (2-4 figures)?
│  ├─ NO → Reduce number of figures
│  └─ YES → Continue below
│
├─ Are you using it for non-commercial education?
│  ├─ NO → Reconsider using it
│  └─ YES → Fair use likely defensible
│
└─ PROCEED with fair use
   - Mark as "Used under fair use (17 U.S.C. § 107)"
   - Document permission attempt
   - Be prepared to remove if challenged
```

---

## 📚 Resources

**U.S. Copyright Law:**
- 17 U.S.C. § 107: https://www.copyright.gov/title17/92chap1.html#107

**IEEE Author Rights:**
- https://www.ieee.org/publications/rights/author-rights-responsibilities.html

**Fair Use Analysis:**
- Stanford Libraries Fair Use Guide
- Columbia University Fair Use Checklist

---

**Last Updated:** February 18, 2026
**Status:** Fair use framework complete, ready for integration
