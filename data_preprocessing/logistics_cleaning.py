import pandas as pd

# Load raw dataset
df = pd.read_csv(
    "C:/projects/SupplyMind/data/raw/dynamic_supply_chain_logistics_dataset.csv"
)

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv(
    "C:/projects/SupplyMind/data/cleaned/logistics_cleaned.csv",
    index=False
)

print("logistics_cleaned.csv created successfully!")