<script>
	import { debounce } from '../services/utils.js'

	let { lines = $bindable(), errors } = $props()

	let content = $derived(lines.join('\n'))
	let lineCount = $derived(lines.length)
	let lineNumbers = $derived(Array.from({ length: lineCount }, (_, i) => i + 1))
	let errorsByLine = $derived(new Map(errors.map((error) => [error.line, error])))
	$inspect(errorsByLine)

	$effect(() => {
		lines = content.split('\n')
	})

	let container = $state(null)
</script>

<div class="container" bind:this={container}>
	<div class="line-numbers">
		{#each lineNumbers as number (number)}
			{@const hasError = errorsByLine.has(number)}
			<span data-line={number} class={hasError ? 'has-error' : ''}>{number}</span>
		{/each}
	</div>
	<textarea bind:value={content} class="text-area" spellcheck="false" wrap="off"></textarea>

	{#each errors as error}
		{@const { top } = document.querySelector(`[data-line="${error.line}"]`).getBoundingClientRect()}
		{@const { right } = container.getBoundingClientRect()}
		<div class="error-msg" style={`top: ${top}px; left: ${right + 10}px`}>
			{error.message}
		</div>
	{/each}
</div>

<style>
	.container {
		display: flex;
		font-family: monospace;
		font-size: 14px;
		line-height: 1.5;
	}

	.line-numbers {
		background-color: var(--editor-linenum-bg-color);
		color: var(--editor-linenum-color);
		padding: 20px 8px;
		text-align: right;
		user-select: none;
		box-sizing: border-box;
		overflow-y: hidden;
		min-width: 40px;

		> .has-error {
			color: var(--editor-error-color);
		}
	}

	.line-numbers > span {
		display: block;
		height: calc(14px * 1.5); /* Match font-size * line-height */
		box-sizing: border-box;
	}

	.text-area {
		flex-grow: 1;
		padding: 20px 10px;
		border: none;
		outline: none;
		resize: none;
		font-family: inherit;
		font-size: inherit;
		line-height: inherit;
		box-sizing: border-box;
		overflow-y: scroll;
		white-space: pre;
		background-color: var(--editor-bg-color);
		color: var(--editor-code-color);
	}

	.error-msg {
		position: absolute;
		font-family: 'DM Sans', sans-serif;
		padding: 0.5em 1em;
		color: var(--editor-error-color);
		background-color: var(--editor-bg-error-color);
		height: calc(14px * 1.5); /* Match font-size * line-height */
		z-index: 1000;
	}
</style>
