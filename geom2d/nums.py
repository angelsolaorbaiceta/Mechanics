import math


def are_close_enough(a, b, tolerance=1e-10):
    """
    Tests whether two `Float` numbers `a` and `b` are closer than
    a given `tolerance` from each other.

    :param a: `Float`
    :param b: `Float`
    :param tolerance: `Float`, defaults to 1E-10
    :return: `Bool`: are `a` and `b` close enough?
    """
    return math.fabs(a - b) < tolerance


def is_close_to_zero(a, tolerance=1e-10):
    """
    Tests whether the `Float` number `a` is close enough to 0.0
    using the given `tolerance`.

    :param a: `Float`
    :param tolerance: `Float`, defaults to 1E-10
    :return: `Bool`: is `a` close to 0.0?
    """
    return are_close_enough(a, 0.0, tolerance)


def is_close_to_one(a, tolerance=1e-10):
    """
    Tests whether the `Float` number `a` is close enough to 1.0
    using the given `tolerance`.

    :param a: `Float`
    :param tolerance: `Float`, defaults to 1E-10
    :return: `Bool`: is `a` close to 0.0?
    """
    return are_close_enough(a, 1.0, tolerance)


def value_or_zero(a, tolerance=1e-10):
    """
    Returns a 0.0 value if `a` is close enough to 0.0, or simply
    `a` otherwise.

    :param a: `Float`
    :param tolerance: `Float`, defaults to 1E-10
    :return: `Float`
    """
    return 0 if is_close_to_zero(a, tolerance) else a
