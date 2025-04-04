<script>
	let { solution, scale } = $props()

	function displacedNodePos(node, scale) {
		const { original, displaced } = node.position
		const dx = displaced.x - original.x
		const dy = displaced.y - original.y

		return {
			x: displaced.x + dx * scale,
			y: displaced.y + dy * scale
		}
	}
</script>

<g id="solution-drawing">
	{#each solution.bars as bar}
		{@const startPos = displacedNodePos(solution.nodesById.get(bar.nodes.start), scale)}
		{@const endPos = displacedNodePos(solution.nodesById.get(bar.nodes.end), scale)}
		<line class={bar.axial} x1={startPos.x} y1={startPos.y} x2={endPos.x} y2={endPos.y} />
	{/each}
</g>

<style>
	.tension {
		stroke: var(--tension-bar-color);
		stroke-width: var(--solution-stroke-width);
	}

	.compression {
		stroke: var(--compression-bar-color);
		stroke-width: var(--solution-stroke-width);
	}
</style>
