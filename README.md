# Machine Learning Laboratory & Journal Solutions

> **Academic ML Practical Suite & University Exam Preparation Framework**  
> Aligned with the University Syllabus (Units 1 to 4) and Complete Journal Practical Questions.

---

## 📑 Table of Contents
1. [Overview & Repository Architecture](#overview--repository-architecture)
2. [Syllabus to Module Mapping](#syllabus-to-module-mapping)
3. [Journal Questions & Code Mapping Table](#journal-questions--code-mapping-table)
4. [Installation & Requirements](#installation--requirements)
5. [How to Run](#how-to-run)
   - [Interactive Terminal Menu](#1-interactive-terminal-menu)
   - [Command-Line Execution](#2-command-line-execution)
   - [University Exam Custom Simulator](#3-university-exam-custom-simulator)
6. [Datasets Included](#datasets-included)
7. [Visualizations Gallery](#visualizations-gallery)
8. [University Exam & Viva Voce Question Bank](#university-exam--viva-voce-question-bank)

---

## 🏛️ Overview & Repository Architecture

This repository contains a modular, exam-ready implementation of the complete Machine Learning syllabus. Rather than duplicating boilerplate code across multiple disconnected files, the project is structured into cohesive unit modules backed by reusable evaluation and plotting utilities.

```
test/
├── data/                                 # All datasets (CSV format)
│   ├── Salary_Data.csv
│   ├── auto.csv
│   ├── FuelConsumption.csv
│   ├── heart.csv
│   ├── insaurance_Practical_3.csv
│   ├── insurance_data.csv
│   ├── people.csv
│   ├── position_salary.csv
│   ├── salaries.csv
│   ├── shopping-data.csv
│   └── titanic.csv
├── outputs/                              # Automatically generated high-res plots
├── unit1_foundations/                    # Unit 1: Foundations & Workflows
│   └── ml_workflow_and_libraries.py
├── unit2_regression/                     # Unit 2: Regression Analysis
│   ├── simple_linear_regression.py
│   ├── multiple_linear_regression.py
│   ├── polynomial_and_nonlinear_regression.py
│   └── logistic_regression.py
├── unit3_supervised_unsupervised/        # Unit 3: Classification & Clustering
│   ├── decision_and_regression_trees.py
│   ├── support_vector_machine.py
│   ├── k_nearest_neighbors.py
│   ├── kmeans_clustering.py
│   └── hierarchical_clustering.py
├── unit4_evaluation/                     # Unit 4: Metrics, Validation & Pitfalls
│   ├── model_evaluation_metrics.py
│   └── validation_and_pitfalls.py
├── utils/                                # Reusable Utilities (Zero Code Duplication)
│   ├── data_loader.py                    # Dataset resolver & loader
│   ├── evaluator.py                      # Standardized metrics printer
│   └── plot_helper.py                    # Dual-mode save and show utility
├── main.py                               # Master CLI runner & interactive menu
├── run.py                                # Convenience executable entry point
├── requirements.txt                      # Pinned Python package dependencies
└── README.md                             # Comprehensive documentation & viva guide
```

---

## 📚 Syllabus to Module Mapping

| Unit | Syllabus Topics | Implemented Module | Key Concepts Demonstrated |
| :--- | :--- | :--- | :--- |
| **Unit 1** | 1.1 Intro to ML, Need, Challenges, Real-World Apps<br>1.2 Types of ML (Supervised, Unsupervised, Semi, RL)<br>1.3 ML Workflow<br>1.5 Libraries (NumPy, Pandas, Scikit-learn) | `unit1_foundations/ml_workflow_and_libraries.py` | Matrix operations, DataFrame manipulation, Train/Test split, feature distributions. |
| **Unit 2** | 2.1-2.3 Simple Linear Regression (OLS, Formula)<br>2.4 Multiple Linear Regression<br>2.5 Polynomial & Non-linear Regression<br>2.6 Introduction to Logistic Regression | `unit2_regression/simple_linear_regression.py`<br>`unit2_regression/multiple_linear_regression.py`<br>`unit2_regression/polynomial_and_nonlinear_regression.py`<br>`unit2_regression/logistic_regression.py` | Slope & intercept formulas, multi-feature coefficients, $R^2$ / MSE, Sigmoid curve, decision thresholds. |
| **Unit 3** | 3.1-3.2 Decision Tree Classifier<br>3.3 Regression Trees<br>3.4 Support Vector Machines (SVM)<br>3.5 K-Nearest Neighbors (KNN)<br>3.6 K-Means & Hierarchical Clustering | `unit3_supervised_unsupervised/decision_and_regression_trees.py`<br>`unit3_supervised_unsupervised/support_vector_machine.py`<br>`unit3_supervised_unsupervised/k_nearest_neighbors.py`<br>`unit3_supervised_unsupervised/kmeans_clustering.py`<br>`unit3_supervised_unsupervised/hierarchical_clustering.py` | Gini impurity, entropy, tree rules, maximal margin, support vectors, RBF kernel, majority voting, scaling impact, elbow method, dendrogram cuts. |
| **Unit 4** | 4.1 Classification Metrics<br>4.2 Regression Metrics<br>4.3 Unsupervised Heuristics<br>4.4 Data Leakage & Validation Pitfalls | `unit4_evaluation/model_evaluation_metrics.py`<br>`unit4_evaluation/validation_and_pitfalls.py` | Confusion Matrix, ROC-AUC, MAE, MSE, RMSE, $R^2$, Silhouette Score, K-Fold CV, Scikit-learn Pipelines vs Data Leakage. |

---

## 📋 Journal Questions & Code Mapping Table

| Question # | Journal Question Description | Module / Function | Output Visualization |
| :---: | :--- | :--- | :--- |
| **Q1** | Split Iris dataset and print features and target. | `unit1_foundations/ml_workflow_and_libraries.py`<br>`solve_journal_q1()` | `outputs/unit1_q01_iris_split_visualization.png` |
| **Q2** | Simple Linear Regression on Diabetes dataset (find $R^2$ & MSE, perform visualization). | `unit2_regression/simple_linear_regression.py`<br>`run_q2_diabetes_regression()` | `outputs/unit2_q02_diabetes_simple_regression.png` |
| **Q3** | Linear Regression on 6 bivariate relationships (Age-Height, Std-%, Height-Shoe, Exp-Salary, Hours-Score, Vehicle-Price) with prediction for new value. | `unit2_regression/simple_linear_regression.py`<br>`run_q3_six_case_predictions()` | `outputs/unit2_q03_six_case_regression_predictions.png` |
| **Q4** | Predict salary for 5 years of experience using `Salary_Data.csv`. | `unit2_regression/simple_linear_regression.py`<br>`run_q4_predict_salary_5_years()` | `outputs/unit2_q04_salary_prediction_5_years.png` |
| **Q5** | Multiple Linear Regression on California Housing dataset (print intercept & coefficients, visualization). | `unit2_regression/multiple_linear_regression.py`<br>`run_q5_california_housing_regression()` | `outputs/unit2_q05_california_housing_regression.png` |
| **Q6** | Multiple Linear Regression on Fuel Consumption dataset (accuracy, intercept, coefficients, actual vs predicted diff table). | `unit2_regression/multiple_linear_regression.py`<br>`run_q6_fuel_consumption_regression()` | `outputs/unit2_q06_fuel_consumption_regression.png` |
| **Q7** | Multiple Linear Regression on Insurance dataset (`insaurance_Practical_3.csv`) (intercept, coefficients, $R^2$ score). | `unit2_regression/multiple_linear_regression.py`<br>`run_q7_insurance_regression()` | `outputs/unit2_q07_insurance_charges_regression.png` |
| **Q8** | Polynomial Regression on `position_salary.csv` (predictions, smooth curve visualization). | `unit2_regression/polynomial_and_nonlinear_regression.py`<br>`run_q8_position_salary_polynomial_regression()` | `outputs/unit2_q08_position_salary_polynomial.png` |
| **Q9** | Polynomial Regression on `auto.csv` (accuracy using $R^2$ and MSE, visualization). | `unit2_regression/polynomial_and_nonlinear_regression.py`<br>`run_q9_auto_polynomial_regression()` | `outputs/unit2_q09_auto_polynomial_regression.png` |
| **Q10** | Logistic Regression on Insurance dataset (`insurance_data.csv`) (predicting bought insurance by age, visualization). | `unit2_regression/logistic_regression.py`<br>`run_q10_insurance_logistic_regression()` | `outputs/unit2_q10_insurance_logistic_regression.png` |
| **Q11** | Logistic Regression on Heart dataset (`heart.csv`) (multi-feature classification, visualization). | `unit2_regression/logistic_regression.py`<br>`run_q11_heart_disease_logistic_regression()` | `outputs/unit2_q11_heart_disease_logistic_regression.png` |
| **b1** | Decision Tree Classifier on `salaries.csv` to predict salary (> $100k). | `unit3_supervised_unsupervised/decision_and_regression_trees.py`<br>`run_decision_tree_salaries()` | `outputs/unit3_dt_salaries_tree.png` |
| **b2** | Decision Tree Classifier on `titanic.csv` to predict survival. | `unit3_supervised_unsupervised/decision_and_regression_trees.py`<br>`run_decision_tree_titanic()` | `outputs/unit3_dt_titanic_survival.png` |
| **b3** | SVM Classifier on Iris displaying Precision, Recall, F1-Score, and Support for each class (setosa, versicolor, virginica). | `unit3_supervised_unsupervised/support_vector_machine.py`<br>`run_svm_iris_classification()` | `outputs/unit3_svm_iris_confusion_matrix.png` |
| **b4** | SVM Classifier for predicting species of new Iris flowers. | `unit3_supervised_unsupervised/support_vector_machine.py`<br>`run_svm_predict_new_flower()` | `outputs/unit3_svm_decision_boundaries_2d.png` |
| **b5** | KNN Classification on Iris displaying accuracy. | `unit3_supervised_unsupervised/k_nearest_neighbors.py`<br>`run_bullet5_knn_iris_accuracy()` | (Console Accuracy Output) |
| **b6** | KNN on Iris with feature scaling vs without scaling and detailed classification report for all three classes. | `unit3_supervised_unsupervised/k_nearest_neighbors.py`<br>`run_bullet6_knn_with_scaling()` | `outputs/unit3_knn_iris_evaluation.png` |
| **b7** | KNN Classifier for predicting species of new Iris flowers. | `unit3_supervised_unsupervised/k_nearest_neighbors.py`<br>`run_bullet7_knn_predict_species()` | (Console Prediction Output) |
| **b8** | K-Means Clustering on `people.csv` (Age vs Income) to group people into clusters. | `unit3_supervised_unsupervised/kmeans_clustering.py`<br>`run_bullet8_kmeans_people()` | `outputs/unit3_kmeans_bullet8_people.png` |
| **b9** | K-Means on Iris using Petal Length and Petal Width (scaling analysis & elbow plot for optimal K). | `unit3_supervised_unsupervised/kmeans_clustering.py`<br>`run_bullet9_kmeans_iris_elbow()` | `outputs/unit3_kmeans_bullet9_iris_elbow.png` |
| **b10** | Agglomerative Hierarchical Clustering on `shopping-data.csv` (dendrogram with threshold cut line & scatter plot). | `unit3_supervised_unsupervised/hierarchical_clustering.py`<br>`run_bullet10_hierarchical_shopping()` | `outputs/unit3_hierarchical_shopping_dendrogram.png` |

---

## ⚙️ Installation & Requirements

Ensure Python 3.9+ is installed. Install all necessary dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 1. Interactive Terminal Menu
Run either `main.py` or `run.py` without arguments:
```bash
python main.py
# or
python run.py
```
This opens an interactive text menu with options:
- Run by Unit (1, 2, 3, 4)
- Run by Journal Question Key (`1` to `11`, `b1` to `b10`)
- University Exam Custom Predictor (interactive input)
- Run ALL practicals in sequence

### 2. Command-Line Execution
Run any specific question or unit directly via command line flags:
```bash
# Run a specific unit
python main.py --unit 2

# Run a specific journal question (e.g., Q4 Salary 5 years, Q8 Polynomial, b3 SVM, b9 K-Means Elbow)
python main.py --question 4
python main.py --question 8
python main.py --question b3
python main.py --question b9

# Run all experiments non-interactively (headless mode, saves all plots to outputs/)
python main.py --all --headless
```

### 3. Individual Script Execution
Every script can also be executed completely independently:
```bash
python unit1_foundations/ml_workflow_and_libraries.py
python unit2_regression/simple_linear_regression.py
python unit2_regression/multiple_linear_regression.py
python unit2_regression/polynomial_and_nonlinear_regression.py
python unit2_regression/logistic_regression.py
python unit3_supervised_unsupervised/decision_and_regression_trees.py
python unit3_supervised_unsupervised/support_vector_machine.py
python unit3_supervised_unsupervised/k_nearest_neighbors.py
python unit3_supervised_unsupervised/kmeans_clustering.py
python unit3_supervised_unsupervised/hierarchical_clustering.py
python unit4_evaluation/model_evaluation_metrics.py
python unit4_evaluation/validation_and_pitfalls.py
```

---

## 📊 Datasets Included

All datasets reside self-contained inside the `data/` folder:
- **`Salary_Data.csv`**: Years of experience vs Salary (for Simple Linear Regression & Regression Tree).
- **`FuelConsumption.csv`**: Engine size, cylinders, fuel consumption vs CO2 emissions.
- **`insaurance_Practical_3.csv`**: Medical charges based on age, sex, bmi, children, smoker, region.
- **`insurance_data.csv`**: Binary purchase decision (bought_insurance: 0/1) based on age.
- **`position_salary.csv`**: Position level (1 to 10) vs Salary for Polynomial Regression.
- **`auto.csv`**: Horsepower, weight, acceleration vs MPG for non-linear regression.
- **`heart.csv`**: Clinical cardiac measurements vs Heart disease diagnosis.
- **`people.csv`**: Name, Age, Income (for K-Means customer segmentation).
- **`salaries.csv`**: Company, job, degree vs Salary > $100k (for Decision Tree classification).
- **`titanic.csv`**: Passenger demographics and fare vs Survival status.
- **`shopping-data.csv`** (and `hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv`): Annual income vs spending score for Agglomerative Hierarchical Clustering.

---

## 🎓 University Exam & Viva Voce Question Bank

### Unit 1: Foundations of Machine Learning
**Q1: What is the fundamental difference between Supervised, Unsupervised, and Reinforcement Learning?**
- **Supervised Learning**: Learns from labeled datasets $(X, y)$ to map inputs to continuous targets (regression) or discrete categories (classification).
- **Unsupervised Learning**: Discovers hidden structures, patterns, or clusters in unlabeled data $(X)$ without prior targets.
- **Reinforcement Learning**: An agent interacts with an environment through trial and error, learning an optimal policy to maximize cumulative rewards.

**Q2: Why is Train-Test Split essential in Machine Learning?**
- If a model is evaluated on the exact data it was trained on, it can simply memorize the training examples (overfitting). Splitting data into disjoint training and testing sets measures how well the model generalizes to unseen data.

---

### Unit 2: Regression Analysis
**Q3: How does Ordinary Least Squares (OLS) find the best-fit line in Simple Linear Regression?**
- OLS minimizes the Sum of Squared Residuals (SSR):
  $$\text{SSR} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n (y_i - (mx_i + c))^2$$
  Setting partial derivatives with respect to $m$ and $c$ to zero yields the closed-form analytical solutions:
  $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \quad c = \bar{y} - m\bar{x}$$

**Q4: What is the difference between $R^2$ and Adjusted $R^2$?**
- **$R^2$ (Coefficient of Determination)**: Proportion of variance in $y$ explained by the features ($1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$). Adding any feature (even useless noise) will always increase or keep $R^2$ constant.
- **Adjusted $R^2$**: Penalizes models for adding irrelevant predictors:
  $$\text{Adjusted } R^2 = 1 - \left[\frac{(1 - R^2)(n - 1)}{n - p - 1}\right]$$
  where $n$ is sample size and $p$ is the number of predictors.

**Q5: Why can't we use Linear Regression for Binary Classification, and why is the Sigmoid function used?**
- Linear regression predictions can exceed $[0, 1]$ (producing probabilities $<0$ or $>1$) and linear regression is highly sensitive to outliers.
- Logistic regression passes the linear combination $z = \beta^T X$ through the **Sigmoid function**:
  $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
  which smoothly squashes any real number $z \in (-\infty, +\infty)$ into a valid probability $p \in [0, 1]$.

---

### Unit 3: Supervised & Unsupervised Models
**Q6: How does a Decision Tree decide which feature to split on?**
- It calculates the impurity before and after splitting. The feature yielding the highest **Information Gain** (reduction in impurity) is selected.
  - **Gini Impurity**: $G = 1 - \sum_{i=1}^C p_i^2$ (computationally faster)
  - **Entropy**: $H = -\sum_{i=1}^C p_i \log_2(p_i)$

**Q7: What are Support Vectors in SVM, and what is the Kernel Trick?**
- **Support Vectors**: The critical data points closest to the separating hyperplane that define the margin. Moving any non-support vector does not alter the decision boundary.
- **Kernel Trick**: Enables SVM to find linear hyperplanes in a transformed higher-dimensional space without explicitly calculating coordinates in that space, via kernel functions such as Radial Basis Function (RBF):
  $$K(x, x') = \exp\left(-\gamma \|x - x'\|^2\right)$$

**Q8: Why is Feature Scaling mandatory for KNN and K-Means?**
- Both KNN and K-Means rely on distance metrics (e.g. Euclidean distance $d = \sqrt{\sum (x_i - y_i)^2}$). If one feature has values in thousands (e.g. Income) and another in single digits (e.g. Age), the larger feature will disproportionately dominate the distance calculation unless normalized (using StandardScaler or MinMaxScaler).

**Q9: How do you determine the optimal number of clusters ($K$) in K-Means?**
- **Elbow Method**: Plot Within-Cluster Sum of Squares (Inertia) against $K$. The optimal $K$ is located at the 'elbow bend' where adding further clusters yields diminishing reductions in inertia.
- **Silhouette Analysis**: Measures how similar an object is to its own cluster compared to neighboring clusters (ranging from -1 to +1). Peak silhouette indicates optimal cluster compactness and separation.

**Q10: What is a Dendrogram in Agglomerative Hierarchical Clustering?**
- A tree-like diagram recording the sequence of merges or splits. The vertical axis represents the Euclidean distance (dissimilarity) at which clusters were joined. Cutting horizontally across the tallest vertical lines that do not cross horizontal cluster lines reveals the optimal number of clusters.

---

### Unit 4: Evaluation, Validation & Data Leakage
**Q11: Define Precision, Recall, and F1-Score.**
- **Precision**: $\frac{\text{TP}}{\text{TP} + \text{FP}}$ — Out of all predicted positive cases, how many were actually positive? (Crucial for spam filtering).
- **Recall (Sensitivity)**: $\frac{\text{TP}}{\text{TP} + \text{FN}}$ — Out of all actual positive cases, how many did the model capture? (Crucial for medical diagnosis).
- **F1-Score**: Harmonic mean of Precision and Recall:
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Q12: What is Data Leakage, and how does Scikit-Learn Pipeline prevent it?**
- **Data Leakage** occurs when information from outside the training dataset (such as mean/std from the test set or future data) leaks into model training.
- *Example*: Calling `scaler.fit_transform(X)` on the entire dataset before `train_test_split` leaks the global mean and variance into the training phase, giving falsely optimistic accuracy.
- *Prevention*: Always use `sklearn.pipeline.Pipeline`:
  ```python
  pipeline = Pipeline([
      ('scaler', StandardScaler()),
      ('model', LogisticRegression())
  ])
  pipeline.fit(X_train, y_train)  # Scaler strictly learns parameters from X_train only!
  ```
