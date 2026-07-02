# Practical 3 - Interactive Pivot Dashboards
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset

## Problem Statement
Stakeholders need dynamic summaries of performance metrics without parsing raw rows. This dashboard aggregates multi-dimensional data to streamline strategic decisions.

## Procedure
1. Duplicated the clean dataset into a new tab named `dataset_cleaned`.
2. Created a `KPI_Summary` tab calculating global count, sum, average, min, max, median, and stdev.
3. Created a `Pivot_Analysis` tab using data range `dataset_cleaned!1:9803`.
4. Generated Table 1 tracking Sales by Region.
5. Generated Table 2 tracking Sales by Category.
6. Generated Table 3 tracking Sales by Order Date grouped by Month.
7. Inserted 3 linked charts (Column, Pie, Line) positioned cleanly below the tables.
8. Added 2 dynamic slicers (Region and Order Date) at the top with "Apply to pivot tables" checked.

## Outputs Created
* **Interactive Workbook:** `p3_excel_eda_dashboard.xlsx`
* **Dashboard Screenshot:** `dashboard_preview.png`

## Observations
* **Which pivot table gave the most useful insight?** The Order Date monthly trend table, as it instantly highlights cyclical sales volume changes over time.
* **What changed when you used slicers?** Filtering a slicer automatically recalculated all three pivot tables and re-rendered their charts simultaneously.
* **What is one limitation of doing this only in Excel?** Performance drops and calculations experience lag when data scales past a few hundred thousand rows.

## Conclusion
Linking interactive control slicers to multi-dimensional pivot tables converts flat data tables into real-time business intelligence tools.