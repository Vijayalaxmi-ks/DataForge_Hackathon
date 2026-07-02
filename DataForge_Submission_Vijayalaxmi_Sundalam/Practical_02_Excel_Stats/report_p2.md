# Practical 2 Report
**Author:** Vijayalaxmi_Sundalam
**Date:** 2026-06-30

## 1. Problem Statement
Raw corporate transaction matrices hide structural flaws, variable column voids, and extreme mathematical outliers that distort business metrics. This practical executes structural quality audits and computes central tendency spreads to validate the statistical distribution of the dataset.

## 2. Concept Elaborated
* **Dispersion Metrics:** Tracking mean, median, and standard deviation establishes baseline variance boundaries, flagging systemic statistical skewness caused by extreme commercial activity.
* **Anomalous Boundary Mapping:** Utilizing color scales and conditional rule parameters maps high-revenue outlier metrics visually, separating run-rate transactions from extreme data points.

## 3. Execution Steps
1. **Deduplication Validation:** Processed the workspace via the *Remove Duplicates* module, confirming a baseline of 0 redundant entries and 9,801 unique transactional rows.
2. **Structural Auditing Dashboard:** Constructed a dedicated `Quality_Audit` tab layout documenting row/column indices, null structural bounds, and file integrity notes.
3. **Statistical Ingestion:** Formed a standalone `Stats Summary` module executing native `=AVERAGE()`, `=MEDIAN()`, and `=STDEV.P()` matrices targeting the primary Sales vector (Column R).
4. **Pipeline Storage:** Applied structural Date and Currency overhauls, saving the workbook outputs to `02_excel/p2_excel_cleaning.xlsx` and the clean split to `01_data/interim/excel_cleaned.csv`.

## 4. Key Insights
- **Highest Data Risk:** Columns S and T represented the primary structural threat due to containing unmapped data blanks across all active data matrices.
- **Cleaning Decision:** Preserved all 9,801 valid unique rows while forcing strict Date formatting on Columns C and D, and Currency formatting on Column R to protect downstream calculations.
- **Data Lineage Separation:** Keeping original raw records independent from working clean assets safeguards structural data lineages against transformation corruption, allowing for fully reproducible pipelines.