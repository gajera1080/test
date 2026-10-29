import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load Dataset
iris = load_iris()
X, y = iris.data, iris.target

print("Features:", iris.feature_names)
print("Target:", iris.target_names)

# 2. Split Dataset (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Train shapes: X={X_train.shape}, y={y_train.shape}")
print(f"Test shapes:  X={X_test.shape}, y={y_test.shape}")

# 3. Visualization
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors="k")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Dataset - Features and Target")
plt.savefig("01_iris_dataset.png")
plt.show()
