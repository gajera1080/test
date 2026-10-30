import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Load Dataset
df = pd.read_csv("data/position_salary.csv")
x = df[["Level"]]
y = df["Salary"]

# 2. Convert X into Polynomial Features
poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(x)

# 3. Train Model
model = LinearRegression()
model.fit(x_poly, y)

# 4. Predict Salary
y_pred = model.predict(poly.transform([[6.5]]))
print("Predicted Salary for Level 6.5:", y_pred[0])

# 5. Visualization
x_grid = np.arange(x["Level"].min(), x["Level"].max(), 0.1).reshape(-1, 1)
plt.scatter(x, y, color="blue")
plt.plot(x_grid, model.predict(poly.transform(x_grid)), color="red")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Position Salary - Polynomial Regression")
plt.show()
