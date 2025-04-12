import { solveStructure as solve } from '../api/solve.js'

export async function solveStructure(structure, lines) {
	// TODO: Basic validation of the structure
	// Has loads applied
	// Has external contraints
	// Is isostatic
	console.log('solveStructure()', structure)
	const { data: solution } = await solve(lines)

	return solution
}
