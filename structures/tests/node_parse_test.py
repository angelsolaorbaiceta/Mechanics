import unittest

from geom2d import Point
from structures.parse.node_parse import parse_node


class NodeParseTest(unittest.TestCase):
    node_str = "1 : (25.0, 45.0)   (xy)"
    node = parse_node(node_str)

    def test_parse_id(self):
        self.assertEqual(1, self.node.id)

    def test_parse_position(self):
        expected = Point(25.0, 45.0)
        self.assertEqual(expected, self.node.position)

    def test_parse_dx_external_constraint(self):
        self.assertTrue(self.node.dx_constrained)

    def test_parse_dy_external_constraint(self):
        self.assertTrue(self.node.dy_constrained)
