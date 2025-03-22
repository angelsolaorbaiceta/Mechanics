from typing import List
from geom2d.point import Point
from geom2d.rect import Rect
from geom2d.size import Size


def make_rect_containing(points: List[Point]):
    """
    Computes the smallest rectangle containing all the passed
    points.

    :param points: `[Point]`
    :return: `Rect`
    """
    if not points:
        raise ValueError("Expected at least one point")

    first_point = points[0]
    min_x, max_x = first_point.x, first_point.x
    min_y, max_y = first_point.y, first_point.y

    for point in points[1:]:
        min_x, max_x = min(min_x, point.x), max(max_x, point.x)
        min_y, max_y = min(min_y, point.y), max(max_y, point.y)

    return Rect(Point(min_x, min_y), Size(max_x - min_x, max_y - min_x))


def make_rect_containing_with_margin(points: List[Point], margin: float):
    """
    Computes the smallest rectangle containing all the passed
    points, and adds a margin to all four sides.

    :param points: `[Point]`
    :param margin: `float`
    :return: `Rect`
    """
    rect = make_rect_containing(points)
    return Rect(
        Point(rect.origin.x - margin, rect.origin.y - margin),
        Size(2 * margin + rect.size.width, 2 * margin + rect.size.height),
    )


def make_rect_centered(center: Point, width: float, height: float):
    """
    Computes a rectangle which center point is `center` and with
    a size of `width` and `height`.

    :param center: `Point`
    :param width: `float`
    :param height: `float`
    :return:
    """
    origin = Point(center.x - width / 2, center.y - height / 2)
    return Rect(origin, Size(width, height))
