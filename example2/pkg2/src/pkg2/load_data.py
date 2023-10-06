from pkg2_data import get_path

def load_data_py() -> str:
    path = get_path("data.txt")
    with open(path, "r") as f:
        return f.read().replace("\n", "")
