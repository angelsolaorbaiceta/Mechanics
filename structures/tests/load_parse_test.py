import unittest

from geom2d import Vector
from structures.parse.load_parse import parse_load


class LoadParseTest(unittest.TestCase):

    load_str = '1 -> (250.0, -3500.0)'
    (node_id, load) = parse_load(load_str)

    def test_parse_node_id(self):
        self.assertEqual(1, self.node_id)

    def test_parse_load_vector(self):
        expected = Vector(250.0, -3500.0)
        self.assertEqual(expected, self.load)
