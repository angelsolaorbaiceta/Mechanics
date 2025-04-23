<script>
	import { ResizableColumns, CodeEditor, StructureDrawing, HelpModal } from '../lib'
	import { appState, solveStructure, clearStructure } from '../lib/state.svelte.js'

	let showHelp = $state(false)
</script>

<header>
	<h2>2D Truss Structures</h2>
	<div>
		<button onclick={clearStructure} class="secondary">New</button>
		<button onclick={solveStructure} disabled={appState.isLoading} class="primary">
			Calculate
		</button>
	</div>
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
		justify-content: space-between;

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
