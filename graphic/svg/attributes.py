from geom2d.affine_transf import AffineTransform


def stroke_color(color):
    """
    Returns an SVG stroke attribute using the given color.

    :param color: `String` color to be used for the stroke
    :return: `String`
    """
    return f'stroke="{color}"'


def stroke_width(width):
    return f'stroke-width="{str(width)}"'


def fill_color(color):
    return f'fill="{color}"'


def fill_opacity(opacity):
    return f'fill-opacity="{str(opacity)}"'


def affine_transform(t: AffineTransform):
    values = f'{t.sx} {t.shy} {t.shx} {t.sy} {t.tx} {t.ty}'
    return f'transform="matrix({values})"'


def font_size(size):
    return f'font-size="{size}px"'


def font_family(font):
    return f'font-family="{font}"'


def attrs_to_str(attrs_list):
    return ' '.join(attrs_list)
