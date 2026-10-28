"""
================================================================================
UNIT 3.6.1 - 3.6.2: K-MEANS CLUSTERING
================================================================================
Syllabus Topics Covered:
- 3.6.1 Clustering Strategies and Real-World Applications (Customer segmentation, anomaly detection)
- 3.6.2 Concepts of Clustering, Distance Metrics, K-Means Algorithm Working:
        1. Initialize K centroids randomly
        2. Assign each point to the closest centroid (Euclidean distance)
        3. Recalculate centroids as the mean of assigned points
        4. Repeat until convergence (Inertia / WCSS stabilizes)

Journal Questions Addressed:
- Bullet 8: K-Means Clustering on people.csv (Age vs Income) to group people into clusters.
- Bullet 9: K-Means Clustering on Iris dataset using Petal Length and Petal Width:
            (i) Preprocessing analysis (Evaluate if feature scaling improves cluster discovery)
            (ii) Draw Elbow Plot to determine the optimal value of K.
- University Variations: Silhouette analysis across K, centroid coordinates printout.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.datasets import load_iris

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_clustering_metrics
from utils.data_loader import load_dataset


def run_bullet8_kmeans_people(k=3, interactive=True):
    """
    Journal Question Bullet 8:
    Write a Python program to implement K-Means Clustering for grouping people
    based on features like Age and Income using a locally created CSV file
    (people.csv with columns: Name, Age, Income).
    """
    print("\n" + "=" * 70)
    print(" BULLET 8: K-MEANS CLUSTERING ON PEOPLE DATASET (AGE & INCOME)")
    print("=" * 70)

    df = load_dataset("people.csv")
    print("\nPeople Dataset Preview:")
    print(df.head())

    X = df[["Age", "Income"]].values

    # Feature Scaling is critical when Age (~20-50) and Income (~40k-120k) have disparate units!
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Fit K-Means
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Inverse transform centroids back to original units for interpretation
    centroids_orig = scaler.inverse_transform(kmeans.cluster_centers_)

    print(f"\n Identified {k} Customer Clusters:")
    for c_id in range(k):
        sub = df[df["Cluster"] == c_id]
        print(f" Cluster {c_id} (Centroid: Age={centroids_orig[c_id, 0]:.1f}, Income=${centroids_orig[c_id, 1]:,.0f}):")
        print(f"   Members ({len(sub)}): {', '.join(sub['Name'].values)}")

    print_clustering_metrics(X_scaled, df["Cluster"], title="People K-Means Clustering Metrics")

    # Visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ["#1f77b4", "#2ca02c", "#d62728", "#9467bd"]
    for c_id in range(k):
        cluster_pts = df[df["Cluster"] == c_id]
        ax.scatter(cluster_pts["Age"], cluster_pts["Income"], s=80, color=colors[c_id % len(colors)], label=f"Cluster {c_id}", edgecolors="k", zorder=3)

    # Plot Centroids
    ax.scatter(centroids_orig[:, 0], centroids_orig[:, 1], color="black", marker="X", s=200, label="Centroids", zorder=5)

    ax.set_title(f"K-Means Clustering of People (K={k})")
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Income ($)")
    ax.legend()

    save_and_show(fig, filename="unit3_kmeans_bullet8_people.png", interactive=interactive)
    return kmeans, df


def run_bullet9_kmeans_iris_elbow(interactive=True):
    """
    Journal Question Bullet 9:
    Write a Python program to implement K-Means Clustering on the Iris dataset
    to group the flowers using petal length and petal width.
    (i) Figure out if any preprocessing such as scaling would help here
    (ii) Draw elbow plot and from that figure out optimal value of K
    """
    print("\n" + "=" * 70)
    print(" BULLET 9: K-MEANS CLUSTERING ON IRIS (PETAL LENGTH & WIDTH)")
    print("=" * 70)

    iris = load_iris()
    # Extract Petal Length (index 2) and Petal Width (index 3)
    X = iris.data[:, 2:4]
    feature_names = ["Petal Length (cm)", "Petal Width (cm)"]

    print("""
