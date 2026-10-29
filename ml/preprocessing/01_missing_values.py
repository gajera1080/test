import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# 1. Create Sample DataFrame with Missing (NaN) Values
data = {
    "Age": [22.0, np.nan, 28.0, 35.0, np.nan, 40.0],
    "Salary": [45000.0, 54000.0, np.nan, 65000.0, 50000.0, 80000.0],
    "City": ["Mumbai", "Delhi", np.nan, "Delhi", "Mumbai", "Pune"]
}
df = pd.DataFrame(data)
print("--- Original DataFrame with Nulls ---\n", df)

# 2. Check for Null Values
print("\nNull Count per Column:\n", df.isnull().sum())

# 3. Method A: Drop Rows with Any Null Value
df_dropped = df.dropna()
print("\n--- After dropna() ---\n", df_dropped)

# 4. Method B: Impute with Pandas fillna (Mean for Numeric, Mode for Categorical)
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].median())
df_filled["Salary"] = df_filled["Salary"].fillna(df_filled["Salary"].mean())
df_filled["City"] = df_filled["City"].fillna(df_filled["City"].mode()[0])
print("\n--- After Pandas fillna() ---\n", df_filled)

# 5. Method C: Impute with Scikit-Learn SimpleImputer
imputer = SimpleImputer(strategy="mean")
df_sklearn = df.copy()
df_sklearn[["Age", "Salary"]] = imputer.fit_transform(df_sklearn[["Age", "Salary"]])
print("\n--- After Scikit-Learn SimpleImputer (Mean) ---\n", df_sklearn)
