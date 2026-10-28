"""
================================================================================
UNIT 3.4: SUPPORT VECTOR MACHINE (SVM) CLASSIFIER
================================================================================
Syllabus Topics Covered:
- 3.4 Supervised Learning with SVM: Concepts of Hyperplane, Support Vectors,
  Margin Maximization, Soft-margin Slack Variables, Kernel Trick (Linear, RBF, Poly).

Journal Questions Addressed:
- Bullet 3: Classification on Iris dataset using SVM classifier displaying
            Precision, Recall, F1-Score, and Support for each Iris class
            (setosa, versicolor, virginica) on test data.
- Bullet 4: SVM Classifier for predicting species of new Iris flowers.
- University Variations: Kernel comparison (Linear vs RBF), decision boundary visualization.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_classification_metrics


def run_svm_iris_classification(kernel="rbf", test_size=0.2, interactive=True):
    """
    Journal Question Bullet 3:
    Perform classification on Iris dataset using SVM classifier.
    Display precision, recall, F1-score, and support for each Iris class
    (setosa, versicolor, virginica) on test data.
    """
    print("\n" + "=" * 70)
    print(" SVM CLASSIFICATION ON IRIS DATASET (PRECISION, RECALL, F1, SUPPORT)")
    print("=" * 70)

    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = list(iris.target_names)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    # Standard scaling ensures isotropic distance metrics for RBF kernel
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train SVM Classifier
    model = SVC(kernel=kernel, C=1.0, probability=True, random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    # Display detailed classification report showing precision, recall, f1, support
    print(f"\n [Kernel: {kernel.upper()}, C: 1.0]")
    metrics = print_classification_metrics(
        y_test, y_pred, target_names=target_names, title="Iris SVM Classification Report"
    )

    # Visualization: Confusion Matrix
    set_plot_style()
    fig, ax = plt.subplots(figsize=(7, 5))
    cm = confusion_matrix(y_test, y_pred)
    im = ax.imshow(cm, interpolation="nearest", cmap="Purples")
    ax.set_title(f"SVM Iris Classification Confusion Matrix (Accuracy: {metrics['accuracy']*100:.1f}%)")
    ax.set_xlabel("Predicted Species")
    ax.set_ylabel("True Species")
    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(target_names)
    ax.set_yticklabels(target_names)
    fig.colorbar(im, ax=ax)

    for i in range(3):
        for j in range(3):
            ax.text(j, i, format(cm[i, j], "d"),
                    ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2.0 else "black",
                    fontsize=14, fontweight="bold")

    save_and_show(fig, filename="unit3_svm_iris_confusion_matrix.png", interactive=interactive)
    return model, scaler, metrics


def run_svm_predict_new_flower(new_measurements=None, model=None, scaler=None):
    """
    Journal Question Bullet 4:
    Implement a Support Vector Machine (SVM) Classifier for predicting
    the species of Iris flowers using the Iris dataset.
    """
    print("\n" + "=" * 70)
    print(" PREDICTING SPECIES OF NEW IRIS FLOWERS USING SVM")
    print("=" * 70)

    iris = load_iris()
    if model is None or scaler is None:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(iris.data)
        model = SVC(kernel="rbf", probability=True, random_state=42).fit(X_scaled, iris.target)

    # Test cases representing Setosa, Versicolor, and Virginica
    if new_measurements is None:
        new_measurements = [
            {"sample": "Sample A", "features": [5.1, 3.5, 1.4, 0.2]},  # typical setosa
            {"sample": "Sample B", "features": [6.0, 2.7, 4.2, 1.3]},  # typical versicolor
            {"sample": "Sample C", "features": [6.9, 3.1, 5.4, 2.1]},  # typical virginica
        ]

    for item in new_measurements:
        feats = np.array(item["features"]).reshape(1, -1)
        feats_scaled = scaler.transform(feats)
        pred_class = model.predict(feats_scaled)[0]
        pred_probs = model.predict_proba(feats_scaled)[0]
        pred_species = iris.target_names[pred_class]

        print(f" {item['sample']} {item['features']}:")
        print(f"   -> Predicted Species: {pred_species.upper()}")
        print(f"   -> Probabilities    : setosa={pred_probs[0]:.3f}, versicolor={pred_probs[1]:.3f}, virginica={pred_probs[2]:.3f}\n")


def visualize_svm_decision_boundaries_2d(interactive=True):
    """
    University Variation / Exam Helper:
    Visualizes SVM 2D decision boundary mesh and support vectors using Petal dimensions.
    """
    iris = load_iris()
    # Petal Length & Petal Width
    X = iris.data[:, 2:4]
    y = iris.target

    model = SVC(kernel="rbf", C=1.0, gamma="scale").fit(X, y)

    # Meshgrid
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    set_plot_style()
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")

    # Plot sample points
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors="k", s=40, label="Iris Samples")

    # Highlight support vectors
    sv = model.support_vectors_
    ax.scatter(sv[:, 0], sv[:, 1], s=120, facecolors="none", edgecolors="red", linewidth=1.5, label=f"Support Vectors (n={len(sv)})")

    ax.set_title("SVM Non-Linear Decision Boundaries & Support Vectors (Petal Dimensions)")
    ax.set_xlabel("Petal Length (cm)")
    ax.set_ylabel("Petal Width (cm)")
    ax.legend()

    save_and_show(fig, filename="unit3_svm_decision_boundaries_2d.png", interactive=interactive)


if __name__ == "__main__":
    trained_model, trained_scaler, _ = run_svm_iris_classification(interactive=False)
    run_svm_predict_new_flower(model=trained_model, scaler=trained_scaler)
    visualize_svm_decision_boundaries_2d(interactive=False)
