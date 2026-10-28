"""
================================================================================
UNIT 1: INTRODUCTION TO MACHINE LEARNING, CORE LIBRARIES & DATA SPLITTING
================================================================================
Syllabus Topics Covered:
- 1.1 What is Machine Learning, Need, Challenges, Real-World Applications
- 1.2 Types of ML (Supervised, Unsupervised, Semi-supervised, Reinforcement Learning)
- 1.3 Machine Learning Workflow (Acquisition -> Cleaning -> Split -> Train -> Validate)
- 1.5 Python Libraries for ML: NumPy, Pandas, Scikit-Learn

Journal Question Addressed:
- Q1: To implement Python code for split iris dataset and print features and target.
- University Variations: Flexible dataset splitting, summary statistics, feature correlation.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ensure utils package can be imported regardless of execution working directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from sklearn.datasets import load_iris, load_wine, load_diabetes
from sklearn.model_selection import train_test_split


def print_unit1_theory_summary():
    """Prints a clear overview of Unit 1 concepts for viva and theoretical exams."""
    print("=" * 70)
    print(" UNIT 1 OVERVIEW: FOUNDATIONS OF MACHINE LEARNING")
    print("=" * 70)
    print("""
1. What is Machine Learning?
   A subfield of AI that enables systems to learn from data and improve
   performance on a task through experience, without explicit programming.

2. Types of Machine Learning:
   - Supervised Learning: Uses labeled data (features X and target y).
     * Regression (continuous output, e.g., salary, price)
     * Classification (discrete categories, e.g., spam/not spam, flower species)
   - Unsupervised Learning: Discovers hidden patterns in unlabeled data.
     * Clustering (K-Means, Hierarchical)
     * Dimensionality Reduction (PCA)
   - Semi-Supervised Learning: Combines a small set of labeled data with a large
     volume of unlabeled data.
   - Reinforcement Learning: Agent learns via trial and error, rewards, and penalties.

3. Standard ML Workflow:
   Problem Definition -> Data Collection -> Data Preprocessing & EDA ->
   Feature Engineering -> Train/Test Split -> Model Training -> Evaluation -> Deployment
""")
    print("=" * 70)


def demonstrate_core_libraries():
    """Demonstrates NumPy array operations, Pandas DataFrame handling, and Scikit-learn workflow."""
    print("\n--- 1.5 DEMONSTRATING CORE PYTHON ML LIBRARIES ---")

    # 1. NumPy
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n[NumPy] 2D Array Shape: {arr.shape}, Mean: {arr.mean():.2f}")
    print(f"[NumPy] Matrix Vector Dot Product:\n{np.dot(arr, np.array([1, 0, 1]))}")

    # 2. Pandas
    sample_df = pd.DataFrame({
        "Study_Hours": [2.5, 5.1, 3.2, 8.5, 3.5],
        "Scores": [21, 47, 27, 75, 30]
    })
    print(f"\n[Pandas] Sample DataFrame Preview:\n{sample_df.head(3)}")
    print(f"[Pandas] Descriptive Statistics:\n{sample_df.describe().round(2)}")


def solve_journal_q1(test_size=0.2, random_state=42, interactive=True):
    """
    Journal Question 1:
    Implement Python code to split iris dataset and print features and target.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 1: SPLIT IRIS DATASET & PRINT FEATURES AND TARGET")
    print("=" * 70)

    # 1. Load Iris dataset from Scikit-Learn
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    print("\n1. Dataset Metadata:")
    print(f"   - Feature Names : {feature_names}")
    print(f"   - Target Names  : {list(target_names)}")
    print(f"   - Total Samples : {X.shape[0]} samples with {X.shape[1]} features each.")

    # Convert to DataFrame for readable preview
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y
    df["species"] = [target_names[i] for i in y]
    print("\n2. Dataset Sample (First 5 Rows):")
    print(df.head(5).to_string())

    # 2. Split dataset into Training and Testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    print("\n3. Train-Test Split Results:")
    print(f"   - Training Features Shape (X_train) : {X_train.shape}")
    print(f"   - Testing Features Shape (X_test)   : {X_test.shape}")
    print(f"   - Training Target Shape (y_train)   : {y_train.shape}")
    print(f"   - Testing Target Shape (y_test)     : {y_test.shape}")
    print(f"   - Test Split Percentage             : {test_size * 100:.0f}%")

    print("\n4. Class Distribution Across Splits:")
    train_counts = pd.Series(y_train).value_counts().sort_index()
    test_counts = pd.Series(y_test).value_counts().sort_index()
    dist_df = pd.DataFrame({
        "Class": target_names,
        "Train Samples": train_counts.values,
        "Test Samples": test_counts.values
    })
    print(dist_df.to_string(index=False))

    # 3. Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Sepal Dimensions
    for class_idx, name in enumerate(target_names):
        axes[0].scatter(
            X[y == class_idx, 0],
            X[y == class_idx, 1],
            label=name,
            alpha=0.8,
            edgecolors="k"
        )
    axes[0].set_xlabel(feature_names[0])
    axes[0].set_ylabel(feature_names[1])
    axes[0].set_title("Iris Sepal Dimensions (Length vs Width)")
    axes[0].legend()

    # Plot 2: Petal Dimensions
    for class_idx, name in enumerate(target_names):
        axes[1].scatter(
            X[y == class_idx, 2],
            X[y == class_idx, 3],
            label=name,
            alpha=0.8,
            edgecolors="k"
        )
    axes[1].set_xlabel(feature_names[2])
    axes[1].set_ylabel(feature_names[3])
    axes[1].set_title("Iris Petal Dimensions (Length vs Width)")
    axes[1].legend()

    save_and_show(fig, filename="unit1_q01_iris_split_visualization.png", interactive=interactive)
    return X_train, X_test, y_train, y_test


def university_variation_dataset_splitter(dataset_choice="wine", test_size=0.25):
    """
    University Variation:
    Handles arbitrary dataset splitting (Wine, Diabetes, etc.) with custom parameters.
    """
    print(f"\n[University Variation] Splitting '{dataset_choice}' dataset with test_size={test_size}...")
    if dataset_choice.lower() == "wine":
        data = load_wine()
    else:
        data = load_diabetes()

    X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=test_size, random_state=42)
    print(f"Features: {data.feature_names[:4]} ... (Total {len(data.feature_names)})")
    print(f"Train Shape: {X_tr.shape}, Test Shape: {X_te.shape}")
    return X_tr, X_te, y_tr, y_te


if __name__ == "__main__":
    print_unit1_theory_summary()
    demonstrate_core_libraries()
    solve_journal_q1(interactive=False)
    university_variation_dataset_splitter("wine", test_size=0.3)
