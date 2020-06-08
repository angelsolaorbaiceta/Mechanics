from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution
from .vector_svg import vector_to_svg


def node_reactions_to_svg(
        solution: StructureSolution,
        settings,
        config
):
    def reaction_svg(node: StrNodeSolution):
        position = node.displaced_pos_scaled(settings.disp_scale)
        reaction = solution.reaction_for_node(node)
        return vector_to_svg(
            origin=position,
            vector=reaction,
            scale=settings.load_scale,
            color=config['colors']['reaction'],
            config=config
        )

    return [
        reaction_svg(node)
        for node in solution.nodes
        if node.is_constrained
    ]
