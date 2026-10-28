"""
================================================================================
UNIT 2.4: MULTIPLE LINEAR REGRESSION
================================================================================
Syllabus Topics Covered:
- 2.4 Multiple Linear Regression: Concepts, Multi-feature Hypotheses, OLS,
  Equation: y = beta_0 + beta_1*x_1 + beta_2*x_2 + ... + beta_n*x_n

Journal Questions Addressed:
- Q5: Multiple Linear Regression on California Housing dataset
      (Print intercept & coefficients, visualize actual vs predicted and residuals).
- Q6: Multiple Linear Regression on Fuel Consumption dataset
      (Print intercept & coefficients, accuracy/R2, difference table, visualization).
- Q7: Multiple Linear Regression on Insurance dataset (insaurance_Practical_3.csv)
      (Categorical feature handling, intercept, coefficients, R2 score, visualization).
- University Variations: Arbitrary multi-feature modeling on any custom dataset.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_regression_metrics, print_coefficients
from utils.data_loader import load_dataset


def run_q5_california_housing_regression(interactive=True):
    """
    Journal Question 5:
    Implement Multiple Linear Regression using Python and Scikit-learn
    for predicting value using California Housing dataset.
    Print value of intercept and coefficient.
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 5: MULTIPLE LINEAR REGRESSION ON CALIFORNIA HOUSING")
    print("=" * 70)

    housing = fetch_california_housing(as_frame=True)
    X = housing.data
    y = housing.target
    feature_names = housing.feature_names

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Print intercept and coefficients
    print_coefficients(model, feature_names=feature_names)
    metrics = print_regression_metrics(y_test, y_pred, X=X_test, title="California Housing Regression Evaluation")

    # Visualization: 2-Panel Plot (Actual vs Predicted & Residuals)
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 1. Actual vs Predicted
    axes[0].scatter(y_test[:300], y_pred[:300], alpha=0.5, color="#1f77b4", edgecolors="k", s=30)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    axes[0].plot([min_val, max_val], [min_val, max_val], color="#d62728", linestyle="--", linewidth=2)
    axes[0].set_title(f"California Housing: Actual vs Predicted\n$R^2 = {metrics['R2']:.4f}$")
    axes[0].set_xlabel("Actual Median House Value ($100,000s)")
    axes[0].set_ylabel("Predicted House Value ($100,000s)")

    # 2. Residual Distribution
    residuals = y_test - y_pred
    axes[1].scatter(y_pred[:300], residuals[:300], alpha=0.5, color="#2ca02c", edgecolors="k", s=30)
    axes[1].axhline(0, color="red", linestyle="--", linewidth=1.5)
    axes[1].set_title("Residuals vs Predicted Values")
    axes[1].set_xlabel("Predicted House Value")
    axes[1].set_ylabel("Residual (Actual - Predicted)")

    save_and_show(fig, filename="unit2_q05_california_housing_regression.png", interactive=interactive)
    return model, metrics


