import pandas as pd

# Load dataset
df = pd.read_csv("C:/projects/SupplyMind/data/raw/retail_store_inventory.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# Extract useful date features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Drop original Date column
df.drop('Date', axis=1, inplace=True)

# Save cleaned dataset
df.to_csv(
    "C:/projects/SupplyMind/data/cleaned/retail_store_inventory_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")
print(df.head())