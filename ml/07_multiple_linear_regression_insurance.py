import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load data & encode binary columns
df = pd.read_csv("data/insaurance_Practical_3.csv")
df["smoker"] = df["smoker"].map({"yes": 1, "no": 0})
df["sex"] = df["sex"].map({"female": 1, "male": 0})

X = df[["age", "bmi", "children", "smoker"]]
y = df["charges"]

# 2. Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

# 3. Print Intercept, Coefficients, and R2 score
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# 4. Visualization
plt.scatter(y_test, y_pred, color="purple")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.title("Insurance Charges (Actual vs Predicted)")
plt.savefig("insurance_regression.png")
plt.show()
