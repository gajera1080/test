import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load data
df = pd.read_csv("data/auto.csv")
X = df[["horsepower"]]
y = df["mpg"]

# 2. Polynomial transformation (degree 2) and training
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression().fit(X_poly, y)
y_pred = model.predict(X_poly)

# 3. Accuracy using R2 score and MSE
print("Accuracy (R2 Score):", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))

# 4. Visualization
plt.scatter(X, y, color="blue", label="Actual")
# Sort for smooth line
sorted_indices = X["horsepower"].argsort()
plt.plot(X.iloc[sorted_indices], y_pred[sorted_indices], color="red", label="Poly Fit")
plt.title("Auto MPG vs Horsepower")
plt.legend()
plt.savefig("auto_polynomial_regression.png")
plt.show()
