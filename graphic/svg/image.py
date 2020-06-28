from geom2d import AffineTransform, Rect, Point
from graphic.svg.read import read_template


def svg_content(
        size, primitives, viewbox_rect=None, transform=None
):
    """
    Returns the string content of an SVG image containing the
    passed list of primitives and 
    :param size:
    :param primitives:
    :param viewbox_rect:
    :param transform:
    :return:
    """
    viewbox_rect = viewbox_rect or __default_viewbox_rect(size)
    transform = transform or __default_transform()
    template = read_template('img')

    return template \
        .replace('{{width}}', str(size.width)) \
        .replace('{{height}}', str(size.height)) \
        .replace('{{content}}', '\n\t'.join(primitives)) \
        .replace('{{viewBox}}', __viewbox_from_rect(viewbox_rect))\
        .replace('{{transf}}', __transf_matrix_vals(transform))


def __default_viewbox_rect(size):
    return Rect(Point(0, 0), size)


def __default_transform():
    return AffineTransform(1, 1, 0, 0)


def __viewbox_from_rect(rect: Rect):
    x = rect.origin.x
    y = rect.origin.y
    width = rect.size.width
    height = rect.size.height

    return f'{x} {y} {width} {height}'


def __transf_matrix_vals(t: AffineTransform):
    return f'{t.sx} {t.shy} {t.shx} {t.sy} {t.tx} {t.ty}'
