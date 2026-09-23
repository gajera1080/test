import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load dataset
df = pd.read_csv("data/Salary_Data.csv")
X = df[["YearsExperience"]]
y = df["Salary"]

# 2. Train model & Predict for 5 years experience
model = LinearRegression().fit(X, y)
pred_salary = model.predict([[5]])[0]
print(f"Predicted Salary for 5 years experience: {pred_salary:.2f}")

# 3. Visualization
plt.scatter(X, y, color="blue", label="Actual")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.scatter([5], [pred_salary], color="green", s=100, label="5 yrs prediction")
plt.title("Salary vs Experience")
plt.legend()
plt.savefig("salary_prediction_5_years.png")
plt.show()
