# Practical 8 - Programmatic Data Wrangling & Imputation
**Student ID:** 2026CS017
**Name:** Vijayalaxmi Sundalam
**Dataset:** Superstore Sales Dataset  

## Problem Statement
Clean anomalies, handle missing indicators, and construct targeted behavioral features within transactional records using absolute code-driven replication controls.

## Procedure & Engineering Strategy
1. Loaded raw baseline metrics into an interactive Python sandbox array environment via Pandas.
2. Programmatically verified columns and dropped empty structures exceeding a strict 50% missingness threshold constraint parameter.
3. Executed row deduplication operations and filled categorical null values with an "Unknown" placeholder string flag.
4. Calculated midpoints on remaining sparse numeric elements using localized field `.median()` statistical vector imputations to keep row vectors intact.
5. Parsed temporal boundaries into datetime objects to extract chronological fields (`Year`, `Month`).
6. Feature-engineered two analytical variables: `Shipping Delay` (measuring order fulfillment latency) and `Total Profit` (modeling standard commercial performance metrics).
7. Aggregated the final dataframe utilizing a `.groupby()` pipeline to extract average sales per territory and recorded clean deliverables to disk.

## Report Questions
* **Q1. What cleaning decision could affect business conclusions?** Choosing a median strategy over completely deleting missing row rows directly shields the overall sample volume from scaling decay. However, because median calculation replaces extreme variance blocks with middle-ground numbers, it can artificially squash statistical variance metrics and shrink outliers that executive strategists rely on to flag regional losses.
* **Q2. Which engineered feature is most useful and why?** The **Shipping Delay** metric provides the highest business utility. Isolating explicit temporal distance numbers directly from raw date configurations gives operations teams an actionable way to pinpoint transport backlogs and evaluate fulfillment infrastructure limits across distribution networks.

## Conclusion
Migrating data preparation tasks from manual interfaces to explicit Python scripts creates a reusable pipeline architecture that processes raw incoming logs instantly and guarantees identical results every single run.