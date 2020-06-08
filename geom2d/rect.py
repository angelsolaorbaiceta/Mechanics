from geom2d.open_interval import OpenInterval
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.size import Size


class Rect:
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size

    def left(self):
        return self.origin.x

    def right(self):
        return self.origin.x + self.size.width

    def bottom(self):
        return self.origin.y

    def top(self):
        return self.origin.y + self.size.height

    def area(self):
        return self.size.width * self.size.height

    def perimeter(self):
        return 2 * self.size.width + 2 * self.size.height

    def contains_point(self, point: Point):
        return self.left() < point.x < self.right() \
               and self.bottom() < point.y < self.top()

    def intersection_with(self, other):
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
