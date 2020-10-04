from geom2d import Point, Polygon


def make_polygon_from_coords(coords: [float]):
    """
    Creates a `Polygon` instance using the passed in coordinates:
    `[x1 y1 x2 y2 ... xn yn]`.

    It raises a `ValueError` if the coordinates list does't have
    an even number of entries.

    :param coords: list of the coordinates of the vertices
    :return: `Polygon`
    """
    if len(coords) % 2 != 0:
        raise ValueError('Need an even number of coordinates')

    indices = range(0, len(coords), 2)
    return Polygon(
        [Point(coords[i], coords[i + 1]) for i in indices]
    )
