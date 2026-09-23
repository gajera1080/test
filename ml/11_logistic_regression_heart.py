import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. Load data
df = pd.read_csv("data/heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

# 2. Train Logistic Regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

# 3. Confusion Matrix Visualization
cm = confusion_matrix(y_test, model.predict(X_test))
ConfusionMatrixDisplay(cm).plot(cmap="Blues")
plt.title("Heart Disease (Confusion Matrix)")
plt.savefig("heart_disease_logistic_regression.png")
plt.show()
