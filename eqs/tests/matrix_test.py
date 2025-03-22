import unittest

from eqs import Vector
from eqs.matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_is_square(self):
        self.assertTrue(Matrix(2, 2).is_square)

    def test_is_not_square(self):
        self.assertFalse(Matrix(2, 3).is_square)

    def test_unset_value_is_zero(self):
        matrix = Matrix(2, 2)
        self.assertEqual(0.0, matrix.value_at(0, 1))

    def test_set_get_value(self):
        value = 10.0
        matrix = Matrix(2, 2).set_value(value, 0, 1)
        self.assertEqual(value, matrix.value_at(0, 1))

    def test_add_to_value(self):
        expected = [1, 12, 3, 4]
        matrix = Matrix(2, 2).set_data([1, 2, 3, 4]).add_to_value(10, 0, 1)
        self.assert_matrix_has_data(matrix, expected)

    def test_set_data(self):
        data = [1, 2, 3, 4, 5, 6]
        matrix = Matrix(2, 3).set_data(data)
        self.assert_matrix_has_data(matrix, data)

    def test_set_identity_row(self):
        expected = [1, 0, 4, 5]
        matrix = Matrix(2, 2).set_data([2, 3, 4, 5]).set_identity_row(0)
        self.assert_matrix_has_data(matrix, expected)

    def test_set_identity_col(self):
        expected = [2, 0, 4, 1]
        matrix = Matrix(2, 2).set_data([2, 3, 4, 5]).set_identity_col(1)
        self.assert_matrix_has_data(matrix, expected)

    def test_scale(self):
        expected = [2, 4, 6, 8, 10, 12]
        matrix = Matrix(2, 3).set_data([1, 2, 3, 4, 5, 6]).scale(2)
        self.assert_matrix_has_data(matrix, expected)

    def test_multiply_vector(self):
        vector = Vector(3).set_data([1, 2, 3])
        matrix = Matrix(2, 3).set_data([1, 2, 3, 4, 5, 6])
        expected = Vector(2).set_data([14, 32])

        self.assertEqual(expected, matrix.times_vector(vector))

    def test_cant_add_matrices(self):
        m1 = Matrix(1, 2)
        m2 = Matrix(2, 3)

        self.assertRaises(ValueError, lambda: m1 + m2)

    def test_add_matrices(self):
        m1 = Matrix(2, 2).set_data([1, 2, 3, 4])
        m2 = Matrix(2, 2).set_data([1, 2, 3, 4])
        expected_data = [2, 4, 6, 8]

        self.assert_matrix_has_data(m1 + m2, expected_data)

    def test_cant_subtract_matrices(self):
        m1 = Matrix(1, 2)
        m2 = Matrix(2, 3)

        self.assertRaises(ValueError, lambda: m1 - m2)

    def test_subtract_matrices(self):
        m1 = Matrix(2, 2).set_data([1, 2, 3, 4])
        m2 = Matrix(2, 2).set_data([4, 3, 2, 1])
        expected_data = [-3, -1, 1, 3]

        self.assert_matrix_has_data(m1 - m2, expected_data)

    def test_cant_multiply_matrices(self):
        m1 = Matrix(2, 3)
        m2 = Matrix(5, 6)

        self.assertRaises(ValueError, lambda: m1 * m2)

    def test_multiply_matrices(self):
        m1 = Matrix(2, 3).set_data([1, 2, 3, 4, 5, 6])
        m2 = Matrix(3, 2).set_data([1, 2, 3, 4, 5, 6])
        expected_data = [22, 28, 49, 64]

        self.assert_matrix_has_data(m1 * m2, expected_data)

    def test_transpose_matrix(self):
        mat = Matrix(2, 3).set_data([1, 2, 3, 4, 5, 6]).transposed()
        expected = Matrix(3, 2).set_data([1, 4, 2, 5, 3, 6])

        self.assertEqual(expected, mat)

    def assert_matrix_has_data(self, matrix, data):
        for row in range(matrix.rows_count):
            offset = matrix.cols_count * row
            for col in range(matrix.cols_count):
                self.assertEqual(data[offset + col], matrix.value_at(row, col))
