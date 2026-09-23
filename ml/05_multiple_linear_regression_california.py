import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Load dataset
housing = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=42)

# 2. Train Multiple Linear Regression
model = LinearRegression().fit(X_train, y_train)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 3. Predict & Visualize Actual vs Predicted
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred, alpha=0.3, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.title("California Housing (Actual vs Predicted)")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.savefig("california_housing_regression.png")
plt.show()
