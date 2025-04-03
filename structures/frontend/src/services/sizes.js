export function structureSVGSizes(structure, { margin = 0, scale = 1, loadsScale = 1 }) {
	if (structure.nodes.length === 0) {
		return {
			width: 0,
			height: 0,
			top: 0,
			left: 0,
			margin
		}
	}

	const firstNodePos = structure.nodes[0].pos
	let minX = firstNodePos.x
	let maxX = firstNodePos.x
	let minY = firstNodePos.y
	let maxY = firstNodePos.y

	for (const { pos, loads } of structure.nodes) {
		const loadXs = loads.map(({ fx }) => pos.x + loadsScale * fx)
		minX = Math.min(minX, pos.x, ...loadXs)
		maxX = Math.max(maxX, pos.x, ...loadXs)

		const loadYs = loads.map(({ fy }) => pos.y + loadsScale * fy)
		minY = Math.min(minY, pos.y, ...loadYs)
		maxY = Math.max(maxY, pos.y, ...loadYs)
	}

	const width = scale * (maxX - minX) + 2 * margin
	const height = scale * (maxY - minY) + 2 * margin

	return {
		width: width,
		height: height,
		left: minX - margin,
		top: minY - margin,
		margin,
		x: [minX, maxX],
		y: [minY, maxY]
	}
}
