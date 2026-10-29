import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Load Data
df = pd.read_csv("data/insurance_data.csv")
X = df[["age"]]
y = df["bought_insurance"]

# 2. Train Logistic Regression Model
model = LogisticRegression().fit(X, y)

# 3. Predict Probability for New Ages
test_ages = [20, 35, 50]
for age in test_ages:
    prob = model.predict_proba([[age]])[0][1]
    print(f"Age {age}: Probability of buying insurance = {prob:.2f}")

# 4. Visualization (Sigmoid Curve)
X_test = np.linspace(float(X["age"].min()) - 5, float(X["age"].max()) + 5, 100).reshape(-1, 1)
y_prob = model.predict_proba(X_test)[:, 1]

plt.scatter(X, y, color="red", marker="+", s=80, label="Actual Data")
plt.plot(X_test, y_prob, color="blue", label="Sigmoid Curve")
plt.axhline(0.5, color="gray", linestyle="--", label="Threshold (0.5)")
plt.xlabel("Age")
plt.ylabel("Bought Insurance Probability")
plt.title("Insurance Purchase - Logistic Regression")
plt.legend()
plt.savefig("10_insurance_logistic.png")
plt.show()