def run_q6_fuel_consumption_regression(interactive=True):
    """
    Journal Question 6:
    Implement Multiple Linear Regression using Python and Scikit-learn
    for predicting value using Fuel consumption dataset.
    Print value of intercept and coefficient. Find Accuracy.
    Print difference between actual value and predicted value.
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 6: MULTIPLE LINEAR REGRESSION ON FUEL CONSUMPTION")
    print("=" * 70)

    df = load_dataset("FuelConsumption.csv")
    features = ["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]
    target = "CO2EMISSIONS"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # 1. Print Intercept and Coefficients
    print_coefficients(model, feature_names=features)

    # 2. Accuracy metrics (R2 score, MSE, RMSE)
    metrics = print_regression_metrics(y_test, y_pred, X=X_test, title="Fuel Consumption Regression Accuracy")

    # 3. Print Difference Table (Actual vs Predicted)
    comparison_df = pd.DataFrame({
        "Actual CO2": y_test.values[:10],
        "Predicted CO2": np.round(y_pred[:10], 2),
        "Difference (Actual - Pred)": np.round(y_test.values[:10] - y_pred[:10], 2),
        "Abs Error %": np.round(np.abs(y_test.values[:10] - y_pred[:10]) / y_test.values[:10] * 100, 2)
    })
    print(" Comparison Table: Actual vs Predicted CO2 Emissions (First 10 Test Samples):")
    print(comparison_df.to_string(index=False))

    # 4. Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Actual vs Predicted with ideal reference line
    axes[0].scatter(y_test, y_pred, color="#1f77b4", alpha=0.7, edgecolors="k", s=35)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="#d62728", linestyle="--", linewidth=2)
    axes[0].set_title(f"Fuel Consumption: Actual vs Predicted\n$R^2 = {metrics['R2']:.4f}$, $MSE = {metrics['MSE']:.2f}$")
    axes[0].set_xlabel("Actual CO2 Emissions (g/km)")
    axes[0].set_ylabel("Predicted CO2 Emissions (g/km)")

    # Plot 2: Difference / Error bar chart for test samples
    sample_diffs = (y_test.values - y_pred)
    n_samples_to_plot = min(20, len(sample_diffs))
    plot_diffs = sample_diffs[:n_samples_to_plot]
    bar_colors = ["#2ca02c" if diff >= 0 else "#d62728" for diff in plot_diffs]
    axes[1].bar(range(1, n_samples_to_plot + 1), plot_diffs, color=bar_colors, edgecolor="black", alpha=0.8)
    axes[1].axhline(0, color="black", linestyle="-", linewidth=1)
    axes[1].set_title(f"Prediction Difference (Actual - Predicted) for Test Samples (n={n_samples_to_plot})")
    axes[1].set_xlabel("Sample Index")
    axes[1].set_ylabel("Error (g/km)")

    save_and_show(fig, filename="unit2_q06_fuel_consumption_regression.png", interactive=interactive)
    return model, metrics


def run_q7_insurance_regression(interactive=True):
    """
    Journal Question 7:
    Implement Multiple Linear Regression using Python and Scikit-learn
    for predicting value using insaurance_Practical_3 dataset.
    Print value of intercept and coefficient.
    Print value of R2 score.
    Perform visualization.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 7: MULTIPLE LINEAR REGRESSION ON INSURANCE CHARGES")
    print("=" * 70)

    df = load_dataset("insaurance_Practical_3.csv")

    # One-hot / dummy encode categorical variables: sex, smoker, region
    df_encoded = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True, dtype=float)

    X = df_encoded.drop("charges", axis=1)
    y = df_encoded["charges"]
    feature_names = list(X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # 1. Print intercept and coefficients
    print_coefficients(model, feature_names=feature_names)

    # 2. Print value of R2 score
    metrics = print_regression_metrics(y_test, y_pred, X=X_test, title="Insurance Charges R2 Score & Evaluation")

    # 3. Visualization
    set_plot_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Actual vs Predicted
    axes[0].scatter(y_test, y_pred, color="#9467bd", alpha=0.7, edgecolors="k", s=35)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="#d62728", linestyle="--", linewidth=2)
    axes[0].set_title(f"Insurance Charges: Actual vs Predicted\n$R^2 = {metrics['R2']:.4f}$")
    axes[0].set_xlabel("Actual Charges ($)")
    axes[0].set_ylabel("Predicted Charges ($)")

    # Plot 2: Top Coefficients Impact
    coef_series = pd.Series(model.coef_, index=feature_names).sort_values()
    coef_series.plot(kind="barh", ax=axes[1], color="#17becf", edgecolor="black")
    axes[1].axvline(0, color="red", linestyle="--")
    axes[1].set_title("Feature Coefficients Impact on Charges")
    axes[1].set_xlabel("Coefficient Value")

    save_and_show(fig, filename="unit2_q07_insurance_charges_regression.png", interactive=interactive)
    return model, metrics


if __name__ == "__main__":
    run_q5_california_housing_regression(interactive=False)
    run_q6_fuel_consumption_regression(interactive=False)
    run_q7_insurance_regression(interactive=False)
