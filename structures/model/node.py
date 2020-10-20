import operator
from functools import reduce

from geom2d import Point, Vector


class StrNode:
    """
    A node in the structure is the point where one or more bars
    meet.

    A node is defined in a position in the plane, an identifier,
    external loads and optional external constraints. The external
    constraints are applied on the displacements
    """

    def __init__(
            self,
            _id: int,
            position: Point,
            loads=None,
            dx_constrained=False,
            dy_constrained=False
    ):
        self.id = _id
        self.position = position
        self.loads = loads or []
        self.dx_constrained = dx_constrained
        self.dy_constrained = dy_constrained

    @property
    def loads_count(self):
        """
        The number of external loads applied in the node.

        :return: `int` number of loads
        """
        return len(self.loads)

    @property
    def net_load(self):
        """
        The net load vector: the result of adding all the applied
        external load vectors.

        :return: `Vector` net load
        """
        return reduce(
            operator.add,
            self.loads,
            Vector(0, 0)
        )

    def add_load(self, load: Vector):
        """
        Adds an external load vector.

        :param load: `Vector` external load
        """
        self.loads.append(load)

    def __eq__(self, other):
        """
        Two nodes are considered equal if their position is equal.

        :param other: `Node`
        :return: are the nodes equal?
        """
        if self is other:
            return True

        if not isinstance(other, StrNode):
            return False

        return self.position == other.position
