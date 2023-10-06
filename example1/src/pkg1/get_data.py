import os
import numpy as np
import tifffile


def get_data() -> np.ndarray:
    package_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(package_dir, "data_file.tif")
    if not os.path.isfile(data_file):
        raise OSError(f"file not found: {data_file} (package_dir = {package_dir})")
    return tifffile.imread(data_file)
