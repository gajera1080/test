import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. Load Data and Encode Categorical Columns
df = pd.read_csv("data/insaurance_Practical_3.csv")
df = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

X = df.drop("charges", axis=1)
y = df["charges"]

# 2. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

# 3. Intercept, Coefficients, and R2 Score
print("Intercept:", model.intercept_)
print("Coefficients:\n", dict(zip(X.columns, model.coef_)))
y_pred = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")

# 4. Visualization
plt.scatter(y_test, y_pred, color="purple", alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Insurance Charges - Multiple Linear Regression")
plt.savefig("07_insurance_charges.png")
plt.show()
