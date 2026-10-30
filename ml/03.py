import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Create Datasets
cases = [
    ("Age vs Height", [2, 4, 6, 8, 10], [85, 105, 115, 130, 140], 5),
    ("Standard vs Percentage", [1, 2, 3, 4, 5], [90, 85, 80, 75, 70], 6),
    ("Height vs Shoe Size", [150, 160, 170, 180], [6, 7, 8, 9], 165),
    ("Experience vs Salary", [1, 2, 3, 4, 5], [30, 40, 50, 60, 70], 6),
    ("Hours vs Score", [1, 2, 3, 4, 5], [40, 50, 65, 75, 90], 3.5),
    ("Vehicle Age vs Price", [1, 2, 3, 4, 5], [20, 17, 14, 11, 8], 3)
]

# 2. Train, Predict and Visualize
plt.figure(figsize=(12, 8))
for i, (title, x, y, new_x) in enumerate(cases, 1):
    x = np.array(x).reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)

    y_pred = model.predict([[new_x]])
    print(title, "Prediction:", y_pred[0])

    plt.subplot(2, 3, i)
    plt.scatter(x, y, color="blue")
    plt.plot(x, model.predict(x), color="red")
    plt.scatter([new_x], y_pred, color="green", marker="*")
    plt.title(title)

plt.tight_layout()
plt.show()
