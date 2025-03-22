import math

from geom2d.nums import are_close_enough
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.vectors import make_vector_between


class Circle:
    """
    A circle is the set of all points in the plane a given distance
    (the radius) from a single point called the center.
    """

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        """
        Area of the circle = 𝜋 ⋅ r^2.

        :return: `float` area
        """
        return math.pi * self.radius**2

    @property
    def circumference(self):
        """
        Length of the circle's edge = 𝜋 ⋅ 2r.

        :return: `float` circumference
        """
        return 2 * math.pi * self.radius

    def contains_point(self, point: Point):
        """
        Tests whether the given point is contained in the circle
        or not.

        :param point: `Point`
        :return: `bool` circle contains point?
        """
        return point.distance_to(self.center) < self.radius

    def overlaps(self, other):
        """
        Tests whether this and `other` circles overlap.

        Two circles overlap if the sum of their radii is smaller
        than the distance between the two center points.

        :param other: `Circle`
        :return: `bool` circles overlap?
        """
        centers_dist = self.center.distance_to(other.center)
        radii_sum = self.radius + other.radius
        return centers_dist < radii_sum

    def penetration_vector(self, other):
        """
        Assuming this and `other` circles overlap, it computes the
        vector going from `other`'s center point towards this'
        center point, and has a length of the maximum penetration
        between the two.

        :param other: `Circle`
        :return: `Vector`
        """
        if not self.overlaps(other):
            return None

        direction = make_vector_between(other.center, self.center)
        centers_dist = self.center.distance_to(other.center)
        radii_sum = self.radius + other.radius

        return direction.with_length(radii_sum - centers_dist)

    def to_polygon(self, divisions: int):
        """
        Creates a polygon to approximate the circle using the given
        number of divisions.

        :param divisions: integer number of divisions
        :return: `Polygon` approximating the circle
        """
        angle_delta = 2 * math.pi / divisions
        return Polygon(
            [self.__point_at_angle(angle_delta * i) for i in range(divisions)]
        )

    def __point_at_angle(self, angle: float):
        return Point(
            self.center.x + self.radius * math.cos(angle),
            self.center.y + self.radius * math.sin(angle),
        )

    def __eq__(self, other):
        """
        Two circles are equal if their center points and radii are
        equal.

        :param other: `Circle`
        :return: are the circles equal?
        """
        if self is other:
            return True

        if not isinstance(other, Circle):
            return False

        return self.center == other.center and are_close_enough(
            self.radius, other.radius
        )

    def __str__(self):
        return f"circle c = {self.center}, r = {self.radius}"
