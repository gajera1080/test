"""
Dual-mode plotting utility for Machine Learning scripts.
Saves high-resolution plots to disk and displays interactively if a GUI is supported.
"""

import os
import sys
import warnings

# Suppress GTK/system module warnings
warnings.filterwarnings("ignore")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import matplotlib
import matplotlib.pyplot as plt

# Auto-detect display environment
HAS_DISPLAY = bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))
if not HAS_DISPLAY:
    # Use non-interactive backend in headless environments to avoid errors
    try:
        matplotlib.use("Agg")
    except Exception:
        pass


def set_plot_style():
    """Apply standard clean styling for academic and journal plots."""
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except Exception:
        plt.style.use("default")
        plt.grid(True, linestyle="--", alpha=0.6)


def save_and_show(fig=None, filename="plot.png", title=None, interactive=True):
    """
    Saves figure to outputs/ directory and displays interactively if GUI is present.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure, optional
        The figure to save. If None, uses plt.gcf().
    filename : str
        Name of the file to save in outputs/ folder.
    title : str, optional
        Console log message to print.
    interactive : bool
        Whether to attempt plt.show() if GUI is available.
    """
    if fig is None:
        fig = plt.gcf()

    # Determine outputs directory relative to project root
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(curr_dir, ".."))
    out_dir = os.path.join(project_root, "outputs")
    os.makedirs(out_dir, exist_ok=True)

    if not filename.endswith(".png"):
        filename += ".png"
    out_path = os.path.join(out_dir, filename)

    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    print(f" [Plot Saved] -> outputs/{filename}")

    if interactive and HAS_DISPLAY:
        try:
            plt.show()
        except Exception as e:
            print(f" [Note] Display unavailable ({e}); plot saved cleanly to disk.")
    else:
        plt.close(fig)

    return out_path
