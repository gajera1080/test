"""
================================================================================
UNIT 2.6: LOGISTIC REGRESSION (CLASSIFICATION VIA REGRESSION)
================================================================================
Syllabus Topics Covered:
- 2.6 Introduction to Logistic Regression: Sigmoid Function, Odds Ratio,
  Log-Loss Cost Function, Decision Thresholds, Probabilistic Predictions.

Journal Questions Addressed:
- Q10: Logistic Regression on Insurance dataset (insurance_data.csv: Age vs Bought Insurance).
       Fitted sigmoid curve visualization, probability predictions.
- Q11: Logistic Regression on Heart Disease dataset (heart.csv).
       Multi-feature classification, Accuracy, Confusion Matrix, ROC-AUC visualization.
- University Variations: Threshold tuning, ROC curve analysis, multi-class extensions.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_classification_metrics
from utils.data_loader import load_dataset


def run_q10_insurance_logistic_regression(interactive=True):
    """
    Journal Question 10:
    Implement Logistic Regression using Python and Scikit-learn
    for predicting value using Insurance dataset (insurance_data.csv).
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 10: LOGISTIC REGRESSION ON INSURANCE PURCHASE")
    print("=" * 70)

    df = load_dataset("insurance_data.csv")
    X = df[["age"]].values
    y = df["bought_insurance"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Probability predictions on test set
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = model.predict(X_test)

    print(f"\n [Model Parameters]")
    print(f" - Coefficient (beta_1) : {model.coef_[0][0]:.4f}")
    print(f" - Intercept (beta_0)   : {model.intercept_[0]:.4f}")
    print(f" - Decision Boundary Age: {-model.intercept_[0] / model.coef_[0][0]:.1f} years (where p = 0.5)")

    # Sample Predictions
    sample_ages = [22, 35, 45, 55, 62]
    print("\n Sample Probability Predictions for New Individuals:")
    for age in sample_ages:
        prob = model.predict_proba([[age]])[0][1]
        decision = "Will Buy (1)" if prob >= 0.5 else "Will NOT Buy (0)"
        print(f" - Age {age:<2}: P(Bought) = {prob:.4f} ({prob*100:.1f}%) -> Prediction: {decision}")

    metrics = print_classification_metrics(y_test, y_pred, target_names=["No Insurance", "Bought Insurance"], title="Insurance Logistic Regression Evaluation")

    # Visualization: Sigmoid Curve with Data Points
    set_plot_style()
    fig, ax = plt.subplots(figsize=(9, 5))

    # Scatter actual points
    ax.scatter(X[y == 0], y[y == 0], color="#d62728", s=60, label="Did Not Buy (0)", alpha=0.8, edgecolors="k")
    ax.scatter(X[y == 1], y[y == 1], color="#2ca02c", s=60, label="Bought (1)", alpha=0.8, edgecolors="k")

    # Smooth Sigmoid curve
    x_range = np.linspace(X.min() - 5, X.max() + 5, 200).reshape(-1, 1)
    y_sigmoid = model.predict_proba(x_range)[:, 1]
    ax.plot(x_range, y_sigmoid, color="#1f77b4", linewidth=2.5, label=r"Fitted Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$")

    # 0.5 Decision boundary line
    boundary_age = -model.intercept_[0] / model.coef_[0][0]
    ax.axhline(0.5, color="gray", linestyle=":", label="Decision Threshold (p = 0.5)")
    ax.axvline(boundary_age, color="purple", linestyle="--", label=f"Threshold Boundary ({boundary_age:.1f} yrs)")

    ax.set_title("Logistic Regression: Insurance Purchase Probability vs Age")
    ax.set_xlabel("Age of Person")
    ax.set_ylabel("Probability of Buying Insurance")
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc="best")

    save_and_show(fig, filename="unit2_q10_insurance_logistic_regression.png", interactive=interactive)
    return model, metrics


def run_q11_heart_disease_logistic_regression(interactive=True):
    """
    Journal Question 11:
    Implement Logistic Regression using Python and Scikit-learn
    for predicting value using Heart dataset (heart.csv).
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 11: LOGISTIC REGRESSION ON HEART DISEASE DATASET")
    print("=" * 70)

    df = load_dataset("heart.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    feature_names = list(X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Standard scaling is critical for convergence in multi-feature logistic regression
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # Evaluation
    metrics = print_classification_metrics(y_test, y_pred, target_names=["No Disease", "Heart Disease"], title="Heart Disease Classification Evaluation")

    # ROC AUC Score
    auc_score = roc_auc_score(y_test, y_prob)
    print(f" Receiver Operating Characteristic Area Under Curve (ROC-AUC): {auc_score:.4f}")

    # Visualization: Confusion Matrix Heatmap & ROC Curve
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Confusion Matrix Heatmap
    cm = confusion_matrix(y_test, y_pred)
    im = axes[0].imshow(cm, interpolation="nearest", cmap="Blues")
    axes[0].set_title(f"Confusion Matrix (Accuracy: {metrics['accuracy']*100:.1f}%)")
    axes[0].set_xlabel("Predicted Label")
    axes[0].set_ylabel("Actual True Label")
    axes[0].set_xticks([0, 1])
    axes[0].set_yticks([0, 1])
    axes[0].set_xticklabels(["No Disease (0)", "Heart Disease (1)"])
    axes[0].set_yticklabels(["No Disease (0)", "Heart Disease (1)"])
    fig.colorbar(im, ax=axes[0])

    for i in range(2):
        for j in range(2):
            axes[0].text(j, i, format(cm[i, j], "d"),
                         ha="center", va="center",
                         color="white" if cm[i, j] > cm.max() / 2.0 else "black",
                         fontsize=14, fontweight="bold")

    # Plot 2: ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    axes[1].plot(fpr, tpr, color="#ff7f0e", linewidth=2.5, label=f"ROC Curve (AUC = {auc_score:.3f})")
    axes[1].plot([0, 1], [0, 1], color="navy", linestyle="--", label="Random Chance (AUC = 0.5)")
    axes[1].set_title("Receiver Operating Characteristic (ROC) Curve")
    axes[1].set_xlabel("False Positive Rate (1 - Specificity)")
    axes[1].set_ylabel("True Positive Rate (Sensitivity / Recall)")
    axes[1].legend(loc="lower right")

    save_and_show(fig, filename="unit2_q11_heart_disease_logistic_regression.png", interactive=interactive)
    return model, metrics


if __name__ == "__main__":
    run_q10_insurance_logistic_regression(interactive=False)
    run_q11_heart_disease_logistic_regression(interactive=False)
