"""
================================================================================
UNIT 2.1 - 2.3: SIMPLE LINEAR REGRESSION
================================================================================
Syllabus Topics Covered:
- 2.1 Introduction to Regression Analysis
- 2.2 Simple Linear Regression: Concepts, Mathematical Formula (y = mx + c), OLS
- 2.3 Scikit-learn Implementation of Simple Linear Regression

Journal Questions Addressed:
- Q2: Simple Linear Regression on diabetes dataset (R2 score, MSE, Visualization).
- Q3: Linear Regression on 6 bivariate relationships with new value predictions:
      i) Age & Height
      ii) Standard & Percentage
      iii) Height & Shoe Size
      iv) Experience & Salary
      v) Hours & Score
      vi) Vehicle Age & Resale Price
- Q4: Predict salary of 5 years of experience using Salary_Data.csv.
================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.plot_helper import save_and_show, set_plot_style
from utils.evaluator import print_regression_metrics, print_coefficients
from utils.data_loader import load_dataset


def run_q2_diabetes_regression(interactive=True):
    """
    Journal Question 2:
    To implement Simple Linear Regression on diabetes dataset.
    Find R2 score and MSE. Perform Visualizations.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 2: SIMPLE LINEAR REGRESSION ON DIABETES DATASET")
    print("=" * 70)

    diabetes = load_diabetes()
    # Feature 2 is BMI (Body Mass Index) - standard single predictor for diabetes progression
    X = diabetes.data[:, np.newaxis, 2]
    y = diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print_coefficients(model, feature_names=["BMI (Body Mass Index)"])
    metrics = print_regression_metrics(y_test, y_pred, X=X_test, title="Diabetes SLR Evaluation")

    # Visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(X_test, y_test, color="#1f77b4", label="Actual Test Data", alpha=0.8, edgecolors="k")
    ax.plot(X_test, y_pred, color="#d62728", linewidth=2.5, label="Fitted Regression Line")
    ax.set_title(f"Diabetes Simple Linear Regression (BMI vs Disease Progression)\n$R^2 = {metrics['R2']:.3f}$, $MSE = {metrics['MSE']:.2f}$")
    ax.set_xlabel("Body Mass Index (BMI, normalized)")
    ax.set_ylabel("Disease Progression Measure")
    ax.legend()

    save_and_show(fig, filename="unit2_q02_diabetes_simple_regression.png", interactive=interactive)
    return model, metrics


