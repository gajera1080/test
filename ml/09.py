import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Data
df = pd.read_csv("data/auto.csv")
X = df[["horsepower"]]
y = df["mpg"]

# 2. Fit Polynomial Features (Degree = 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)

# 3. Accuracy Metrics (R2 and MSE)
y_pred = model.predict(X_poly)
print("Mean Squared Error (MSE):", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# 4. Visualization
X_plot = np.linspace(float(X["horsepower"].min()), float(X["horsepower"].max()), 100).reshape(-1, 1)
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X_plot, model.predict(poly.transform(X_plot)), color="red", label="Polynomial Fit (deg 2)")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title("Auto Dataset - Polynomial Regression")
plt.legend()
plt.savefig("09_auto_poly.png")
plt.show()
