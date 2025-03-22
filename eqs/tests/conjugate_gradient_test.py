import unittest

from eqs import Matrix, Vector
from eqs.conjugate_gradient import conjugate_gradient_solve


class ConjugateGradientTest(unittest.TestCase):
    sys_matrix = Matrix(4, 4).set_data(
        [
            4.0,
            -2.0,
            4.0,
            2.0,
            -2.0,
            10.0,
            -2.0,
            -7.0,
            4.0,
            -2.0,
            8.0,
            4.0,
            2.0,
            -7.0,
            4.0,
            7.0,
        ]
    )
    sys_vec = Vector(4).set_data([20, -16, 40, 28])
    solution = Vector(4).set_data([1.0, 2.0, 3.0, 4.0])

    def test_solve(self):
        actual = conjugate_gradient_solve(self.sys_matrix, self.sys_vec)
        self.assertEqual(self.solution, actual)
