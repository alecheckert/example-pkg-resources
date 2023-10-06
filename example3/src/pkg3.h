#ifndef _PKG3_H
#define _PKG3_H

// Look up the env variable "DATA_DIR" at runtime
#define DATA_DIR getenv("DATA_DIR")

#include <iostream>
#include <fstream>
#include <string>

namespace pkg3{

std::string get_data_dir()
{
    return std::string(DATA_DIR);
}

std::string get_data()
{
    const std::string path = get_data_dir() + "/data.txt";
    std::ifstream f;
    f.open(path);
    if(!f.is_open()){
        throw std::runtime_error("failed to open");
    }
    std::string contents;
    char c;
    while(f){
        c = f.get();
        contents += c;
    }
    contents.pop_back();
    contents.pop_back();
    return contents;
}

}

#endif
