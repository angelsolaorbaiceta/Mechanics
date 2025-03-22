from typing import List
from structures.solution.bar import StrBarSolution
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution
from utils.strings import list_to_string

__DECIMAL_POS = 4
__SEPARATION = ["------------------------------------------", "\n"]


def structure_solution_to_string(result: StructureSolution):
    """
    Returns a string containing a human-readable text report of the
    structure's resolution. This report includes the displacement
    vector of every node, and their external reaction force. For
    the case of bars, it includes the stress and strain values.

    :param result: the structure's result model
    :return: text report
    """
    nodes_text = __nodes_to_string(result)
    bars_text = __bars_to_string(result.bars)
    return list_to_string(nodes_text + __SEPARATION + bars_text)


def __nodes_to_string(result: StructureSolution):
    return [__node_to_string(result, node) for node in result.nodes]


def __node_to_string(result: StructureSolution, node: StrNodeSolution):
    orig_pos = node.original_pos.to_formatted_str(__DECIMAL_POS)
    displacement = node.global_disp.to_formatted_str(__DECIMAL_POS)
    disp_pos = node.displaced_pos.to_formatted_str(__DECIMAL_POS)

    strings = [
        f"NODE {node.id}",
        f"\toriginal position: {orig_pos}",
        f"\tdisplacement: {displacement}",
        f"\tdisplaced position: {disp_pos}",
    ]

    if node.is_constrained:
        react = result.reaction_for_node(node)
        react_str = react.to_formatted_str(__DECIMAL_POS)
        strings.append(f"\treaction: {react_str}")

    return list_to_string(strings) + "\n"


def __bars_to_string(bars: List[StrBarSolution]):
    return [__bar_to_string(bar) for bar in bars]


def __bar_to_string(bar: StrBarSolution):
    nodes_str = f"{bar.start_node.id} ➜ {bar.end_node.id}"
    type_str = "⊕ TENSION" if bar.stress >= 0 else "⊖ COMPRESSION"
    elongation = round(bar.elongation, __DECIMAL_POS)
    strain = "{:.3e}".format(bar.strain)
    stress = round(bar.stress, __DECIMAL_POS)

    return list_to_string(
        [
            f"BAR {bar.id} ({nodes_str}) : {type_str}",
            f"\tΔl (elongation) = {elongation}",
            f"\tϵ  (strain)     = {strain}",
            f"\tσ  (stress)     = {stress}\n",
        ]
    )
