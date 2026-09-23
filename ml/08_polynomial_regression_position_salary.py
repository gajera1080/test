import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Load data
df = pd.read_csv("data/position_salary.csv")
X = df[["Level"]]
y = df["Salary"]

# 2. Transform to Polynomial features (degree 4) and train model
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

model = LinearRegression().fit(X_poly, y)

# 3. Predict value (e.g. Level 6.5)
pred = model.predict(poly.transform([[6.5]]))[0]
print(f"Predicted Salary for Level 6.5: {pred:.2f}")

# 4. Visualization
plt.scatter(X, y, color="red", label="Actual")
plt.plot(X, model.predict(X_poly), color="blue", label="Polynomial Fit")
plt.scatter([6.5], [pred], color="green", s=100, label="Pred 6.5")
plt.title("Position vs Salary (Polynomial Regression)")
plt.legend()
plt.savefig("position_salary_polynomial_regression.png")
plt.show()
