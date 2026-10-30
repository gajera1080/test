import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
diabetes = load_diabetes()
x = diabetes.data[:, [2]]
y = diabetes.target

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# 4. Predict and Evaluate
y_pred = model.predict(x_test)
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 5. Visualization
plt.scatter(x_test, y_test, color="blue")
plt.plot(x_test, y_pred, color="red")
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Simple Linear Regression - Diabetes")
plt.show()
