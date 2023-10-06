#include "pkg2.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_pkg2, m)
{
    m.def("hello", &pkg2::hello);
    m.def("get_data_dir", &pkg2::get_data_dir);
}
