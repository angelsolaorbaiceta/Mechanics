<script>
	import { displacedNodePos, calculateLabelTransform } from '../services/drawing.js'

	let { solution, scale, reactionsScale, units, showBarPopover } = $props()
	let displacedNodePosById = $derived(
		new Map(solution.nodes.map((node) => [node.id, displacedNodePos(node, scale)]))
	)
	let stressUnits = $derived(`${units.force}/${units.length}2`)

	function strokeWidthForBar({ stress }) {
		// Choose numbers from 2 to 8, in increments of 0.25 based on the stress
		const { min, max } = solution.meta.stress
		const percentage = (Math.abs(stress) - min) / (max - min)
		const rawInterpolated = 2 + percentage * 6
		const rounded = Math.round(rawInterpolated * 4) / 4

		return rounded
	}
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
			stroke-width={strokeWidthForBar(bar)}
			onmouseover={(event) => showBarPopover(event.target, bar)}
		/>

		{@const { cx, cy, transform } = calculateLabelTransform(startPos, endPos)}
		<text
			class={`label label-${bar.axial}`}
			x={cx}
			y={cy}
			text-anchor="middle"
			dominant-baseline="central"
			transform-origin="center"
			{transform}
		>
			{`σ=${bar.stress} ${stressUnits}`}
		</text>
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
				<text
					class="label label-reaction"
					x={cx}
					y={cy}
					text-anchor="middle"
					dominant-baseline="central"
					transform-origin="center"
					{transform}
					>{`R=${value.toFixed(3)} ${units.force}`}
				</text>
			{/if}
		{/each}
	</g>
</g>

<style>
	.label {
		stroke: none;
		transform-box: fill-box;
		font-size: 12px;
		user-select: none;
	}

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
