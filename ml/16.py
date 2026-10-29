import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 1. Load Data
df = pd.read_csv("data/people.csv")
X = df[["Age", "Income"]]

# 2. Preprocess with Scaling (Age & Income have different scales)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 3. Apply K-Means (K = 3)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)
print("Clustered People:\n", df[["Name", "Age", "Income", "Cluster"]])

# 4. Visualization
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(df["Age"], df["Income"], c=df["Cluster"], cmap="rainbow", s=60)
plt.scatter(centroids[:, 0], centroids[:, 1], color="black", marker="X", s=200, label="Centroids")
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K-Means Clustering on People Dataset")
plt.legend()
plt.savefig("16_kmeans_people.png")
plt.show()
