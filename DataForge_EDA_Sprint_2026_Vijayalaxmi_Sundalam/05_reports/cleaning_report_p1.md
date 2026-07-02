# Practical 1 Report: Data Acquisition & Structural Cleaning
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset

## 1. Problem Statement
Raw, uncurated business datasets contain structural inconsistencies, duplicate line-items, unmapped missing values, and corrupted data types that derail automated analysis tools. This practical implements structural cleaning to standardize the Superstore Sales dataset.

## 2. Core Concepts
* **Data Typing:** Forcing text entries into strict *Date* formats or numeric values into *Currency* layouts prevents calculation breakdowns during metric aggregation and charting.
* **Imputation Logic:** Leaving cells completely blank breaks visualization pipelines. Missing text strings are assigned a generic token (`"Unknown"`) to preserve transactional data lines without fabricating information.

## 3. Execution Steps
1. **Deduplication:** Selected the worksheet in Google Sheets and executed *Data > Data cleanup > Remove duplicates* to purge redundant records.
* **Targeted Imputation:** Boundary-selected the active data space via `Ctrl + Shift + End`. Triggered `Ctrl + H`, using the regular expression `^$` to search exclusively for blank cells within the data grid boundaries, globally replacing them with `"Unknown"`.
3. **Type Overrides:** Converted the text entries in Columns C (`Order Date`) and D (`Ship Date`) into true *Date* types. Applied the *Currency* format to Column R (`Sales`).
4. **Workspace Export:** Downloaded the file as an Excel Workbook, saving it to `02_excel/dataset_cleaned.xlsx`.

## 4. Analytical Evaluation Questions

### Q1. What does one row in this dataset represent?
A single row represents a distinct, individual line-item transaction within a customer order, specifying the product type, quantity, financial performance, and shipping metadata for that item.

### Q2. Which columns look numerical, categorical, and date/time?
* **Numerical:** `Sales` (Column R), `Quantity`, `Discount`, `Profit`, `Row ID`.
* **Categorical:** `Order ID`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`.
* **Date/Time:** `Order Date` (Column C), `Ship Date` (Column D).

### Q3. What can go wrong if a team starts analysis without a data dictionary?
* **Metric Misinterpretation:** Analysts may conflate distinct definitions like revenue versus profit, corrupting critical KPIs.
* **Schema Breakdown:** Inconsistent parsing of text, numbers, or dates across different users will crash automated code execution scripts.
* **Operational Inefficiency:** Engineering velocity drops as team members waste hours manually verifying column definitions instead of delivering analytics.