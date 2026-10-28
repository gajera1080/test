"""
Dataset loading utility for ML experiments.
Locates datasets from the project's data/ directory consistently.
"""

import os
import pandas as pd


def get_project_root():
    """Return the absolute path to the project root directory."""
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(curr_dir, ".."))


def get_dataset_path(filename):
    """
    Returns the absolute path to a file inside the data/ folder.
    Raises FileNotFoundError if file is not found.
    """
    root = get_project_root()
    path = os.path.join(root, "data", filename)
    if not os.path.exists(path):
        # Check alternative common names
        alt_names = {
            "shopping-data.csv": "hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv",
            "hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv": "shopping-data.csv",
            "insurance.csv": "insaurance_Practical_3.csv",
        }
        if filename in alt_names:
            alt_path = os.path.join(root, "data", alt_names[filename])
            if os.path.exists(alt_path):
                return alt_path
        raise FileNotFoundError(f"Dataset '{filename}' not found in {os.path.join(root, 'data')}")
    return path


def load_dataset(filename, verbose=True):
    """
    Load a CSV dataset by filename and return a pandas DataFrame.
    """
    path = get_dataset_path(filename)
    df = pd.read_csv(path)
    if verbose:
        print(f" Loaded '{filename}' (Shape: {df.shape[0]} rows, {df.shape[1]} columns)")
    return df
