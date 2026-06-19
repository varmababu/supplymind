import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# =====================================
# Load Dataset
# =====================================
df = pd.read_csv(
    "C:/projects/SupplyMind/data/cleaned/scms_cleaned.csv"
)

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# =====================================
# Feature Engineering
# =====================================

# Cost per kg
if {'Freight Cost (USD)', 'Weight (Kilograms)'}.issubset(df.columns):
    df["cost_per_kg"] = (
        df["Freight Cost (USD)"] /
        (df["Weight (Kilograms)"] + 1)
    )

# Insurance ratio
if {'Line Item Insurance (USD)', 'Line Item Value'}.issubset(df.columns):
    df["insurance_ratio"] = (
        df["Line Item Insurance (USD)"] /
        (df["Line Item Value"] + 1)
    )

# Value density
if {'Line Item Value', 'Weight (Kilograms)'}.issubset(df.columns):
    df["value_density"] = (
        df["Line Item Value"] /
        (df["Weight (Kilograms)"] + 1)
    )

# Pack efficiency
if {'Line Item Quantity', 'Weight (Kilograms)'}.issubset(df.columns):
    df["pack_efficiency"] = (
        df["Line Item Quantity"] /
        (df["Weight (Kilograms)"] + 1)
    )

# Price margin
if {'Pack Price', 'Unit Price'}.issubset(df.columns):
    df["price_margin"] = (
        df["Pack Price"] -
        df["Unit Price"]
    )

# Delivery gap days
if {
    'Delivered to Client Date_Day',
    'Scheduled Delivery Date_Day'
}.issubset(df.columns):

    df["delivery_gap_days"] = (
        df["Delivered to Client Date_Day"] -
        df["Scheduled Delivery Date_Day"]
    ).abs()

# =====================================
# Encode Categorical Columns
# =====================================

categorical_cols = [
    'Country',
    'Managed By',
    'Fulfill Via',
    'Vendor INCO Term',
    'Shipment Mode',
    'Product Group',
    'Sub Classification',
    'Vendor',
    'Brand',
    'Dosage Form',
    'Manufacturing Site'
]

encoder = LabelEncoder()

for col in categorical_cols:
    if col in df.columns:
        df[col] = encoder.fit_transform(
            df[col].astype(str)
        )

# =====================================
# Scale Numerical Features
# =====================================

scale_cols = [
    'Line Item Quantity',
    'Line Item Value',
    'Pack Price',
    'Unit Price',
    'Weight (Kilograms)',
    'Line Item Insurance (USD)',
    'cost_per_kg',
    'insurance_ratio',
    'value_density',
    'pack_efficiency',
    'price_margin',
    'delivery_gap_days'
]

available_cols = [
    col for col in scale_cols
    if col in df.columns
]

if available_cols:
    scaler = StandardScaler()
    df[available_cols] = scaler.fit_transform(
        df[available_cols]
    )

# =====================================
# Save Dataset
# =====================================

output_path = (
    "C:/projects/SupplyMind/data/cleaned/scms_features.csv"
)

df.to_csv(output_path, index=False)

print("✅ SCMS feature engineering completed successfully!")
print("Saved to:", output_path)