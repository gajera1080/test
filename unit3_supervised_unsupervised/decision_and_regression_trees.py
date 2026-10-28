"""
================================================================================
UNIT 3.1 - 3.3: DECISION TREES & REGRESSION TREES
================================================================================
Syllabus Topics Covered:
- 3.1 Introduction to Classification, Classification Terminologies
- 3.2 Decision Tree Classifier: Concepts, Splitting Criteria (Gini Impurity, Entropy)
- 3.3 Regression Trees: DecisionTreeRegressor, Continuous Output Prediction

Journal Questions Addressed:
- Bullet 1: Decision Tree Classifier on salaries dataset to predict salary (>100k).
- Bullet 2: Decision Tree Classifier on titanic dataset (survival prediction).
- Syllabus 3.3: Regression Tree implementation and non-linear step-function visualization.
- University Variations: Max-depth tuning, Gini vs Entropy comparison.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_text, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_classification_metrics, print_regression_metrics
from utils.data_loader import load_dataset


def run_decision_tree_salaries(interactive=True):
    """
    Journal Question Bullet 1:
    Write a Python program to implement a Decision Tree Classifier
    on the salaries dataset to predict the salary (>100k).
    """
    print("\n" + "=" * 70)
    print(" DECISION TREE CLASSIFIER ON SALARIES DATASET")
    print("=" * 70)

    df = load_dataset("salaries.csv")
    print("\nDataset Preview:")
    print(df.head())

    # Encode categorical features: company, job, degree
    le_company = LabelEncoder()
    le_job = LabelEncoder()
    le_degree = LabelEncoder()

    df_encoded = df.copy()
    df_encoded["company_n"] = le_company.fit_transform(df["company"])
    df_encoded["job_n"] = le_job.fit_transform(df["job"])
    df_encoded["degree_n"] = le_degree.fit_transform(df["degree"])

    feature_cols = ["company_n", "job_n", "degree_n"]
    target_col = "salary_more_then_100k"

    X = df_encoded[feature_cols]
    y = df_encoded[target_col]

    model = DecisionTreeClassifier(criterion="gini", random_state=42)
    model.fit(X, y)

    # Display Textual Tree Rules
    print("\n Learned Decision Tree Rules:")
    tree_rules = export_text(model, feature_names=feature_cols)
    print(tree_rules)

    # Test sample predictions:
    # 1. Google (n=2), Computer Programmer (n=1), Masters (n=1)
    # 2. Google (n=2), Business Manager (n=0), Bachelors (n=0)
    test_samples = [
        ("google", "computer programmer", "masters"),
        ("google", "business manager", "bachelors"),
        ("abc pharma", "sales executive", "bachelors"),
        ("facebook", "computer programmer", "bachelors")
    ]

    print(" Sample Employee Predictions (Salary > $100k?):")
    for comp, j, deg in test_samples:
        c_val = le_company.transform([comp])[0]
        j_val = le_job.transform([j])[0]
        d_val = le_degree.transform([deg])[0]
        pred = model.predict([[c_val, j_val, d_val]])[0]
        ans = "YES (> $100k)" if pred == 1 else "NO (<= $100k)"
        print(f" - {comp:<10} | {j:<20} | {deg:<10} ==> Prediction: {ans}")

    # Plot Decision Tree
    set_plot_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_tree(model, feature_names=feature_cols, class_names=["<=100k", ">100k"], filled=True, rounded=True, ax=ax)
    ax.set_title("Decision Tree for Salary Prediction (> $100k)")

    save_and_show(fig, filename="unit3_dt_salaries_tree.png", interactive=interactive)
    return model


def run_decision_tree_titanic(interactive=True):
    """
    Journal Question Bullet 2:
    Write a Python program to implement a Decision Tree Classifier on the titanic dataset.
    """
    print("\n" + "=" * 70)
    print(" DECISION TREE CLASSIFIER ON TITANIC DATASET")
    print("=" * 70)

    df = load_dataset("titanic.csv")

    # Select features & target
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
    X = df[features].copy()
    y = df["Survived"]

    # Preprocessing: Impute missing Age with median, encode Sex to numeric
    X["Age"] = X["Age"].fillna(X["Age"].median())
    X["Fare"] = X["Fare"].fillna(X["Fare"].median())
    X["Sex"] = (X["Sex"] == "male").astype(int)  # 1 for male, 0 for female

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train Decision Tree with max_depth to prevent overfitting
    model = DecisionTreeClassifier(max_depth=4, criterion="entropy", random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Evaluation
    metrics = print_classification_metrics(y_test, y_pred, target_names=["Perished (0)", "Survived (1)"], title="Titanic Survival Decision Tree Evaluation")

    # Feature Importance Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Feature Importances
    importances = pd.Series(model.feature_importances_, index=features).sort_values()
    importances.plot(kind="barh", ax=axes[0], color="#2ca02c", edgecolor="black")
    axes[0].set_title("Titanic Decision Tree Feature Importances")
    axes[0].set_xlabel("Gini / Entropy Importance")

    # Plot 2: Decision Tree Visual Structure
    plot_tree(model, feature_names=features, class_names=["Perished", "Survived"], filled=True, rounded=True, ax=axes[1], max_depth=3, fontsize=8)
    axes[1].set_title("Titanic Decision Tree (Top 3 Levels)")

    save_and_show(fig, filename="unit3_dt_titanic_survival.png", interactive=interactive)
    return model, metrics


def run_regression_tree_continuous(interactive=True):
    """
    Syllabus Topic 3.3:
    Regression Trees implementation for continuous target prediction.
    """
    print("\n" + "=" * 70)
    print(" SYLLABUS TOPIC 3.3: REGRESSION TREE IMPLEMENTATION")
    print("=" * 70)

    df = load_dataset("Salary_Data.csv")
    X = df[["YearsExperience"]].values
    y = df["Salary"].values

    # Train Regression Tree
    reg_tree = DecisionTreeRegressor(max_depth=3, random_state=42)
    reg_tree.fit(X, y)

    # Predictions
    x_test_grid = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
    y_pred_grid = reg_tree.predict(x_test_grid)

    print_regression_metrics(y, reg_tree.predict(X), X=X, title="Regression Tree on Salary Evaluation")

    # Visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(X, y, color="#1f77b4", label="Actual Data Points", s=50, edgecolors="k")
    ax.step(x_test_grid, y_pred_grid, color="#d62728", linewidth=2.5, label="Regression Tree Prediction (Step Function)")
    ax.set_title("Regression Tree: Non-Linear Piecewise Constant Surface")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary ($)")
    ax.legend()

    save_and_show(fig, filename="unit3_dt_regression_tree.png", interactive=interactive)
    return reg_tree


if __name__ == "__main__":
    run_decision_tree_salaries(interactive=False)
    run_decision_tree_titanic(interactive=False)
    run_regression_tree_continuous(interactive=False)
