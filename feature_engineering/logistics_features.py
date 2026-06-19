import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# =====================================
# Load Dataset
# =====================================
df = pd.read_csv(
    "C:/projects/SupplyMind/data/cleaned/logistics_cleaned.csv"
)

# =====================================
# Feature Engineering
# =====================================

# Supply Efficiency
df["supply_efficiency"] = (
    df["supplier_reliability_score"] /
    (df["lead_time_days"] + 1)
)

# Warehouse Utilization
df["warehouse_utilization"] = (
    df["historical_demand"] /
    (df["warehouse_inventory_level"] + 1)
)

# Equipment Efficiency
df["equipment_efficiency"] = (
    df["handling_equipment_availability"] /
    (df["loading_unloading_time"] + 1)
)

# Driver Safety Index
df["driver_safety_index"] = (
    df["driver_behavior_score"] +
    df["fatigue_monitoring_score"]
) / 2

# Route Risk Impact
df["route_risk_impact"] = (
    df["route_risk_level"] *
    df["traffic_congestion_level"]
)

# Customs Delay Ratio
df["customs_delay_ratio"] = (
    df["customs_clearance_time"] /
    (df["lead_time_days"] + 1)
)

# Cost Per Lead Day
df["cost_per_day"] = (
    df["shipping_costs"] /
    (df["lead_time_days"] + 1)
)

# Temperature Deviation
df["temperature_deviation"] = abs(
    df["iot_temperature"] -
    df["iot_temperature"].mean()
)

# =====================================
# Encode Categorical Columns
# =====================================
categorical_cols = [
    "order_fulfillment_status",
    "weather_condition_severity",
    "cargo_condition_status"
]

encoder = LabelEncoder()

for col in categorical_cols:
    if col in df.columns:
        df[col] = encoder.fit_transform(df[col].astype(str))

# =====================================
# Scale Numerical Features
# =====================================
scale_cols = [
    "fuel_consumption_rate",
    "eta_variation_hours",
    "traffic_congestion_level",
    "warehouse_inventory_level",
    "loading_unloading_time",
    "shipping_costs",
    "supplier_reliability_score",
    "lead_time_days",
    "historical_demand",
    "iot_temperature",
    "customs_clearance_time",
    "driver_behavior_score",
    "fatigue_monitoring_score",
    "disruption_likelihood_score",
    "supply_efficiency",
    "warehouse_utilization",
    "equipment_efficiency",
    "driver_safety_index",
    "route_risk_impact",
    "customs_delay_ratio",
    "cost_per_day",
    "temperature_deviation"
]

scaler = StandardScaler()

available_cols = [col for col in scale_cols if col in df.columns]

df[available_cols] = scaler.fit_transform(df[available_cols])

# =====================================
# Save Engineered Dataset
# =====================================
output_path = "C:/projects/SupplyMind/data/cleaned/logistics_features.csv"

df.to_csv(output_path, index=False)

print("✅ Logistics feature engineering completed successfully!")
print("Saved to:", output_path)