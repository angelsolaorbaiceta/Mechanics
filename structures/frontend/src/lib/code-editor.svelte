<script>
	let { lines } = $props()

	let content = $derived(lines.join('\n'))
	let lineCount = $derived(lines.length)
	let lineNumbers = $derived(Array.from({ length: lineCount }, (_, i) => i + 1))
</script>

<div class="editor-container">
	<div class="line-numbers">
		{#each lineNumbers as number (number)}
			<span>{number}</span>
		{/each}
	</div>
	<textarea bind:value={content} class="text-area" spellcheck="false" wrap="off"></textarea>
</div>

<style>
	.editor-container {
		display: flex;
		font-family: monospace;
		font-size: 14px;
		line-height: 1.5;
		height: 100%;
		overflow: hidden;
	}

	.line-numbers {
		background-color: var(--editor-linenum-bg-color);
		color: var(--editor-linenum-color);
		padding: 10px 8px;
		text-align: right;
		user-select: none;
		box-sizing: border-box;
		overflow-y: hidden;
		min-width: 40px;
	}

	.line-numbers span {
		display: block;
		height: calc(14px * 1.5); /* Match font-size * line-height */
		box-sizing: border-box;
	}

	.text-area {
		flex-grow: 1;
		padding: 10px;
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
</style>
