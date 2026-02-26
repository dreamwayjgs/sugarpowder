import sys
import os


def add_path():
    """
    Add the project root directory to sys.path.

    Useful in Jupyter notebooks where the working directory
    is not the project root and local imports fail.
    """
    current_path = os.path.dirname(os.path.abspath("__file__"))
    root_path = os.path.join(current_path, "..")
    sys.path.append(root_path)
