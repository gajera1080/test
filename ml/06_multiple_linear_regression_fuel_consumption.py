import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load data
df = pd.read_csv("data/FuelConsumption.csv")
X = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]]
y = df["CO2EMISSIONS"]

# 2. Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

# 3. Intercept, Coefficients & Accuracy (R2)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
y_pred = model.predict(X_test)
print("Accuracy (R2 Score):", r2_score(y_test, y_pred))

# 4. Difference between Actual and Predicted
diff = pd.DataFrame({"Actual": y_test, "Predicted": y_pred, "Difference": y_test - y_pred})
print("\nActual vs Predicted Difference:\n", diff.head())

# 5. Visualization
plt.scatter(y_test, y_pred, color="blue")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.title("Fuel Consumption (Actual vs Predicted)")
plt.savefig("fuel_consumption_regression.png")
plt.show()
