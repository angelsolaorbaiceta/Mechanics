from geom2d import Vector
from structures.model.node import StrNode


class StrNodeSolution:
    """
    A truss structure node with the solution values included.

    This class is a decorator of the original `StrNode` class that
    includes the global displacements vector.
    """

    def __init__(
            self,
            original_node: StrNode,
            global_disp: Vector
    ):
        self.__original_node = original_node
        self.global_disp = global_disp

    @property
    def id(self):
        """
        Identifier for the original node.

        :return: id for the node
        """
        return self.__original_node.id

    @property
    def original_pos(self):
        """
        The position of the original node, before the application
        of loads.

        :return: `Point` original position
        """
        return self.__original_node.position

    @property
    def is_constrained(self):
        """
        Whether the node has any external constraint applied.

        :return: `True` if the node has any external constraint
        """
        return self.__original_node.dx_constrained \
               or self.__original_node.dy_constrained

    @property
    def loads(self):
        """
        Sequence of external loads applied to the node.

        :return: external loads
        """
        return self.__original_node.loads

    @property
    def is_loaded(self):
        """
        Whether the node has at least one load applied.

        :return: `True` if there's at least one load
        """
        return self.__original_node.loads_count > 0

    @property
    def net_load(self):
        """
        The net load applied in the node.

        :return: `Vector`, net load
        """
        return self.__original_node.net_load

    @property
    def displaced_pos(self):
        """
        The position of the node after applying the global
        displacements.

        :return: `Point` displaced position
        """
        return self.original_pos.displaced(self.global_disp)

    def displaced_pos_scaled(self, scale=1):
        """
        Computes the position of the node after applying the global
        displacements vector scaled using the given scale.

        This method can be used when the displacements of the
        solution structure need to be scaled for plotting purposes.

        :param scale: `float`
        :return: `Point`, displaced position
        """
        return self.original_pos.displaced(self.global_disp, scale)
