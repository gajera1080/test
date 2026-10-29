import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Load Data & Select Features
df = pd.read_csv("data/titanic.csv")
features = ["Pclass", "Sex", "Age", "Fare"]
X = df[features].copy()
y = df["Survived"]

# 2. Preprocessing (Handle missing values & encode Sex)
X["Age"] = X["Age"].fillna(X["Age"].median())
X["Sex"] = (X["Sex"] == "male").astype(int)

# 3. Train Decision Tree
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)

# 4. Evaluate
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# 5. Visualization
plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=features, class_names=["Died", "Survived"], filled=True)
plt.title("Decision Tree on Titanic Dataset")
plt.savefig("13_decision_tree_titanic.png")
plt.show()
