import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/projects/SupplyMind/data/raw/retail_store_inventory.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------------
# Basic Information
# -------------------------------
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# -------------------------------
# Summary Statistics
# -------------------------------
print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# Numerical and Categorical Columns
# -------------------------------
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

print("\nNumerical Columns:")
print(num_cols)

print("\nCategorical Columns:")
print(cat_cols)

# -------------------------------
# Histograms
# -------------------------------
df[num_cols].hist(figsize=(15, 10))
plt.tight_layout()
plt.show()

# -------------------------------
# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10, 8))

sns.heatmap(
    df[num_cols].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Boxplots for Outlier Detection
# -------------------------------
for col in num_cols:
    plt.figure(figsize=(8, 3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# -------------------------------
# Value Counts for Categorical Columns
# -------------------------------
for col in cat_cols:
    print(f"\n{col}")
    print(df[col].value_counts())