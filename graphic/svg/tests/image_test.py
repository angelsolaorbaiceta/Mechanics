import unittest

from geom2d import Point, Size, Rect
from graphic.svg.image import svg_content


class TestSvgImage(unittest.TestCase):

    size = Size(200, 350)
    viewbox = Rect(Point(4, 5), Size(180, 230))

    def test_parse_width(self):
        svg = svg_content(self.size, [])
        self.assertTrue('width="200"' in svg)

    def test_parse_height(self):
        svg = svg_content(self.size, [])
        self.assertTrue('height="350"' in svg)

    def test_parse_default_viewbox(self):
        svg = svg_content(self.size, [])
        self.assertTrue('viewBox="0 0 200 350"' in svg)

    def test_parse_viewbox(self):
        svg = svg_content(self.size, [], self.viewbox)
        self.assertTrue('viewBox="4 5 180 230"' in svg)
