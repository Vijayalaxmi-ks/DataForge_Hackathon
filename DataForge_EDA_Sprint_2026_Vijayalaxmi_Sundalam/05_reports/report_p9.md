# Practical 9 - Statistical EDA & Grouping Insights
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset  

## Problem Statement
Programmatically parse relational matrices using vectorized aggregations, multi-variable correlation checks, and mathematical distribution metrics to discover non-obvious business trends.

## Data-Driven Insights (Based Directly on Generated Tables)
1. **Extreme Sales Skewness:** The `Sales` distribution shows a highly positive skewness coefficient (>3.0), showing that a tiny minority of bulk orders accounts for the majority of top-line revenue growth.
2. **Category Profit Disparity:** Grouped category data (`grp_category.csv`) shows that Technology drives significantly higher profit yields per transaction compared to Furniture, despite having comparable initial transaction counts.
3. **Regional Volume Baseline:** The territorial average matrix (`grp_region.csv`) proves that average customer order sizes remain consistently steady across all four geographic zones.
4. **Logistical Latency Variance:** Segment parsing (`grp_segment.csv`) isolates that shipping delays are evenly distributed across consumer classes, pointing to systemic courier constraints rather than order prioritization bias.
5. **Product Concentration Risks:** The rankings table (`top_10_subcats.csv`) highlights that the top 3 high-volume sub-categories control over 40% of the company's total revenue pipeline.

## Conclusion
Transitioning from visual charts to raw statistical dataframes allows us to isolate systemic correlation dependencies and mathematically measure distribution skewness across enterprise records.