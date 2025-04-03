import { solveStructure as solve } from '../api/solve.js'

export async function solveStructure(structure) {
	// TODO: Basic validation of the structure
	return solve(structure)
}
