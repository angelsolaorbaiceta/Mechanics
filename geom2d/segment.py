from geom2d import tparam
from geom2d.line import Line
from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor_between


class Segment:
    """
    A segment is a straight line limited by two end points:
    `start` and `end`.
    """

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @property
    def direction_vector(self):
        """
        Vector in the direction of the segment, going from `start`
        to `end` and with the same length as the segment itself.

        :return: `Vector` with length equal to segment's length
        """
        return make_vector_between(self.start, self.end)

    @property
    def direction_versor(self):
        """
        Vector in the direction of the segment, going from `start`
        to `end` and unitary length.

        :return: `Vector` of unitary length
        """
        return make_versor_between(self.start, self.end)

    @property
    def normal_versor(self):
        """
        Vector normal (perpendicular) to the segments direction
        and unitary length.

        This vector is the result of rotating 90º the segment's
        `direction_versor`.

        :return: `Vector` normal to the segment's direction
        """
        return self.direction_versor.perpendicular()

    @property
    def length(self):
        """
        Length of the segment.
        Equals to the distance from `start` to `end``

        :return: `float` equal to the segment's length
        """
        return self.start.distance_to(self.end)

    def point_at(self, t: float):
        """
        Returns a segment's middle point at a given position
        between `start` and `end` given by the `t` parameter.

        :param t: `float` in the range [0, 1]
        :return: `Point`
        """
        tparam.ensure_valid(t)
        return self.start.displaced(self.direction_vector, t)

    @property
    def middle(self):
        """
        Returns the point at `t = 0.5`, that is, the point inside
        the segment equidistant between `start` and `end`.

        :return: `Point` at `t = 0.5`
        """
        return self.point_at(tparam.MIDDLE)

    def closest_point_to(self, p: Point):
        """
        Computes the point which belongs to the segment and is
        closest to a given external point `p`.

        :param p: `Point`
        :return: `Point` in segment closest to `p`
        """
        v = make_vector_between(self.start, p)
        d = self.direction_versor
        vs = v.projection_over(d)

        if vs < 0:
            return self.start

        if vs > self.length:
            return self.end

        return self.start.displaced(d, vs)

    def distance_to(self, p: Point):
        """
        Computes the distance between the given point `p` and
        the segment's closest point to `p`.

        :param p: `Point`
        :return: `float` distance to the closest point in segment
        """
        return p.distance_to(
            self.closest_point_to(p)
        )

    def intersection_with(self, other):
        """
        Computes the intersection point with another segment:
        `other`.

        The result of the intersection may be a `Point` or `None`
        in the cases where the segments don't intersect or have
        infinite intersection points (overlapping segments).

        :param other: `Segment`
        :return: `Point` or `None`
        """
        d1, d2 = self.direction_vector, other.direction_vector

        if d1.is_parallel_to(d2):
            return None

        cross_prod = d1.cross(d2)
        delta = other.start - self.start
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross_prod
        t2 = (delta.u * d1.v - delta.v * d1.u) / cross_prod

        if tparam.is_valid(t1) and tparam.is_valid(t2):
            return self.point_at(t1)
        else:
            return None

    @property
    def bisector(self):
        """
        Computes the bisector line: a `Line` perpendicular to the
        segment and which passes through its middle `Point`.

        :return: `Line` bisecting the segment
        """
        return Line(self.middle, self.normal_versor)

    def __eq__(self, other):
        """
        Two segments are equal if their start and end points are
        equal.

        :param other: `Segment`
        :return: are the segments equal?
        """
        if self is other:
            return True

        if not isinstance(other, Segment):
            return False

        return self.start == other.start \
               and self.end == other.end

    def __str__(self):
        return f'segment from {self.start} to {self.end}'
