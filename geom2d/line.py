from geom2d.point import Point
from geom2d.vector import Vector
from geom2d.vectors import make_vector_between


class Line:
    def __init__(self, base: Point, direction: Vector):
        self.base = base
        self.direction = direction

    def is_parallel_to(self, other):
        return self.direction.is_parallel_to(other.direction)

    def is_perpendicular_to(self, other):
        return self.direction.is_perpendicular_to(other.direction)

    def perpendicular_through(self, point):
        return Line(point, self.direction.perpendicular())

    def parallel_through(self, point):
        return Line(point, self.direction)

    def intersection_with(self, other):
        if self.is_parallel_to(other):
            return None

        d1, d2 = self.direction, other.direction
        cross_prod = d1.cross(d2)
        delta = make_vector_between(self.base, other.base)
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross_prod

        return self.base.displaced(d1, t1)
