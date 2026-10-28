import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# 1. Load Data (Annual Income vs Spending Score)
df = pd.read_csv("data/shopping-data.csv")
X = df.iloc[:, [3, 4]].values

# 2. Plot Dendrogram using Ward Linkage
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrogram (Ward's Method)")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")

# 3. Fit Agglomerative Clustering (n_clusters = 5)
hc = AgglomerativeClustering(n_clusters=5, linkage="ward")
y_hc = hc.fit_predict(X)

# 4. Scatter Plot of Clusters
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_hc, cmap="rainbow", s=50)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Agglomerative Clusters (K = 5)")

plt.tight_layout()
plt.savefig("18_hierarchical_shopping.png")
plt.show()
