import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

# 1. Load Dataset
iris = load_iris()
x = iris.data
y = iris.target

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Apply Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 4. Train KNN Model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

# 5. Predict and Evaluate
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 6. Predict New Flower
new_flower = scaler.transform([[6.0, 2.7, 4.2, 1.3]])
pred = model.predict(new_flower)
print("Predicted Species:", iris.target_names[pred[0]])

# 7. Visualization
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, display_labels=iris.target_names
)
plt.title("KNN - Iris Dataset")
plt.show()
