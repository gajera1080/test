from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 1. Load Data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split and Apply Feature Scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# 3. Train KNN Classifier (K = 5)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)

# 4. Accuracy & Detailed Classification Report for all 3 classes
y_pred = knn.predict(X_test_s)
print("KNN Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. Predict species of new Iris flower
new_flower = scaler.transform([[6.0, 2.7, 4.2, 1.3]])
pred_species = iris.target_names[knn.predict(new_flower)[0]]
print(f"Predicted species for sample: {pred_species}")

# 6. Visualization
ConfusionMatrixDisplay.from_estimator(knn, X_test_s, y_test, display_labels=iris.target_names, cmap="Greens")
plt.title("KNN on Iris Dataset (With Scaling)")
plt.savefig("15_knn_iris.png")
plt.show()
