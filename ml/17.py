import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 1. Load Dataset
iris = load_iris()
x = iris.data[:, 2:4]

# 2. Apply Feature Scaling
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# 3. Find WCSS for Different K Values
wcss = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(x_scaled)
    wcss.append(model.inertia_)

# 4. Apply K-Means with K = 3
model = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = model.fit_predict(x_scaled)

# 5. Visualization
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")

plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=y_pred, cmap="viridis")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("K-Means Clusters")

plt.tight_layout()
plt.show()
