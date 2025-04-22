<script>
	import { ResizableColumns, CodeEditor, StructureDrawing, HelpModal } from '../lib'
	import { appState, solveStructure } from '../lib/state.svelte.js'

	let showHelp = $state(false)
</script>

<header>
	<h2>2D Truss Structures</h2>
	<button onclick={solveStructure} disabled={appState.isLoading}>Calculate</button>
</header>
<main>
	<ResizableColumns>
		{#snippet left()}
			<CodeEditor onShowHelp={() => (showHelp = true)} />
		{/snippet}
		{#snippet right()}
			<StructureDrawing />
		{/snippet}
	</ResizableColumns>
</main>

{#if showHelp}
	<HelpModal onClose={() => (showHelp = false)} />
{/if}

<style>
	header {
		background-color: var(--main-color);
		padding: 1em;
		display: flex;

		> h2 {
			margin: 0;
		}
	}

	main {
		display: flex;
		flex-grow: 1;
		overflow: hidden;
	}
</style>
