"""
================================================================================
UNIT 4.4: VALIDATION TECHNIQUES & AVOIDING DATA LEAKAGE PITFALLS
================================================================================
Syllabus Topics Covered:
- 4.4 Data Leakage and Other Pitfalls:
  - Train / Validation / Test Splits
  - K-Fold and Stratified K-Fold Cross-Validation
  - What is Data Leakage? How Preprocessing Before Splitting Corrupts Evaluation
  - Pipeline Design to Guarantee Zero Leakage
  - Learning Curves to Diagnose High Bias (Underfitting) vs High Variance (Overfitting)

University Exam Value:
- Demonstrates the #1 most common interview and viva question:
  'Why must scaling and imputation only be fitted on the training set?'
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import (
    KFold, StratifiedKFold, cross_val_score, learning_curve, train_test_split
)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style


def demonstrate_data_leakage():
    """
    Simulates a high-dimensional noisy dataset to prove the catastrophic effect
    of Data Leakage (preprocessing/feature selection prior to train-test split).
    """
    print("\n" + "=" * 70)
    print(" 4.4 DEMONSTRATION OF DATA LEAKAGE & PITFALLS")
    print("=" * 70)

    # Generate synthetic dataset where features have virtually NO real correlation with y
    np.random.seed(42)
    n_samples = 150
    n_features = 2000  # High dimensional noise
    X = np.random.randn(n_samples, n_features)
    y = np.random.binomial(1, 0.5, size=n_samples)

    # -------------------------------------------------------------
    # PITFALL A: FLAWED APPROACH (DATA LEAKAGE)
    # Preprocessing / Feature normalization performed on ENTIRE dataset before splitting!
    # -------------------------------------------------------------
    scaler_leaked = StandardScaler()
    X_leaked = scaler_leaked.fit_transform(X)

    # Finding top correlated features across ALL data (LEAKING TEST LABELS!)
    correlations = np.abs([np.corrcoef(X_leaked[:, i], y)[0, 1] for i in range(n_features)])
    top_leaked_indices = np.argsort(correlations)[-5:]  # Pick top 5 spurious features
    X_leaked_top = X_leaked[:, top_leaked_indices]

    X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(X_leaked_top, y, test_size=0.3, random_state=42)
    clf_leaked = LogisticRegression().fit(X_train_l, y_train_l)
    acc_leaked = clf_leaked.score(X_test_l, y_test_l)

    # -------------------------------------------------------------
    # CLEAN APPROACH B: PROPER PIPELINE (ZERO LEAKAGE)
    # Splitting FIRST, then fitting preprocessing strictly on training data
    # -------------------------------------------------------------
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=42)

    # Fit scaler ONLY on train
    clean_scaler = StandardScaler()
    X_train_c_s = clean_scaler.fit_transform(X_train_c)
    X_test_c_s = clean_scaler.transform(X_test_c)

    # Feature selection strictly on train
    train_corrs = np.abs([np.corrcoef(X_train_c_s[:, i], y_train_c)[0, 1] for i in range(n_features)])
    top_clean_indices = np.argsort(train_corrs)[-5:]

    clf_clean = LogisticRegression().fit(X_train_c_s[:, top_clean_indices], y_train_c)
    acc_clean = clf_clean.score(X_test_c_s[:, top_clean_indices], y_test_c)

    print(f"""
[RESULTS ON PURE NOISE DATASET]:
- Flawed Model (With Data Leakage) Accuracy : {acc_leaked * 100:.2f}%  <-- DECEPTIVE! Spurious high score.
- Clean Model (No Data Leakage) Accuracy   : {acc_clean * 100:.2f}%  <-- REALISTIC (~50% coin flip on noise).

CRITICAL TAKEAWAY FOR EXAMS & VIVA:
- Never call fit() or fit_transform() on the entire dataset.
- Always use scikit-learn Pipeline(steps=[('scaler', StandardScaler()), ('clf', Model())])
  to guarantee that validation/test folds are strictly transformed using only training statistics!
""")


def demonstrate_cross_validation_and_learning_curves(interactive=True):
    """
    Demonstrates K-Fold and Stratified K-Fold Cross-Validation,
    along with Learning Curves to diagnose Underfitting vs Overfitting.
    """
    print("\n" + "=" * 70)
    print(" K-FOLD CROSS-VALIDATION & LEARNING CURVE ANALYSIS")
    print("=" * 70)

    # Standard benchmark dataset
    X, y = make_classification(n_samples=500, n_features=10, n_informative=8, random_state=42)

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(random_state=42))
    ])

    # 1. Standard K-Fold Cross Validation
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    kfold_scores = cross_val_score(pipeline, X, y, cv=kfold, scoring="accuracy")

    # 2. Stratified K-Fold Cross Validation (preserves class ratios per fold)
    strat_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    strat_scores = cross_val_score(pipeline, X, y, cv=strat_kfold, scoring="accuracy")

    print(f" 5-Fold Standard K-Fold Accuracies   : {[round(s, 4) for s in kfold_scores]}")
    print(f" -> Mean: {kfold_scores.mean():.4f} (+/- {kfold_scores.std():.4f})")
    print(f"\n 5-Fold Stratified K-Fold Accuracies: {[round(s, 4) for s in strat_scores]}")
    print(f" -> Mean: {strat_scores.mean():.4f} (+/- {strat_scores.std():.4f})")

    # 3. Learning Curve Computation (Diagnose Bias/Variance)
    train_sizes, train_scores, val_scores = learning_curve(
        pipeline, X, y, cv=5, scoring="accuracy", train_sizes=np.linspace(0.1, 1.0, 6), random_state=42
    )

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)

    # Visualizations
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Panel 1: Cross-Validation Boxplot
    axes[0].boxplot([kfold_scores, strat_scores], tick_labels=["Standard K-Fold", "Stratified K-Fold"], patch_artist=True, boxprops=dict(facecolor="#1f77b4", alpha=0.6))
    axes[0].set_title("5-Fold Cross-Validation Accuracy Comparison")
    axes[0].set_ylabel("Accuracy Score")

    # Panel 2: Learning Curve
    axes[1].plot(train_sizes, train_mean, "o-", color="#1f77b4", label="Training Score")
    axes[1].fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.15, color="#1f77b4")
    axes[1].plot(train_sizes, val_mean, "o-", color="#2ca02c", label="Cross-Validation Score")
    axes[1].fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.15, color="#2ca02c")
    axes[1].set_title("Learning Curve (Diagnosing Bias & Variance)")
    axes[1].set_xlabel("Number of Training Samples")
    axes[1].set_ylabel("Accuracy")
    axes[1].legend(loc="lower right")

    save_and_show(fig, filename="unit4_cross_validation_and_learning_curve.png", interactive=interactive)


if __name__ == "__main__":
    demonstrate_data_leakage()
    demonstrate_cross_validation_and_learning_curves(interactive=False)
