import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

# 1. Load Data
df = pd.read_csv("data/heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

# 2. Scale Features & Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression().fit(X_train_s, y_train)

# 3. Predict & Print Metrics
y_pred = model.predict(X_test_s)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 4. Visualization (Confusion Matrix Display)
ConfusionMatrixDisplay.from_estimator(model, X_test_s, y_test, cmap="Blues")
plt.title("Heart Disease - Logistic Regression Confusion Matrix")
plt.savefig("11_heart_logistic.png")
plt.show()
