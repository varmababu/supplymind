"""
food_report_cleaning.py
----------------------
Cleaning pipeline for: Food Report - Oct. 2022.xlsx
Dataset order: 5

Run:
    python src/data_preprocessing/food_report_cleaning.py
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/Food Report - Oct. 2022.xlsx")
CLEANED_PATH = Path("data/cleaned/food_report_cleaned.csv")


def load_data(path: Path, sheet_name=0) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()

    # TODO: drop fully empty rows/columns common in exported Excel reports
    # df = df.dropna(how="all")
    # df = df.dropna(axis=1, how="all")

    # TODO: parse date columns if present

    # TODO: fix numeric quantity/cost columns
    # df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

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
