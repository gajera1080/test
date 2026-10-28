#!/usr/bin/env python3
"""
================================================================================
MACHINE LEARNING PRACTICAL SUITE & INTERACTIVE RUNNER
================================================================================
Covers Complete Syllabus (Units 1 - 4) & All Journal Questions (Q1-Q11 + Bullets)
"""

import sys
import os
import argparse

# Add repository root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Unit 1 imports
from unit1_foundations.ml_workflow_and_libraries import (
    solve_journal_q1, print_unit1_theory_summary, demonstrate_core_libraries
)

# Unit 2 imports
from unit2_regression.simple_linear_regression import (
    run_q2_diabetes_regression, run_q3_six_case_predictions, run_q4_predict_salary_5_years
)
from unit2_regression.multiple_linear_regression import (
    run_q5_california_housing_regression, run_q6_fuel_consumption_regression, run_q7_insurance_regression
)
from unit2_regression.polynomial_and_nonlinear_regression import (
    run_q8_position_salary_polynomial_regression, run_q9_auto_polynomial_regression
)
from unit2_regression.logistic_regression import (
    run_q10_insurance_logistic_regression, run_q11_heart_disease_logistic_regression
)

# Unit 3 imports
from unit3_supervised_unsupervised.decision_and_regression_trees import (
    run_decision_tree_salaries, run_decision_tree_titanic, run_regression_tree_continuous
)
from unit3_supervised_unsupervised.support_vector_machine import (
    run_svm_iris_classification, run_svm_predict_new_flower, visualize_svm_decision_boundaries_2d
)
from unit3_supervised_unsupervised.k_nearest_neighbors import (
    run_bullet5_knn_iris_accuracy, run_bullet6_knn_with_scaling, run_bullet7_knn_predict_species
)
from unit3_supervised_unsupervised.kmeans_clustering import (
    run_bullet8_kmeans_people, run_bullet9_kmeans_iris_elbow
)
from unit3_supervised_unsupervised.hierarchical_clustering import (
    run_bullet10_hierarchical_shopping
)

# Unit 4 imports
from unit4_evaluation.model_evaluation_metrics import (
    demonstrate_classification_metrics, demonstrate_regression_metrics, demonstrate_unsupervised_metrics
)
from unit4_evaluation.validation_and_pitfalls import (
    demonstrate_data_leakage, demonstrate_cross_validation_and_learning_curves
)


QUESTION_MAP = {
    "1": ("Q1: Split Iris dataset & print features/target", lambda inter: solve_journal_q1(interactive=inter)),
    "2": ("Q2: Simple Linear Regression on Diabetes dataset", lambda inter: run_q2_diabetes_regression(interactive=inter)),
    "3": ("Q3: Linear Regression on 6 bivariate pairs with predictions", lambda inter: run_q3_six_case_predictions(interactive=inter)),
    "4": ("Q4: Predict salary for 5 years experience (Salary_Data.csv)", lambda inter: run_q4_predict_salary_5_years(years=5.0, interactive=inter)),
    "5": ("Q5: Multiple Linear Regression on California Housing", lambda inter: run_q5_california_housing_regression(interactive=inter)),
    "6": ("Q6: Multiple Linear Regression on Fuel Consumption dataset", lambda inter: run_q6_fuel_consumption_regression(interactive=inter)),
    "7": ("Q7: Multiple Linear Regression on Insurance dataset (R2 score)", lambda inter: run_q7_insurance_regression(interactive=inter)),
    "8": ("Q8: Polynomial Regression on position_salary.csv", lambda inter: run_q8_position_salary_polynomial_regression(interactive=inter)),
    "9": ("Q9: Polynomial Regression on auto.csv (R2 and MSE)", lambda inter: run_q9_auto_polynomial_regression(interactive=inter)),
    "10": ("Q10: Logistic Regression on Insurance dataset", lambda inter: run_q10_insurance_logistic_regression(interactive=inter)),
    "11": ("Q11: Logistic Regression on Heart disease dataset", lambda inter: run_q11_heart_disease_logistic_regression(interactive=inter)),
    "b1": ("Bullet 1: Decision Tree on Salaries dataset (>100k)", lambda inter: run_decision_tree_salaries(interactive=inter)),
    "b2": ("Bullet 2: Decision Tree on Titanic dataset", lambda inter: run_decision_tree_titanic(interactive=inter)),
    "b3": ("Bullet 3: SVM on Iris with precision/recall/F1/support", lambda inter: run_svm_iris_classification(interactive=inter)),
    "b4": ("Bullet 4: SVM predicting species of new Iris flowers", lambda inter: run_svm_predict_new_flower()),
    "b5": ("Bullet 5: KNN classification accuracy on Iris", lambda inter: run_bullet5_knn_iris_accuracy()),
    "b6": ("Bullet 6: KNN on Iris with feature scaling & report", lambda inter: run_bullet6_knn_with_scaling(interactive=inter)),
    "b7": ("Bullet 7: KNN predicting species of new Iris flowers", lambda inter: run_bullet7_knn_predict_species()),
    "b8": ("Bullet 8: K-Means Clustering on people.csv (Age & Income)", lambda inter: run_bullet8_kmeans_people(interactive=inter)),
    "b9": ("Bullet 9: K-Means on Iris (scaling analysis & elbow plot)", lambda inter: run_bullet9_kmeans_iris_elbow(interactive=inter)),
    "b10": ("Bullet 10: Agglomerative Hierarchical Clustering (Dendrogram & Scatter)", lambda inter: run_bullet10_hierarchical_shopping(interactive=inter)),
}


