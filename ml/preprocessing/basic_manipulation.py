import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Sample DataFrame with Null Values and String Columns
data = {
    "Age": [22.0, np.nan, 28.0, 35.0, 40.0],
    "Gender": ["Male", "Female", "Female", "Male", "Female"],
    "City": ["Mumbai", "Delhi", "Delhi", "Mumbai", "Pune"],
    "Purchased": ["No", "Yes", "No", "Yes", "Yes"]
}
df = pd.DataFrame(data)
print("--- 1. Original Data ---")
print(df)

# 2. Surface-Level Null Handling
print("\nNull Values Count:")
print(df.isnull().sum())

# Option A: Remove rows with nulls -> df = df.dropna()
# Option B: Fill nulls with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 3. Convert String Columns to Numeric using LabelEncoder (fit_transform)
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])        # Female -> 0, Male -> 1
df["City"] = le.fit_transform(df["City"])            # Delhi -> 0, Mumbai -> 1, Pune -> 2
df["Purchased"] = le.fit_transform(df["Purchased"])  # No -> 0, Yes -> 1

print("\n--- 2. After Handling Nulls & Label Encoding (fit_transform) ---")
print(df)
