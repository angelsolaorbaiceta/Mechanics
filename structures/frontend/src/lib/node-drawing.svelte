<script>
	let { node, radius, showLabels } = $props()
</script>

<circle cx={node.pos.x} cy={node.pos.y} r={radius} />

{#if node.isXConstraint()}
	<line
		x1={node.pos.x - 4 * radius}
		y1={node.pos.y}
		x2={node.pos.x + 4 * radius}
		y2={node.pos.y}
		stroke-linecap="round"
		class="constraint constx"
	/>
{/if}
{#if node.isYConstraint()}
	<line
		x1={node.pos.x}
		y1={node.pos.y - 4 * radius}
		x2={node.pos.x}
		y2={node.pos.y + 4 * radius}
		stroke-linecap="round"
		class="constraint consty"
	/>
{/if}

{#if showLabels}
	<text
		transform="scale(1 -1)"
		x={node.pos.x + 2 * radius}
		y={-node.pos.y + 4 * radius}
		class="label"
	>
		N{node.id}
	</text>
{/if}

<style>
	.label {
		stroke: none;
		fill: var(--drawing-text-color);
		font: 13px sans-serif;
	}
	.constraint {
		stroke-width: var(--constraint-stroke-width);
	}
	.constx {
		stroke: var(--code-xdir-color);
	}
	.consty {
		stroke: var(--code-ydir-color);
	}
</style>
