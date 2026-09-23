from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load Iris Dataset
iris = load_iris()
X, y = iris.data, iris.target

print("Features:\n", iris.feature_names)
print("Target:\n", iris.target_names)

# 2. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Train shapes: X={X_train.shape}, y={y_train.shape}")
print(f"Test shapes:  X={X_test.shape}, y={y_test.shape}")
