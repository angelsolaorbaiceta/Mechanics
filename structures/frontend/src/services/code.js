const commentLineRe = /^\s*#.*$/g
const headerLineRe = /^\s*nodes|loads|bars\s*$/g

export function highlightCode(lines) {
	const result = []

	for (const line of lines) {
		if (line.match(commentLineRe)) {
			result.push(span(line, ['comment']))
			continue
		}

		if (line.match(headerLineRe)) {
			result.push(span(line, ['header']))
			continue
		}

		const tokens = tokenizeNode(line) || tokenizeLoad(line) || tokenizeBar(line)
		if (tokens !== null) {
			result.push(tokens.map(({ type, text }) => span(text, [type])).join(''))
			continue
		}

		result.push(span(line))
	}

	return result
}

function span(content, classes = []) {
	return `<span class="codeh ${classes.join(' ')}">${content}</span>`
}

function tokenizeNode(line) {
	const regex =
		/^(\s*)(\d+)(\s*:\s*\(\s*)([+-]?\d+(?:\.\d+)?)(\s*,\s*)([+-]?\d+(?:\.\d+)?)(\s*\)\s*\([a-zA-Z]*\)\s*)$/
	const match = line.match(regex)
	if (!match) return null

	const [, leading, id, beforeX, xdir, betweenXY, ydir, afterY] = match

	return [
		{ type: 'text', text: leading },
		{ type: 'id', text: id },
		{ type: 'text', text: beforeX },
		{ type: 'xdir', text: xdir },
		{ type: 'text', text: betweenXY },
		{ type: 'ydir', text: ydir },
		{ type: 'text', text: afterY }
	]
}

function tokenizeLoad(line) {
	const regex =
		/^(\s*)(\d+)(\s*->\s*\(\s*)([+-]?\d+(?:\.\d+)?)(\s*,\s*)([+-]?\d+(?:\.\d+)?)(\s*\)\s*)$/
	const match = line.match(regex)
	if (!match) return null

	const [, leading, id, beforeX, xdir, betweenXY, ydir, afterY] = match

	return [
		{ type: 'text', text: leading },
		{ type: 'id', text: id },
		{ type: 'text', text: beforeX },
		{ type: 'xdir', text: xdir },
		{ type: 'text', text: betweenXY },
		{ type: 'ydir', text: ydir },
		{ type: 'text', text: afterY }
	]
}

function tokenizeBar(line) {
	const regex =
		/^(\s*)(\d+)(\s*:\s*\()\s*(\d+)(\s*->\s*)(\d+)(\s*\)\s*\d+(?:\.\d+)?\s+[+-]?\d+(?:\.\d+)?\s*)$/
	const match = line.match(regex)
	if (!match) return null

	const [, leading, outerId, beforeInner, fromId, arrow, toId, afterTo] = match

	return [
		{ type: 'text', text: leading },
		{ type: 'id', text: outerId },
		{ type: 'text', text: beforeInner },
		{ type: 'id', text: fromId },
		{ type: 'text', text: arrow },
		{ type: 'id', text: toId },
		{ type: 'text', text: afterTo }
	]
}
