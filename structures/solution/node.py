from geom2d import Vector
from structures.model.node import StrNode


class StrNodeSolution:

    def __init__(
            self,
            original_node: StrNode,
            global_disp: Vector
    ):
        self.__original_node = original_node
        self.global_disp = global_disp

    @property
    def id(self):
        return self.__original_node.id

    @property
    def original_pos(self):
        return self.__original_node.position

    @property
    def is_constrained(self):
        return self.__original_node.dx_constrained \
               or self.__original_node.dy_constrained

    @property
    def loads(self):
        return self.__original_node.loads

    @property
    def is_loaded(self):
        return self.__original_node.loads_count > 0

    @property
    def net_load(self):
        return self.__original_node.net_load

    @property
    def displaced_pos(self):
        return self.original_pos.displaced(self.global_disp)

    def displaced_pos_scaled(self, scale=1):
        return self.original_pos.displaced(self.global_disp, scale)
