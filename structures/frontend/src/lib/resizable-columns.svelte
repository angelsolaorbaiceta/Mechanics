<script>
	import { onMount } from 'svelte'

	let { left, right } = $props()

	const minWidth = 300

	let leftEl = $state(null)
	let rightEl = $state(null)
	let containerEl = $state(null)

	let position = $state(minWidth)
	let isResizing = $state(false)
	let startMouseX = $state(0)
	let startPosition = $state(0)

	function setSafePosition(pos) {
		const maxPosition = containerEl.clientWidth - minWidth
		position = Math.min(maxPosition, Math.max(minWidth, pos))
	}

	onMount(() => {
		setSafePosition(Math.round(containerEl.clientWidth * 0.25))
	})

	$effect(() => {
		if (leftEl) {
			leftEl.style.width = `${position}px`
		}
	})

	function startResize(event) {
		isResizing = true
		startMouseX = event.clientX
		startPosition = position

		document.body.classList.add('no-select')
	}

	function resize(event) {
		if (!isResizing) return

		const dx = event.clientX - startMouseX
		setSafePosition(startPosition + dx)
	}

	function endResize() {
		isResizing = false
		document.body.classList.remove('no-select')
	}
</script>

<svelte:document onmousemove={resize} onmouseup={endResize} />

<div class="columns" bind:this={containerEl}>
	<section bind:this={leftEl} class={isResizing ? 'isResizing' : ''}>
		{@render left?.()}
	</section>
	<div
		class={`resizer ${isResizing ? 'active' : ''}`}
		onmousedown={startResize}
		onmouseup={endResize}
	></div>
	<section bind:this={rightEl} class={isResizing ? 'isResizing' : ''}>
		{@render right?.()}
	</section>
</div>

<style>
	.columns {
		display: flex;
		overflow: hidden;
	}
	section {
		overflow: auto;
		box-sizing: border-box;
		min-width: 300px;
	}
	section:first-child {
		/* Don't grow, don't shrink, use width as set */
		flex: 0 0 auto;
	}
	section:last-child {
		/* Grow to fill remaining space */
		flex: 1 1 auto;
	}
	.resizer {
		width: 4px;
		flex: 0 0 auto;
		height: 100%;
		background-color: var(--separator-line-color);
		cursor: col-resize;
		position: relative;
	}
	.resizer:hover,
	.resizer.active {
		background-color: var(--text-color);
	}
	.resizer::after {
		content: '';
		position: absolute;
		top: 0;
		left: 50%;
		height: 100%;
		border-left: 2px dashed var(--editor-bg-color);
		transform: translateX(-50%);
		opacity: 0;
		transition: opacity 0.2s;
	}
	.resizer:hover::after,
	.resizer.active::after {
		opacity: 1;
	}

	.isResizing {
		user-select: none;
	}
</style>
