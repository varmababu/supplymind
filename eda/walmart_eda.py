import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Create output folder
# ==========================================
output_dir = "C:/projects/SupplyMind/reports/figures/walmart"
os.makedirs(output_dir, exist_ok=True)

# ==========================================
# Load dataset
# ==========================================
df = pd.read_csv("C:/projects/SupplyMind/data/raw/Walmart.csv")

# ==========================================
# Convert Date column
# ==========================================
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(
        df['Date'],
        format='%d-%m-%Y'
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
# Numerical Columns
# ==========================================
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("\nNumerical Columns:")
print(num_cols)

# ==========================================
# Histograms
# ==========================================
df[num_cols].hist(figsize=(15,10))
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

print("\nEDA completed successfully!")
print(f"\nPlots saved in:\n{output_dir}")
