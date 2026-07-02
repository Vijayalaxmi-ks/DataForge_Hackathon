# Practical 5 - Data Modeling & DAX Formulation
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset 

## Problem Statement
Standard flat data columns are insufficient for granular analytical insight. We must develop optimized, dynamic DAX measures and target calculated metrics to expose core underlying performance trends.

## KPI Definition & Strategic Interpretation
* **What is a KPI?** A Key Performance Indicator (KPI) is a quantifiable metric used to evaluate the operational success of an enterprise against strategic targets. In data architectures, it turns raw transaction logs into high-level status signals for stakeholders.
* **Our Core KPI Context:** Based on building custom logic models and analyzing software system flows, KPIs act as structural evaluation criteria. Much like analyzing a script's runtime efficiency, our calculated KPIs (like Profit Margin) measure systemic data performance, helping prioritize resource allocation and isolate processing bottlenecks instantly.

## Procedure & Model Architecture
1. Saved the active project space into the dedicated tracking asset `p5_powerbi_model_dax.pbix`.
2. Opened the **Model View** pane to verify structural field availability and check native temporal date hierarchies.
3. Formulated and validated high-performance scalar aggregates including `Total Sales`, `Total Profit`, `Order Count`, and `Average Discount`.
4. Engineered a robust multi-measure `Profit Margin` utilizing safe division blocks (`DIVIDE`) to protect dashboard visuals from mathematical zero-denominator error exceptions.
5. Injected a specialized row-by-row calculated column named `Shipping Delay` tracking supply chain fulfillment speed across operational entities.
6. Captured a visual trace of the underlying architecture schema as `model_schema.png`.

## Report Questions
* **Q1. What is the difference between a column and a measure?** A calculated column is computed row-by-row during data refresh and permanently consumes storage RAM inside the database model. A DAX measure is calculated entirely on-the-fly at runtime, reacting dynamically based on whatever filters, slicers, or visual boundaries the user interacts with on the dashboard canvas without increasing file sizes.
* **Q2. Which KPI would you put on top of the dashboard and why?** **Profit Margin** belongs at the absolute apex of the dashboard. While tracking volume metrics like Total Sales or Order Count is valuable, Net Revenue velocity can mislead stakeholders if operations are running at a structural deficit. Profit Margin immediately signals real enterprise health and operational scaling efficiency in a single, glanceable metric.

## Conclusion
Implementing explicit DAX dimensions unlocks the true depth of transactional layers, moving the dataset from a static historical grid to a highly interactive, responsive business intelligence engine.