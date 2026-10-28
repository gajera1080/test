import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load Data
df = pd.read_csv("data/Salary_Data.csv")
X = df[["YearsExperience"]]
y = df["Salary"]

# 2. Fit Linear Regression
model = LinearRegression().fit(X, y)

# 3. Predict for 5 years of experience
pred_5 = model.predict([[5.0]])[0]
print(f"Predicted Salary for 5 years of experience: Rs. {pred_5:.2f}")

# 4. Visualization
plt.scatter(X, y, color="blue", label="Actual")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.scatter([5.0], [pred_5], color="green", s=100, marker="*", label=f"5 yrs: {pred_5:.0f}")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.savefig("04_salary_prediction.png")
plt.show()
