from geom2d import Vector, Point
from graphic import svg
from structures.solution.node import StrNodeSolution
from .vector_svg import vector_to_svg


def loads_to_svg(nodes: [StrNodeSolution], settings, config):
    def svg_node_loads(node: StrNodeSolution):
        position = node.displaced_pos_scaled(settings.disp_scale)
        return svg.group(
            [
                svg_load(position, load)
                for load in node.loads
            ]
        )

    def svg_load(position: Point, load: Vector):
        return vector_to_svg(
            position=position,
            vector=load,
            scale=settings.load_scale,
            color=config['colors']['load'],
            config=config
        )

    return [
        svg_node_loads(node)
        for node in nodes
        if node.is_loaded
    ]
