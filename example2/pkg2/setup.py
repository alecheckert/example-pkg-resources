import os
import setuptools
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pkg2_data


SRC_FILES = [os.path.join("src", f) for f in ["func.cpp", "module.cpp"]]
INC_DIRS = ["src"]
DATA_DIR = os.path.dirname(pkg2_data.__file__)

ext_modules = [
    Pybind11Extension(
        "_pkg2",
        SRC_FILES,
        include_dirs=INC_DIRS,
        libraries=[],
        library_dirs=[],
        runtime_library_dirs=[],
        cxx_std=14,
        extra_compile_args=[f'-DDATA_DIR=\"{DATA_DIR}\"'],
    ),
]

setuptools.setup(
    name="pkg2",
    version="0.0.1",
    packages=["pkg2"],
    install_requires=["pybind11>=2.6", "pkg2_data"],
    package_dir={"": "src"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
