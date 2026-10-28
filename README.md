# Machine Learning Practical & Journal Solutions

> **Simple, Essential & Exam-Ready Machine Learning Code**  
> Covers the complete University Syllabus (Units 1 to 4) and all Journal Questions.  
> Every script is self-contained, 15–30 lines of code, and easy to memorize for practical exams.

---

## 📁 Repository Structure

```
test/
├── ml/
│   ├── data/                                             # All CSV datasets
│   │   ├── auto.csv
│   │   ├── FuelConsumption.csv
│   │   ├── heart.csv
│   │   ├── insaurance_Practical_3.csv
│   │   ├── insurance_data.csv
│   │   ├── people.csv
│   │   ├── position_salary.csv
│   │   ├── salaries.csv
│   │   ├── Salary_Data.csv
│   │   ├── shopping-data.csv
│   │   └── titanic.csv
│   │
│   ├── 01_split_iris_dataset.py                          # Q1: Split Iris dataset
│   ├── 02_simple_linear_regression_diabetes.py           # Q2: SLR on Diabetes (MSE & R2)
│   ├── 03_linear_regression_predictions.py               # Q3: 6 Bivariate Predictions
│   ├── 04_predict_salary_5_years_exp.py                  # Q4: Predict Salary for 5 Yrs Exp
│   ├── 05_multiple_linear_regression_california.py       # Q5: MLR on California Housing
│   ├── 06_multiple_linear_regression_fuel_consumption.py # Q6: MLR on Fuel Consumption
│   ├── 07_multiple_linear_regression_insurance.py        # Q7: MLR on Insurance Charges
│   ├── 08_polynomial_regression_position_salary.py       # Q8: Polynomial on Position Salary
│   ├── 09_polynomial_regression_auto.py                  # Q9: Polynomial on Auto Dataset
│   ├── 10_logistic_regression_insurance.py               # Q10: Logistic Regression on Insurance
│   ├── 11_logistic_regression_heart.py                   # Q11: Logistic Regression on Heart Disease
│   ├── 12_decision_tree_salaries.py                      # Bullet 1: Decision Tree on Salaries
│   ├── 13_decision_tree_titanic.py                       # Bullet 2: Decision Tree on Titanic
│   ├── 14_svm_iris.py                                    # Bullet 3 & 4: SVM on Iris & Prediction
│   ├── 15_knn_iris.py                                    # Bullet 5, 6 & 7: KNN on Iris & Scaling
│   ├── 16_kmeans_people.py                               # Bullet 8: K-Means on People Dataset
│   ├── 17_kmeans_iris_elbow.py                           # Bullet 9: K-Means on Iris with Elbow Plot
│   └── 18_hierarchical_clustering_shopping.py            # Bullet 10: Agglomerative Clustering & Dendrogram
│
├── requirements.txt                                      # Python packages
└── README.md                                             # Practical guide & mapping
```

---

## 📑 Journal Questions & Script Mapping

| # | Question / Practical Prompt | Script Name | Dataset Used |
| :---: | :--- | :--- | :--- |
| **Q1** | Split iris dataset and print features and target. | `ml/01_split_iris_dataset.py` | Scikit-learn Iris |
| **Q2** | Simple Linear Regression on diabetes dataset (R2 score, MSE, Visualization). | `ml/02_simple_linear_regression_diabetes.py` | Scikit-learn Diabetes |
| **Q3** | Linear Regression and predict new value for 6 pairs (Age/Height, Std/%, Height/Shoe, Exp/Salary, Hours/Score, Vehicle Age/Price). | `ml/03_linear_regression_predictions.py` | Built-in arrays |
| **Q4** | Linear Regression and predict salary for 5 years of experience. | `ml/04_predict_salary_5_years_exp.py` | `data/Salary_Data.csv` |
| **Q5** | Multiple Linear Regression using California Housing dataset (intercept & coefficients, visualization). | `ml/05_multiple_linear_regression_california.py` | Scikit-learn California |
| **Q6** | Multiple Linear Regression using Fuel consumption dataset (intercept, coefficients, accuracy, difference table, visualization). | `ml/06_multiple_linear_regression_fuel_consumption.py` | `data/FuelConsumption.csv` |
| **Q7** | Multiple Linear Regression using Insurance dataset (intercept, coefficients, R2 score, visualization). | `ml/07_multiple_linear_regression_insurance.py` | `data/insaurance_Practical_3.csv` |
| **Q8** | Polynomial Regression for predicting value using Position Salary dataset and perform visualization. | `ml/08_polynomial_regression_position_salary.py` | `data/position_salary.csv` |
| **Q9** | Polynomial Regression using Auto dataset (accuracy using R2 score and MSE, visualization). | `ml/09_polynomial_regression_auto.py` | `data/auto.csv` |
| **Q10** | Logistic Regression using Insurance dataset (bought insurance vs age, visualization). | `ml/10_logistic_regression_insurance.py` | `data/insurance_data.csv` |
| **Q11** | Logistic Regression using Heart dataset (accuracy, confusion matrix, visualization). | `ml/11_logistic_regression_heart.py` | `data/heart.csv` |
| **B1** | Decision Tree Classifier on Salaries dataset to predict salary (> $100k). | `ml/12_decision_tree_salaries.py` | `data/salaries.csv` |
| **B2** | Decision Tree Classifier on Titanic dataset to predict survival. | `ml/13_decision_tree_titanic.py` | `data/titanic.csv` |
| **B3 & B4** | SVM on Iris (display precision, recall, F1, support, and predict species of new flower). | `ml/14_svm_iris.py` | Scikit-learn Iris |
| **B5, B6, B7** | KNN on Iris (accuracy, feature scaling comparison, classification report, and predict species of new flower). | `ml/15_knn_iris.py` | Scikit-learn Iris |
| **B8** | K-Means Clustering on people (Age and Income) using `people.csv`. | `ml/16_kmeans_people.py` | `data/people.csv` |
| **B9** | K-Means on Iris using Petal Length and Width (scaling analysis & elbow plot for optimal K). | `ml/17_kmeans_iris_elbow.py` | Scikit-learn Iris |
| **B10** | Agglomerative Hierarchical Clustering on shopping data (dendrogram and scatter plot). | `ml/18_hierarchical_clustering_shopping.py` | `data/shopping-data.csv` |

---

## 🚀 How to Run

1. Navigate to the `ml/` directory:
   ```bash
   cd ml
   ```

2. Run any practical script directly:
   ```bash
   python 01_split_iris_dataset.py
   python 04_predict_salary_5_years_exp.py
   python 14_svm_iris.py
   python 17_kmeans_iris_elbow.py
   ```

Each script will print the metrics to the console, save a plot image (`.png`) in the current folder, and display the plot window with `plt.show()`.
