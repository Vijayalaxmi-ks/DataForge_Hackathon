# Practical 5 - Data Modeling & DAX Formulation
**Author:** Vijayalaxmi_Sundalam
**Date:** 2026-07-01 

## Problem Statement
Deploy calculated metric expressions and relational attributes inside Power BI to lay down an analytical layer for dashboard construction.

## Core KPI Overview
* **Definition:** Key Performance Indicators (KPIs) act as essential diagnostic metrics that measure data health and operational velocity. 
* **Application:** Leveraging our technical pipeline experience, we treat KPIs as the primary metric layer. Instead of looking at unorganized columns, KPIs provide a structured, high-level summary that allows immediate verification of system performance, margins, and logistical speed.

## Executed Outputs
* **Master Workspace Asset:** `p5_powerbi_model_dax.pbix`
* **Formula Inventory Script:** `03_powerbi/dax_formulas.txt`
* **Schema Blueprint Visual:** Saved as `model_schema.png` inside the submission repository.
* *Note: Complete answers to evaluation queries are detailed inside the primary development documentation path (`05_reports/report_p5.md`).*

## Key Insights Created
* **Fulfillment Latency:** The custom `Shipping Delay` calculation highlights localized transport bottlenecks where certain order paths experience disproportionate processing delays.
* **Profitability Realities:** Utilizing the dynamic `Profit Margin` measure highlights how high-revenue categories occasionally harbor remarkably low margin profiles.

## Conclusion
Structuring our metrics through a robust, formal DAX modeling tier ensures strict analytical accuracy and guarantees optimal, sub-second performance scaling when we transition to visualization.