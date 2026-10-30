import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load Dataset
df = pd.read_csv("data/Salary_Data.csv")
x = df[["YearsExperience"]]
y = df["Salary"]

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# 4. Predict Salary for 5 Years
y_pred = model.predict([[5]])
print("Predicted Salary for 5 years:", y_pred[0])

# 5. Visualization
plt.scatter(x, y, color="blue")
plt.plot(x, model.predict(x), color="red")
plt.scatter([5], y_pred, color="green", marker="*")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction")
plt.show()
