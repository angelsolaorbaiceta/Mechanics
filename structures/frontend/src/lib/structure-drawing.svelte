<script>
	import { structureSVGSizes } from '../services/drawing.js'
	import SolutionDrawing from './solution-drawing.svelte'
	import Popover from './popover.svelte'
	import BarResults from './bar-results.svelte'

	let { structure, solution } = $props()

	$effect(() => {
		if (solution !== null) {
			appearance.structure.opacity = 0.25
			appearance.loads.show = false

			const { meta } = solution
			appearance.solution.scale = meta.displacement.suggestedScale
			appearance.solution.reactionsScale = meta.reaction.suggestedScale
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

	const lenghtUnits = [
		{ value: 'cm', label: 'cm' },
		{ value: 'm', label: 'm' },
		{ value: 'in', label: 'in' },
		{ value: 'ft', label: 'ft' }
	]
	const forceUnits = [
		{ value: 'N', label: 'N' },
		{ value: 'kN', label: 'kN' },
		{ value: 'lbf', label: 'lbf' },
		{ value: 'kips', label: 'kips' }
	]

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

	<footer>
		<section>
			<h3>Structure</h3>
			<label for="structure-scale">
				Scale:
				<div>
					<button>-</button>
					<input
						type="number"
						id="structure-scale"
						bind:value={appearance.structure.scale}
						min="0.000001"
						max="100000"
						step="0.1"
					/>
					<button>+</button>
				</div>
			</label>
			<label for="structure-opacity">
				Opacity ({appearance.structure.opacity * 100}%):
				<input
					type="range"
					id="structure-opacity"
					min="0.0"
					max="1.0"
					step="0.1"
					bind:value={appearance.structure.opacity}
				/>
			</label>
		</section>

		<div class="vertical-separator"></div>

		<section>
			<h3>Loads</h3>
			<label for="loads-scale">
				Scale:
				<input
					type="number"
					id="loads-scale"
					bind:value={appearance.loads.scale}
					min="0.00001"
					max="1000"
					step="0.1"
				/>
			</label>
			<label for="show-loads">
				Show:
				<input type="checkbox" id="show-loads" bind:checked={appearance.loads.show} />
			</label>
		</section>

		<div class="vertical-separator"></div>

		<section>
			<h3>Units</h3>
			<label for="length-units">
				Length:
				<select id="length-units" bind:value={appearance.units.length}>
					{#each lenghtUnits as units}
						<option value={units.value}>{units.label}</option>
					{/each}
				</select>
			</label>
			<label for="force-units">
				Force:
				<select id="force-units" bind:value={appearance.units.force}>
					{#each forceUnits as units}
						<option value={units.value}>{units.label}</option>
					{/each}
				</select>
			</label>
		</section>

		<div class="vertical-separator"></div>

		<section>
			<h3>Solution</h3>
			<label for="solution-scale">
				Disp. scale:
				<input
					type="number"
					id="solution-scale"
					bind:value={appearance.solution.scale}
					min="1"
					max="10000"
					step="5"
				/>
			</label>
			<label for="reactions-scale">
				Reactions scale:
				<input
					type="number"
					id="reactions-scale"
					bind:value={appearance.solution.reactionsScale}
					min="0.000001"
					max="1000"
					step="0.001"
				/>
			</label>
		</section>
	</footer>
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

	footer {
		background-color: var(--editor-bg-color);
		border-top: 1px solid var(--separator-line-color);
		padding: 1.5em 2em;
		display: flex;
		justify-content: space-around;

		> section {
			display: flex;
			flex-direction: column;
			gap: 1em;
			> h3 {
				margin: 0;
			}
		}
	}
	.vertical-separator {
		width: 0;
		border-right: 1px dashed white;
	}
	#definition-drawing {
		transition: opacity 150ms ease-in-out;
	}
</style>
