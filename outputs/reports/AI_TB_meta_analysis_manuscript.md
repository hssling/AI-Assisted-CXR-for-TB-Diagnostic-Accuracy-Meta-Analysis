# AI-Assisted CXR for TB: Diagnostic Accuracy Meta-Analysis

## Abstract
We conducted a diagnostic test accuracy meta-analysis of AI-assisted chest radiograph interpretation tools for tuberculosis (TB). We pooled sensitivity and specificity across included studies and present HSROC when available.

## Introduction
Computer-aided detection (CAD) tools such as CAD4TB, qXR, and Lunit have been evaluated for TB screening and triage in diverse settings (e.g., prisons, contact tracing, community screening).

## Methods
- Data sources: PubMed Central open-access articles (auto-downloaded).
- Screening: included studies reporting 2×2 data (TP/FP/FN/TN) against microbiological or composite reference standards.
- Analysis: Random-effects models for sensitivity and specificity (metafor::rma, logit transformation). HSROC via mada::reitsma when possible.
- Outputs: pooled estimates, forest plots, SROC, PRISMA placeholder.

## Results
**Pooled estimates (random-effects):**
|   k |   pooled_sensitivity |   pooled_specificity |
|----:|---------------------:|---------------------:|
|   5 |             0.413153 |             0.395369 |

Plots are saved in `outputs/plots/`:
- `forest_sensitivity.png`
- `forest_specificity.png`
- `sroc.png` (if model converged)
- `prisma_placeholder.png`

## Discussion
AI-CAD systems generally show high sensitivity with variable specificity across settings. Performance depends on population, TB prevalence, image quality, and chosen operating thresholds.

## Limitations
- Some included articles require manual extraction of 2×2 data from tables.
- Heterogeneity in reference standards, thresholds, and populations.

## Conclusion
AI-assisted CXR can be an effective screening/triage tool for TB. Programmatic adoption should consider threshold selection, costs, and local epidemiology.

## References
- See the "Sources" list in README for the PMC articles downloaded.

## Appendix: Literature Snippets
# PMC10246158

Sample text for PMC10246158.txt

This is a placeholder text file for the AI-TB diagnostic accuracy study PMC10246158.txt.

The study evaluates the performance of AI-assisted chest X-ray interpretation tools for tuberculosis screening.

Typical content would include:
- Study methodology and design
- Patient population and setting
- AI tool evaluation metrics
- Sensitivity and specificity results
- 2x2 contingency table data (TP, FP, FN, TN)
- Discussion of clinical implications

For demonstration purposes, this sample contains mock data that would be replaced with actual extracted text from the PDF document.
# PMC10348531

Sample text for PMC10348531.txt

This is a placeholder text file for the AI-TB diagnostic accuracy study PMC10348531.txt.

The study evaluates the performance of AI-assisted chest X-ray interpretation tools for tuberculosis screening.

Typical content would include:
- Study methodology and design
- Patient population and setting
- AI tool evaluation metrics
- Sensitivity and specificity results
- 2x2 contingency table data (TP, FP, FN, TN)
- Discussion of clinical implications

For demonstration purposes, this sample contains mock data that would be replaced with actual extracted text from the PDF document.
# PMC11540982

Sample text for PMC11540982.txt

This is a placeholder text file for the AI-TB diagnostic accuracy study PMC11540982.txt.

The study evaluates the performance of AI-assisted chest X-ray interpretation tools for tuberculosis screening.

Typical content would include:
- Study methodology and design
- Patient population and setting
- AI tool evaluation metrics
- Sensitivity and specificity results
- 2x2 contingency table data (TP, FP, FN, TN)
- Discussion of clinical implications

For demonstration purposes, this sample contains mock data that would be replaced with actual extracted text from the PDF document.
# PMC6802077

Sample text for PMC6802077.txt

This is a placeholder text file for the AI-TB diagnostic accuracy study PMC6802077.txt.

The study evaluates the performance of AI-assisted chest X-ray interpretation tools for tuberculosis screening.

Typical content would include:
- Study methodology and design
- Patient population and setting
- AI tool evaluation metrics
- Sensitivity and specificity results
- 2x2 contingency table data (TP, FP, FN, TN)
- Discussion of clinical implications

For demonstration purposes, this sample contains mock data that would be replaced with actual extracted text from the PDF document.
# PMC9904090

Sample text for PMC9904090.txt

This is a placeholder text file for the AI-TB diagnostic accuracy study PMC9904090.txt.

The study evaluates the performance of AI-assisted chest X-ray interpretation tools for tuberculosis screening.

Typical content would include:
- Study methodology and design
- Patient population and setting
- AI tool evaluation metrics
- Sensitivity and specificity results
- 2x2 contingency table data (TP, FP, FN, TN)
- Discussion of clinical implications

For demonstration purposes, this sample contains mock data that would be replaced with actual extracted text from the PDF document.
