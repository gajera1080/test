import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Load Data
housing = fetch_california_housing(as_frame=True)
X, y = housing.data, housing.target

# 2. Split and Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

# 3. Print Intercept and Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:\n", dict(zip(housing.feature_names, model.coef_)))

# 4. Visualization (Actual vs Predicted)
y_pred = model.predict(X_test)
plt.scatter(y_test[:200], y_pred[:200], alpha=0.5, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", linewidth=2)
plt.xlabel("Actual Value")
plt.ylabel("Predicted Value")
plt.title("California Housing - Multiple Linear Regression")
plt.savefig("05_california_regression.png")
plt.show()
