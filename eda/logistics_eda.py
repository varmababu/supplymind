import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Create output folder
# ==========================================
output_dir = "C:/projects/SupplyMind/reports/figures/logistics"
os.makedirs(output_dir, exist_ok=True)

# ==========================================
# Load dataset
# ==========================================
df = pd.read_csv(
    "C:/projects/SupplyMind/data/raw/dynamic_supply_chain_logistics_dataset.csv"
)

# ==========================================
# Basic Information
# ==========================================
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
print(df.describe())

# ==========================================
# Numerical and Categorical Columns
# ==========================================
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include='object').columns

print("\nNumerical Columns:")
print(num_cols)

print("\nCategorical Columns:")
print(cat_cols)

# ==========================================
# Histograms
# ==========================================
df[num_cols].hist(figsize=(18, 12))
plt.tight_layout()
plt.savefig(f"{output_dir}/histograms.png")
plt.close()

# ==========================================
# Correlation Heatmap
# ==========================================
plt.figure(figsize=(12,8))
sns.heatmap(
    df[num_cols].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{output_dir}/correlation_heatmap.png")
plt.close()

# ==========================================
# Boxplots
# ==========================================
for col in num_cols:
    plt.figure(figsize=(8,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot - {col}")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/{col}_boxplot.png")
    plt.close()

# ==========================================
# Categorical Value Counts
# ==========================================
for col in cat_cols:
    print(f"\n{col}")
    print(df[col].value_counts())

print("\nEDA completed successfully!")
print(f"\nPlots saved in: {output_dir}")