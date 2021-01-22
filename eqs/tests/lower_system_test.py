import unittest

from eqs.lower_system import solve_lower_sys
from eqs.matrix import Matrix
from eqs.vector import Vector


class LowerSystemResolutionTest(unittest.TestCase):
    low_matrix = Matrix(4, 4).set_data([
        2.0, 0.0, 0.0, 0.0,
        -1.0, 3.0, 0.0, 0.0,
        2.0, 0.0, 2.0, 0.0,
        1.0, -2.0, 1.0, 1.0
    ])
    sys_vec = Vector(4).set_data([20, -16, 40, 28])
    expected_solution = Vector(4).set_data([10, -2, 10, 4])

    def test_lower_system_resolution(self):
        actual = solve_lower_sys(self.low_matrix, self.sys_vec)
        self.assertEqual(self.expected_solution, actual)
