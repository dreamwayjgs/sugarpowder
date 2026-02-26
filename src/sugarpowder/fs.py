from pathlib import Path


def create_directory_recursive(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")
