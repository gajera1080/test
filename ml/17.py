import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 1. Load Data (Petal Length & Petal Width: indices 2, 3)
iris = load_iris()
X = iris.data[:, 2:4]

# (i) Preprocessing with Scaling (Brings petal length and width to 0-1 range)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# (ii) Draw Elbow Plot to figure out optimal K (from K=1 to 10)
k_range = range(1, 11)
wcss = []
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(k_range, wcss, marker="o", color="blue")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method (Optimal K = 3)")

# Cluster plot for optimal K=3
km3 = KMeans(n_clusters=3, random_state=42)
y_clusters = km3.fit_predict(X_scaled)

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_clusters, cmap="viridis")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clusters (K = 3)")

plt.tight_layout()
plt.savefig("17_kmeans_iris_elbow.png")
plt.show()
