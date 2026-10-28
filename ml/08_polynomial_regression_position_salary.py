import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Load Data
df = pd.read_csv("data/position_salary.csv")
X = df[["Level"]]
y = df["Salary"]

# 2. Transform Features (Degree = 4) and Fit Model
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)

# 3. Predict for Level 6.5
pred_65 = model.predict(poly.transform([[6.5]]))[0]
print(f"Predicted Salary for Level 6.5: ${pred_65:,.2f}")

# 4. Visualization (Smooth Curve)
X_grid = np.arange(float(X["Level"].min()), float(X["Level"].max()) + 0.1, 0.1).reshape(-1, 1)
plt.scatter(X, y, color="red", label="Actual")
plt.plot(X_grid, model.predict(poly.transform(X_grid)), color="blue", label="Polynomial Fit (deg 4)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Position Salary - Polynomial Regression")
plt.legend()
plt.savefig("08_position_salary_poly.png")
plt.show()
