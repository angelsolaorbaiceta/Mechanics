from geom2d.point import Point
from geom2d.vector import Vector


def make_vector_between(p: Point, q: Point):
    """
    Creates a `Vector` going from point `p` to point `q`.

    :param p: origin `Point`
    :param q: tip `Point`
    :return: `Vector`
    """
    return Vector(q.x - p.x, q.y - p.y)


def make_versor(u, v):
    """
    Creates a `Vector` with `u` and `v` projections, then
    normalizes it.

    :param u: `float` horizontal projection
    :param v: `float` vertical projection
    :return: `Vector` with unitary norm
    """
    return Vector(u, v).normalized()


def make_versor_between(p: Point, q: Point):
    """
    Returns a `Vector` with unitary length in the direction
    defined from point `p` to point `q`.

    :param p: origin `Point`
    :param q: tip `Point`
    :return: `Vector` with unitary norm
    """
    return make_vector_between(p, q).normalized()
