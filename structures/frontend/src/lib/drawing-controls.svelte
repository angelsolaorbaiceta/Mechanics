<script>
	import ScaleField from './scale-field.svelte'
	import { appState } from './state.svelte.js'

	let appearance = $derived(appState.appearance)

	const drawingScaleValues = [
		0.01, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25,
		3.5, 3.75, 4.0
	]

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
</script>

<div aria-label="drawing controls">
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
		<h3>Structure</h3>
		<ScaleField
			bind:value={appearance.structure.scale}
			id="structure-scale"
			min="0.000001"
			max="100000"
			step="0.1"
			values={drawingScaleValues}
		/>

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
		<ScaleField
			bind:value={appearance.loads.scale}
			id="loads-scale"
			min="0.00001"
			max="1000"
			step="0.1"
		/>
		<div class="fields-row">
			<label for="show-loads"> Show: </label>
			<input type="checkbox" id="show-loads" bind:checked={appearance.loads.show} />
		</div>
	</section>

	<div class="vertical-separator"></div>

	<section>
		<h3>Solution</h3>
		<ScaleField
			bind:value={appearance.solution.scale}
			id="solution-scale"
			min="1"
			max="10000"
			step="5"
		/>
		<ScaleField
			bind:value={appearance.solution.reactionsScale}
			id="reactions-scale"
			min="0.000001"
			max="1000"
			step="0.001"
		/>
	</section>
</div>

<style>
	[aria-label='drawing controls'] {
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

	.fields-row {
		display: flex;
		gap: 0.5em;
	}
</style>
