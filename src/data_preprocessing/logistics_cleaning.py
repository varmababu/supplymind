"""
logistics_cleaning.py
----------------------
Cleaning pipeline for: dynamic_supply_chain_logistics_dataset.csv
Dataset order: 3

Run:
    python src/data_preprocessing/logistics_cleaning.py
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/dynamic_supply_chain_logistics_dataset.csv")
CLEANED_PATH = Path("data/cleaned/logistics_cleaned.csv")


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()

    # TODO: parse timestamp columns
    # df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # TODO: handle missing sensor/logistics readings
    # df["traffic_congestion_level"] = df["traffic_congestion_level"].fillna(method="ffill")

    # TODO: clip/validate outliers in continuous fields (e.g. delays, fuel consumption)

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
