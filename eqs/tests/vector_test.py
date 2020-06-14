import unittest

from eqs.vector import Vector


class VectorTest(unittest.TestCase):

    def test_length(self):
        self.assertEqual(5, Vector(5).length)

    def test_sum(self):
        vector = Vector(3).set_data([1, 2, 3])
        self.assertEqual(6, vector.sum)

    def test_unset_value_is_zero(self):
        vector = Vector(2)
        self.assertEqual(0.0, vector.value_at(0))
        self.assertEqual(0.0, vector.value_at(1))

    def test_set_get_value(self):
        value = 10.0
        vector = Vector(2).set_value(value, 1)
        self.assertEqual(0.0, vector.value_at(0))
        self.assertEqual(value, vector.value_at(1))

    def test_add_to_value(self):
        vector = Vector(2).set_data([1, 2]).add_to_value(10, 0)
        self.assertEqual(11, vector.value_at(0))
        self.assertEqual(2, vector.value_at(1))

    def test_scaled(self):
        vector = Vector(3).set_data([1, 2, 3])
        expected = Vector(3).set_data([2, 4, 6])

        self.assertEqual(expected, vector.scaled(2))

    def test_subtract_vectors(self):
        v1 = Vector(2).set_data([4, 5])
        v2 = Vector(2).set_data([2, 1])
        expected = Vector(2).set_data([2, 4])

        self.assertEqual(expected, v1 - v2)

    def test_add_vectors(self):
        v1 = Vector(2).set_data([4, 5])
        v2 = Vector(2).set_data([2, 3])
        expected = Vector(2).set_data([6, 8])

        self.assertEqual(expected, v1 + v2)

    def test_multiply_vectors(self):
        v1 = Vector(2).set_data([4, 5])
        v2 = Vector(2).set_data([2, 3])
        expected = Vector(2).set_data([8, 15])

        self.assertEqual(expected, v1 * v2)
