import math

from geom2d.affine_transf import AffineTransform
from geom2d.interpolation import ease_in_out_t_sequence, \
    interpolate
from geom2d.point import Point


def make_scale(sx: float, sy: float, center=Point(0, 0)):
    """
    Creates a scaling affine transformation about the `center`
    point and using the `sx` and `sy` scale factors.

    :param sx: scale in the x-axis
    :param sy: scale in the y-axis
    :param center: center point
    :return: `AffineTransform`
    """
    return AffineTransform(
        sx=sx,
        sy=sy,
        tx=center.x * (1.0 - sx),
        ty=center.y * (1.0 - sy)
    )


def make_rotation(radians: float, center=Point(0, 0)):
    """
    Creates a rotation affine transformation of the given angle
    in radians about the `center` point.

    :param radians: angle in radians
    :param center: center point
    :return: `AffineTransform`
    """
    cos = math.cos(radians)
    sin = math.sin(radians)
    one_minus_cos = 1.0 - cos

    return AffineTransform(
        sx=cos,
        sy=cos,
        tx=center.x * one_minus_cos + center.y * sin,
        ty=center.y * one_minus_cos - center.x * sin,
        shx=-sin,
        shy=sin
    )


def ease_in_out_interpolation(
        start: AffineTransform,
        end: AffineTransform,
        steps: int
):
    """
    Creates a sequence of affine transformations from a `start`
    transformation to an `end` transformation using an ease-out
    interpolation function.

    :param start: start affine transformation
    :param end: end affine transformation
    :param steps: number of steps to use in the interpolation
    :return:
    """
    t_seq = ease_in_out_t_sequence(steps)
    return [__interpolated(start, end, t) for t in t_seq]


def __interpolated(s: AffineTransform, e: AffineTransform, t: float):
    return AffineTransform(
        sx=interpolate(s.sx, e.sx, t),
        sy=interpolate(s.sy, e.sy, t),
        tx=interpolate(s.tx, e.tx, t),
        ty=interpolate(s.ty, e.ty, t),
        shx=interpolate(s.shx, e.shx, t),
        shy=interpolate(s.shy, e.shy, t)
    )
