import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# 1. Load Dataset
df = pd.read_csv("data/shopping-data.csv")
x = df.iloc[:, [3, 4]].values

# 2. Draw Dendrogram
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sch.dendrogram(sch.linkage(x, method="ward"))
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.title("Dendrogram")

# 3. Apply Hierarchical Clustering
model = AgglomerativeClustering(n_clusters=5, linkage="ward")
y_pred = model.fit_predict(x)

# 4. Visualization
plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=y_pred, cmap="rainbow")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Hierarchical Clustering")

plt.tight_layout()
plt.show()
