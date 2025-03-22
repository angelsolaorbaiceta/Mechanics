import unittest

from eqs.matrix import Matrix
from eqs.upper_system import solve_upper_sys
from eqs.vector import Vector


class UpperSystemResolutionTest(unittest.TestCase):
    upper_matrix = Matrix(4, 4).set_data(
        [
            2.0,
            -1.0,
            2.0,
            1.0,
            0.0,
            3.0,
            0.0,
            -2.0,
            0.0,
            0.0,
            2.0,
            1.0,
            0.0,
            0.0,
            0.0,
            1.0,
        ]
    )
    sys_vec = Vector(4).set_data([10, -2, 10, 4])
    expected_solution = Vector(4).set_data([1.0, 2.0, 3.0, 4.0])

    def test_upper_system_resolution(self):
        actual = solve_upper_sys(self.upper_matrix, self.sys_vec)
        self.assertEqual(self.expected_solution, actual)
