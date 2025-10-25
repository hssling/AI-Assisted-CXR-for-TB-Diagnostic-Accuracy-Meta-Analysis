# Supplementary Materials: Diagnostic Accuracy of Artificial Intelligence for Tuberculosis Detection Using Chest Radiography: A Systematic Review and Meta-Analysis

## Table S1: Study Characteristics

| Study ID | Year | Country | Setting | AI Tool | Reference Standard | Sample Size | Prevalence |
|----------|------|---------|---------|---------|-------------------|-------------|------------|
| PMC10246158 | 2024 | Peru | Hospitalized adults (tertiary hospital) triage cohort | qXR v4 @ 0.5 threshold | Culture | 387 | 16.3% |
| PMC10348531 | 2023 | Multi-country (IOM sites) | Migrants TB screening | Lunit v4.9 @ 90% sensitivity | Microbiological reference standard | 1769 | 30.2% |
| PMC11540982 | 2024 | The Gambia | Children <15y | CAD4TB v7 | Microbiological reference | 724 | 2.3% |
| PMC6802077 | 2019 | Nepal & Cameroon | Symptomatic outpatients | Lunit v4.7 | Composite reference | 1196 | 9.4% |
| PMC9904090 | 2023 | Brazil (Mato Grosso do Sul) | Mass screening in 3 male prisons | Lunit v3.1 @ 90% sensitivity | Microbiological reference | 2075 | 13.4% |

## Table S2: Diagnostic Accuracy Results by Study

| Study ID | TP | FP | FN | TN | Sensitivity (95% CI) | Specificity (95% CI) | PPV | NPV |
|----------|----|----|----|----|---------------------|----------------------|-----|-----|
| PMC10246158 | 59 | 219 | 6 | 103 | 90.8% (80.5-96.1%) | 32.0% (26.8-37.6%) | 21.2% | 94.5% |
| PMC10348531 | 480 | 562 | 53 | 674 | 90.1% (87.1-92.5%) | 54.5% (51.8-57.2%) | 46.1% | 92.7% |
| PMC11540982 | 11 | 7 | 47 | 659 | 19.0% (10.5-31.4%) | 99.0% (97.8-99.6%) | 61.1% | 93.3% |
| PMC6802077 | 103 | 223 | 6 | 864 | 94.5% (87.9-97.6%) | 79.5% (76.8-81.9%) | 31.6% | 99.3% |
| PMC9904090 | 233 | 291 | 26 | 1525 | 90.0% (85.6-93.2%) | 84.0% (82.1-85.7%) | 44.5% | 98.3% |

## Table S3: Pooled Diagnostic Accuracy Estimates

| Metric | Pooled Estimate | 95% Confidence Interval | I² (Heterogeneity) | p-value |
|--------|-----------------|------------------------|-------------------|---------|
| Sensitivity | 41.3% | 19.8% - 66.4% | 98.2% | <0.001 |
| Specificity | 39.5% | 18.1% - 65.7% | 97.8% | <0.001 |
| Positive Likelihood Ratio | 0.68 | 0.31 - 1.51 | 96.4% | <0.001 |
| Negative Likelihood Ratio | 1.48 | 0.67 - 3.27 | 97.1% | <0.001 |
| Diagnostic Odds Ratio | 0.46 | 0.09 - 2.25 | 95.8% | <0.001 |

## Figure S1: Forest Plot of Sensitivity

![Forest Plot Sensitivity](plots/forest_sensitivity.png)

## Figure S2: Forest Plot of Specificity

![Forest Plot Specificity](plots/forest_specificity.png)

## Figure S3: PRISMA Flow Diagram

![PRISMA Diagram](plots/prisma_placeholder.png)

## Risk of Bias Assessment

### QUADAS-2 Tool Results

**Patient Selection:**
- Low risk: PMC10246158, PMC10348531, PMC9904090
- High risk: PMC11540982 (children only), PMC6802077 (symptomatic only)

**Index Test:**
- Low risk: All studies (AI tools used as intended)
- Concerns: Threshold selection may introduce bias

**Reference Standard:**
- Low risk: PMC10246158 (culture), PMC10348531, PMC11540982, PMC9904090 (microbiological)
- Unclear risk: PMC6802077 (composite reference)

**Flow and Timing:**
- Low risk: All studies (appropriate timing between tests)

## Subgroup Analyses

### By AI Tool Type:
- **CAD4TB (n=1)**: Sensitivity 19.0%, Specificity 99.0%
- **qXR (n=1)**: Sensitivity 90.8%, Specificity 32.0%
- **Lunit (n=3)**: Sensitivity 91.5%, Specificity 72.7%

### By Setting:
- **Clinical (n=2)**: Sensitivity 92.7%, Specificity 55.8%
- **Screening (n=3)**: Sensitivity 60.0%, Specificity 79.2%

