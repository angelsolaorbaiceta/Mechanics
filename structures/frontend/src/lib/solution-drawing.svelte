<script>
	import { displacedNodePos, calculateLabelTransform } from '../services/drawing.js'

	let { solution, scale, reactionsScale, units, showBarPopover } = $props()
	let displacedNodePosById = $derived(
		new Map(solution.nodes.map((node) => [node.id, displacedNodePos(node, scale)]))
	)
	let stressUnits = $derived(`${units.force}/${units.length}2`)
</script>

<g id="solution-drawing">
	{#each solution.bars as bar}
		{@const startPos = displacedNodePosById.get(bar.nodes.start)}
		{@const endPos = displacedNodePosById.get(bar.nodes.end)}
		{@const { cx, cy, transform } = calculateLabelTransform(startPos, endPos)}
		<g
			aria-describedby="bar-result-popover"
			role="graphics-symbol"
			onmouseover={(event) => showBarPopover(event.target, bar)}
			onfocus={(event) => showBarPopover(event.target, bar)}
		>
			<line
				class={bar.axial}
				x1={startPos.x}
				y1={startPos.y}
				x2={endPos.x}
				y2={endPos.y}
				stroke-linecap="round"
				stroke-width={solution.meta.barStrokes.get(bar.id)}
			/>

			<text
				class={`svg-label label-${bar.axial}`}
				x={cx}
				y={cy}
				text-anchor="middle"
				dominant-baseline="central"
				transform-origin="center"
				{transform}
			>
				{`σ=${bar.stress} ${stressUnits}`}
			</text>
		</g>
	{/each}

	<g class="reactions">
		{#each solution.nodes as node}
			{#if node.reaction}
				{@const { x, y } = displacedNodePosById.get(node.id)}
				{@const reaction = node.reaction}
				{@const endPos = { x: x + reactionsScale * reaction.x, y: y + reactionsScale * reaction.y }}
				{@const { cx, cy, transform } = calculateLabelTransform({ x, y }, endPos)}
				{@const value = Math.sqrt(reaction.x ** 2 + reaction.y ** 2)}
				<line
					x1={x}
					y1={y}
					x2={endPos.x}
					y2={endPos.y}
					stroke-linecap="round"
					marker-end="url(#arrow)"
				/>
				<text class="label-reaction svg-label" x={cx} y={cy} {transform}
					>{`R=${value.toFixed(3)} ${units.force}`}
				</text>
			{/if}
		{/each}
	</g>
</g>

<style>
	.tension {
		stroke: var(--tension-bar-color);
	}
	.label-tension {
		fill: var(--tension-bar-color);
	}

	.compression {
		stroke: var(--compression-bar-color);
	}
	.label-compression {
		fill: var(--compression-bar-color);
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
