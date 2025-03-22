import unittest

from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.rect import Rect
from geom2d.size import Size


class TestRect(unittest.TestCase):
    origin = Point(0, 0)
    size = Size(10, 5)
    rect = Rect(origin, size)

    # --- CONTAINS --- #
    def test_contains_point(self):
        point = Point(5, 3)
        self.assertTrue(self.rect.contains_point(point))

    def test_doesnt_contain_point(self):
        point = Point(50, 7)
        self.assertFalse(self.rect.contains_point(point))

    # --- INTERSECTION --- #
    def test_no_intersection_horizontal_overlap(self):
        other = Rect(Point(50, 0), self.size)
        self.assertIsNone(self.rect.intersection_with(other))

    def test_no_intersection_vertical_overlap(self):
        other = Rect(Point(0, 50), self.size)
        self.assertIsNone(self.rect.intersection_with(other))

    def test_intersection(self):
        other = Rect(Point(5, 2), self.size)
        actual = self.rect.intersection_with(other)
        expected = Rect(other.origin, Size(5, 3))
        self.assertEqual(expected, actual)

    # --- POLYGON --- #
    def test_to_polygon(self):
        actual = self.rect.to_polygon()
        expected = Polygon([self.origin, Point(10, 0), Point(10, 5), Point(0, 5)])
        self.assertEqual(expected, actual)
