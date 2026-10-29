import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 1. Sample Numeric Data with Different Ranges
data = {
    "Age": [20, 25, 30, 40, 50],
    "Salary": [30000, 45000, 60000, 80000, 120000]
}
df = pd.DataFrame(data)
print("--- Original Data ---\n", df)

# 2. Method A: StandardScaler (Z-Score: mean = 0, std = 1)
# Formula: z = (x - mean) / std
scaler_std = StandardScaler()
df_std = pd.DataFrame(scaler_std.fit_transform(df), columns=["Age_Std", "Salary_Std"])
print("\n--- After StandardScaler (Z-Score) ---\n", df_std.round(3))
print("Mean:", df_std.mean().round(2).to_dict())
print("Std: ", df_std.std(ddof=0).round(2).to_dict())

# 3. Method B: MinMaxScaler (Normalizes values into [0, 1] range)
# Formula: x_scaled = (x - min) / (max - min)
scaler_minmax = MinMaxScaler()
df_minmax = pd.DataFrame(scaler_minmax.fit_transform(df), columns=["Age_Norm", "Salary_Norm"])
print("\n--- After MinMaxScaler (Range 0 to 1) ---\n", df_minmax.round(3))
print("Min: ", df_minmax.min().to_dict())
print("Max: ", df_minmax.max().to_dict())
