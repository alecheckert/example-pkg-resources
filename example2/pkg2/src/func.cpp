#include "pkg2.h"

namespace pkg2{

std::string hello()
{
    return std::string("hello world");
}

std::string get_data_dir()
{
    return std::string(DATA_DIR);
}

}
