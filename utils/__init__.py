"""
Machine Learning Utility Package
Provides dataset loaders, standardized evaluation printers, and dual-mode plot handlers.
"""

from .data_loader import get_dataset_path, load_dataset
from .evaluator import (
    print_regression_metrics,
    print_classification_metrics,
    print_clustering_metrics,
    print_coefficients,
)
from .plot_helper import save_and_show, set_plot_style

__all__ = [
    "get_dataset_path",
    "load_dataset",
    "print_regression_metrics",
    "print_classification_metrics",
    "print_clustering_metrics",
    "print_coefficients",
    "save_and_show",
    "set_plot_style",
]
