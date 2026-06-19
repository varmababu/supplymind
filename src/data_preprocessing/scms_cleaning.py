"""
scms_cleaning.py
----------------------
Cleaning pipeline for: SCMS_Delivery_History_Dataset_20150929.csv
Dataset order: 4

Run:
    python src/data_preprocessing/scms_cleaning.py
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/SCMS_Delivery_History_Dataset_20150929.csv")
CLEANED_PATH = Path("data/cleaned/scms_delivery_cleaned.csv")


def load_data(path: Path) -> pd.DataFrame:
    # encoding="latin1" is often needed for this dataset
    df = pd.read_csv(path, encoding="latin1")
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()

    # TODO: parse date columns (po_sent_to_vendor_date, scheduled_delivery_date, delivered_to_client_date)
    # date_cols = ["scheduled_delivery_date", "delivered_to_client_date"]
    # for col in date_cols:
    #     df[col] = pd.to_datetime(df[col], errors="coerce")

    # TODO: clean currency/numeric fields (unit_price, line_item_value, freight_cost_(usd))
    # df["freight_cost_(usd)"] = pd.to_numeric(df["freight_cost_(usd)"], errors="coerce")

    # TODO: standardize categorical text fields (country, vendor, shipment_mode)

    return df


def save_data(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved cleaned data to {path} ({len(df)} rows)")


def main():
    df = load_data(RAW_PATH)
    df_clean = clean_data(df)
    save_data(df_clean, CLEANED_PATH)


if __name__ == "__main__":
    main()
