import math
import unittest

from geom2d import tparam
from geom2d.point import Point
from geom2d.segment import Segment


class TestSegment(unittest.TestCase):

    start = Point(400, 0)
    end = Point(0, 400)
    segment = Segment(start, end)

    def test_length(self):
        expected = 400 * math.sqrt(2)
        actual = self.segment.length
        self.assertAlmostEqual(expected, actual)

    # --- POINT AT --- #
    def test_point_at_wrong_t(self):
        self.assertRaises(
            tparam.TParamError,
            self.segment.point_at,
            56.7
        )

    def test_point_at(self):
        t = tparam.make(0.25)
        expected = Point(300, 100)
        actual = self.segment.point_at(t)
        self.assertEqual(expected, actual)

    def test_middle_point(self):
        expected = Point(200, 200)
        actual = self.segment.middle()
        self.assertEqual(expected, actual)

    # --- CLOSEST POINT --- #
    def test_closest_point_is_start(self):
        p = Point(500, 20)
        expected = self.start
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    def test_closest_point_is_end(self):
        p = Point(20, 500)
        expected = self.end
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    def test_closest_point_is_middle(self):
        p = Point(250, 250)
        expected = Point(200, 200)
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    # --- INTERSECTIONS --- #
    def test_parallel_segments_no_intersection(self):
        other = Segment(Point(200, 0), Point(0, 200))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_intersection(self):
        other = Segment(Point(0, 0), Point(400, 400))
        expected = Point(200, 200)
        actual = self.segment.intersection_with(other)
        self.assertEqual(expected, actual)

