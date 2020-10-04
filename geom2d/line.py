from geom2d.point import Point
from geom2d.vector import Vector
from geom2d.vectors import make_vector_between


class Line:
    """
    A line is defined by a base point and a direction. A line has
    neither start nor end and contains infinite points.
    """

    def __init__(self, base: Point, direction: Vector):
        self.base = base
        self.direction = direction

    def is_parallel_to(self, other):
        """
        Tests whether this and other lines are parallel.

        :param other: `Line`
        :return: are the lines parallel?
        """
        return self.direction.is_parallel_to(other.direction)

    def is_perpendicular_to(self, other):
        """
        Tests whether this and other lines are perpendicular.

        :param other: `Line`
        :return: are the lines perpendicular?
        """
        return self.direction.is_perpendicular_to(other.direction)

    def perpendicular_through(self, point: Point):
        """
        Creates a new line passing through a given point which
        direction is perpendicular to this one.

        :param point: `Point` the line will pass through
        :return: `Line` perpendicular to this one
        """
        return Line(point, self.direction.perpendicular())

    def parallel_through(self, point: Point):
        """
        Creates a new line passing through a given point which
        direction is parallel to this one.

        :param point: `Point` the line will pass through
        :return: `Line` parallel to this one
        """
        return Line(point, self.direction)

    def intersection_with(self, other):
        """
        Computes the intersection with another line. Returns `None`
        if the lines don't intersect.

        :param other: `Line`
        :return: intersection `Point` or `None`
        """
        if self.is_parallel_to(other):
            return None

        d1, d2 = self.direction, other.direction
        cross_prod = d1.cross(d2)
        delta = make_vector_between(self.base, other.base)
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross_prod

        return self.base.displaced(d1, t1)
