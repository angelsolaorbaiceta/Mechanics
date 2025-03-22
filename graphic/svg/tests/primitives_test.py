import unittest

from geom2d import Point, Rect, Segment, Size, Polygon, Circle, Vector
from graphic.svg import primitives


class TestSvgPrimitives(unittest.TestCase):
    def test_segment(self):
        segment = Segment(Point(2, 3), Point(4, 5))
        actual = primitives.segment(segment)
        expected = '<line x1="2" y1="3" x2="4" y2="5" />'
        self.assertEqual(expected, actual)

    def test_rectangle(self):
        rect = Rect(Point(2, 3), Size(4, 5))
        actual = primitives.rectangle(rect)
        expected = '<rect x="2" y="3" width="4" height="5" />'
        self.assertEqual(expected, actual)

    def test_circle(self):
        circle = Circle(Point(1, 2), 5)
        actual = primitives.circle(circle)
        expected = '<circle cx="1" cy="2" r="5" />'
        self.assertEqual(expected, actual)

    def test_polygon(self):
        polygon = Polygon([Point(2, 3), Point(4, 5), Point(6, 7)])
        actual = primitives.polygon(polygon)
        expected = '<polygon points="2,3 4,5 6,7" />'
        self.assertEqual(expected, actual)

    def test_text(self):
        actual = primitives.text("foo bar", Point(2, 3), Vector(4, 5))
        props = 'x="2" y="3" dx="4" dy="5"'
        expected = f"<text {props} >\n    foo bar\n</text>"
        self.assertEqual(expected, actual)

    def test_group(self):
        content = ["<foo />", "<bar />"]
        actual = primitives.group(content)
        expected = "<g >\n    <foo />\n\t<bar />\n</g>"
        self.assertEqual(expected, actual)
