# Capstone Project: Automated EDA Tool
# Standalone Regional Medical Resource Tracker

An offline-ready, installation-free data tracking application designed to convert raw inventory spreadsheets (CSVs) into clean, scannable alert dashboards. 

This project is built explicitly for non-technical frontline health coordinators to manage critical resources (Oxygen, Antivenom, and Power Backups) during localized emergencies, such as heavy monsoon disruptions or power grid failures.

---

## 📌 Project Architecture & Deliverables Directory

This repository is organized into distinct, modular documentation files for clear academic evaluation:

* **`ABSTRACT.md`**: Core overview of the real-world problem statement, the technical solution framework, and operational target impact.
* **`ARCHITECTURE.md`**: Deep dive into the serverless client-side lifecycle, non-destructive file ingestion, and reactive DOM rendering pipeline.
* **`TESTING.md`**: Sequential verification checklist, user evaluation matrix, and system error-handling safeguards.
* **`CONCLUSION.md`**: Technical achievements, privacy advantages, and future development horizons.

---

## 🚀 Quick Start Guide (Zero Installation)

Because this system has **zero external dependencies**, it does not require running terminal commands, installing `npm` packages, or setting up local servers.

1.  **Download the Source:** Save the `Resource_Tracker.html` file to your computer (you can keep it on a desktop or an offline USB flash drive).
2.  **Launch the App:** Double-click `Resource_Tracker.html` to open it instantly inside any standard web browser.
3.  **Load the Data:** Click the **"Select CSV Inventory File"** button and select your spreadsheet (e.g., the provided `medical_inventory.csv` file).
4.  **Coordinate Resources:** Use the **Filter Zone** dropdown to view specific clusters, or click **Simulate Emergency Disruption** to run a predictive supply-chain stress evaluation.
5.  **Update on-the-go:** Click **🔄 Upload New File** in the upper-right corner at any time to instantly overwrite memory with fresh operational logs.

---

## 🛠️ Technology Stack & Core Principles

* **HTML5 & Native Vanilla JavaScript:** Uses the browser's built-in `FileReader` API to parse comma-separated values locally on-the-fly.
* **Tailwind CSS (via CDN):** Implements a highly functional, high-contrast user interface that scales cleanly across mobile phones, tablets, and old legacy desktop monitors.
* **Local Client Privacy Sandboxing:** Spreadsheet rows are processed completely within the local browser window memory frame. Data never leaves the machine and is never transmitted over the internet.