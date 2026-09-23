import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 6 pairs of (Title, X, y, New_X_to_predict)
cases = [
    ("Age vs Height", [2, 4, 6, 8, 10], [85, 105, 115, 130, 140], 5),
    ("Standard vs Percentage", [1, 2, 3, 4, 5], [90, 85, 80, 75, 70], 6),
    ("Height vs Shoe Size", [150, 160, 170, 180], [6, 7, 8, 9], 165),
    ("Experience vs Salary", [1, 2, 3, 4, 5], [30, 40, 50, 60, 70], 6),
    ("Hours vs Score", [1, 2, 3, 4, 5], [40, 50, 65, 75, 90], 3.5),
    ("Vehicle Age vs Price", [1, 2, 3, 4, 5], [20, 17, 14, 11, 8], 3)
]

plt.figure(figsize=(12, 8))

for i, (title, x, y, new_x) in enumerate(cases, 1):
    X = np.array(x).reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    pred_y = model.predict([[new_x]])[0]
    print(f"{i}. {title}: For X={new_x} -> Predicted Y={pred_y:.2f}")

    plt.subplot(2, 3, i)
    plt.scatter(x, y, color="blue")
    plt.plot(x, model.predict(X), color="red")
    plt.scatter([new_x], [pred_y], color="green")
    plt.title(title)

plt.tight_layout()
plt.savefig("linear_regression_6_cases.png")
plt.show()
