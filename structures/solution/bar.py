from typing import Dict

from geom2d import Segment, make_vector_between
from structures.model.bar import StrBar
from .node import StrNodeSolution


class StrBarSolution:

    def __init__(
            self,
            original_bar: StrBar,
            start_node: StrNodeSolution,
            end_node: StrNodeSolution
    ):
        if original_bar.start_node.id != start_node.id:
            raise ValueError('Wrong start node')

        if original_bar.end_node.id != end_node.id:
            raise ValueError('Wrong end node')

        self.__original_bar = original_bar
        self.start_node = start_node
        self.end_node = end_node

    @property
    def id(self):
        return self.__original_bar.id

    @property
    def cross_section(self):
        return self.__original_bar.cross_section

    @property
    def young_mod(self):
        return self.__original_bar.young_mod

    @property
    def original_geometry(self):
        return self.__original_bar.geometry

    @property
    def final_geometry(self):
        return Segment(
            self.start_node.displaced_pos,
            self.end_node.displaced_pos
        )

    @property
    def original_length(self):
        return self.original_geometry.length

    @property
    def final_length(self):
        return self.final_geometry.length

    @property
    def elongation(self):
        return self.final_length - self.original_length

    @property
    def strain(self):
        return self.elongation / self.original_length

    @property
    def stress(self):
        return self.young_mod * self.strain

    @property
    def internal_force_value(self):
        return self.stress * self.cross_section

    def force_in_node(self, node: StrNodeSolution):
        if node is self.start_node:
            return make_vector_between(
                self.end_node.displaced_pos,
                self.start_node.displaced_pos
            ).with_length(
                self.internal_force_value
            )
        elif node is self.end_node:
            return make_vector_between(
                self.start_node.displaced_pos,
                self.end_node.displaced_pos
            ).with_length(
                self.internal_force_value
            )

        raise ValueError(
            f'Bar {self.id} does not know about node {node.id}'
        )

    def has_node(self, node: StrNodeSolution):
        return node is self.start_node or node is self.end_node

    def final_geometry_scaling_displacement(self, scale: float):
        return Segment(
            self.start_node.displaced_pos_scaled(scale),
            self.end_node.displaced_pos_scaled(scale)
        )
