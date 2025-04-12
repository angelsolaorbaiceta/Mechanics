<script>
	import { displacedNodePos, calculateLabelTransform } from '../services/drawing.js'

	let { solution, scale, reactionsScale } = $props()
	let displacedNodePosById = $derived(
		new Map(solution.nodes.map((node) => [node.id, displacedNodePos(node, scale)]))
	)
</script>

<g id="solution-drawing">
	{#each solution.bars as bar}
		{@const startPos = displacedNodePosById.get(bar.nodes.start)}
		{@const endPos = displacedNodePosById.get(bar.nodes.end)}
		<line
			class={bar.axial}
			x1={startPos.x}
			y1={startPos.y}
			x2={endPos.x}
			y2={endPos.y}
			stroke-linecap="round"
		/>

		{@const { cx, cy, transform } = calculateLabelTransform(startPos, endPos)}
		<text
			class={`label-${bar.axial}`}
			x={cx}
			y={cy}
			text-anchor="middle"
			dominant-baseline="central"
			transform-origin="center"
			{transform}
		>
			{`σ=${bar.stress}`}
		</text>
	{/each}

	<g class="reactions">
		{#each solution.nodes as node}
			{#if node.reaction}
				{@const { x, y } = displacedNodePosById.get(node.id)}
				{@const reaction = node.reaction}
				{@const endPos = { x: x + reactionsScale * reaction.x, y: y + reactionsScale * reaction.y }}
				{@const { cx, cy, transform } = calculateLabelTransform({ x, y }, endPos)}
				<line
					x1={x}
					y1={y}
					x2={endPos.x}
					y2={endPos.y}
					stroke-linecap="round"
					marker-end="url(#arrow)"
				/>
				<text
					class="label-reaction"
					x={cx}
					y={cy}
					text-anchor="middle"
					dominant-baseline="central"
					transform-origin="center"
					{transform}
					>{`R={${reaction.x.toFixed(1)}, ${reaction.y.toFixed(1)}}`}
				</text>
			{/if}
		{/each}
	</g>
</g>

<style>
	.tension {
		stroke: var(--tension-bar-color);
		stroke-width: var(--solution-stroke-width);
	}
	.label-tension {
		stroke: none;
		fill: var(--tension-bar-color);
		transform-box: fill-box;
	}

	.compression {
		stroke: var(--compression-bar-color);
		stroke-width: var(--solution-stroke-width);
	}
	.label-compression {
		stroke: none;
		fill: var(--compression-bar-color);
		transform-box: fill-box;
	}

	.reactions {
		stroke: var(--reaction-forces);
		fill: none;
		stroke-width: var(--loads-stroke-width);
	}
	.label-reaction {
		stroke: none;
		fill: var(--reaction-forces);
		transform-box: fill-box;
	}
</style>
