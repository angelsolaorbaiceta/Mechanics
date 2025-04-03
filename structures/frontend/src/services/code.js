export function highlightCode(lines) {
	const code = lines.map((line) => `<div class="line">${line}</div>`).join('\n')
	console.log(code)
	return code
}
