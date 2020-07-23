from geom2d import Circle, Rect, Segment, Point, Polygon, Vector
from graphic.svg.attributes import attrs_to_str
from graphic.svg.read import read_template

__segment_template = read_template('line')
__rect_template = read_template('rect')
__circle_template = read_template('circle')
__polygon_template = read_template('polygon')
__polyline_template = read_template('polyline')
__text_template = read_template('text')
__group_template = read_template('group')


def segment(seg: Segment, attributes=()):
    """
    Returns an SVG line segment element as string.

    :param seg: `Segment` geometric primitive
    :param attributes: list of SVG attributes
    :return: <line x1="" y1="" x2="" y2="" ... />
    """
    return __segment_template \
        .replace('{{x1}}', str(seg.start.x)) \
        .replace('{{y1}}', str(seg.start.y)) \
        .replace('{{x2}}', str(seg.end.x)) \
        .replace('{{y2}}', str(seg.end.y)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def rectangle(rect: Rect, attributes=()):
    """
    Returns an SVG rectangle element as string.

    :param rect: `Rect` geometric primitive
    :param attributes: list of SVG attributes
    :return: <rect x="" y="" width="" height="" ... />
    """
    return __rect_template \
        .replace('{{x}}', str(rect.origin.x)) \
        .replace('{{y}}', str(rect.origin.y)) \
        .replace('{{width}}', str(rect.size.width)) \
        .replace('{{height}}', str(rect.size.height)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def circle(circ: Circle, attributes=()):
    """
    Returns an SVG circle element as string.

    :param circ: `Circle` geometric primitive
    :param attributes: list of SVG attributes
    :return: <circle cx="" cy="" r="" ... />
    """
    return __circle_template \
        .replace('{{cx}}', str(circ.center.x)) \
        .replace('{{cy}}', str(circ.center.y)) \
        .replace('{{r}}', str(circ.radius)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def polygon(pol: Polygon, attributes=()):
    """
    Returns an SVG polygon element as string.

    :param pol: `Polygon` geometric primitive
    :param attributes:  list of SVG attributes
    :return: <polygon points="" ... />
    """
    return __polygon_template \
        .replace('{{points}}', __format_points(pol.vertices)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def polyline(points, attributes=()):
    return __polyline_template \
        .replace('{{points}}', __format_points(points)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def text(txt, pos: Point, disp: Vector, attrs_list=()):
    return __text_template \
        .replace('{{x}}', str(pos.x)) \
        .replace('{{y}}', str(pos.y)) \
        .replace('{{dx}}', str(disp.u)) \
        .replace('{{dy}}', str(disp.v)) \
        .replace('{{text}}', txt) \
        .replace('{{attrs}}', attrs_to_str(attrs_list))


def group(primitives, attributes=()):
    return __group_template \
        .replace('{{content}}', '\n\t'.join(primitives)) \
        .replace('{{attrs}}', attrs_to_str(attributes))


def arrow(_segment: Segment, length, height, attributes=()):
    director = _segment.direction_vector
    v_l = director.opposite().with_length(length)
    v_h1 = director.perpendicular().with_length(height / 2.0)
    v_h2 = v_h1.opposite()

    return group(
        [
            segment(_segment),
            polyline([
                _segment.end.displaced(v_l + v_h1),
                _segment.end,
                _segment.end.displaced(v_l + v_h2)
            ])
        ],
        attributes
    )


def __format_points(points):
    return ' '.join([f'{p.x},{p.y}' for p in points])
