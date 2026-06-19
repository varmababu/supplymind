<<<<<<< HEAD
# SupplyMind

A supply chain & retail analytics project covering inventory management, retail sales, logistics, and procurement/delivery data. The project moves through exploratory data analysis (EDA) and cleaning across six datasets in a recommended order, building toward unified supply chain insights.

## Project Structure

```
SupplyMind/
│
├── data/
│   ├── raw/              # Original, unmodified datasets
│   └── cleaned/           # Cleaned datasets output by src/data_preprocessing scripts
│
├── notebooks/             # EDA notebooks, one per dataset
│   ├── 01_inventory_eda.ipynb
│   ├── 02_walmart_eda.ipynb
│   ├── 03_logistics_eda.ipynb
│   ├── 04_scms_eda.ipynb
│   ├── 05_food_report_eda.ipynb
│   └── 06_consumables_eda.ipynb
│
├── src/
│   └── data_preprocessing/    # Cleaning scripts, one per dataset
│       ├── inventory_cleaning.py
│       ├── walmart_cleaning.py
│       ├── logistics_cleaning.py
│       ├── scms_cleaning.py
│       ├── food_report_cleaning.py
│       └── consumables_cleaning.py
│
├── reports/
│   ├── figures/            # Saved plots/visualizations
│   └── insights/           # Written findings, summaries
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Recommended Dataset Order

| # | Dataset | Notebook | Cleaning Script |
|---|---------|----------|------------------|
| 1 | `retail_store_inventory.csv` | `01_inventory_eda.ipynb` | `inventory_cleaning.py` |
| 2 | `Walmart.csv` | `02_walmart_eda.ipynb` | `walmart_cleaning.py` |
| 3 | `dynamic_supply_chain_logistics_dataset.csv` | `03_logistics_eda.ipynb` | `logistics_cleaning.py` |
| 4 | `SCMS_Delivery_History_Dataset_20150929.csv` | `04_scms_eda.ipynb` | `scms_cleaning.py` |
| 5 | `Food Report - Oct. 2022.xlsx` | `05_food_report_eda.ipynb` | `food_report_cleaning.py` |
| 6 | `Consumables Report - Oct. 2022.xlsx` | `06_consumables_eda.ipynb` | `consumables_cleaning.py` |

## Getting Started

1. **Clone / unzip the project** and place raw data files into `data/raw/` (they are currently empty placeholders — drop in your actual CSV/XLSX files with the exact filenames listed above).

2. **Set up the environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the notebooks in order** (1 → 6) to explore each dataset:
   ```bash
   jupyter notebook notebooks/01_inventory_eda.ipynb
   ```

4. **Run cleaning scripts** once EDA findings are incorporated into the TODOs:
   ```bash
   python src/data_preprocessing/inventory_cleaning.py
   ```
   Each script reads from `data/raw/` and writes a cleaned CSV to `data/cleaned/`.

5. **Save figures and insights** as you go:
   - Plots → `reports/figures/`
   - Written takeaways → `reports/insights/`

## Workflow per Dataset

Each dataset follows the same pattern:
1. **EDA notebook** — load data, check shape/dtypes/missing values/duplicates, explore distributions and correlations, and log cleaning TODOs.
2. **Cleaning script** — convert EDA notes into a repeatable, scripted cleaning pipeline (column standardization, dtype fixes, missing value handling, deduplication).
3. **Cleaned output** — saved to `data/cleaned/` for downstream analysis or modeling.

## Notes

- Raw data files are currently empty placeholders generated for the folder scaffold — replace them with your actual data files before running notebooks/scripts.
- `data/raw/`, `data/cleaned/`, and `reports/figures|insights` contents are gitignored by default (only `.gitkeep` is tracked) so large/raw data doesn't bloat version control.
=======
# supplymind
>>>>>>> 0f50521b21d810e0104d10723553ecfca6be76d7
