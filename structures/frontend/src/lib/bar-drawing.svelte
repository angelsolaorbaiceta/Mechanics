<script>
	import { calculateLabelTransform } from '../services/drawing.js'

	let { bar, nodesById, showLabels } = $props()
	let start = $derived(nodesById.get(bar.startNodeId))
	let end = $derived(nodesById.get(bar.endNodeId))
	let labelPos = $derived(calculateLabelTransform(start.pos, end.pos))
</script>

<line x1={start.pos.x} y1={start.pos.y} x2={end.pos.x} y2={end.pos.y} />
{#if showLabels}
	<text class="svg-label label" x={labelPos.cx} y={labelPos.cy} transform={labelPos.transform}>
		B{bar.id}
	</text>
{/if}

<style>
	.label {
		fill: var(--drawing-text-color);
	}
</style>
