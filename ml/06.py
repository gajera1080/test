import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load Dataset
df = pd.read_csv("data/FuelConsumption.csv")
x = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]]
y = df["CO2EMISSIONS"]

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# 4. Print Intercept and Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 5. Predict and Check Accuracy
y_pred = model.predict(x_test)
print("R2 Score:", r2_score(y_test, y_pred))

# 6. Difference between Actual and Predicted
result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred,
    "Difference": y_test - y_pred
})
print(result.head())

# 7. Visualization
plt.scatter(y_test, y_pred, color="blue")
plt.xlabel("Actual CO2 Emissions")
plt.ylabel("Predicted CO2 Emissions")
plt.title("Fuel Consumption - Multiple Linear Regression")
plt.show()
