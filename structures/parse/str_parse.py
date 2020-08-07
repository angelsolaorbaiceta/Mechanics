import re

from structures.model.structure import Structure
from .bar_parse import parse_bar
from .load_parse import parse_load
from .node_parse import parse_node

__COMMENT_INDICATOR = '#'
__NODES_HEADER = 'nodes'
__LOADS_HEADER = 'loads'
__BARS_HEADER = 'bars'


def parse_structure(structure_string: str):
    """
    Parses a `Structure` from a string or raises a `ValueError` if
    the given string doesn't follow the expected format.

    The input string should contain the structure definition split
    into lines. This function first splits those lines and parses
    the structure parsing line by line using the appropriate
    parsing logic.

    :param structure_string: definition string
    :return: `Structure`
    """
    lines = structure_string.split('\n')
    return parse_structure_from_lines(lines)


def parse_structure_from_lines(lines: [str]):
    """
    Parses a `Structure` from a list of strings: the definition
    lines. This function will raise a `ValueError` if there is
    any problem parsing the structure.

    :param lines: definition lines
    :return: `Structure`
    """
    parsed = __parse_lines(lines)
    nodes_dict = parsed['nodes']
    loads = parsed['loads']
    bars = parsed['bars']

    __apply_loads_to_nodes(loads, nodes_dict)

    return Structure(
        list(nodes_dict.values()),
        bars
    )


def __apply_loads_to_nodes(loads, nodes):
    for node_id, load in loads:
        nodes[node_id].add_load(load)


def __parse_lines(lines: [str]):
    reading = ''
    result = {'nodes': {}, 'loads': [], 'bars': []}

    for i, line in enumerate(lines):
        if __should_ignore_line(line):
            continue

        # <--- header ---> #
        if re.match(__NODES_HEADER, line):
            reading = 'nodes'
        elif re.match(__BARS_HEADER, line):
            reading = 'bars'
        elif re.match(__LOADS_HEADER, line):
            reading = 'loads'

        # <--- definition ---> #
        elif reading == 'nodes':
            node = parse_node(line)
            result['nodes'][node.id] = node
        elif reading == 'bars':
            bar = parse_bar(line, result['nodes'])
            result['bars'].append(bar)
        elif reading == 'loads':
            load = parse_load(line)
            result['loads'].append(load)
        else:
            raise RuntimeError(
                f'Unknown error in line ${i}: ${line}'
            )

    return result


def __should_ignore_line(line: str):
    stripped = line.strip()
    return len(stripped) == 0 or \
           stripped.startswith(__COMMENT_INDICATOR)
