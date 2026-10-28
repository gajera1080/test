"""
================================================================================
UNIT 4.1 - 4.3: MACHINE LEARNING EVALUATION METRICS
================================================================================
Syllabus Topics Covered:
- 4.1 Classification Metrics:
      Confusion Matrix (TP, FP, TN, FN), Accuracy, Precision, Recall/Sensitivity,
      Specificity, F1-Score (Macro/Micro/Weighted), ROC-AUC Curve, Log-Loss.
- 4.2 Regression Metrics:
      Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE),
      R-Squared (R2), Adjusted R-Squared, Residual Analysis.
- 4.3 Evaluating Unsupervised Models:
      Inertia / WCSS, Silhouette Coefficient, Davies-Bouldin Index, Calinski-Harabasz Score.

University Exam Value:
- Demonstrates exact formulas and interpretations asked in university viva & theory exams.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_diabetes, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score, precision_recall_curve,
    mean_squared_error, mean_absolute_error, r2_score,
    silhouette_score, silhouette_samples, davies_bouldin_score, calinski_harabasz_score
)
from sklearn.preprocessing import StandardScaler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style


def demonstrate_classification_metrics(interactive=True):
    """
    4.1 Comprehensive Classification Metrics Demonstration
    """
    print("\n" + "=" * 70)
    print(" 4.1 CLASSIFICATION METRICS & EVALUATION TECHNIQUES")
    print("=" * 70)

    # Use Breast Cancer dataset (Binary classification: Malignant vs Benign)
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_train_s, y_train)

    y_pred = clf.predict(X_test_s)
    y_prob = clf.predict_proba(X_test_s)[:, 1]

    # Confusion Matrix Breakdown
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    # Formulas
    acc = (tp + tn) / (tp + tn + fp + fn)
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    spec = tn / (tn + fp) if (tn + fp) > 0 else 0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0
    auc = roc_auc_score(y_test, y_prob)

    print(f"""
1. Confusion Matrix Breakdown:
   - True Negatives (TN)  : {tn:<4} (Actual 0, Predicted 0)
   - False Positives (FP) : {fp:<4} (Type I Error: Actual 0, Predicted 1)
   - False Negatives (FN) : {fn:<4} (Type II Error: Actual 1, Predicted 0)
   - True Positives (TP)  : {tp:<4} (Actual 1, Predicted 1)

2. Mathematical Metrics:
   - Accuracy    = (TP + TN) / Total            : {acc:.4f} ({acc*100:.2f}%)
   - Precision   = TP / (TP + FP)               : {prec:.4f} (Reliability of positive alarm)
   - Recall      = TP / (TP + FN) [Sensitivity] : {rec:.4f} (Coverage of positive cases)
   - Specificity = TN / (TN + FP)               : {spec:.4f} (Coverage of negative cases)
   - F1-Score    = 2 * (Prec * Rec)/(Prec + Rec): {f1:.4f} (Harmonic Mean)
   - ROC-AUC     = Area Under ROC Curve         : {auc:.4f}
""")

    # Visualizations: 3-Panel Metric Dashboard
    set_plot_style()
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel 1: Confusion Matrix
    im = axes[0].imshow(cm, cmap="Blues", interpolation="nearest")
    axes[0].set_title(f"Confusion Matrix (Acc={acc*100:.1f}%)")
    axes[0].set_xlabel("Predicted Class")
    axes[0].set_ylabel("Actual Class")
    axes[0].set_xticks([0, 1])
    axes[0].set_yticks([0, 1])
    axes[0].set_xticklabels(cancer.target_names)
    axes[0].set_yticklabels(cancer.target_names)
    for i in range(2):
        for j in range(2):
            axes[0].text(j, i, str(cm[i, j]), ha="center", va="center", color="white" if cm[i, j] > cm.max()/2 else "black", fontsize=14, fontweight="bold")

    # Panel 2: ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    axes[1].plot(fpr, tpr, color="#ff7f0e", linewidth=2.5, label=f"ROC Curve (AUC = {auc:.3f})")
    axes[1].plot([0, 1], [0, 1], "k--", label="Random Classifier (AUC = 0.50)")
    axes[1].set_title("ROC Curve (Sensitivity vs 1 - Specificity)")
    axes[1].set_xlabel("False Positive Rate")
    axes[1].set_ylabel("True Positive Rate")
    axes[1].legend(loc="lower right")

    # Panel 3: Precision-Recall Curve
    precisions, recalls, _ = precision_recall_curve(y_test, y_prob)
    axes[2].plot(recalls, precisions, color="#2ca02c", linewidth=2.5, label="Precision-Recall Curve")
    axes[2].set_title("Precision-Recall Curve")
    axes[2].set_xlabel("Recall")
    axes[2].set_ylabel("Precision")
    axes[2].legend(loc="lower left")

    save_and_show(fig, filename="unit4_classification_metrics_dashboard.png", interactive=interactive)


def demonstrate_regression_metrics(interactive=True):
    """
    4.2 Comprehensive Regression Metrics Demonstration
    """
    print("\n" + "=" * 70)
    print(" 4.2 REGRESSION METRICS & RESIDUAL ANALYSIS")
    print("=" * 70)

    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    n = len(y_test)
    p = X_test.shape[1]

    # Metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

    print(f"""
