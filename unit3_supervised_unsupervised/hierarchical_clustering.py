"""
================================================================================
UNIT 3.6.3: AGGLOMERATIVE HIERARCHICAL CLUSTERING & DENDROGRAMS
================================================================================
Syllabus Topics Covered:
- 3.6.3 Hierarchical Clustering: Agglomerative (Bottom-Up) vs Divisive (Top-Down),
  Linkage Criteria (Ward's Minimum Variance, Complete, Single, Average),
  Dendrogram Construction, Euclidean Distance Matrix, Distance Threshold Cut.

Journal Questions Addressed:
- Bullet 10: Agglomerative Hierarchical Clustering on Shopping dataset
  (hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv)
  Plot Dendrogram and 2D Scatter plot of clusters.
- University Variations: Linkage comparison, cophenetic correlation coefficient.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_clustering_metrics
from utils.data_loader import load_dataset


def run_bullet10_hierarchical_shopping(n_clusters=5, interactive=True):
    """
    Journal Question Bullet 10:
    Write a Python program to implement Agglomerative Hierarchical Clustering
    on below dataset (hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv)
    and plot Dendrogram and scatter plot too.
    """
    print("\n" + "=" * 70)
    print(" BULLET 10: AGGLOMERATIVE HIERARCHICAL CLUSTERING ON SHOPPING DATA")
    print("=" * 70)

    # Load dataset
    df = load_dataset("hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv")
    print("\nShopping Dataset Preview (First 5 Rows):")
    print(df.head())

    # Extract features: Annual Income (k$) and Spending Score (1-100)
    # Typically columns at index 3 and 4
    features = ["Annual Income (k$)", "Spending Score (1-100)"]
    X = df[features].values

    # Step 1: Dendrogram Computation using Ward Linkage (minimizes variance within clusters)
    print("\n Computing Linkage Matrix (Ward's Method, Euclidean Metric)...")
    linkage_matrix = sch.linkage(X, method="ward")

    # Step 2: Fit Agglomerative Clustering
    model = AgglomerativeClustering(n_clusters=n_clusters, metric="euclidean", linkage="ward")
    df["Cluster"] = model.fit_predict(X)

    print(f"\n Clustering Complete into {n_clusters} Distinct Customer Segments:")
    cluster_profiles = df.groupby("Cluster")[features].mean().round(2)
    cluster_profiles["Member Count"] = df["Cluster"].value_counts()
    print(cluster_profiles)

    # Evaluate unsupervised clustering metrics
    print_clustering_metrics(X, df["Cluster"], title="Shopping Agglomerative Clustering Metrics")

    # Step 3: Visualization (2-Panel Plot: Dendrogram & Clustered Scatter Plot)
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Panel 1: Dendrogram
    dendro = sch.dendrogram(linkage_matrix, ax=axes[0], truncate_mode="lastp", p=30, show_leaf_counts=True)
    # Draw horizontal threshold cut line
    threshold_val = 150.0  # standard threshold cutting into 5 clusters
    axes[0].axhline(y=threshold_val, color="red", linestyle="--", linewidth=2, label=f"Threshold Cut = {threshold_val} ({n_clusters} Clusters)")
    axes[0].set_title("Hierarchical Clustering Dendrogram (Ward Linkage)")
    axes[0].set_xlabel("Sample / Cluster Size")
    axes[0].set_ylabel("Euclidean Distance")
    axes[0].legend(loc="upper right")

    # Panel 2: Scatter Plot of Customer Segments
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    cluster_names = [
        "Careful (Low Income, Low Spend)",
        "Standard (Mid Income, Mid Spend)",
        "Target / High Value (High Income, High Spend)",
        "Careless (Low Income, High Spend)",
        "Sensible (High Income, Low Spend)"
    ]

    for c_id in range(n_clusters):
        c_data = df[df["Cluster"] == c_id]
        c_label = cluster_names[c_id] if c_id < len(cluster_names) else f"Cluster {c_id}"
        axes[1].scatter(
            c_data["Annual Income (k$)"],
            c_data["Spending Score (1-100)"],
            s=65,
            color=colors[c_id % len(colors)],
            label=f"C{c_id}: {c_label}",
            edgecolors="k",
            alpha=0.85
        )

    axes[1].set_title(f"Agglomerative Clustering: Shopping Customer Segments (n={n_clusters})")
    axes[1].set_xlabel("Annual Income (k$)")
    axes[1].set_ylabel("Spending Score (1-100)")
    axes[1].legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=9)

    save_and_show(fig, filename="unit3_hierarchical_shopping_dendrogram.png", interactive=interactive)
    return model, linkage_matrix


if __name__ == "__main__":
    run_bullet10_hierarchical_shopping(n_clusters=5, interactive=False)
