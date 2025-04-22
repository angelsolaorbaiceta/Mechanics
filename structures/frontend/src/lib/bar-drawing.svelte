<script>
	import { calculateLabelTransform } from '../services/drawing.js'

	let { bar, nodesById, showLabels } = $props()
	let start = $derived(nodesById.get(bar.startNodeId))
	let end = $derived(nodesById.get(bar.endNodeId))
	let labelPos = $derived(calculateLabelTransform(start.pos, end.pos))
</script>

<line x1={start.pos.x} y1={start.pos.y} x2={end.pos.x} y2={end.pos.y} />
{#if showLabels}
	<text
		class="label"
		x={labelPos.cx}
		y={labelPos.cy}
		text-anchor="middle"
		dominant-baseline="central"
		transform-origin="center"
		transform={labelPos.transform}
	>
		B{bar.id}
	</text>
{/if}

<style>
	.label {
		stroke: none;
		transform-box: fill-box;
		fill: var(--drawing-text-color);
		font: 13px sans-serif;
	}
</style>
