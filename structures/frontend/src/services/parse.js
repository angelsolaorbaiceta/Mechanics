const nodesHeaderRe = /^\s*nodes\s*$/i
const loadsHeaderRe = /^\s*loads\s*$/i
const barsHeaderRe = /^\s*bars\s*$/i
const commentRe = /^\s*#.*$/
const nodeRe = /(?<id>\d+)\s*:\s*\((?<pos>[\d\s\\.,\\-]+)\)\s*\((?<ec>[xy]{0,2})\)/
const barRe =
	/(?<id>\d+)\s*:\s*\((?<startId>\d+)\s*->\s*(?<endId>\d+)\)\s*(?<sec>[\d\\.]+)\s+(?<young>[\d\\.]+)/
const loadRe = /^(?<id>\d+)\s+->\s+\(\s*(?<fx>-?\d+(\.\d+)?)\s*,\s*(?<fy>-?\d+(\.\d+)?)\s*\)$/

const Sections = {
	NONE: 'none',
	NODES: 'nodes',
	LOADS: 'loads',
	BARS: 'bars'
}

export function parseStructure(lines) {
	let section = Sections.NONE
	const nodes = []
	const bars = []
	const loads = []
	const errors = []
	let lineNum = 0

	function updateSection(line) {
		if (nodesHeaderRe.test(line)) {
			section = Sections.NODES
			return true
		}

		if (loadsHeaderRe.test(line)) {
			section = Sections.LOADS
			return true
		}

		if (barsHeaderRe.test(line)) {
			section = Sections.BARS
			return true
		}

		return false
	}

	for (const line of lines) {
		lineNum++

		if (commentRe.test(line) || line.trim() === '') {
			continue
		}
		if (updateSection(line)) {
			continue
		}

		// Attempt to parse an entity according to the section
		switch (section) {
			case Sections.NONE:
				errors.push({
					line: lineNum,
					message: `Can't parse "${line}" outside of a section ('nodes', 'loads', or 'bars')`
				})
				break

			case Sections.NODES:
				try {
					nodes.push(parseNode(line))
				} catch (err) {
					errors.push({ line: lineNum, message: err.message })
				}
				break

			case Sections.BARS:
				try {
					bars.push(parseBar(line))
				} catch (err) {
					errors.push({ line: lineNum, message: err.message })
				}
				break

			case Sections.LOADS:
				try {
					loads.push(parseLoad(line, lineNum))
				} catch (err) {
					errors.push({ line: lineNum, message: err.message })
				}
				break
		}
	}

	const nodesById = new Map(nodes.map((node) => [node.id, node]))

	for (const { nodeId, lineNum, fx, fy } of loads) {
		if (!nodesById.has(nodeId)) {
			errors.push({ line: lineNum, message: `Node with id ${nodeId} doesn't exist` })
		} else {
			nodesById.get(nodeId).loads.push({ fx, fy })
		}
	}

	return {
		structure: { nodes, nodesById, bars },
		errors
	}
}

function parseNode(line) {
	const match = line.match(nodeRe)
	if (!match) {
		throw new Error(`Can't parse node of: "${line}"`)
	}

	const { id, pos, ec } = match.groups
	const [x, y] = pos.split(',').map((n) => parseFloat(n))

	return {
		line,
		id,
		pos: { x, y },
		const: {
			x: ec.includes('x'),
			y: ec.includes('y')
		},
		isXConstraint() {
			return this.const.x
		},
		isYConstraint() {
			return this.const.y
		},
		isXYConstraint() {
			return this.const.x && this.const.y
		},
		loads: []
	}
}

function parseBar(line) {
	const match = line.match(barRe)
	if (!match) {
		throw new Error(`Can't parse bar of: "${line}"`)
	}

	const { id, startId, endId, sec, young } = match.groups

	return {
		id,
		line,
		startNodeId: startId,
		endNodeId: endId,
		section: parseFloat(sec),
		young: parseFloat(young)
	}
}

function parseLoad(line, lineNum) {
	const match = line.match(loadRe)
	if (!match) {
		throw new Error(`Can't parse load of: "${line}"`)
	}

	const { id, fx, fy } = match.groups

	return {
		nodeId: id,
		fx: parseFloat(fx),
		fy: parseFloat(fy),
		lineNum
	}
}
