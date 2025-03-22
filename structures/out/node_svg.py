from typing import List
from geom2d import Circle, Vector
from graphic import svg
from graphic.svg import attributes
from structures.solution.node import StrNodeSolution
from .captions_svg import caption_to_svg


def nodes_to_svg(nodes: List[StrNodeSolution], settings, config):
    def node_to_svg(node: StrNodeSolution):
        radius = config["sizes"]["node_radius"]
        stroke_size = config["sizes"]["stroke"]
        stroke_color = config["colors"]["node_stroke"]
        fill_color = config["colors"]["back"]
        position = node.displaced_pos_scaled(settings.disp_scale)
        caption_pos = position.displaced(Vector(radius, radius))

        return svg.group(
            [
                svg.circle(
                    Circle(position, radius),
                    [
                        attributes.stroke_width(stroke_size),
                        attributes.stroke_color(stroke_color),
                        attributes.fill_color(fill_color),
                    ],
                ),
                caption_to_svg(f"{node.id}", caption_pos, 0, stroke_color, config),
            ]
        )

    return [node_to_svg(node) for node in nodes]
