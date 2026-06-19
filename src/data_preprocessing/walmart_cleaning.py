"""
walmart_cleaning.py
----------------------
Cleaning pipeline for: Walmart.csv
Dataset order: 2

Run:
    python src/data_preprocessing/walmart_cleaning.py
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/Walmart.csv")
CLEANED_PATH = Path("data/cleaned/walmart_cleaned.csv")


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()

    # TODO: parse date column
    # df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    # TODO: handle missing values
    # df["weekly_sales"] = df["weekly_sales"].fillna(df["weekly_sales"].median())

    # TODO: fix dtypes (holiday flag, temperature, fuel price, cpi, unemployment)

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
