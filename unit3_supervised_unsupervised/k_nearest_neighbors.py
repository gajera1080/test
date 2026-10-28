"""
================================================================================
UNIT 3.5: K-NEAREST NEIGHBORS (KNN) CLASSIFIER
================================================================================
Syllabus Topics Covered:
- 3.5 Supervised Learning with KNN: Concepts, Distance Metrics (Euclidean, Manhattan),
  Working of KNN (Lazy Learning, Majority Voting), Impact of K, Feature Scaling.

Journal Questions Addressed:
- Bullet 5: Classification on Iris dataset using KNN with accuracy score.
- Bullet 6: Classification on Iris using KNN WITH Feature Scaling (StandardScaler),
            displaying accuracy and detailed classification report for all three classes.
- Bullet 7: KNN Classifier for predicting species of new Iris flowers.
- University Variations: Optimal K selection (Elbow / Error rate curve across K=1..30).
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_classification_metrics


def run_bullet5_knn_iris_accuracy(n_neighbors=5):
    """
    Journal Question Bullet 5:
    Write a Python program to perform classification on the Iris dataset
    using the K-Nearest Neighbors (KNN) algorithm.
    The program should display the accuracy of the KNN model for classifying the Iris dataset.
    """
    print("\n" + "=" * 70)
    print(f" BULLET 5: KNN CLASSIFICATION ACCURACY ON IRIS (K={n_neighbors})")
    print("=" * 70)

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )

    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)

    accuracy = knn.score(X_test, y_test)
    print(f"\n >>> KNN (K={n_neighbors}) Test Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%) <<<\n")
    return knn, accuracy


def run_bullet6_knn_with_scaling(n_neighbors=5, interactive=True):
    """
    Journal Question Bullet 6:
    Write a Python program to perform classification on the Iris dataset
    using the K-Nearest Neighbors (KNN) algorithm with feature scaling.
    The program should display the accuracy of the KNN model and a detailed
    classification report for all three Iris classes (setosa, versicolor, virginica).
    """
    print("\n" + "=" * 70)
    print(" BULLET 6: KNN CLASSIFIER WITH FEATURE SCALING & FULL REPORT")
    print("=" * 70)

    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = list(iris.target_names)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 1. Without Scaling
    knn_raw = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_raw.fit(X_train, y_train)
    acc_raw = knn_raw.score(X_test, y_test)

    # 2. With Feature Scaling (StandardScaler: mean=0, std=1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    knn_scaled = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_scaled.fit(X_train_scaled, y_train)
    y_pred_scaled = knn_scaled.predict(X_test_scaled)
    acc_scaled = knn_scaled.score(X_test_scaled, y_test)

    print(f"\n [Comparison: Impact of Feature Scaling]")
    print(f" - Accuracy WITHOUT Feature Scaling : {acc_raw:.4f} ({acc_raw * 100:.2f}%)")
    print(f" - Accuracy WITH Feature Scaling    : {acc_scaled:.4f} ({acc_scaled * 100:.2f}%)")

    metrics = print_classification_metrics(
        y_test, y_pred_scaled, target_names=target_names, title="Iris KNN (Scaled) Classification Report"
    )

    # Optimal K exploration (University Variation)
    k_range = range(1, 31)
    error_rates = []
    for k in k_range:
        k_clf = KNeighborsClassifier(n_neighbors=k).fit(X_train_scaled, y_train)
        error_rates.append(1.0 - k_clf.score(X_test_scaled, y_test))

    # Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Error Rate vs K Value
    axes[0].plot(k_range, error_rates, color="#d62728", linestyle="dashed", marker="o", markerfacecolor="#1f77b4", markersize=7)
    best_k = list(k_range)[np.argmin(error_rates)]
    axes[0].axvline(best_k, color="green", linestyle=":", label=f"Optimal K = {best_k}")
    axes[0].set_title("KNN Parameter Tuning: Error Rate vs K Value")
    axes[0].set_xlabel("Number of Neighbors (K)")
    axes[0].set_ylabel("Classification Error Rate")
    axes[0].legend()

    # Plot 2: Accuracy Comparison
    axes[1].bar(["Without Scaling", "With Scaling"], [acc_raw * 100, acc_scaled * 100], color=["#ff7f0e", "#2ca02c"], edgecolor="black", width=0.5)
    axes[1].set_ylabel("Accuracy (%)")
    axes[1].set_ylim(80, 105)
    axes[1].set_title(f"Accuracy Comparison (K={n_neighbors})")
    for i, v in enumerate([acc_raw * 100, acc_scaled * 100]):
        axes[1].text(i, v + 0.5, f"{v:.1f}%", ha="center", fontweight="bold")

    save_and_show(fig, filename="unit3_knn_iris_evaluation.png", interactive=interactive)
    return knn_scaled, scaler, metrics


def run_bullet7_knn_predict_species(new_measurements=None, knn_model=None, scaler=None):
    """
    Journal Question Bullet 7:
    Write a Python program to implement a K-Nearest Neighbors (KNN)
    Classifier for predicting the species of Iris flowers using the Iris dataset.
    """
    print("\n" + "=" * 70)
    print(" BULLET 7: PREDICTING IRIS SPECIES USING KNN CLASSIFIER")
    print("=" * 70)

    iris = load_iris()
    if knn_model is None or scaler is None:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(iris.data)
        knn_model = KNeighborsClassifier(n_neighbors=5).fit(X_scaled, iris.target)

    if new_measurements is None:
        new_measurements = [
            {"label": "Flower #1", "features": [4.8, 3.4, 1.6, 0.2]},
            {"label": "Flower #2", "features": [5.7, 2.8, 4.1, 1.3]},
            {"label": "Flower #3", "features": [6.5, 3.0, 5.5, 1.8]},
        ]

    for item in new_measurements:
        arr = np.array(item["features"]).reshape(1, -1)
        arr_scaled = scaler.transform(arr)
        pred_idx = knn_model.predict(arr_scaled)[0]
        probs = knn_model.predict_proba(arr_scaled)[0]
        species = iris.target_names[pred_idx]

        print(f" {item['label']} (Features: {item['features']}):")
        print(f"   -> Predicted Class: {species.upper()}")
        print(f"   -> Neighbor Vote Proportions: Setosa={probs[0]:.2f}, Versicolor={probs[1]:.2f}, Virginica={probs[2]:.2f}\n")


if __name__ == "__main__":
    run_bullet5_knn_iris_accuracy(n_neighbors=5)
    model_s, sc, _ = run_bullet6_knn_with_scaling(n_neighbors=5, interactive=False)
    run_bullet7_knn_predict_species(knn_model=model_s, scaler=sc)
