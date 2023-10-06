#include "pkg3.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_pkg3, m)
{
    m.def("get_data_dir", &pkg3::get_data_dir);
    m.def("get_data", &pkg3::get_data);
}
