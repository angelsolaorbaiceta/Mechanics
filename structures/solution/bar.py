from geom2d import Segment, make_vector_between
from structures.model.bar import StrBar
from .node import StrNodeSolution


class StrBarSolution:
    """
    A truss structure bar with the solution values included.

    This class is a decorator of the original `StrBar` class that's
    linked to the solution nodes, that include their displacement
    vectors. It's thanks to the solution displaced nodes that we
    can obtain the stress and strain values for the bar.
    """

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
        """
        The original bar's identifier.

        :return: id for the bar
        """
        return self.__original_bar.id

    @property
    def cross_section(self):
        """
        The original bar's cross section area value.

        :return: the cross section
        """
        return self.__original_bar.cross_section

    @property
    def young_mod(self):
        """
        The original bar's Young modulus (or elasticity modulus).

        :return: the Young modulus
        """
        return self.__original_bar.young_mod

    @property
    def original_geometry(self):
        """
        The original bar's geometry described by a line segment.

        :return: the bar's geometry
        """
        return self.__original_bar.geometry

    @property
    def final_geometry(self):
        """
        The bar's geometry, described by a line segment, after the
        computed displacements are applied.

        :return: the solution bar's geometry
        """
        return Segment(
            self.start_node.displaced_pos,
            self.end_node.displaced_pos
        )

    @property
    def original_length(self):
        """
        The original bar's length. This is, the distance between
        its nodes.

        :return: the bar's length
        """
        return self.original_geometry.length

    @property
    def final_length(self):
        """
        The bar's length after the computed displacements are
        applied. This is the distance between the solution nodes.

        :return: the solution bar's length
        """
        return self.final_geometry.length

    @property
    def elongation(self):
        """
        The difference between the solution bar's length and the
        original bar's length.

        A positive elongation means the bar has elongated (due to
        a tensile stress) and a negative elongation means the bar
        has shortened (due to a compressive stress).

        :return: the bar's elongation
        """
        return self.final_length - self.original_length

    @property
    def strain(self):
        """
        The bar's elongation per unit of length. This is a
        unit-less quantity.

        :return: the bar's strain
        """
        return self.elongation / self.original_length

    @property
    def stress(self):
        """
        The bar's axial force per unit of cross section area.

        Using Hooke's law, the stress can be computed as the
        product of the bar's strain and Young modulus.
        :return:
        """
        return self.young_mod * self.strain

    @property
    def internal_force_value(self):
        """
        The bar's internal force.

        :return: the bar's internal force
        """
        return self.stress * self.cross_section

    def force_in_node(self, node: StrNodeSolution):
        """
        Returns the force this bar exerts on of of its to nodes.

        The passed in node needs to be one or the bar's end nodes,
        otherwise, this method will throw a `ValueError`.

        :param node: one of the bar's end nodes
        :return: force exerted by the bar on the given node
        """
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
        """
        Tests whether the given `node` is one of this bar's end
        nodes.

        :param node: structure node
        :return: is the node connected with this bar?
        """
        return node is self.start_node or node is self.end_node

    def final_geometry_scaling_displacement(self, scale: float):
        """
        Computes the geometry of the bar after the displacements
        of its nodes have been applied with a given scale factor.

        This scaled geometry can be used for drawing the solution
        diagram.

        :param scale: used to scale the displacements
        :return: the solution bar's final geometry scaled
        """
        return Segment(
            self.start_node.displaced_pos_scaled(scale),
            self.end_node.displaced_pos_scaled(scale)
        )
