import os
import setuptools
from pybind11.setup_helpers import Pybind11Extension, build_ext


SRC_FILES = [os.path.join("src", f) for f in ["module.cpp"]]
INC_DIRS = ["src"]

ext_modules = [
    Pybind11Extension(
        "_pkg3",
        SRC_FILES,
        include_dirs=INC_DIRS,
        libraries=[],
        library_dirs=[],
        runtime_library_dirs=[],
        cxx_std=14,
    ),
]

setuptools.setup(
    name="pkg3",
    version="0.0.1",
    packages=["pkg3"],
    install_requires=[],
    package_dir={"": "src"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
