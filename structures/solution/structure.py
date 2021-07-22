import operator
from functools import reduce
from typing import List

from geom2d import make_rect_containing_with_margin, Vector
from .bar import StrBarSolution
from .node import StrNodeSolution


class StructureSolution:
    """
    Truss structure solution model.

    The solution model groups the list of solution nodes and the
    list of solution bars.
    """

    def __init__(
            self,
            nodes: List[StrNodeSolution],
            bars: List[StrBarSolution]
    ):
        self.nodes = nodes
        self.bars = bars

    def bounds_rect(self, margin: float, scale=1):
        """
        Computes the rectangle that contains all the structure
        displaced nodes and including a given margin.

        This rectangular bounds can be used to compute the solution
        diagram's size.

        :param margin: extra space added to the sides
        :param scale: scale used for the node displacements
        :return: rectangular bounds
        """
        d_pos = [
            node.displaced_pos_scaled(scale)
            for node in self.nodes
        ]
        return make_rect_containing_with_margin(d_pos, margin)

    def reaction_for_node(self, node: StrNodeSolution):
        """
        Computes the external reaction force for a given node.

        To compute the reaction, it takes into account the external
        loads and the internal forces from the bars connected to
        the node.

        A node that isn't externally constrained has no reaction
        force.

        :param node: node to compute the reaction force
        :return: reaction force on the node
        """
        if not node.is_constrained:
            return Vector(0, 0)

        forces = [
            bar.force_in_node(node)
            for bar in self.bars
            if bar.has_node(node)
        ]

        if node.is_loaded:
            forces.append(node.net_load.opposite())

        return reduce(operator.add, forces)
