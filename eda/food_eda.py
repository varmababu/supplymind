import os
import pandas as pd

# Output folder
output_dir = "C:/projects/SupplyMind/reports/figures/food"
os.makedirs(output_dir, exist_ok=True)

# Load Excel file
df = pd.read_excel(
    "C:/projects/SupplyMind/data/raw/Food Report - Oct. 2022.xlsx"
)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe(include='all'))