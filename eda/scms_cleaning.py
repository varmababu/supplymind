import pandas as pd
import numpy as np

# ==========================================
# Load Dataset
# ==========================================
df = pd.read_csv(
    "C:/projects/SupplyMind/data/raw/SCMS_Delivery_History_Dataset_20150929.csv",
    encoding='latin1'
)

# ==========================================
# Fill Missing Values
# ==========================================
df['Shipment Mode'] = df['Shipment Mode'].fillna(
    df['Shipment Mode'].mode()[0]
)

df['Dosage'] = df['Dosage'].fillna(
    'Unknown'
)

df['Line Item Insurance (USD)'] = df[
    'Line Item Insurance (USD)'
].fillna(
    df['Line Item Insurance (USD)'].median()
)

# ==========================================
# Weight Column Cleaning
# ==========================================
df['Weight (Kilograms)'] = pd.to_numeric(
    df['Weight (Kilograms)'],
    errors='coerce'
)

df['Weight (Kilograms)'] = df[
    'Weight (Kilograms)'
].fillna(
    df['Weight (Kilograms)'].median()
)

# ==========================================
# Freight Cost Cleaning
# ==========================================
df['Freight Cost (USD)'] = pd.to_numeric(
    df['Freight Cost (USD)'],
    errors='coerce'
)

df['Freight Cost (USD)'] = df[
    'Freight Cost (USD)'
].fillna(
    df['Freight Cost (USD)'].median()
)

# ==========================================
# Date Columns
# ==========================================
date_cols = [
    'PQ First Sent to Client Date',
    'PO Sent to Vendor Date',
    'Scheduled Delivery Date',
    'Delivered to Client Date',
    'Delivery Recorded Date'
]

for col in date_cols:
    df[col] = pd.to_datetime(
        df[col],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

# ==========================================
# Date Feature Engineering
# ==========================================
for col in date_cols:
    df[f'{col}_Year'] = df[col].dt.year
    df[f'{col}_Month'] = df[col].dt.month
    df[f'{col}_Day'] = df[col].dt.day

# ==========================================
# Save Cleaned Dataset
# ==========================================
df.to_csv(
    "C:/projects/SupplyMind/data/cleaned/scms_cleaned.csv",
    index=False
)

# ==========================================
# Verification
# ==========================================
print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nSCMS cleaned dataset saved successfully!")