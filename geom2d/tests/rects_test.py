import unittest

from geom2d.rects import *
from geom2d.size import Size


class TestRects(unittest.TestCase):
    points = [Point(0, 5), Point(10, 0), Point(5, 7)]

    def test_containing_points(self):
        actual = make_rect_containing(self.points)
        expected = Rect(Point(0, 0), Size(10, 7))
        self.assertEqual(expected, actual)

    def test_containing_points_margin(self):
        actual = make_rect_containing_with_margin(self.points, 1)
        expected = Rect(Point(-1, -1), Size(12, 9))
        self.assertEqual(expected, actual)

    def test_make_centered(self):
        actual = make_rect_centered(Point(5, 10), 20, 40)
        expected = Rect(Point(-5, -10), Size(20, 40))
        self.assertEqual(expected, actual)
