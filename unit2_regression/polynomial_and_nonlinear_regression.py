"""
================================================================================
UNIT 2.5: POLYNOMIAL AND NON-LINEAR REGRESSION
================================================================================
Syllabus Topics Covered:
- 2.5 Polynomial Regression: Concepts, Hypothesis Function,
  Equation: y = beta_0 + beta_1*x + beta_2*x^2 + ... + beta_d*x^d
  Feature mapping using PolynomialFeatures, Bias-Variance Tradeoff.

Journal Questions Addressed:
- Q8: Polynomial Regression on position_salary.csv (Predicting values, smooth curve visualization).
- Q9: Polynomial Regression on auto.csv (Accuracy via R2 score and MSE, curve visualization).
- University Variations: Overfitting detection, degree selection across degrees 1 to 5.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_regression_metrics, print_coefficients
from utils.data_loader import load_dataset


def run_q8_position_salary_polynomial_regression(test_level=6.5, interactive=True):
    """
    Journal Question 8:
    Implement Polynomial Regression using Python and Scikit-learn
    for predicting value using position_salary dataset and perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 8: POLYNOMIAL REGRESSION ON POSITION SALARY")
    print("=" * 70)

    df = load_dataset("position_salary.csv")
    X = df[["Level"]].values
    y = df["Salary"].values

    # 1. Fit Linear Regression (Degree 1) as baseline
    lin_reg = LinearRegression().fit(X, y)
    lin_pred_test = lin_reg.predict([[test_level]])[0]

    # 2. Fit Polynomial Regressions (Degrees 2, 3, 4)
    poly_models = {}
    poly_preds_test = {}
    for deg in [2, 3, 4]:
        model = make_pipeline(PolynomialFeatures(degree=deg), LinearRegression())
        model.fit(X, y)
        poly_models[deg] = model
        poly_preds_test[deg] = model.predict([[test_level]])[0]

    # Print Predictions for the target level (e.g. Level 6.5)
    print(f"\n [Predictions for Position Level {test_level}]:")
    print(f" - Linear Regression (Degree 1)     : ${lin_pred_test:,.2f}")
    for deg, pred_val in poly_preds_test.items():
        print(f" - Polynomial Regression (Degree {deg}) : ${pred_val:,.2f}")

    # Best fit model (Degree 4)
    best_poly = poly_models[4]
    y_pred_all = best_poly.predict(X)
    print_regression_metrics(y, y_pred_all, X=X, title="Position Salary Polynomial (Degree 4) Fit")

    # 3. High-resolution smooth curve visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(9, 6))

    # Actual data points
    ax.scatter(X, y, color="#d62728", s=60, label="Actual Salaries", zorder=5, edgecolors="k")

    # Smooth X grid
    x_min, x_max = float(X.min()), float(X.max())
    X_grid = np.arange(x_min, x_max + 0.1, 0.05).reshape(-1, 1)

    # Plot Linear fit
    ax.plot(X_grid, lin_reg.predict(X_grid), color="gray", linestyle="--", label="Linear Fit (Degree 1)")

    # Plot Polynomial fits
    colors = {2: "#2ca02c", 3: "#ff7f0e", 4: "#1f77b4"}
    for deg in [2, 3, 4]:
        ax.plot(X_grid, poly_models[deg].predict(X_grid), color=colors[deg], linewidth=2, label=f"Polynomial (Degree {deg})")

    # Mark the predicted point for Degree 4
    ax.scatter([test_level], [poly_preds_test[4]], color="purple", marker="*", s=160, label=f"Level {test_level} Pred: ${poly_preds_test[4]:,.0f}", zorder=6)

    ax.set_title(f"Polynomial Regression on Position Salaries (Level vs Salary)")
    ax.set_xlabel("Position Level")
    ax.set_ylabel("Salary ($)")
    ax.legend()

    save_and_show(fig, filename="unit2_q08_position_salary_polynomial.png", interactive=interactive)
    return poly_models, poly_preds_test


def run_q9_auto_polynomial_regression(interactive=True):
    """
    Journal Question 9:
    Implement Polynomial Regression using Python and Scikit-learn
    for predicting value using auto dataset and find accuracy using R2 score and MSE.
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 9: POLYNOMIAL REGRESSION ON AUTO DATASET")
    print("=" * 70)

    df = load_dataset("auto.csv")
    # Clean missing values if any
    df = df.dropna()

    X = df[["horsepower"]].values
    y = df["mpg"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    degrees = [1, 2, 3, 4]
    comparison_records = []
    models = {}

    for deg in degrees:
        pipe = make_pipeline(PolynomialFeatures(degree=deg), LinearRegression())
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)

        mse = np.mean((y_test - y_pred) ** 2)
        r2 = pipe.score(X_test, y_test)

        comparison_records.append({
            "Degree": deg,
            "MSE": round(mse, 4),
            "RMSE": round(np.sqrt(mse), 4),
            "R2 Score": round(r2, 4)
        })
        models[deg] = pipe

    comp_df = pd.DataFrame(comparison_records)
    print("\n Accuracy Comparison Across Polynomial Degrees (Auto Dataset: Horsepower vs MPG):")
    print(comp_df.to_string(index=False))

    # Detailed metrics for optimal quadratic model (Degree 2 is physically appropriate for mpg vs hp)
    y_pred_deg2 = models[2].predict(X_test)
    metrics = print_regression_metrics(y_test, y_pred_deg2, X=X_test, title="Auto Dataset Polynomial (Degree 2) Evaluation")

    # Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Curves for each degree
    X_plot = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
    axes[0].scatter(X, y, color="black", alpha=0.4, s=25, label="Observed Data")
    colors = {1: "red", 2: "green", 3: "blue", 4: "purple"}
    for deg in degrees:
        axes[0].plot(X_plot, models[deg].predict(X_plot), color=colors[deg], linewidth=2, label=f"Degree {deg} ($R^2={comp_df.loc[comp_df['Degree']==deg, 'R2 Score'].values[0]}$)")
    axes[0].set_title("Auto MPG vs Horsepower: Polynomial Fits")
    axes[0].set_xlabel("Horsepower")
    axes[0].set_ylabel("Miles Per Gallon (MPG)")
    axes[0].legend()

    # Plot 2: R2 and MSE vs Degree bar chart
    deg_indices = np.arange(len(degrees))
    width = 0.35
    axes[1].bar(deg_indices - width/2, comp_df["R2 Score"], width, label="R2 Score (higher is better)", color="#1f77b4")
    axes[1].bar(deg_indices + width/2, comp_df["MSE"] / comp_df["MSE"].max(), width, label="Relative MSE (lower is better)", color="#d62728")
    axes[1].set_xticks(deg_indices)
    axes[1].set_xticklabels([f"Deg {d}" for d in degrees])
    axes[1].set_title("Model Complexity vs Performance")
    axes[1].set_xlabel("Polynomial Degree")
    axes[1].set_ylabel("Normalized Metric Value")
    axes[1].legend()

    save_and_show(fig, filename="unit2_q09_auto_polynomial_regression.png", interactive=interactive)
    return models, comp_df


if __name__ == "__main__":
    run_q8_position_salary_polynomial_regression(test_level=6.5, interactive=False)
    run_q9_auto_polynomial_regression(interactive=False)
