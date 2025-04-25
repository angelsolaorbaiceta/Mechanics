<script>
	import { calculateLabelTransform } from '../services/drawing.js'
	import { lengthBetween } from '../services/utils.js'
	import { appState } from './state.svelte.js'

	let { bar, nodesById } = $props()
	let start = $derived(nodesById.get(bar.startNodeId))
	let end = $derived(nodesById.get(bar.endNodeId))
	let labelPos = $derived(calculateLabelTransform(start.pos, end.pos))
	let length = $derived(lengthBetween(start.pos, end.pos))
</script>

<line x1={start.pos.x} y1={start.pos.y} x2={end.pos.x} y2={end.pos.y} />
{#if appState.appearance.labels.show}
	<text class="svg-label label" x={labelPos.cx} y={labelPos.cy} transform={labelPos.transform}>
		B{bar.id} ({length.toFixed(2)}
		{appState.appearance.units.length})
	</text>
{/if}

<style>
	.label {
		fill: var(--drawing-text-color);
	}
</style>
