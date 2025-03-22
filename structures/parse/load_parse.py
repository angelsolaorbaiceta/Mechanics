import re

from geom2d import Vector

__LOAD_REGEX = (
    r"(?P<node_id>\d+)\s*->\s*"
    r"\((?P<vec>[\d\s\.,\-]+)\)"
)


def parse_load(load_str: str):
    """
    Parses a load vector from a string or raises a `ValueError` if
    the given string doesn't follow the expected format.

    :param load_str: definition string
    :return: tuple of node id and load vector
    """

    match = re.match(__LOAD_REGEX, load_str)
    if not match:
        raise ValueError(f'Cannot parse load from string: "{load_str}"')

    node_id = int(match.group("node_id"))
    [fx, fy] = [float(num) for num in match.group("vec").split(",")]

    return node_id, Vector(fx, fy)
