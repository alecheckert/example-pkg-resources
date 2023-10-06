import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(data_file: str) -> str:
    return os.path.join(PACKAGE_DIR, data_file)
