import operator
from functools import reduce

from geom2d import Point, Vector


class StrNode:

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
        return len(self.loads)

    @property
    def net_load(self):
        return reduce(
            operator.add,
            self.loads,
            Vector(0, 0)
        )

    def add_load(self, load: Vector):
        self.loads.append(load)

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, StrNode):
            return False

        return self.position == other.position
