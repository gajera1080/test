import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Load Dataset
df = pd.read_csv("data/insurance_data.csv")
x = df[["age"]]
y = df["bought_insurance"]

# 2. Train Model
model = LogisticRegression()
model.fit(x, y)

# 3. Predict for New Ages
new_age = [[20], [35], [50]]
y_pred = model.predict(new_age)
print("Predictions:", y_pred)

# 4. Predict Probability
print("Probabilities:")
print(model.predict_proba(new_age))

# 5. Visualization
x_line = np.linspace(x["age"].min(), x["age"].max(), 100).reshape(-1, 1)
y_prob = model.predict_proba(x_line)[:, 1]

plt.scatter(x, y, color="blue")
plt.plot(x_line, y_prob, color="red")
plt.xlabel("Age")
plt.ylabel("Probability of Buying Insurance")
plt.title("Logistic Regression - Insurance")
plt.show()
