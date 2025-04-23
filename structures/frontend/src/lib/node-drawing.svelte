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
		x={node.pos.x}
		y={node.pos.y}
		transform={`scale(1 -1) translate(20 15)`}
		class="svg-label label"
	>
		N{node.id}
	</text>
{/if}

<style>
	.label {
		fill: var(--drawing-text-color);
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
