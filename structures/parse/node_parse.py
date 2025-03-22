import re

from geom2d import Point
from structures.model.node import StrNode

__NODE_REGEX = (
    r"(?P<id>\d+)\s*:\s*"
    r"\((?P<pos>[\d\s\.,\-]+)\)\s*"
    r"\((?P<ec>[xy]{0,2})\)"
)


def parse_node(node_str: str):
    """
    Parses a `StrNode` from a string or raises a `ValueError` if
    the given string doesn't follow the expected format.

    :param node_str: definition string
    :return: `StrNode`
    """

    match = re.match(__NODE_REGEX, node_str)
    if not match:
        raise ValueError(f"Cannot parse node from string: {node_str}")

    _id = int(match.group("id"))
    [x, y] = [float(num) for num in match.group("pos").split(",")]
    ext_const = match.group("ec")

    return StrNode(_id, Point(x, y), None, "x" in ext_const, "y" in ext_const)
