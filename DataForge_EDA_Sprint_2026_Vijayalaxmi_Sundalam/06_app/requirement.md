# Capstone Requirement Documentation - Auto-EDA Engine
**Author:** Vijayalaxmi Sundalam 
**Implementation Stack:** Vanilla HTML5, Tailwind CSS, PapaParse Core JS, Chart.js Visualizer  

# Software Requirements Specification (SRS)
**Project Title:** Standalone Regional Medical Resource Tracker  
**Target User:** Non-Technical Public Health & Emergency Coordinators  
**Deployment Model:** Offline-Ready Single-File System  

---

## 1. Core Functional Requirements
* **Local Ingestion:** System must parse standard comma-separated value (.csv) logs instantly using the native browser `FileReader` API without uploading data to an external server.
* **Flexible Schema Mapping:** Parsing logic must dynamically locate target data rows using string lookups (e.g., matching "zone" or "region" to geographical indices).
* **Interactive Dynamic Filtering:** Users must be able to isolate medical facility subsets on-the-fly via a single dropdown menu selection.
* **Hot-Swapping Datasets:** A distinct re-upload feature must be available at all times, allowing operators to switch or update spreadsheet files with zero page reloads.
* **Emergency Stress Simulation:** A manual trigger button must immediately apply negative modifiers to inventory parameters (-4 Oxygen days, -6 Antivenom vials, -2 Power days) to forecast downstream facility supply failures.

## 2. User Interface (UI) & Accessibility Rules
* **High Scannability:** Layout must prioritize clear, color-coded status elements (Red for critical deficits, Green for stable baseline) instead of dense technical jargon.
* **Zero Technical Complications:** Interface labels must translate metric math into immediate plain-English warnings that any user can interpret during a crisis.
* **Responsive Architecture:** The view layout must adjust fluidly to remain completely legible on small mobile devices, old legacy computers, or tablets.

## 3. Non-Functional & Environmental Constraints
* **Zero Dependencies:** The application must run using only basic HTML5 and browser-native JavaScript. External runtime installations, local servers, or backend setups are strictly prohibited.
* **Air-Gapped Operation:** The tracker must function perfectly in remote, completely offline environments with no internet access.
* **Absolute Data Privacy:** Data handling must be strictly sandboxed within browser window memory frames to protect sensitive public health inventory records.