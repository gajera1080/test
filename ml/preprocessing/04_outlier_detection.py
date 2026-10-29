import pandas as pd

# 1. Sample Data with Clear Outliers (e.g. Salary = 300,000 is an outlier)
data = {"Salary": [25000, 28000, 31000, 29000, 33000, 35000, 32000, 300000]}
df = pd.DataFrame(data)
print("--- Original Data with Outlier ---\n", df)

# 2. Compute Quartiles and IQR
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

# 3. Calculate Boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nQ1 (25%): {Q1}, Q3 (75%): {Q3}, IQR: {IQR}")
print(f"Valid Range: [{lower_bound:.1f}, {upper_bound:.1f}]")

# 4. Identify Outliers
outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]
print("\nIdentified Outliers:\n", outliers)

# 5. Remove Outliers (Trimming)
df_clean = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]
print("\n--- Cleaned Data (Outliers Removed) ---\n", df_clean)
