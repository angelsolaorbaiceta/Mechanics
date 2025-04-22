<script>
	import { structureSVGSizes } from '../services/drawing.js'
	import SolutionDrawing from './solution-drawing.svelte'
	import Popover from './popover.svelte'
	import BarResults from './bar-results.svelte'
	import DrawingControls from './drawing-controls.svelte'
	import NodeDrawing from './node-drawing.svelte'
	import BarDrawing from './bar-drawing.svelte'
	import { appState } from '../lib/state.svelte.js'

	let structure = $derived(appState.structure)
	let solution = $derived(appState.solution)

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
						<BarDrawing {bar} nodesById={structure.nodesById} showLabels={appearance.labels.show} />
					{/each}

					{#each structure.nodes as node}
						<NodeDrawing
							{node}
							radius={appearance.structure.nodeRadius}
							showLabels={appearance.labels.show}
						/>
					{/each}
				</g>

				{#if appearance.loads.show}
					<g class="loads">
						{#each structure.nodes as node}
							{#each node.loads as load}
								{@const tipX = node.pos.x + appearance.loads.scale * load.fx}
								{@const tipY = node.pos.y + appearance.loads.scale * load.fy}

								<line
									x1={node.pos.x}
									y1={node.pos.y}
									x2={tipX}
									y2={tipY}
									stroke-linecap="round"
									marker-end="url(#arrow)"
								/>
								{#if appearance.labels.show}
									<text
										x={tipX}
										y={tipY}
										class="load-label"
										text-anchor="middle"
										dominant-baseline="central"
										transform-origin="center"
										transform="scale(1 -1) translate(0 15)"
									>
										{Math.sqrt(load.fx ** 2 + load.fy ** 2).toFixed(2)}
										{appearance.units.force}
									</text>
								{/if}
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
	.load-label {
		stroke: none;
		transform-box: fill-box;
		fill: var(--loads-color);
		font: 13px sans-serif;
	}

	#definition-drawing {
		transition: opacity 150ms ease-in-out;
	}
</style>
