from geom2d import tparam
from geom2d.line import Line
from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor_between


class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def direction_vector(self):
        return make_vector_between(self.start, self.end)

    def direction_versor(self):
        return make_versor_between(self.start, self.end)

    def normal_versor(self):
        return self.direction_versor().perpendicular()

    def length(self):
        return self.start.distance_to(self.end)

    def point_at(self, t):
        tparam.ensure_valid(t)
        return self.start.displaced(self.direction_vector(), t)

    def middle(self):
        return self.point_at(tparam.MIDDLE)

    def closest_point_to(self, p: Point):
        v = make_vector_between(self.start, p)
        d = self.direction_versor()
        vs = v.projection_over(d)

        if vs < 0:
            return self.start

        if vs > self.length():
            return self.end

        return self.start.displaced(d, vs)

    def distance_to(self, p: Point):
        return p.distance_to(
            self.closest_point_to(p)
        )

    def intersection_with(self, other):
        d1, d2 = self.direction_vector(), other.direction_vector()

        if d1.is_parallel_to(d2):
            return None

        cross_prod = d1.cross(d2)
        delta = other.start - self.start
        t1 = (delta.x * d2.v - delta.y * d2.u) / cross_prod
        t2 = (delta.x * d1.v - delta.y * d1.u) / cross_prod

        if tparam.is_valid(t1) and tparam.is_valid(t2):
            return self.point_at(t1)
        else:
            return None

    def bisector(self):
        return Line(
            self.middle(),
            self.direction_versor().perpendicular()
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Segment):
            return False

        return self.start == other.start \
               and self.end == other.end

    def __str__(self):
        return f'segment from {self.start} to {self.end}'
