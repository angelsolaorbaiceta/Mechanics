<script>
	import { structureSVGSizes } from '../services/drawing.js'
	import SolutionDrawing from './solution-drawing.svelte'
	import Popover from './popover.svelte'
	import BarResults from './bar-results.svelte'
	import DrawingControls from './drawing-controls.svelte'

	let { structure, solution } = $props()

	$effect(() => {
		if (solution !== null) {
			appearance.structure.opacity = 0.25
			appearance.loads.show = false

			const { meta } = solution
			appearance.solution.scale = meta.displacement.suggestedScale
			appearance.solution.reactionsScale = meta.reaction.suggestedScale
		} else {
			appearance.structure.opacity = 1.0
			appearance.loads.show = true
		}
	})

	let appearance = $state({
		units: {
			force: 'N',
			length: 'cm'
		},
		structure: {
			margin: 50,
			scale: 1,
			nodeRadius: 5,
			opacity: 1.0
		},
		loads: {
			scale: 0.025,
			show: true
		},
		solution: {
			scale: 5,
			reactionsScale: 0.0025
		},
		labels: {
			show: true
		}
	})
	let sizes = $derived(
		structureSVGSizes(structure, solution, {
			margin: appearance.structure.margin,
			scale: appearance.structure.scale,
			loadsScale: appearance.loads.scale,
			solutionScale: appearance.solution.scale,
			reactionsScale: appearance.solution.reactionsScale
		})
	)

	let isSolutionPopoverOpen = $state(false)
	let solutionPopoverAnchor = $state(null)
	let solutionPopoverBar = $state(null)

	function showSolutionBarPopover(barEl, bar) {
		solutionPopoverAnchor = barEl
		solutionPopoverBar = bar
		isSolutionPopoverOpen = true
	}
</script>

<div class="container">
	<div class="viewport">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			version="1.1"
			role="graphics-document"
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

			<g id="definition-drawing" style={`opacity: ${appearance.structure.opacity}`}>
				<g class="geometry">
					{#each structure.bars as bar}
						{@const start = structure.nodesById.get(bar.startNodeId)}
						{@const end = structure.nodesById.get(bar.endNodeId)}
						<line x1={start.pos.x} y1={start.pos.y} x2={end.pos.x} y2={end.pos.y} />
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

				{#if appearance.loads.show}
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
				{/if}
			</g>

			{#if solution !== null}
				<SolutionDrawing
					{solution}
					scale={appearance.solution.scale}
					reactionsScale={appearance.solution.reactionsScale}
					units={appearance.units}
					showBarPopover={showSolutionBarPopover}
				/>
			{/if}
		</svg>
	</div>

	<Popover
		bind:isOpen={isSolutionPopoverOpen}
		anchorElement={solutionPopoverAnchor}
		id="bar-result-popover"
	>
		<BarResults bar={solutionPopoverBar} units={appearance.units} />
	</Popover>

	<DrawingControls bind:appearance />
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		height: 100%;
	}
	.viewport {
		background-color: var(--canvas-bg-color);
		width: 100%;
		flex: 1;
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
		stroke: none;
		fill: var(--text-color);
		font: 13px sans-serif;
	}

	#definition-drawing {
		transition: opacity 150ms ease-in-out;
	}
</style>
