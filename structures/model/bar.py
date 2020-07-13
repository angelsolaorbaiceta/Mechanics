from eqs import Matrix
from geom2d import Segment
from .node import StrNode


class StrBar:

    def __init__(
            self,
            _id: int,
            start_node: StrNode,
            end_node: StrNode,
            cross_section: float,
            young_mod: float
    ):
        self.id = _id
        self.start_node = start_node
        self.end_node = end_node
        self.cross_section = cross_section
        self.young_mod = young_mod

    @property
    def geometry(self):
        return Segment(
            self.start_node.position,
            self.end_node.position
        )

    @property
    def length(self):
        return self.geometry.length()

    def global_stiffness_matrix(self) -> Matrix:
        direction = self.geometry.direction_vector
        eal = self.young_mod * self.cross_section / self.length
        c = direction.cosine
        s = direction.sine

        c2_eal = (c ** 2) * eal
        s2_eal = (s ** 2) * eal
        sc_eal = (s * c) * eal

        return Matrix(4, 4).set_data([
            c2_eal, sc_eal, -c2_eal, -sc_eal,
            sc_eal, s2_eal, -sc_eal, -s2_eal,
            -c2_eal, -sc_eal, c2_eal, sc_eal,
            -sc_eal, -s2_eal, sc_eal, s2_eal
        ])
