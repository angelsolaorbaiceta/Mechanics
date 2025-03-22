from structures.solution.bar import StrBarSolution
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution

__DECIMAL_POS = 4


def structure_solution_to_json(result: StructureSolution):
    return {
        "data": {
            "nodes": [__node_to_json(node, result) for node in result.nodes],
            "bars": [__bar_to_json(bar) for bar in result.bars],
        }
    }


def __node_to_json(node: StrNodeSolution, result: StructureSolution):
    node_json = {
        "id": node.id,
        "position": {
            "original": {
                "x": round(node.original_pos.x, __DECIMAL_POS),
                "y": round(node.original_pos.y, __DECIMAL_POS),
            },
            "displaced": {
                "x": round(node.displaced_pos.x, __DECIMAL_POS),
                "y": round(node.displaced_pos.y, __DECIMAL_POS),
            },
        },
    }

    if node.is_constrained:
        react = result.reaction_for_node(node)
        node_json["reaction"] = {
            "x": round(react.u, __DECIMAL_POS),
            "y": round(react.v, __DECIMAL_POS),
        }

    return node_json


def __bar_to_json(bar: StrBarSolution):
    return {
        "id": bar.id,
        "nodes": {
            "start": bar.start_node.id,
            "end": bar.end_node.id,
        },
        "axial": "tension" if bar.stress >= 0 else "compression",
        "elongation": round(bar.elongation, __DECIMAL_POS),
        "strain": round(bar.strain, 2 * __DECIMAL_POS),
        "stress": round(bar.stress, __DECIMAL_POS),
    }
