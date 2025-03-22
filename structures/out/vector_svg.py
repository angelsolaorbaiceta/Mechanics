from geom2d import Point, Vector, Segment
from graphic import svg
from graphic.svg import attributes
from .captions_svg import caption_to_svg

__I_VERSOR = Vector(1, 0)
__CAPTION_DISP = 10
__DECIMAL_POS = 2


def vector_to_svg(position: Point, vector: Vector, scale: float, color: str, config):
    """
    Creates an SVG representation of the given vector using an
    arrow and a label aligned with the arrow.

    :param position: origin of the vector
    :param vector: `Vector`
    :param scale: scale to use in the drawing
    :param color: color to use for the arrow and label
    :param config: configuration dictionary
    :return: SVG arrow and label
    """
    segment = Segment(position.displaced(vector, -scale), position)
    caption_origin = segment.start.displaced(segment.normal_versor, __CAPTION_DISP)

    def svg_arrow():
        width = config["sizes"]["stroke"]
        arrow_size = config["sizes"]["arrow"]

        return svg.arrow(
            segment,
            arrow_size,
            arrow_size,
            [
                attributes.stroke_color(color),
                attributes.stroke_width(width),
                attributes.fill_color("none"),
            ],
        )

    def svg_caption():
        return caption_to_svg(
            vector.to_formatted_str(__DECIMAL_POS),
            caption_origin,
            vector.angle_to(__I_VERSOR),
            color,
            config,
        )

    return svg.group([svg_arrow(), svg_caption()])
