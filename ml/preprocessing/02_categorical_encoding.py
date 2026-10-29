import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 1. Sample Categorical DataFrame
data = {
    "Country": ["India", "USA", "France", "India", "USA"],
    "Education": ["High School", "Bachelors", "PhD", "Masters", "Bachelors"],
    "Purchased": ["No", "Yes", "No", "Yes", "Yes"]
}
df = pd.DataFrame(data)
print("--- Original Categorical Data ---\n", df)

# 2. Method A: Label Encoding (Transforms classes to integers 0, 1, 2...)
le = LabelEncoder()
df["Purchased_Num"] = le.fit_transform(df["Purchased"])
print("\n--- After LabelEncoder (Purchased) ---\n", df[["Purchased", "Purchased_Num"]])

# 3. Method B: Ordinal Mapping with Dictionary (Preserves Natural Order)
edu_map = {"High School": 1, "Bachelors": 2, "Masters": 3, "PhD": 4}
df["Education_Num"] = df["Education"].map(edu_map)
print("\n--- After Ordinal Mapping (Education) ---\n", df[["Education", "Education_Num"]])

# 4. Method C: One-Hot Encoding via Pandas get_dummies (Nominal Features)
df_dummies = pd.get_dummies(df[["Country"]], drop_first=True, dtype=int)
print("\n--- After pd.get_dummies (drop_first=True) ---\n", df_dummies)

# 5. Method D: One-Hot Encoding via Scikit-Learn OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, drop="first")
country_ohe = ohe.fit_transform(df[["Country"]])
print("\n--- After Sklearn OneHotEncoder Array ---\n", country_ohe)
