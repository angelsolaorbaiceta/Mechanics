import unittest

from geom2d.circles import Circle, make_circle_from_points
from geom2d.point import Point


class TestCircles(unittest.TestCase):
    def test_circle_from_points(self):
        a = Point(-10, 0)
        b = Point(0, 10)
        c = Point(10, 0)
        actual = make_circle_from_points(a, b, c)
        expected = Circle(Point(0, 0), 10)
        self.assertEqual(expected, actual)
