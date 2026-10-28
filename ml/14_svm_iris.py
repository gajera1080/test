from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 1. Load Data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train SVM Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = SVC(kernel="linear").fit(X_train, y_train)

# 3. Print Precision, Recall, F1-Score, and Support for each Iris class
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# 4. Predict species of new unseen Iris flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
pred_species = iris.target_names[model.predict(new_flower)[0]]
print(f"Predicted species for {new_flower}: {pred_species}")

# 5. Visualization
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, display_labels=iris.target_names, cmap="Blues")
plt.title("SVM on Iris Dataset")
plt.savefig("14_svm_iris.png")
plt.show()
