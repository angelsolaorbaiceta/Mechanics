<script>
	let { bar, units } = $props()
</script>

<header>
	Bar {bar.id} (N{bar.nodes.start} ➞︎ N{bar.nodes.end})
</header>

<section>
	<div class="row">
		<label for="bar-stress">Stress: </label>
		<div class="bar-stress">
			σ = {bar.stress.toFixed(3)} <strong>{units.force}/{units.length}<sup>2</sup></strong>
		</div>
	</div>

	<div class="row">
		<label for="bar-strain">Strain: </label>
		<div class="bar-strain">
			ϵ = {bar.strain}
		</div>
	</div>

	<div class="row">
		<label for="bar-elongation">Elongation: </label>
		<div class="bar-elongation">
			Δl = {bar.elongation} <strong>{units.length}</strong>
		</div>
	</div>
</section>

<style>
	header {
		margin-top: 0.5em;
		margin-bottom: 0.5em;
		padding-bottom: 0.5em;
		border-bottom: 1px solid var(--editor-linenum-color);
		font-size: large;
		font-weight: bold;
	}
	section {
		display: flex;
		flex-direction: column;
		gap: 0.5em;
	}
</style>
