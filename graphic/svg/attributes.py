from geom2d.affine_transf import AffineTransform


def stroke_color(color: str):
    """
    Returns an SVG stroke attribute using the given color.

    :param color: `string` stroke color
    :return: stoke="<color>"
    """
    return f'stroke="{color}"'


def stroke_width(width: float):
    """
    Returns an SVG stroke width attribute using the given width.

    :param width: `float` stroke width
    :return: stroke-width="<width>"
    """
    return f'stroke-width="{str(width)}"'


def fill_color(color: str):
    """
    Returns an SVG fill color attribute using the given color.

    :param color: `string` fill color
    :return: fill="<color>"
    """
    return f'fill="{color}"'


def fill_opacity(opacity: float):
    """
    Returns an SVG fill opacity using the given value between 0
    and 1, where 0 means fully transparent and 1 is fully opaque.

    :param opacity: `float` opacity value
    :return: fill-opacity="<opacity>"
    """
    return f'fill-opacity="{str(opacity)}"'


def affine_transform(t: AffineTransform):
    """
    Returns an SVG affine transformation matrix attribute.

    :param t: `AffineTransform`
    :return: transform="matrix(sx shy shx sy tx ty)"
    """
    values = f'{t.sx} {t.shy} {t.shx} {t.sy} {t.tx} {t.ty}'
    return f'transform="matrix({values})"'


def font_size(size: int):
    """
    Returns an SVG font size attribute using the given size.

    :param size: `int` font size
    :return: font-size="<size>px"
    """
    return f'font-size="{str(size)}px"'


def font_family(font: str):
    """
    Returns an SVG font family attribute using the given font name.

    :param font: `str` font name
    :return: font-family="<font>"
    """
    return f'font-family="{font}"'


def attrs_to_str(attrs_list: [str]):
    """
    Combines a list of SVG attributes in a single string.

    :param attrs_list: list of attributes
    :return: combined attributes string
    """
    return ' '.join(attrs_list)
