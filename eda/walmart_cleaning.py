import pandas as pd

# Load dataset
df = pd.read_csv("C:/projects/SupplyMind/data/raw/Walmart.csv")

# Convert Date column
df['Date'] = pd.to_datetime(
    df['Date'],
    format='%d-%m-%Y'
)

# Create Date Features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Week'] = df['Date'].dt.isocalendar().week
df['Quarter'] = df['Date'].dt.quarter

# Drop original Date column
df.drop('Date', axis=1, inplace=True)

# Save cleaned dataset
df.to_csv(
    "C:/projects/SupplyMind/data/cleaned/walmart_cleaned.csv",
    index=False
)

print("Walmart cleaned dataset saved successfully!")
print(df.head())