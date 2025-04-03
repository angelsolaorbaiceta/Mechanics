<script>
	import { structureSVGSizes } from '../services/sizes.js'

	let { structure } = $props()
	$inspect(structure)

	let appearance = $state({
		structure: {
			margin: 50,
			scale: 1,
			nodeRadius: 5
		},
		loads: {
			scale: 0.025
		},
		labels: {
			show: true
		}
	})
	let sizes = $derived(
		structureSVGSizes(structure, {
			margin: appearance.structure.margin,
			scale: appearance.structure.scale,
			loadsScale: appearance.loads.scale
		})
	)
	$inspect(sizes)
</script>

<div class="viewport">
	<svg
		xmlns="http://www.w3.org/2000/svg"
		version="1.1"
		width={`${sizes.width}px`}
		height={`${sizes.height}px`}
		viewBox={`${sizes.left} ${sizes.top} ${sizes.width} ${sizes.height}`}
		transform={`scale(${appearance.structure.scale} -${appearance.structure.scale})`}
	>
		<defs>
			<marker
				id="arrow"
				viewBox="0 0 10 10"
				refX="8"
				refY="5"
				markerWidth="6"
				markerHeight="6"
				stroke-linecap="round"
				orient="auto-start-reverse"
				markerUnits="strokeWidth"
				overflow="visible"
			>
				<path
					d="M 0 0 L 10 5 L 0 10"
					stroke-width="context-stroke-width"
					stroke="context-stroke"
					fill="context-fill"
				/>
			</marker>
		</defs>

		<g>
			<g class="geometry">
				{#each structure.bars as bar}
					<line
						x1={structure.nodesById.get(bar.startNodeId).pos.x}
						y1={structure.nodesById.get(bar.startNodeId).pos.y}
						x2={structure.nodesById.get(bar.endNodeId).pos.x}
						y2={structure.nodesById.get(bar.endNodeId).pos.y}
					/>
				{/each}
				{#each structure.nodes as node}
					<circle cx={node.pos.x} cy={node.pos.y} r={appearance.structure.nodeRadius} />
					{#if appearance.labels.show}
						<text
							transform="scale(1 -1)"
							x={node.pos.x}
							y={-node.pos.y + 4 * appearance.structure.nodeRadius}
							class="small"
						>
							N{node.id}
						</text>
					{/if}
					{#if node.isXYConstraint()}{/if}
				{/each}
			</g>

			<g class="loads">
				{#each structure.nodes as node}
					{#each node.loads as load}
						<line
							x1={node.pos.x}
							y1={node.pos.y}
							x2={node.pos.x + appearance.loads.scale * load.fx}
							y2={node.pos.y + appearance.loads.scale * load.fy}
							stroke-linecap="round"
							marker-end="url(#arrow)"
						/>
					{/each}
				{/each}
			</g>
		</g>
	</svg>
</div>

<style>
	.viewport {
		background-color: var(--canvas-bg-color);
		height: 100%;
		width: 100%;
		overflow: auto;
	}
	.geometry {
		stroke: var(--geometry-color);
		stroke-width: var(--geometry-stroke-width);
	}
	.loads {
		stroke: var(--loads-color);
		fill: none;
		stroke-width: var(--loads-stroke-width);
	}
	.small {
		font: italic 13px sans-serif;
	}
</style>
