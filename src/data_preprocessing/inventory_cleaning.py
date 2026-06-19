"""
inventory_cleaning.py
----------------------
Cleaning pipeline for: retail_store_inventory.csv
Dataset order: 1

Run:
    python src/data_preprocessing/inventory_cleaning.py
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/retail_store_inventory.csv")
CLEANED_PATH = Path("data/cleaned/retail_store_inventory_cleaned.csv")


def load_data(path: Path) -> pd.DataFrame:
    """Load raw CSV into a DataFrame."""
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning steps: dedupe, type fixes, missing value handling."""
    df = df.copy()

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Drop exact duplicates
    df = df.drop_duplicates()

    # TODO: parse date columns, e.g.
    # df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # TODO: handle missing values per column
    # df["units_sold"] = df["units_sold"].fillna(0)

    # TODO: fix dtypes for numeric columns
    # numeric_cols = ["units_sold", "inventory_level", "price"]
    # df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

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
