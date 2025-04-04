import { solveStructure as solve } from '../api/solve.js'

export async function solveStructure(structure, lines) {
	// TODO: Basic validation of the structure
	console.log(structure)
	const { data: solution } = await solve(lines)

	solution.nodesById = new Map(solution.nodes.map((node) => [node.id, node]))

	return solution
}
