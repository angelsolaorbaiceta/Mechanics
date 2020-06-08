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
    lines = structure_string.split('\n')
    return parse_structure_from_lines(lines)


def parse_structure_from_lines(lines: [str]):
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
        elif reading is 'nodes':
            node = parse_node(line)
            result['nodes'][node.id] = node
        elif reading is 'bars':
            bar = parse_bar(line, result['nodes'])
            result['bars'].append(bar)
        elif reading is 'loads':
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
