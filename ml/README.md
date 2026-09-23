# Machine Learning Practicals

This directory contains implementations for all 11 Machine Learning practical assignments using Python, Scikit-learn, Pandas, and Matplotlib.

## Setup Instructions
Install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## Practicals Overview

| # | Script Name | Algorithm / Topic | Dataset | Key Outputs |
|---|---|---|---|---|
| **1** | `01_split_iris_dataset.py` | Train-Test Split | Iris Dataset (`load_iris`) | Feature matrix, target vectors, 80/20 train/test shapes |
| **2** | `02_simple_linear_regression_diabetes.py` | Simple Linear Regression | Diabetes Dataset (`load_diabetes`) | R2 score, MSE, regression equation, `diabetes_regression.png` |
| **3** | `03_linear_regression_predictions.py` | Linear Regression on 6 Scenarios | Synthetic Real-World Pairs | Slope, intercept, predictions for: (i) Age/Height, (ii) Standard/%, (iii) Height/Shoe Size, (iv) Exp/Salary, (v) Hours/Score, (vi) Age/Resale Price. Output: `linear_regression_6_cases.png` |
| **4** | `04_predict_salary_5_years_exp.py` | Simple Linear Regression | `data/Salary_Data.csv` | Exact predicted salary for 5 years experience, R2 score, MSE, `salary_prediction_5_years.png` |
| **5** | `05_multiple_linear_regression_california.py` | Multiple Linear Regression | California Housing (`fetch_california_housing`) | Intercept, feature coefficients, R2 score, MSE, `california_housing_regression.png` |
| **6** | `06_multiple_linear_regression_fuel_consumption.py` | Multiple Linear Regression | `data/FuelConsumption.csv` | Intercept, coefficients, R2 accuracy, Actual vs Predicted differences, `fuel_consumption_regression.png` |
| **7** | `07_multiple_linear_regression_insurance.py` | Multiple Linear Regression | `data/insaurance_Practical_3.csv` | Intercept, feature coefficients, R2 score, `insurance_regression.png` |
| **8** | `08_polynomial_regression_position_salary.py` | Polynomial Regression (deg 4) | `data/position_salary.csv` | Linear vs Polynomial comparison, Level 6.5 predicted salary, `position_salary_polynomial_regression.png` |
| **9** | `09_polynomial_regression_auto.py` | Polynomial Regression | `data/auto.csv` | Accuracy using R2 score and MSE, fitted curve plot `auto_polynomial_regression.png` |
| **10** | `10_logistic_regression_insurance.py` | Logistic Regression (Binary) | `data/insurance_data.csv` | Sigmoid probability curve, decision boundary age, accuracy, confusion matrix, `insurance_logistic_regression.png` |
| **11** | `11_logistic_regression_heart.py` | Logistic Regression (Classification) | `data/heart.csv` | Feature scaling, Confusion matrix heatmap, ROC curve & AUC score, `heart_disease_logistic_regression.png` |

---

## Datasets
All custom and benchmark CSV datasets are located in the `data/` subdirectory:
- `data/Salary_Data.csv`
- `data/FuelConsumption.csv`
- `data/insaurance_Practical_3.csv`
- `data/position_salary.csv`
- `data/auto.csv`
- `data/insurance_data.csv`
- `data/heart.csv`

Every script also includes a built-in fallback data dictionary, ensuring that each script can run self-contained even if moved.
