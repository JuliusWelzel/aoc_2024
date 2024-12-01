import os
from pathlib import Path

def define_dir(root, *names):
    """Creates a directory and ensures it exists."""
    path = root
    for name in names:
        path = path / name  # use pathlib's '/' operator to join paths
    path.mkdir(parents=True, exist_ok=True)
    return path

# Get the current directory where the script is executed
dir_proj = Path.cwd().parent

# Define the paths for 'logs' and 'results' directories
dir_results = define_dir(dir_proj, "results")  # Results directory path
dir_data = define_dir(dir_proj, "data")  # data directory path