1. Error Metrics:
   - Mean Absolute Error (MAE)       : {mae:.4f}  (Formula: 1/n * sum|y - y_hat|)
   - Mean Squared Error (MSE)        : {mse:.4f}  (Formula: 1/n * sum(y - y_hat)^2)
   - Root Mean Squared Error (RMSE)  : {rmse:.4f}  (Formula: sqrt(MSE))

2. Goodness-of-Fit Metrics:
   - R-Squared (R2 Score)            : {r2:.4f} ({r2*100:.2f}%) (Formula: 1 - SS_res / SS_tot)
   - Adjusted R-Squared (Adj R2)     : {adj_r2:.4f} ({adj_r2*100:.2f}%) (Penalizes extra features)
""")

    # Visualizations: Residual Plot & Q-Q Plot
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    residuals = y_test - y_pred
    axes[0].scatter(y_pred, residuals, color="#1f77b4", alpha=0.7, edgecolors="k")
    axes[0].axhline(0, color="red", linestyle="--", linewidth=2)
    axes[0].set_title("Residual Plot (Homoscedasticity Check)")
    axes[0].set_xlabel("Predicted Values")
    axes[0].set_ylabel("Residuals (Actual - Predicted)")

    # Error Histogram
    axes[1].hist(residuals, bins=15, color="#2ca02c", edgecolor="black", alpha=0.8)
    axes[1].axvline(0, color="red", linestyle="--", linewidth=2)
    axes[1].set_title("Residual Error Distribution (Normality Check)")
    axes[1].set_xlabel("Residual Error")
    axes[1].set_ylabel("Frequency")

    save_and_show(fig, filename="unit4_regression_metrics_residuals.png", interactive=interactive)


def demonstrate_unsupervised_metrics(interactive=True):
    """
    4.3 Heuristics and Techniques for Evaluating Unsupervised Learning Models
    """
    print("\n" + "=" * 70)
    print(" 4.3 EVALUATING UNSUPERVISED LEARNING MODELS")
    print("=" * 70)

    iris = load_iris()
    X = StandardScaler().fit_transform(iris.data[:, 2:4])

    k_values = [2, 3, 4, 5]
    records = []

    for k in k_values:
        km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
        sil = silhouette_score(X, km.labels_)
        db = davies_bouldin_score(X, km.labels_)
        ch = calinski_harabasz_score(X, km.labels_)
        records.append({
            "K": k,
            "Inertia (WCSS)": round(km.inertia_, 2),
            "Silhouette Score": round(sil, 4),
            "Davies-Bouldin": round(db, 4),
            "Calinski-Harabasz": round(ch, 2)
        })

    eval_df = pd.DataFrame(records)
    print(" Clustering Heuristics Across Cluster Counts (K = 2 to 5):")
    print(eval_df.to_string(index=False))
    print("""
Interpretation:
- Inertia: Monotonically decreases; look for the 'Elbow'.
- Silhouette Score: Measures separation vs cohesion [-1 to 1]. Maximum at optimal K.
- Davies-Bouldin Index: Ratio of within-cluster distance to between-cluster separation. Lower is better!
- Calinski-Harabasz: Ratio of between-cluster dispersion to within-cluster dispersion. Higher is better!
""")

    # Visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(eval_df["K"], eval_df["Silhouette Score"], marker="s", color="#9467bd", linewidth=2.5, markersize=8, label="Silhouette Score")
    ax.set_title("Silhouette Analysis Across Cluster Numbers (K)")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("Silhouette Score")
    ax.set_xticks(k_values)
    ax.legend()

    save_and_show(fig, filename="unit4_unsupervised_silhouette_analysis.png", interactive=interactive)


if __name__ == "__main__":
    demonstrate_classification_metrics(interactive=False)
    demonstrate_regression_metrics(interactive=False)
    demonstrate_unsupervised_metrics(interactive=False)
