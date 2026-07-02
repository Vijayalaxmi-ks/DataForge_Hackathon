# System Architecture & Lifecycle Mechanics

This document details the completely serverless, decoupled client-side data workflow that governs the application without requiring external runtime dependencies or installations.

---

## 1. Structural Data Flow Diagram

```text
[ Raw CSV Spreadsheet File ] 
             │
             ▼
┌────────────────────────────────────────────────────────┐
│ 🔹 Browser FileReader API (Local Client Sandboxing)     │
└────────────┬───────────────────────────────────────────┘
             │ (Asynchronous Data Stream)
             ▼
┌────────────────────────────────────────────────────────┐
│ 🔹 Native JavaScript Structural Parser                 │
│    - Strips quote artifacts & splits index rows        │
│    - Maps columns dynamically using text heuristics    │
└────────────┬───────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────┐
│ 🔹 Core Mathematical Transformation Engine             │
│    - Baseline Math: Normalizes row strings to bounds   │
│    - Disruption Override Modifiers (-4 O2, -6 Venom)  │
└────────────┬───────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────┐
│ 🔹 Live UI Rendering Layer                              │
│    - Dynamic Card Component Threshold Indicators       │
│    - Contextual Row Background Tinting                 │
└────────────────────────────────────────────────────────┘