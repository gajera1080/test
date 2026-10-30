import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# 1. Load Dataset
iris = load_iris()
x = iris.data
y = iris.target

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Train Model
model = SVC(kernel="linear")
model.fit(x_train, y_train)

# 4. Predict and Print Report
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. Predict New Flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
pred = model.predict(new_flower)
print("Predicted Species:", iris.target_names[pred[0]])

# 6. Visualization
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, display_labels=iris.target_names
)
plt.title("SVM - Iris Dataset")
plt.show()
