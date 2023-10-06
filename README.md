# example-pkg-resources
Example of a hybrid C++/Python package bundled with non-code data files. An example
package for myself to reference in future projects.

## Purpose

Say we have a package that includes some non-code data files that we need to reference at
runtime. For a pure Python package, a simple way to make this work is to include these
data files as package data. This is provided as `example1`.

The harder case is when we have a combined C++/Python package. (Here, we're
using `pybind11` to make Python bindings for the C++ code). The C++ code
needs to reference data files located in the Python package at runtime.
How do we do this?

One way, which we have taken in `example2`, is to separate the data files
and code into two packages (`pkg2_data` and `pkg2`). Then we do the following:
 1. Install `pkg2_data`.
 2. Reference `pkg2_data` at build time by `pkg2`.

Unfortunately this doesn't play well with `pip install`, which automatically
performs the build (including installation of all build-time dependencies)
in an isolated virtual environment that is deleted after the build. That is,
any paths to build-time dependencies baked into a wheel will be
invalid at runtime. This can be disabled with the `--no-build-isolation`
option to `pip`, but at the cost of disabling `pip`'s attractive ability to
resolve build-time dependencies as listed in the `build-system.requires`
section of the `pyproject.toml`.

A second disadvantage of `example2` is that each user needs to compile
their own extensions, which is asking for trouble.
