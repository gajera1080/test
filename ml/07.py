import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load Dataset
df = pd.read_csv("data/insaurance_Practical_3.csv")

# 2. Convert Categorical Data into Numeric Data
df["sex"] = df["sex"].astype("category").cat.codes
df["smoker"] = df["smoker"].astype("category").cat.codes
df["region"] = df["region"].astype("category").cat.codes

x = df.drop(columns="charges")
y = df["charges"]

# 3. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 4. Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# 5. Print Intercept, Coefficients and R2 Score
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

y_pred = model.predict(x_test)
print("R2 Score:", r2_score(y_test, y_pred))

# 6. Visualization
plt.scatter(y_test, y_pred, color="blue")
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Insurance Charges - Multiple Linear Regression")
plt.show()
