from eqs.matrix import Matrix
from eqs.vector import Vector


def solve_upper_sys(up_matrix: Matrix, vector: Vector) -> Vector:
    """
    Given an upper triangular matrix `up_matrix` [U] and a vector
    `vector` [b], computes the [U][x] = [b] system solution,
    [x], by backward substitution.

    :param up_matrix: upper triangular `Matrix` [U]
    :param vector: system's `Vector` [b]
    :return: solution vector [x]
    """
    size = vector.length
    last_index = size - 1
    solution = Vector(size)

    for i in range(last_index, -1, -1):
        _sum = 0.0

        for j in range(i + 1, size):
            u_ij = up_matrix.value_at(i, j)
            x_j = solution.value_at(j)
            _sum += u_ij * x_j

        y_i = vector.value_at(i)
        u_ii = up_matrix.value_at(i, i)
        solution_val = (y_i - _sum) / u_ii
        solution.set_value(solution_val, i)

    return solution
