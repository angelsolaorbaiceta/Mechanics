from eqs import Matrix
from geom2d import Segment
from .node import StrNode


class StrBar:
    """
    A bar is a resistant element whose geometry is represented by a
    line segment. A bar is defined between two nodes.

    The resistant properties for a bar in a truss structure are its
    cross section and its material's Young modulus.
    """

    def __init__(
        self,
        _id: int,
        start_node: StrNode,
        end_node: StrNode,
        cross_section: float,
        young_mod: float,
    ):
        self.id = _id
        self.start_node = start_node
        self.end_node = end_node
        self.cross_section = cross_section
        self.young_mod = young_mod

    @property
    def geometry(self):
        """
        Line segment representing the geometry of the bar.

        :return: `Segment`
        """
        return Segment(self.start_node.position, self.end_node.position)

    @property
    def length(self):
        """
        The length of the bar's directrix.

        :return: `float` length of the directrix
        """
        return self.geometry.length

    def global_stiffness_matrix(self) -> Matrix:
        """
        Computes the bar's stiffness matrix in global coordinates.

        :return: global stiffness `Matrix`
        """
        direction = self.geometry.direction_vector
        eal = self.young_mod * self.cross_section / self.length
        c = direction.cosine
        s = direction.sine

        c2_eal = (c**2) * eal
        s2_eal = (s**2) * eal
        sc_eal = (s * c) * eal

        return Matrix(4, 4).set_data(
            [
                c2_eal,
                sc_eal,
                -c2_eal,
                -sc_eal,
                sc_eal,
                s2_eal,
                -sc_eal,
                -s2_eal,
                -c2_eal,
                -sc_eal,
                c2_eal,
                sc_eal,
                -sc_eal,
                -s2_eal,
                sc_eal,
                s2_eal,
            ]
        )
