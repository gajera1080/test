import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
df = pd.read_csv("data/auto.csv")
df = df.sort_values("horsepower")
x = df[["horsepower"]]
y = df["mpg"]

# 2. Convert X into Polynomial Features
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# 3. Train Model
model = LinearRegression()
model.fit(x_poly, y)

# 4. Predict and Evaluate
y_pred = model.predict(x_poly)
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# 5. Visualization
plt.scatter(x, y, color="blue")
plt.plot(x, y_pred, color="red")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title("Polynomial Regression - Auto Dataset")
plt.show()