def run_unit(unit_num, interactive=True):
    print(f"\n=======================================================")
    print(f" >>> RUNNING COMPLETE PRACTICALS FOR UNIT {unit_num} <<<")
    print(f"=======================================================")
    if unit_num == 1:
        print_unit1_theory_summary()
        demonstrate_core_libraries()
        solve_journal_q1(interactive=interactive)
    elif unit_num == 2:
        run_q2_diabetes_regression(interactive=interactive)
        run_q3_six_case_predictions(interactive=interactive)
        run_q4_predict_salary_5_years(years=5.0, interactive=interactive)
        run_q5_california_housing_regression(interactive=interactive)
        run_q6_fuel_consumption_regression(interactive=interactive)
        run_q7_insurance_regression(interactive=interactive)
        run_q8_position_salary_polynomial_regression(interactive=interactive)
        run_q9_auto_polynomial_regression(interactive=interactive)
        run_q10_insurance_logistic_regression(interactive=interactive)
        run_q11_heart_disease_logistic_regression(interactive=interactive)
    elif unit_num == 3:
        run_decision_tree_salaries(interactive=interactive)
        run_decision_tree_titanic(interactive=interactive)
        run_regression_tree_continuous(interactive=interactive)
        run_svm_iris_classification(interactive=interactive)
        run_svm_predict_new_flower()
        visualize_svm_decision_boundaries_2d(interactive=interactive)
        run_bullet5_knn_iris_accuracy()
        run_bullet6_knn_with_scaling(interactive=interactive)
        run_bullet7_knn_predict_species()
        run_bullet8_kmeans_people(interactive=interactive)
        run_bullet9_kmeans_iris_elbow(interactive=interactive)
        run_bullet10_hierarchical_shopping(interactive=interactive)
    elif unit_num == 4:
        demonstrate_classification_metrics(interactive=interactive)
        demonstrate_regression_metrics(interactive=interactive)
        demonstrate_unsupervised_metrics(interactive=interactive)
        demonstrate_data_leakage()
        demonstrate_cross_validation_and_learning_curves(interactive=interactive)


def run_all(interactive=False):
    print("\n" + "#" * 70)
    print(" EXECUTING ENTIRE MACHINE LEARNING SYLLABUS & JOURNAL SUITE")
    print("#" * 70)
    for u in [1, 2, 3, 4]:
        run_unit(u, interactive=interactive)
    print("\n" + "=" * 70)
    print(" ALL PRACTICALS COMPLETED! Generated plots saved in 'outputs/' folder.")
    print("=" * 70)


