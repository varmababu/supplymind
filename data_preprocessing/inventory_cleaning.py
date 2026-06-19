import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# Load dataset
df = pd.read_csv("data/raw/retail_store_inventory.csv")

# -------------------------------
# Basic Information
# -------------------------------
print(df.head())
print(df.info())
print(df.isnull().sum())

# -------------------------------
# Remove duplicates
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# Handle Missing Values
# -------------------------------
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# -------------------------------
# Encode Categorical Columns
# -------------------------------
le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# -------------------------------
# Save cleaned dataset
# -------------------------------
df.to_csv("data/cleaned/retail_store_inventory_cleaned.csv",
          index=False)

print("Cleaned dataset saved!")

# -------------------------------
# Target Variable
# -------------------------------
target = "Demand Forecast"

X = df.drop(columns=[target])
y = df[target]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
print("\nModel Performance")
print("----------------------")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("RMSE :", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score :", r2_score(y_test, y_pred))