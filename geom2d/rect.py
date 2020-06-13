from geom2d.open_interval import OpenInterval
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.size import Size


class Rect:
    """
    Rectangle defined by an origin point and size.
    """
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def left(self):
        """
        Min x value for the rectangle.

        :return: `float`
        """
        return self.origin.x

    def right(self):
        """
        Max x value for the rectangle.

        :return: `float`
        """
        return self.origin.x + self.size.width

    def bottom(self):
        """
        Min y value for the rectangle.

        :return: `float`
        """
        return self.origin.y

    def top(self):
        """
        Max y value for the rectangle.

        :return: `float`
        """
        return self.origin.y + self.size.height

    def area(self):
        """
        Area of the rectangle.

        :return: `float`
        """
        return self.size.width * self.size.height

    def perimeter(self):
        """
        Length of the length of all sides of the rectangle.

        :return: `float`
        """
        return 2 * self.size.width + 2 * self.size.height

    def contains_point(self, point: Point):
        """
        Tests whether `point` is inside the rectangle or not.

        :param point: `Point`
        :return: `bool`
        """
        return self.left() < point.x < self.right() \
               and self.bottom() < point.y < self.top()

    def intersection_with(self, other):
        """
        Computes the intersection between this rectangle and
        another rectangle `other`.

        The intersection result may be a `Rect` or `None`.

        :param other: `Rect`
        :return: `bool`
        """
        h_overlap = self.__horizontal_overlap_with(other)
        if h_overlap is None:
            return None

        v_overlap = self.__vertical_overlap_with(other)
        if v_overlap is None:
            return None

        return Rect(
            Point(h_overlap.start, v_overlap.start),
            Size(h_overlap.length(), v_overlap.length())
        )

    def __horizontal_overlap_with(self, other):
        self_interval = OpenInterval(self.left(), self.right())
        other_interval = OpenInterval(other.left(), other.right())

        return self_interval.compute_overlap_with(other_interval)

    def __vertical_overlap_with(self, other):
        self_interval = OpenInterval(self.bottom(), self.top())
        other_interval = OpenInterval(other.bottom(), other.top())

        return self_interval.compute_overlap_with(other_interval)

    def to_polygon(self):
        """
        Creates a `Polygon` equivalent to this rectangle.
        The polygon is made of the rectangle vertices in the
        following order:
            - (left, bottom) ≡ origin
            - (right, bottom)
            - (right, top)
            - (left, top)

        :return: `Polygon`
        """
        return Polygon([
            self.origin,
            Point(self.right(), self.bottom()),
            Point(self.right(), self.top()),
            Point(self.left(), self.top())
        ])

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Rect):
            return False

        return self.origin == other.origin \
               and self.size == other.size
