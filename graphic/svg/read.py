from importlib import resources
from os import path


def read_template(file_name: str):
    file_path = path.join("templates", file_name)
    bytes_str = resources.files(__package__).joinpath(file_path).read_bytes()
    return bytes_str.decode("UTF-8")
