# Practical 1 Report
**Author:** Vijayalaxmi_Sundalam
**Date:** 2026-06-30

## 1. Problem Statement
Raw business data contains duplicates, missing fields, and broken data types that distort metrics. This practical establishes a structured, local repository environment and implements structural cleaning to standardize the Superstore Sales dataset for downstream analytics.

## 2. Concept Elaborated
* **Data Typing:** Forcing text fields into explicit formats (e.g., converting strings to true *Dates* or values to *Currency*) ensures calculations and plotting tools function without structural errors.
* **Missing Value Imputation:** Empty grid cells disrupt automation scripts. Globally substituting missing data boundaries with a placeholder (`"Unknown"`) preserves the integrity of transaction rows without fabricating arbitrary variables.

## 3. Execution Steps
1. **Workspace Setup:** Developed a standardized local directory structure (`00_admin`, `01_data`, `02_excel`, `05_reports`) inside the `D:` drive to handle a clean development pipeline.
2. **Deduplication:** Opened Google Sheets and utilized *Data > Data cleanup > Remove duplicates* to scrub redundant line items.
3. **Targeted Imputation:** Boundary-selected active fields via `Ctrl + Shift + End`. Used Find & Replace (`Ctrl + H`) with regular expression `^$` to safely swap empty cells (including columns S and T) for `"Unknown"`.
4. **Data Overrides:** Reconfigured column C (`Order Date`) and column D (`Ship Date`) into strict Date formats, set column R (`Sales`) to Currency, and saved the copy locally as `02_excel/dataset_cleaned.xlsx`.

## 4. Key Insights
- **Data Protection:** Purging duplicate lines eliminates artificially inflated performance indicators and safeguards database reliability.
- **Timeline Optimization:** Standardizing dates prevents data tools from sorting chronological timelines alphabetically during exploration.
- **Engineering Velocity:** Constructing a workspace metadata layout allows analytical sprints to proceed immediately without structural or parsing bottlenecks.