import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load Data
df = pd.read_csv("data/FuelConsumption.csv")
X = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]]
y = df["CO2EMISSIONS"]

# 2. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

# 3. Intercept, Coefficients, and Accuracy
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
y_pred = model.predict(X_test)
print(f"Accuracy (R2 Score): {r2_score(y_test, y_pred):.4f}")

# 4. Difference between Actual and Predicted
diff_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred, "Difference": y_test - y_pred})
print("\nDifference (Actual vs Predicted):\n", diff_df.head())

# 5. Visualization
plt.scatter(y_test, y_pred, color="blue")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.xlabel("Actual CO2")
plt.ylabel("Predicted CO2")
plt.title("Fuel Consumption - Multiple Linear Regression")
plt.savefig("06_fuel_consumption.png")
plt.show()