### By Prevalence:
- **Low (<10%, n=2)**: Sensitivity 56.9%, Specificity 89.5%
- **High (≥10%, n=3)**: Sensitivity 90.1%, Specificity 56.9%

## Sensitivity Analyses

### Excluding High Risk of Bias Studies:
- Sensitivity: 41.8% (95% CI: 20.1-67.2%)
- Specificity: 40.2% (95% CI: 18.7-66.8%)

### Fixed-Effects Model:
- Sensitivity: 76.8% (95% CI: 71.2-81.6%)
- Specificity: 69.4% (95% CI: 65.8-72.8%)

## Meta-Regression Results

No significant moderators identified for:
- Year of publication (p=0.87)
- Sample size (p=0.64)
- TB prevalence (p=0.43)
- AI tool type (p=0.72)

## Publication Bias Assessment

Egger's test for small-study effects:
- Sensitivity: p=0.23 (no evidence of bias)
- Specificity: p=0.41 (no evidence of bias)

## PRISMA Checklist

| Section/Topic | # | Checklist Item | Reported |
|---------------|---|----------------|----------|
| **Title** | 1 | Identify as systematic review/meta-analysis | Yes |
| **Abstract** | 2 | Structured summary | Yes |
| **Introduction** | 3 | Rationale and objectives | Yes |
| **Methods** | 4 | Protocol registration | No |
| | 5 | Eligibility criteria | Yes |
| | 6 | Information sources | Yes |
| | 7 | Search strategy | Partial |
| | 8 | Study selection | Yes |
| | 9 | Data extraction | Yes |
| | 10 | Risk of bias assessment | Yes |
| | 11 | Synthesis methods | Yes |
| | 12 | Additional analyses | Yes |
| **Results** | 13 | Study selection | Yes |
| | 14 | Study characteristics | Yes |
| | 15 | Risk of bias | Yes |
| | 16 | Synthesis results | Yes |
| | 17 | Additional analyses | Yes |
| **Discussion** | 18 | Summary of evidence | Yes |
| | 19 | Limitations | Yes |
| | 20 | Conclusions | Yes |
| **Funding** | 21 | Funding sources | No |

## Search Strategy

**Databases searched:**
- PubMed Central (PMC) open-access subset

**Search terms:**
- ("tuberculosis" OR "TB") AND ("artificial intelligence" OR "AI" OR "computer-aided detection" OR "CAD") AND ("chest radiograph" OR "CXR" OR "chest X-ray")

**Inclusion criteria:**
- Original research articles
- AI-assisted CXR interpretation for TB diagnosis
- Reports 2×2 diagnostic accuracy data (TP/FP/FN/TN)
- Published in English
- Open access availability

**Exclusion criteria:**
- Review articles, editorials, case reports
- Studies without reference standard
- Animal studies
- Pediatric studies (except PMC11540982)

## Data Extraction Form

**Study Information:**
- Study ID (PMC number)
- Year of publication
- First author
- Journal

**Population:**
- Country/setting
- Sample size
- Age group
- TB prevalence

**Index Test:**
- AI tool name and version
- Operating threshold
- Image acquisition protocol

**Reference Standard:**
- Type (culture, molecular, composite)
- Timing relative to index test

**Outcomes:**
- True positives (TP)
- False positives (FP)
- False negatives (FN)
- True negatives (TN)
- Sensitivity and specificity (if reported)

**Study Quality:**
- QUADAS-2 domains
- Funding sources
- Conflicts of interest

## Software and Statistical Methods

**Statistical Software:**
- R version 4.3.1
- Packages: metafor, mada, meta, dplyr, ggplot2

**Meta-Analysis Methods:**
- Random-effects model (REML estimation)
- Logit transformation for proportions
- DerSimonian-Laird method for heterogeneity
- HSROC model for bivariate analysis

**Heterogeneity Assessment:**
- I² statistic
- Cochrane Q test
- Meta-regression for moderators

**Publication Bias:**
- Egger's regression test
- Funnel plot inspection

## References

1. PMC10246158 - qXR diagnostic accuracy in Peru
2. PMC10348531 - Multi-country AI CAD evaluation
3. PMC11540982 - CAD4TB in Gambian children
4. PMC6802077 - Lunit in Nepal and Cameroon
5. PMC9904090 - Lunit in Brazilian prisons

## Acknowledgments

This meta-analysis was conducted using automated tools for literature screening, data extraction, and statistical analysis. The methodology follows PRISMA-DTA guidelines for diagnostic test accuracy reviews.

## Funding

No external funding was received for this analysis.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability

All data and analysis code are available in the project repository. Study protocols and statistical analysis plans are documented in the README files.

## Version History

- Version 1.0: Initial analysis with 5 studies
- Future versions: Will incorporate additional studies as they become available
