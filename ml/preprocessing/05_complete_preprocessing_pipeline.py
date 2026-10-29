import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# 1. Sample Raw Dataset with Missing Values & Categorical Text
data = {
    "Age": [22.0, np.nan, 30.0, 38.0],
    "Salary": [40000.0, 52000.0, np.nan, 85000.0],
    "Department": ["HR", "IT", np.nan, "IT"],
    "Gender": ["Female", "Male", "Male", "Female"]
}
df = pd.DataFrame(data)
print("--- Raw Input Data ---\n", df)

# 2. Define Pipelines for Numeric and Categorical Features
num_cols = ["Age", "Salary"]
cat_cols = ["Department", "Gender"]

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(drop="first", sparse_output=False))
])

# 3. Combine with ColumnTransformer
preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])

# 4. Transform Data into Final Ready-to-Train Numeric Array
X_processed = preprocessor.fit_transform(df)
print("\n--- Final Processed Numeric Matrix (Zero Nulls, Scaled & Encoded) ---\n")
print(np.round(X_processed, 3))
