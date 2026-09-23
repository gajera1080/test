import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Load data
df = pd.read_csv("data/insurance_data.csv")
X = df[["age"]]
y = df["bought_insurance"]

# 2. Train Logistic Regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression().fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

# 3. Visualization (Sigmoid curve)
plt.scatter(X, y, color="blue", label="Actual (0/1)")
age_range = np.linspace(X.min().iloc[0], X.max().iloc[0], 100).reshape(-1, 1)
plt.plot(age_range, model.predict_proba(age_range)[:, 1], color="red", label="Probability Curve")
plt.title("Insurance Purchase (Logistic Regression)")
plt.xlabel("Age")
plt.ylabel("Probability")
plt.legend()
plt.savefig("insurance_logistic_regression.png")
plt.show()
