# Practical 2 - Data Quality Auditing and Descriptive Statistics
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset

## Problem Statement
The task was to audit a transactional dataset for structural anomalies, handle missing values, and calculate baseline descriptive statistics. This process ensures downstream predictive models and business forecasts are built on reliable, uncorrupted data lineages.

## Procedure
1. Imported the raw dataset into Google Sheets and loaded the active workspace.
2. Executed the *Remove Duplicates* tool on the entire sheet, verifying that 0 duplicate rows were found and 9,801 unique records remain.
3. Created a dedicated `Quality_Audit` tab tracking dataset dimensions, row counts, and structural blanks.
4. Identified 19,602 total blank cells localized entirely within Columns S and T.
5. Added a new sheet tab titled `Stats Summary` to compute core central tendency values.
6. Applied native formulas `=AVERAGE()`, `=MEDIAN()`, `=STDEV.P()`, and `=QUARTILE()` targeting the Sales data in Column R.
7. Applied a conditional formatting color scale gradient to Column R to visually map high-revenue outliers.
8. Exported the assets as Excel workbooks and a clean interim CSV to their designated workspace folders.

## Outputs Created
* **Spreadsheets:** `p2_excel_cleaning.xlsx` and `stats_summary.xlsx` saved in `02_excel/`.
* **Data File:** `excel_cleaned.csv` saved in `01_data/interim/`.
* **Audit Dashboard:** `Quality_Audit` and `Stats Summary` tabs built directly into the active workbooks.

## Observations | Analytical Evaluation Questions
* **Q1. Which column had the highest data quality risk?** Columns S and T represented the highest risk due to complete data voids (19,602 empty cells) across all active records.
* **Q2. What cleaning decision did you take and why?** Redundant rows were checked to ensure unique baselines. Columns S and T were preserved with placeholder data to safeguard grid structures, while Column R was forced to strict currency formatting to protect analytical math.
* **Q3. Why should raw data and cleaned data be kept separately?** Separating files ensures data lineage preservation. If a formula error corrupts the active clean layout, the immutable raw source remains safe for full pipeline re-runs.

## Conclusion
Comparing the transactional mean (~230.77) directly against the median reveals structural right-skewness, proving that high-value outlier orders heavily influence total revenue metrics.