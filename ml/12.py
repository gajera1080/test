import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. Load Dataset
df = pd.read_csv("data/salaries.csv")

# 2. Convert Categorical Data into Numeric Data
le = LabelEncoder()
df["company"] = le.fit_transform(df["company"])
df["job"] = le.fit_transform(df["job"])
df["degree"] = le.fit_transform(df["degree"])

x = df[["company", "job", "degree"]]
y = df["salary_more_then_100k"]

# 3. Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(x, y)

# 4. Predict
y_pred = model.predict([[2, 1, 1]])
print("Predicted Salary More Than 100k:", y_pred[0])

# 5. Visualization
plot_tree(model, feature_names=x.columns, filled=True)
plt.title("Decision Tree - Salaries")
plt.show()
