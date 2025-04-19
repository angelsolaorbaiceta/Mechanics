<script>
	import { debounce } from '../services/utils.js'
	import { highlightCode } from '../services/code.js'

	let { lines = $bindable(), errors } = $props()

	let content = $derived(lines.join('\n'))
	let lineCount = $derived(lines.length)
	let lineNumbers = $derived(Array.from({ length: lineCount }, (_, i) => i + 1))
	let errorsByLine = $derived(new Map(errors.map((error) => [error.line, error])))
	$inspect(errorsByLine)

	let highlightedLines = $derived(highlightCode(lines))

	$effect(() => {
		lines = content.split('\n')
	})

	let container = $state(null)
	let editor = $state(null)
	let highlightLayer = $state(null)
</script>

<div class="container" bind:this={container}>
	<div class="line-numbers">
		{#each lineNumbers as number (number)}
			{@const hasError = errorsByLine.has(number)}
			<span data-line={number} class={hasError ? 'has-error' : ''}>{number}</span>
		{/each}
	</div>

	<div class="editor-container">
		<textarea bind:value={content} bind:this={editor} class="editor" spellcheck="false" wrap="off"
		></textarea>

		<div bind:this={highlightLayer} class="highlight-layer" aria-hidden="true">
			{#each highlightedLines as line}
				<div class="code-line">{@html line}</div>
			{/each}
		</div>
	</div>

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

	/* .editor {
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
	} */

	.editor-container {
		position: relative;
		flex: 1;
		overflow: hidden;
	}

	.editor,
	.highlight-layer {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 20px 0 0 10px;
		font-family: monospace;
		font-size: 14px;
		line-height: 1.5;
		overflow: auto;
	}

	.editor {
		border: none;
		outline: none;
		resize: none;
		color: transparent;
		background: transparent;
		caret-color: var(--editor-code-color);
		resize: none;
		z-index: 2;
	}

	.highlight-layer {
		pointer-events: none;
		z-index: 1;
		background-color: var(--editor-bg-color);
		color: var(--editor-code-color);
		white-space: pre;
	}

	.code-line {
		min-height: 1.5em; /* Match line-height */
		white-space: pre;
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
