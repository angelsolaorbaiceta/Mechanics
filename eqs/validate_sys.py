from eqs import Matrix, Vector


def validate_system(sys_matrix: Matrix, sys_vector: Vector):
    """
    Makes sure the system of equations represented by the given
    matrix and vector match in size and that the matrix is square.

    :param sys_matrix: `Matrix`
    :param sys_vector: `Vector`
    """
    if sys_matrix.cols_count != sys_vector.length:
        raise ValueError('Size mismatch between matrix and vector')

    if not sys_matrix.is_square:
        raise ValueError('System matrix must be square')
