import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 1. Load Dataset
df = pd.read_csv("data/people.csv")
x = df[["Age", "Income"]]

# 2. Apply Feature Scaling
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

# 3. Apply K-Means Clustering
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(x_scaled)
print(df[["Name", "Age", "Income", "Cluster"]])

# 4. Visualization
centroids = scaler.inverse_transform(model.cluster_centers_)
plt.scatter(df["Age"], df["Income"], c=df["Cluster"], cmap="rainbow")
plt.scatter(centroids[:, 0], centroids[:, 1], color="black", marker="X")
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K-Means Clustering - People")
plt.show()
