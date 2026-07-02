# User Verification & Testing Protocol

This testing matrix provides a straightforward verification process to ensure the application works correctly and is simple for non-technical users to navigate.

---

## Execution Checklist

Run through these verification checkpoints sequentially using a standard web browser and the provided sample dataset file:

| Step | Action | Expected System Response | Visual Validation Metric | Pass / Fail |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Open `app.html` inside any standard web browser. | The layout loads cleanly and displays a simple setup layout requesting a data file. | The workspace tables and metric summary cards remain completely hidden from view. | [ ] |
| **2** | Upload the 100-row `medical_inventory.csv` dataset. | The system processes the rows instantly, closes the upload pane, and reveals the core tracker. | The "Total Facilities" counter instantly updates to **100**. The main banner reads `SYSTEM STATUS NORMAL` in green. | [ ] |
| **3** | Click the **"Filter Zone"** selection menu and pick **"East Zone"**. | The data table removes all unrelated rows, leaving only facilities matching the East Zone. | The facility count changes to match only the filtered subset, and table items show matching tags. | [ ] |
| **4** | Click the **"Simulate Emergency Disruption"** action button. | The button turns deep crimson. The top alert panel changes state, and table rows flash warning indicators. | The top banner switches to `DISRUPTION SIMULATION`, and high-risk facility rows turn soft pink/red. | [ ] |
| **5** | Click the **"🔄 Upload New File"** action button in the upper header. | The system opens the native operating system file explorer prompt without resetting page state. | Users can select a separate updated spreadsheet log, immediately overwriting memory cache. | [ ] |

---

## System Error Handling Verification
* **Empty Row Safeguard:** If a row contains missing cells, the internal parsing index automatically skips the bad data row or inserts an `Unknown Facility` label to protect the spreadsheet application from freezing or crashing.
* **Malformed Input Defenses:** Attempting to feed an incompatible or raw non-CSV file will be rejected by the browser input mask, keeping data paths clean and stable.