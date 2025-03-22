from geom2d import Point, Vector, make_rotation, make_scale
from graphic import svg
from graphic.svg import attributes


def caption_to_svg(caption: str, position: Point, angle: float, color: str, config):
    """
    Creates the SVG caption with the `caption` text, located at
    `position` and rotated `angle` radians.

    :param caption: caption's text
    :param position: caption's position
    :param angle: caption's rotated angle
    :param color: caption's color
    :param config: configuration dictionary
    :return: `SVG`
    """
    font = config["font"]["family"]
    size = config["font"]["size"]

    rotation = make_rotation(angle, position)
    scale = make_scale(1, -1, position)
    transform = rotation.then(scale)

    return svg.text(
        caption,
        position,
        Vector(0, 0),
        [
            attributes.fill_color(color),
            attributes.affine_transform(transform),
            attributes.font_family(font),
            attributes.font_size(size),
        ],
    )
