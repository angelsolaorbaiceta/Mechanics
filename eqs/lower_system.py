from eqs.matrix import Matrix
from eqs.vector import Vector


def solve_lower_sys(low_mat: Matrix, vector: Vector) -> Vector:
    """
    Given a lower triangular matrix `low_mat` [L] and a vector
    `vector' [b], computes the [L][x] = [b] system solution,
    [x], by forward substitution.

    :param low_mat: lower triangular `Matrix` [L]
    :param vector: system's `Vector` [b]
    :return: solution `Vector` [x]
    """
    size = vector.length
    solution = Vector(size)

    for i in range(size):
        _sum = 0.0

        for j in range(i):
            l_ij = low_mat.value_at(i, j)
            y_j = solution.value_at(j)
            _sum += l_ij * y_j

        b_i = vector.value_at(i)
        l_ii = low_mat.value_at(i, i)
        solution_val = (b_i - _sum) / l_ii
        solution.set_value(solution_val, i)

    return solution
