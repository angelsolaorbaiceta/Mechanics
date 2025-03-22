import unittest

from eqs import Vector
from eqs.doolitle import doolitle_decomposition, doolitle_solve
from eqs.matrix import Matrix


class DoolitleTest(unittest.TestCase):
    sys_matrix = Matrix(3, 3).set_data(
        [2.0, -1.0, -2.0, -4.0, 6.0, 3.0, -4.0, -2.0, 8.0]
    )
    expected_lower_matrix = Matrix(3, 3).set_data(
        [1.0, 0.0, 0.0, -2.0, 1.0, 0.0, -2.0, -1.0, 1.0]
    )
    expected_upper_matrix = Matrix(3, 3).set_data(
        [2.0, -1.0, -2.0, 0.0, 4.0, -1.0, 0.0, 0.0, 3.0]
    )

    sys_vec = Vector(3).set_data([-6, 17, 16])
    expected_solution = Vector(3).set_data([1.0, 2.0, 3.0])

    def test_doolitle_lower_decomposition(self):
        (lower, _) = doolitle_decomposition(self.sys_matrix)
        self.assertEqual(self.expected_lower_matrix, lower)

    def test_doolitle_upper_decomposition(self):
        (_, upper) = doolitle_decomposition(self.sys_matrix)
        self.assertEqual(self.expected_upper_matrix, upper)

    def test_solve_system(self):
        actual = doolitle_solve(self.sys_matrix, self.sys_vec)
        self.assertEqual(self.expected_solution, actual)
