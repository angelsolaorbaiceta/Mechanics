from geom2d.point import Point
from geom2d.vector import Vector


def make_vector_between(p: Point, q: Point):
    return Vector(q.x - p.x, q.y - p.y)


def make_versor(u, v):
    return Vector(u, v).normalized()


def make_versor_between(p, q):
    return make_vector_between(p, q).normalized()
