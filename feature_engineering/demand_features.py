import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ==========================
# Load cleaned dataset
# ==========================
df = pd.read_csv("../data/cleaned/retail_store_inventory_cleaned.csv")

# ==========================
# Feature Engineering
# ==========================

# Inventory Utilization
if {'Units Sold', 'Inventory Level'}.issubset(df.columns):
    df['inventory_utilization'] = (
        df['Units Sold'] / (df['Inventory Level'] + 1)
    )

# Supply Coverage
if {'Inventory Level', 'Units Sold'}.issubset(df.columns):
    df['supply_coverage'] = (
        df['Inventory Level'] / (df['Units Sold'] + 1)
    )

# Stock Gap
if {'Inventory Level', 'Reorder Point'}.issubset(df.columns):
    df['stock_gap'] = (
        df['Inventory Level'] - df['Reorder Point']
    )

# Order Ratio
if {'Units Ordered', 'Units Sold'}.issubset(df.columns):
    df['order_ratio'] = (
        df['Units Ordered'] / (df['Units Sold'] + 1)
    )

# Price Gap
if {'Price', 'Competitor Pricing'}.issubset(df.columns):
    df['price_gap'] = (
        df['Price'] - df['Competitor Pricing']
    )

# Discount Percentage
if {'Discount', 'Price'}.issubset(df.columns):
    df['discount_percent'] = (
        df['Discount'] / (df['Price'] + 1)
    )

# Stockout Risk
if {'Inventory Level', 'Reorder Point'}.issubset(df.columns):
    df['stockout_risk'] = (
        df['Inventory Level'] < df['Reorder Point']
    ).astype(int)

# Overstock Indicator
if {'Inventory Level', 'Units Sold'}.issubset(df.columns):
    df['overstock'] = (
        df['Inventory Level'] > 2 * df['Units Sold']
    ).astype(int)

# ==========================
# Encode Categorical Columns
# ==========================
categorical_cols = [
    'Category',
    'Region',
    'Weather Condition',
    'Seasonality'
]

encoder = LabelEncoder()

for col in categorical_cols:
    if col in df.columns:
        df[col] = encoder.fit_transform(df[col].astype(str))

# ==========================
# Scale Numerical Features
# ==========================
scale_cols = [
    'Inventory Level',
    'Units Sold',
    'Units Ordered',
    'Price',
    'Competitor Pricing',
    'Lead Time',
    'inventory_utilization',
    'supply_coverage',
    'stock_gap',
    'order_ratio',
    'price_gap',
    'discount_percent'
]

available_cols = [col for col in scale_cols if col in df.columns]

if available_cols:
    scaler = StandardScaler()
    df[available_cols] = scaler.fit_transform(df[available_cols])

# ==========================
# Save Feature Dataset
# ==========================
output_path = "../data/cleaned/retail_features.csv"

df.to_csv(output_path, index=False)

print("✅ Demand forecasting features created successfully.")
print(f"Saved to: {output_path}")