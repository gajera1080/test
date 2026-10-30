import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
df = pd.read_csv("data/titanic.csv")
x = df[["Pclass", "Sex", "Age", "Fare"]].copy()
y = df["Survived"]

# 2. Preprocessing
x["Age"] = x["Age"].fillna(x["Age"].median())
x["Sex"] = (x["Sex"] == "male").astype(int)

# 3. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 4. Train Model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(x_train, y_train)

# 5. Predict and Evaluate
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6. Visualization
plot_tree(model, feature_names=x.columns, class_names=["Died", "Survived"], filled=True)
plt.title("Decision Tree - Titanic")
plt.show()
