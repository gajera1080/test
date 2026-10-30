import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Load Dataset
housing = fetch_california_housing()
x = housing.data
y = housing.target

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

# 5. Predict
y_pred = model.predict(x_test)

# 6. Visualization
plt.scatter(y_test, y_pred, color="blue")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("California Housing - Multiple Linear Regression")
plt.show()