def interactive_menu():
    while True:
        print("\n" + "=" * 65)
        print(" MACHINE LEARNING LAB & JOURNAL INTERACTIVE MASTER MENU")
        print("=" * 65)
        print(" 1. Run by Syllabus Unit (Unit 1, 2, 3, or 4)")
        print(" 2. Run by Journal Question (Q1 to Q11, Bullets b1 to b10)")
        print(" 3. University Exam Interactive Predictor (Custom Inputs)")
        print(" 4. Run ALL Experiments & Generate Full Plot Suite")
        print(" 0. Exit")
        print("=" * 65)

        choice = input("Enter your choice (0-4): ").strip()
        if choice == "0":
            print("\nExiting. Good luck with your Machine Learning exams!\n")
            break
        elif choice == "1":
            u_choice = input("Enter Unit number (1, 2, 3, 4): ").strip()
            if u_choice in ["1", "2", "3", "4"]:
                run_unit(int(u_choice), interactive=True)
            else:
                print("Invalid Unit number!")
        elif choice == "2":
            print("\nAvailable Questions:")
            for k, (desc, _) in QUESTION_MAP.items():
                print(f" [{k:>3}] {desc}")
            q_choice = input("\nEnter Question Key (e.g., 4, 8, b3, b9): ").strip().lower()
            if q_choice in QUESTION_MAP:
                QUESTION_MAP[q_choice][1](True)
            else:
                print(f"Question '{q_choice}' not recognized!")
        elif choice == "3":
            print("\n--- UNIVERSITY EXAM SIMULATOR ---")
            print("a) Custom Salary Prediction for any Years of Experience")
            print("b) Custom Iris Flower Species Prediction (SVM & KNN)")
            print("c) Custom Insurance Probability by Age")
            sim_choice = input("Select simulation (a/b/c): ").strip().lower()
            if sim_choice == "a":
                try:
                    exp = float(input("Enter years of experience (e.g. 3.5, 7.2): "))
                    run_q4_predict_salary_5_years(years=exp, interactive=True)
                except ValueError:
                    print("Invalid numerical input.")
            elif sim_choice == "b":
                try:
                    sl = float(input("Sepal Length in cm (e.g. 5.1): "))
                    sw = float(input("Sepal Width in cm (e.g. 3.5): "))
                    pl = float(input("Petal Length in cm (e.g. 1.4): "))
                    pw = float(input("Petal Width in cm (e.g. 0.2): "))
                    custom_sample = [{"sample": "Exam Custom Sample", "features": [sl, sw, pl, pw]}]
                    run_svm_predict_new_flower(new_measurements=custom_sample)
                except ValueError:
                    print("Invalid measurements.")
            elif sim_choice == "c":
                try:
                    age = float(input("Enter Age (e.g. 42): "))
                    from unit2_regression.logistic_regression import run_q10_insurance_logistic_regression
                    m, _ = run_q10_insurance_logistic_regression(interactive=False)
                    prob = m.predict_proba([[age]])[0][1]
                    print(f"\nResult: For Age {age}, Purchase Probability = {prob:.4f} ({prob*100:.1f}%)")
                    print(f"Prediction: {'Will Buy Insurance' if prob >= 0.5 else 'Will NOT Buy Insurance'}")
                except ValueError:
                    print("Invalid age.")
        elif choice == "4":
            run_all(interactive=False)
        else:
            print("Invalid selection. Please choose an option from the menu.")


def main():
    parser = argparse.ArgumentParser(description="Machine Learning Syllabus & Journal Runner")
    parser.add_argument("--all", action="store_true", help="Run all experiments and generate all plots")
    parser.add_argument("--unit", type=int, choices=[1, 2, 3, 4], help="Run all practicals for a specific unit")
    parser.add_argument("--question", type=str, help="Run a specific journal question (1..11 or b1..b10)")
    parser.add_argument("--headless", action="store_true", help="Run without opening interactive GUI windows")

    args = parser.parse_args()

    interactive = not args.headless

    if args.all:
        run_all(interactive=interactive)
    elif args.unit:
        run_unit(args.unit, interactive=interactive)
    elif args.question:
        q_key = args.question.lower()
        if q_key in QUESTION_MAP:
            QUESTION_MAP[q_key][1](interactive)
        else:
            print(f"Question '{args.question}' not recognized. Choose from: {list(QUESTION_MAP.keys())}")
    else:
        # If no arguments provided, launch interactive menu
        interactive_menu()


if __name__ == "__main__":
    main()