def run_q3_six_case_predictions(custom_test_inputs=None, interactive=True):
    """
    Journal Question 3:
    Perform Linear Regression and predict new value :
    i) Age and height
    ii) Standard and percentage
    iii) Height and shoesize
    iv) Experience and Salary
    v) Hours and score
    vi) Vehicle age and resale price
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 3: SIX BIVARIATE LINEAR REGRESSION PREDICTIONS")
    print("=" * 70)

    # Standard paired case datasets with target test values
    cases = [
        {
            "id": "i",
            "title": "Age vs Height",
            "x_label": "Age (years)",
            "y_label": "Height (cm)",
            "X": [2, 4, 6, 8, 10, 12],
            "y": [85, 105, 115, 130, 140, 152],
            "test_val": 5.0
        },
        {
            "id": "ii",
            "title": "Standard vs Percentage",
            "x_label": "Standard / Grade",
            "y_label": "Percentage (%)",
            "X": [1, 2, 3, 4, 5, 6],
            "y": [92, 88, 83, 79, 74, 69],
            "test_val": 6.0
        },
        {
            "id": "iii",
            "title": "Height vs Shoe Size",
            "x_label": "Height (cm)",
            "y_label": "Shoe Size (UK)",
            "X": [150, 158, 165, 172, 180, 188],
            "y": [5.5, 6.5, 7.5, 8.5, 9.5, 10.5],
            "test_val": 168.0
        },
        {
            "id": "iv",
            "title": "Experience vs Salary",
            "x_label": "Experience (years)",
            "y_label": "Salary (in 1000s)",
            "X": [1, 2, 3, 4, 5, 7],
            "y": [30, 42, 53, 62, 75, 96],
            "test_val": 6.0
        },
        {
            "id": "v",
            "title": "Hours vs Score",
            "x_label": "Study Hours",
            "y_label": "Exam Score (out of 100)",
            "X": [1, 2, 3, 4, 5, 6],
            "y": [38, 51, 64, 76, 88, 97],
            "test_val": 3.5
        },
        {
            "id": "vi",
            "title": "Vehicle Age vs Resale Price",
            "x_label": "Vehicle Age (years)",
            "y_label": "Resale Price (in Lakhs)",
            "X": [1, 2, 3, 4, 5, 7],
            "y": [11.5, 9.8, 8.2, 6.9, 5.5, 3.2],
            "test_val": 3.0
        }
    ]

    set_plot_style()
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    axes = axes.flatten()

    results = []
    for idx, case in enumerate(cases):
        x_raw = np.array(case["X"], dtype=float).reshape(-1, 1)
        y_raw = np.array(case["y"], dtype=float)

        model = LinearRegression().fit(x_raw, y_raw)
        test_x = custom_test_inputs.get(case["id"], case["test_val"]) if custom_test_inputs else case["test_val"]
        pred_y = float(model.predict([[test_x]])[0])

        slope = model.coef_[0]
        intercept = model.intercept_

        print(f" {case['id']}) {case['title']:<28}: Formula: y = {slope:.2f}x + {intercept:.2f}")
        print(f"     -> Input {case['x_label']} = {test_x}  ==>  Predicted {case['y_label']} = {pred_y:.2f}\n")

        results.append({"title": case["title"], "input": test_x, "predicted": pred_y, "slope": slope, "intercept": intercept})

        # Visualization
        x_line = np.linspace(min(case["X"]) - 0.5, max(case["X"]) + 0.5, 100).reshape(-1, 1)
        y_line = model.predict(x_line)

        ax = axes[idx]
        ax.scatter(case["X"], case["y"], color="#2ca02c", s=50, label="Observed Data", zorder=3)
        ax.plot(x_line, y_line, color="#1f77b4", linestyle="-", label="Regression Line", zorder=2)
        ax.scatter([test_x], [pred_y], color="#d62728", s=100, marker="*", label=f"Pred ({test_x}, {pred_y:.1f})", zorder=4)
        ax.set_title(f"{case['id']}) {case['title']}")
        ax.set_xlabel(case["x_label"])
        ax.set_ylabel(case["y_label"])
        ax.legend(fontsize=8)

    save_and_show(fig, filename="unit2_q03_six_case_regression_predictions.png", interactive=interactive)
    return results


def run_q4_predict_salary_5_years(years=5.0, interactive=True):
    """
    Journal Question 4:
    Perform Linear Regression and predict salary of 5 years of experience
    using Salary_Data.csv dataset.
    """
    print("\n" + "=" * 70)
    print(" JOURNAL QUESTION 4: PREDICT SALARY OF 5 YEARS OF EXPERIENCE")
    print("=" * 70)

    df = load_dataset("Salary_Data.csv")
    X = df[["YearsExperience"]].values
    y = df["Salary"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict for specific requested year (5.0)
    pred_salary = model.predict([[years]])[0]

    print(f"\n [Model Parameters]")
    print(f" - Slope (m)     : {model.coef_[0]:.2f}")
    print(f" - Intercept (c) : {model.intercept_:.2f}")
    print(f" - Equation      : Salary = ({model.coef_[0]:.2f} * YearsExperience) + {model.intercept_:.2f}")
    print(f"\n >>> PREDICTION FOR {years} YEARS OF EXPERIENCE: Rs. {pred_salary:,.2f} <<<\n")

    y_pred_test = model.predict(X_test)
    metrics = print_regression_metrics(y_test, y_pred_test, X=X_test, title="Salary Prediction Model Evaluation")

    # Visualization
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(X, y, color="#1f77b4", label="Actual Employees", alpha=0.8, edgecolors="k")
    x_range = np.linspace(X.min() - 0.5, X.max() + 0.5, 100).reshape(-1, 1)
    ax.plot(x_range, model.predict(x_range), color="#ff7f0e", linewidth=2, label="Regression Line")
    ax.scatter([years], [pred_salary], color="#d62728", s=130, marker="P", label=f"Target: {years} yrs = ${pred_salary:,.0f}", zorder=5)

    ax.set_title("Salary vs Experience Linear Regression")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary ($)")
    ax.legend()

    save_and_show(fig, filename="unit2_q04_salary_prediction_5_years.png", interactive=interactive)
    return pred_salary, metrics


if __name__ == "__main__":
    run_q2_diabetes_regression(interactive=False)
    run_q3_six_case_predictions(interactive=False)
    run_q4_predict_salary_5_years(years=5.0, interactive=False)
