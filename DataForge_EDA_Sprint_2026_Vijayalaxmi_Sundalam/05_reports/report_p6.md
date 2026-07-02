# Practical 6 - Executive Dashboard & Visual Storytelling
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset 

## Problem Statement
Design a single-page interactive report for the CEO that translates raw transaction grids into structured business intelligence, emphasizing core operational health and margins.

## Executive Dashboard Layout & Design
* **KPI Header Strip:** Tracks high-level indicators (`Total Sales`, `Total Profit`, `Profit Margin`, and `Avg Shipping Delay`) at a glance.
* **Slicer Panel:** Offers instantaneous data filtering across chronological, category, and regional dimensions.
* **Analytical Core:** Combines a Line Chart (temporal trend analysis), a Bar Chart (product volume comparison), a Treemap (geographic concentration tracking), and a Scatter Plot (outlier category detection).

## Report Questions
* **Q1. What is the dashboard’s main business message?** The core message is that overall revenue expansion is highly dependent on a few high-volume product categories, while logistical friction points (evidenced by higher delivery latencies in specific regions) are quietly eating away at latent profit margins.
* **Q2. Which filter changes the story most strongly?** The **Category / Sub-Category** slicer changes the narrative most drastically. Selecting low-margin accessories reveals that massive transaction spikes fail to drive real net profitability, immediately shifting the strategic focus from volume acquisition to margin optimization.
* **Q3. What would you improve if you had one more day?** Given an extra day, I would implement dynamic tooltips showing underlying supplier performance on hover and introduce row-level tracking metrics to immediately flag regional shipping facilities exceeding target fulfillment delay constraints.

## Conclusion
Structuring the user interface based on strict visual hierarchy ensures enterprise stakeholders can pivot from macroscopic summaries to microscopic root-cause investigations in seconds.