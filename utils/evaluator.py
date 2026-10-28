"""
Evaluation and Metrics Utility
Provides consistent, academic-standard formatted output for regression,
classification, and unsupervised clustering metrics.
"""

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score,
)


def print_regression_metrics(y_true, y_pred, X=None, title="Regression Model Evaluation"):
    """
    Computes and prints standard regression metrics:
    MSE, RMSE, MAE, R-squared (R2), and Adjusted R-squared.
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    print(f"\n{'='*50}")
    print(f" {title.upper()}")
    print(f"{'='*50}")
    print(f" Mean Squared Error (MSE)       : {mse:.4f}")
    print(f" Root Mean Squared Error (RMSE) : {rmse:.4f}")
    print(f" Mean Absolute Error (MAE)      : {mae:.4f}")
    print(f" R-squared (R2 Score)           : {r2:.4f} ({r2*100:.2f}%)")

    metrics = {"MSE": mse, "RMSE": rmse, "MAE": mae, "R2": r2}

    if X is not None:
        n = len(y_true)
        p = X.shape[1] if len(X.shape) > 1 else 1
        if n > p + 1:
            adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))
            print(f" Adjusted R2 Score              : {adj_r2:.4f} ({adj_r2*100:.2f}%)")
            metrics["Adj_R2"] = adj_r2
    print(f"{'='*50}\n")
    return metrics


def print_coefficients(model, feature_names=None):
    """
    Prints model intercept and coefficients in a clean aligned table.
    """
    print(f"\n{'-'*50}")
    print(" MODEL PARAMETERS (INTERCEPT & COEFFICIENTS)")
    print(f"{'-'*50}")
    intercept = getattr(model, "intercept_", None)
    if intercept is not None:
        if isinstance(intercept, (list, np.ndarray)):
            intercept_val = intercept[0] if len(intercept) == 1 else intercept
            print(f" Intercept (beta_0) : {intercept_val}")
        else:
            print(f" Intercept (beta_0) : {intercept:.6f}")

    coef = getattr(model, "coef_", None)
    if coef is not None:
        coef = np.ravel(coef)
        if feature_names is None or len(feature_names) != len(coef):
            feature_names = [f"X{i+1}" for i in range(len(coef))]

        print(" Coefficients:")
        for name, val in zip(feature_names, coef):
            print(f"   {name:<28} : {val:+.6f}")
    print(f"{'-'*50}\n")


def print_classification_metrics(y_true, y_pred, target_names=None, title="Classification Model Evaluation"):
    """
    Computes and prints accuracy, detailed classification report, and confusion matrix.
    """
    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)

    print(f"\n{'='*55}")
    print(f" {title.upper()}")
    print(f"{'='*55}")
    print(f" Overall Accuracy: {acc:.4f} ({acc*100:.2f}%)")
    print("\n Detailed Classification Report:")
    print(classification_report(y_true, y_pred, target_names=target_names, digits=4, zero_division=0))
    print(" Confusion Matrix:")
    print(cm)
    print(f"{'='*55}\n")

    return {"accuracy": acc, "confusion_matrix": cm}


def print_clustering_metrics(X, labels, title="Clustering Evaluation"):
    """
    Computes heuristics for unsupervised clustering:
    Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index.
    """
    n_labels = len(set(labels)) - (1 if -1 in labels else 0)
    print(f"\n{'='*55}")
    print(f" {title.upper()} (Identified Clusters: {n_labels})")
    print(f"{'='*55}")
    metrics = {}
    if n_labels > 1:
        sil = silhouette_score(X, labels)
        db = davies_bouldin_score(X, labels)
        ch = calinski_harabasz_score(X, labels)
        print(f" Silhouette Score        : {sil:.4f}  (Range: [-1, 1], higher is better)")
        print(f" Davies-Bouldin Index    : {db:.4f}  (Lower is better)")
        print(f" Calinski-Harabasz Score : {ch:.4f}  (Higher is better)")
        metrics = {"silhouette": sil, "davies_bouldin": db, "calinski_harabasz": ch}
    else:
        print(" [Warning] Clustering resulted in <= 1 cluster; metrics cannot be calculated.")
    print(f"{'='*55}\n")
    return metrics
