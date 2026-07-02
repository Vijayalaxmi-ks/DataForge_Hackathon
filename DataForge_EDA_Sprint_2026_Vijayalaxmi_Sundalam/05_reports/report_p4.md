# Practical 4 - Power Query ETL Engine
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset

## Problem Statement
Automate the data transformation steps so that when new transactional data arrives, the cleaning pipeline runs instantaneously without manual cell-by-cell manipulation.

## Procedure
1. Connected Power BI Desktop to the source file `dataset_raw.csv` and initialized the Power Query ETL engine.
2. Promoted the initial row to structural table headers and validated column metadata data types.
3. Cleaned anomalies by executing a global error-removal sweep across the dataset grid.
4. Split the compound `Order ID` attribute into modular columns using its natural string delimiter.
5. Injected a logical business rule via an engineered Conditional Column classifying records as either "Profitable" or "Loss".
6. Extracted structural chronological parameters directly from the `Order Date` column to isolate localized Year dimensions.
7. Exported the compiled underlying Power Query M code asset into the project environment.

## Outputs Created
* **ETL Pipeline Automation Code:** `03_powerbi/p4_power_query_m_code.txt`
* **Local Power BI Project Workspace:** `03_powerbi/p4_power_query_pipeline.pbix`

## Observations
* **Q1. How is Power Query different from manual Excel cleaning?** Power Query acts as a non-destructive pipeline that logs steps as a functional program (M code) rather than changing cells directly. Excel manual overrides must be repeated from scratch every time data shifts, whereas Power Query records the recipe once.
* **Q2. Which transformation would save time when new CSV data arrives?** The absolute layout parsing—such as automated header promotion, automatic error purging, and programmatic conditional parsing—saves the most time. When a new raw file drops in, clicking "Refresh" re-runs the entire sequence in one second.

## Conclusion
Transitioning from manual data cleaning sheets to programmatic ETL pipelines enforces strict structural compliance and guarantees automated reproducibility for enterprise scaling.