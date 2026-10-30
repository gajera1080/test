import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# 1. Load Dataset
df = pd.read_csv("data/heart.csv")
x = df.drop(columns="target")
y = df["target"]

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Apply Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 4. Train Model
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# 5. Predict and Check Accuracy
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 6. Visualization
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Heart Disease - Logistic Regression")
plt.show()
