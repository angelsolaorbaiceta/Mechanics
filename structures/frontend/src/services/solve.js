import { solveStructure as solve } from '../api/solve.js'

export async function solveStructure(structure, lines) {
	// TODO: Basic validation of the structure
	// Has loads applied
	// Has external contraints
	// Is isostatic
	console.log('solveStructure()', structure)
	const { data: solution } = await solve(lines)

	const stress = calculateStressMeta(solution.bars)

	return {
		...solution,
		meta: {
			stress,
			displacement: calculateDisplacementsMeta(solution.nodes),
			reaction: calculateReactionsMeta(solution.nodes),
			barStrokes: new Map(solution.bars.map((bar) => [bar.id, strokeWidthForBar(bar, stress)]))
		}
	}
}

function calculateStressMeta(bars) {
	const firstBar = bars[0]
	const { min, max } = bars.reduce(
		({ min, max }, bar) => ({
			min: Math.min(min, Math.abs(bar.stress)),
			max: Math.max(max, Math.abs(bar.stress))
		}),
		{ min: Math.abs(firstBar.stress), max: Math.abs(firstBar.stress) }
	)

	return { min, max }
}

function calculateDisplacementsMeta(nodes) {
	const displacements = nodes.map(({ position }) => {
		const { original, displaced } = position
		return distanceBetween(original, displaced)
	})

	const { max, p50 } = calculateMetrics(displacements)

	// Suggest a scale that makes the p50 displacement at least 50 units in the drawing
	const suggestedScale = Math.ceil(50 / p50)

	return {
		max,
		p50,
		suggestedScale
	}
}

function calculateReactionsMeta(nodes) {
	const reactions = nodes
		.filter((node) => !!node.reaction)
		.map(({ reaction }) => Math.sqrt(reaction.x ** 2 + reaction.y ** 2))

	const { max, p50 } = calculateMetrics(reactions)

	// Suggest a scale that makes the max reaction be around 200 units in the drawing
	const suggestedScale = Number((200 / max).toFixed(4))

	return { max, p50, suggestedScale }
}

function calculateMetrics(nums) {
	if (nums.length === 0) {
		return {
			max: 0,
			p50: 0
		}
	}

	if (nums.length === 1) {
		return {
			max: nums[0],
			p50: nums[0]
		}
	}

	nums.sort()

	const midIndex = Math.floor(nums.length / 2)
	const p50 = nums.length % 2 === 0 ? (nums[midIndex - 1] + nums[midIndex]) / 2 : nums[midIndex]

	return {
		max: nums[nums.length - 1],
		p50
	}
}

function distanceBetween(one, two) {
	return Math.sqrt((two.x - one.x) ** 2 + (two.y - one.y) ** 2)
}

function strokeWidthForBar({ stress }, { min, max }) {
	// Choose numbers from 2 to 10, in increments of 0.25 based on the stress
	const percentage = (Math.abs(stress) - min) / (max - min)
	const rawInterpolated = 2 + percentage * 8
	const rounded = Math.round(rawInterpolated * 4) / 4

	return rounded
}
