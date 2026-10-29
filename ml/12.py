import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# 1. Load Data
df = pd.read_csv("data/salaries.csv")

# 2. Encode Categorical Features
le = LabelEncoder()
df["company_n"] = le.fit_transform(df["company"])
df["job_n"] = le.fit_transform(df["job"])
df["degree_n"] = le.fit_transform(df["degree"])

X = df[["company_n", "job_n", "degree_n"]]
y = df["salary_more_then_100k"]

# 3. Train Decision Tree
model = DecisionTreeClassifier(random_state=42).fit(X, y)

# 4. Predict for sample employee: company=google(2), job=programmer(1), degree=masters(1)
pred = model.predict([[2, 1, 1]])[0]
print("Predicted Salary > 100k (1=Yes, 0=No):", pred)

# 5. Visualization (Plot Tree)
plot_tree(model, feature_names=list(X.columns), class_names=["<=100k", ">100k"], filled=True)
plt.title("Decision Tree on Salaries Dataset")
plt.savefig("12_decision_tree_salaries.png")
plt.show()
