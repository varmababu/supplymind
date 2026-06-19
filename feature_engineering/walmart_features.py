import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================
# Load Dataset
# =====================================
df = pd.read_csv(
    "C:/projects/SupplyMind/data/cleaned/walmart_cleaned.csv"
)

# =====================================
# Feature Engineering
# =====================================

# Inflation-adjusted purchasing power
df["sales_per_cpi"] = (
    df["Weekly_Sales"] /
    (df["CPI"] + 1)
)

# Fuel efficiency indicator
df["fuel_impact"] = (
    df["Weekly_Sales"] /
    (df["Fuel_Price"] + 1)
)

# Temperature impact
df["temp_sales_ratio"] = (
    df["Weekly_Sales"] /
    (df["Temperature"] + 1)
)

# Economic stress indicator
df["economic_stress"] = (
    df["Unemployment"] *
    df["Fuel_Price"]
)

# Seasonal indicator
df["is_year_end"] = (
    df["Month"].isin([11, 12])
).astype(int)

# Quarter-Holiday interaction
df["holiday_quarter"] = (
    df["Holiday_Flag"] *
    df["Quarter"]
)

# =====================================
# Store-Level Statistics
# =====================================

store_avg_sales = (
    df.groupby("Store")["Weekly_Sales"]
    .transform("mean")
)

df["store_avg_sales"] = store_avg_sales

# Relative store performance
df["sales_vs_store_avg"] = (
    df["Weekly_Sales"] /
    (df["store_avg_sales"] + 1)
)

# =====================================
# Scaling
# =====================================

scale_cols = [
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment",
    "Year",
    "Month",
    "Week",
    "Quarter",
    "sales_per_cpi",
    "fuel_impact",
    "temp_sales_ratio",
    "economic_stress",
    "store_avg_sales",
    "sales_vs_store_avg"
]

available_cols = [col for col in scale_cols if col in df.columns]

scaler = StandardScaler()
df[available_cols] = scaler.fit_transform(df[available_cols])

# =====================================
# Save Feature Dataset
# =====================================

output_path = (
    "C:/projects/SupplyMind/data/cleaned/walmart_features.csv"
)

df.to_csv(output_path, index=False)

print("✅ Walmart feature engineering completed successfully!")
print("Saved to:", output_path)