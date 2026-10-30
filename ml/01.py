import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load Dataset
iris = load_iris()
x = iris.data
y = iris.target

print("Features:", iris.feature_names)
print("Target:", iris.target_names)

# 2. Split Dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("X Train:", x_train.shape)
print("X Test:", x_test.shape)
print("Y Train:", y_train.shape)
print("Y Test:", y_test.shape)

# 3. Visualization
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="viridis")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset")
plt.show()
