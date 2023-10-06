# example-pkg-resources
Example of a hybrid C++/Python package bundled with non-code data files. An example
package for myself to reference in future projects.

## Purpose

Say we have a package that includes some non-code data files that we need to reference at
runtime. For a pure Python package, a simple way to make this work is to include these
data files as package data.

To make this concrete, suppose we have a simple `setuptools`-based package in `src` layout as follows:
```
mypackage/
    pyproject.toml
    setup.py
    MANIFEST.in
    src/
        mypackage/
            __init__.py
            data_file.tif
            get_data.py
```

For a package in `src` layout, we can do this as follows:
```
# pyproject.toml
[build-system]
requires = ["setuptools>42"]
build-backend = "setuptools.build_meta"
```

```
# setup.py
import setuptools
setuptools.setup(
    name="mypackage",
    version="0.0.1",
    packages=["mypackage"],
    package_dir={"src": ""},
    include_package_data=True,
)
```
```
# MANIFEST.in
include src/mypackage/data_file.tif
```
```
# get_data.py
import os
def get_path_to_data() -> str:
    dirname = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dirname, "data_file.tif")
```