----------------------------------------------------------------------
(i) PREPROCESSING ANALYSIS: DOES FEATURE SCALING HELP HERE?
----------------------------------------------------------------------
Both features (Petal Length and Petal Width) are already measured in the
exact same physical units (centimeters, cm) with similar numerical ranges
(length: 1.0 to 6.9 cm, width: 0.1 to 2.5 cm).
However, applying MinMaxScaler or StandardScaler normalizes variance across
axes. Let us empirically compare clustering performance with and without scaling!
""")

    # 1. Without Scaling
    km_raw = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)
    raw_inertia = km_raw.inertia_

    # 2. With MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    km_scaled = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X_scaled)

    print(f" - Raw Data Inertia (WCSS)        : {raw_inertia:.2f}")
    print(f" - Scaled Data Inertia (WCSS)     : {km_scaled.inertia_:.4f}")
    print(" Conclusion: Scaling balances the variance contribution of width relative to length.")

    # (ii) Draw Elbow Plot to find optimal K (WCSS vs K from 1 to 10)
    print("\n----------------------------------------------------------------------")
    print("(ii) COMPUTING ELBOW METHOD (K = 1 to 10)")
    print("----------------------------------------------------------------------")

    k_range = range(1, 11)
    wcss = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        wcss.append(km.inertia_)
        print(f" K={k:<2} -> WCSS (Inertia) = {km.inertia_:.4f}")

    print("\n >> The Elbow bend visibly occurs at K = 3, which matches the 3 true Iris species! <<")

    # Metrics for K=3
    print_clustering_metrics(X_scaled, km_scaled.labels_, title="Iris Petal K-Means (K=3) Clustering Metrics")

    # Visualizations: 2-Panel Plot (Elbow Curve & Clustered Scatter Plot)
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: Elbow Plot
    axes[0].plot(k_range, wcss, marker="o", color="#1f77b4", linewidth=2.5, markersize=8)
    axes[0].scatter([3], [wcss[2]], color="#d62728", s=160, zorder=5, label="Optimal Elbow (K = 3)")
    axes[0].annotate("Elbow Point (K = 3)", xy=(3, wcss[2]), xytext=(4, wcss[2] + 2),
                     arrowprops=dict(facecolor="black", shrink=0.05, width=1.5, headwidth=8),
                     fontsize=11, fontweight="bold")
    axes[0].set_title("Elbow Method: WCSS vs Number of Clusters (K)")
    axes[0].set_xlabel("Number of Clusters (K)")
    axes[0].set_ylabel("Within-Cluster Sum of Squares (Inertia)")
    axes[0].set_xticks(list(k_range))
    axes[0].legend()

    # Panel 2: Clusters with Centroids
    labels = km_scaled.labels_
    centroids = scaler.inverse_transform(km_scaled.cluster_centers_)

    colors = ["#1f77b4", "#2ca02c", "#ff7f0e"]
    for c_id in range(3):
        axes[1].scatter(X[labels == c_id, 0], X[labels == c_id, 1],
                        color=colors[c_id], label=f"Cluster {c_id}", alpha=0.8, edgecolors="k", s=45)

    axes[1].scatter(centroids[:, 0], centroids[:, 1], color="red", marker="X", s=200, label="Cluster Centroids", zorder=6)
    axes[1].set_title("K-Means Clusters (Petal Length vs Petal Width)")
    axes[1].set_xlabel(feature_names[0])
    axes[1].set_ylabel(feature_names[1])
    axes[1].legend()

    save_and_show(fig, filename="unit3_kmeans_bullet9_iris_elbow.png", interactive=interactive)
    return km_scaled, wcss


if __name__ == "__main__":
    run_bullet8_kmeans_people(k=3, interactive=False)
    run_bullet9_kmeans_iris_elbow(interactive=False)
