<script>
	import { highlightCode } from '../services/code.js'

	let { lines = $bindable(), errors } = $props()

	let content = $derived(lines.join('\n'))
	let lineCount = $derived(lines.length)
	let lineNumbers = $derived(Array.from({ length: lineCount }, (_, i) => i + 1))
	let errorsByLine = $derived(new Map(errors.map((error) => [error.line, error])))

	let highlightedLines = $derived(highlightCode(lines))

	$effect(() => {
		lines = content.split('\n')
	})
</script>

<div class="container">
	<div class="line-numbers">
		{#each lineNumbers as number}
			{@const hasError = errorsByLine.has(number)}
			<span data-line={number} class={hasError ? 'linenum-has-error' : ''}>{number}</span>
		{/each}
	</div>

	<div class="editor-container">
		<textarea bind:value={content} class="editor" spellcheck="false" wrap="off"></textarea>

		<div class="highlight-layer" aria-hidden="true">
			{#each highlightedLines as line, i}
				{@const error = errorsByLine.get(i + 1)}
				<div class={`code-line ${error ? 'has-error' : ''}`}>
					{@html line}
					{#if error}
						<span class="error-msg">{error.message}</span>
					{/if}
				</div>
			{/each}
		</div>
	</div>
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
	}
	.linenum-has-error {
		color: var(--editor-error-color);
	}

	.line-numbers > span {
		display: block;
		height: calc(14px * 1.5); /* Match font-size * line-height */
		box-sizing: border-box;
	}

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

	.has-error {
		color: var(--editor-error-color);
		background-color: var(--editor-bg-error-color);
	}
	.error-msg {
		font-family: 'DM Sans', sans-serif;
		font-style: italic;
		margin: 0 1em;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}
</style>
