export function structureSVGSizes(
	structure,
	solution,
	{ margin = 0, scale = 1, loadsScale = 1, solutionScale = 1, reactionsScale = 1 }
) {
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

	function updateX(...xValues) {
		minX = Math.min(minX, ...xValues)
		maxX = Math.max(maxX, ...xValues)
	}

	function updateY(...yValues) {
		minY = Math.min(minY, ...yValues)
		maxY = Math.max(maxY, ...yValues)
	}

	for (const { pos, loads } of structure.nodes) {
		const loadXs = loads.map(({ fx }) => pos.x + loadsScale * fx)
		const loadYs = loads.map(({ fy }) => pos.y + loadsScale * fy)
		updateX(pos.x, ...loadXs)
		updateY(pos.y, ...loadYs)
	}

	// Account for the solution geometry and loads
	for (const node of solution?.nodes ?? []) {
		const { x, y } = displacedNodePos(node, solutionScale)

		updateX(x)
		updateY(y)

		if (node.reaction) {
			updateX(x + node.reaction.x * reactionsScale)
			updateY(y + node.reaction.y * reactionsScale)
		}
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

export function displacedNodePos(node, scale) {
	const { original, displaced } = node.position
	const dx = displaced.x - original.x
	const dy = displaced.y - original.y

	return {
		x: displaced.x + dx * scale,
		y: displaced.y + dy * scale
	}
}

export function calculateLabelTransform(startPos, endPos, separation = 15) {
	const centerX = Math.round((startPos.x + endPos.x) / 2)
	const centerY = Math.round((startPos.y + endPos.y) / 2)
	const angle = (Math.atan2(endPos.y - startPos.y, endPos.x - startPos.x) * 180) / Math.PI
	const adjustedAngle = angle > 90 || angle < -90 ? angle + 180 : angle

	return {
		transform: `rotate(${adjustedAngle.toFixed(3)}) translate(0, ${separation}) scale(1, -1)`,
		cx: centerX,
		cy: centerY
	}
}
