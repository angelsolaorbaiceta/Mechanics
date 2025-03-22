import unittest
from unittest.mock import patch, Mock

from geom2d import Point
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution


class StructureSolutionTest(unittest.TestCase):
    p_one = Point(2, 3)
    p_two = Point(5, 1)

    def setUp(self):
        self.n_one = Mock(spec=StrNodeSolution)
        self.n_one.displaced_pos_scaled.return_value = self.p_one
        self.n_two = Mock(spec=StrNodeSolution)
        self.n_two.displaced_pos_scaled.return_value = self.p_two

    def test_node_displaced_scaled_positions_called(self):
        solution = StructureSolution([self.n_one, self.n_two], [])
        solution.bounds_rect(margin=10, scale=4)

        self.n_one.displaced_pos_scaled.assert_called_once_with(4)
        self.n_two.displaced_pos_scaled.assert_called_once_with(4)

    @patch("structures.solution.structure.make_rect_containing_with_margin")
    def test_make_rect_called(self, make_rect_mock):
        solution = StructureSolution([self.n_one, self.n_two], [])
        solution.bounds_rect(margin=10, scale=4)

        make_rect_mock.assert_called_once_with([self.p_one, self.p_two], 10)
