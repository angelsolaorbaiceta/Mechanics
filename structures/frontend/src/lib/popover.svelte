<script>
	import { onDestroy } from 'svelte'

	let { isOpen = $bindable(), anchorElement, children, id } = $props()
	let closeTimer

	function handleClickOutside(event) {
		if (isOpen && !event.target.closest('.popover-container')) {
			isOpen = false
		}
	}

	function startCloseTimer() {
		clearTimeout(closeTimer)
		closeTimer = setTimeout(() => {
			isOpen = false
		}, 1000)
	}

	function cancelCloseTimer() {
		clearTimeout(closeTimer)
	}

	function handleMouseLeave() {
		startCloseTimer()
	}

	function handleMouseEnter() {
		cancelCloseTimer()
	}

	$effect(() => {
		if (isOpen && anchorElement) {
			anchorElement.addEventListener('mouseleave', handleMouseLeave)
			anchorElement.addEventListener('mouseenter', handleMouseEnter)
		}

		return () => {
			if (anchorElement) {
				anchorElement.removeEventListener('mouseleave', handleMouseLeave)
				anchorElement.removeEventListener('mouseenter', handleMouseEnter)
			}
		}
	})

	$effect(() => {
		if (!isOpen) {
			cancelCloseTimer()
		}
	})

	// Clean up any timers when component is destroyed
	onDestroy(() => {
		cancelCloseTimer()
		if (anchorElement) {
			anchorElement.removeEventListener('mouseleave', handleMouseLeave)
			anchorElement.removeEventListener('mouseenter', handleMouseEnter)
		}
	})

	// Position the popover based on anchor element
	function getPositionStyles() {
		if (!anchorElement) return ''

		const { top, height, left, width } = anchorElement.getBoundingClientRect()
		const midX = top + height / 2
		const midY = left + width / 2
		return `top: ${midX}px; left: ${midY}px; transform: translate(-50%, 0%);`
	}
</script>

<svelte:window on:click={handleClickOutside} />

{#if isOpen}
	<div
		class="popover-container"
		style={getPositionStyles()}
		role="dialog"
		aria-modal="true"
		{id}
		bind:this={popoverElement}
		on:mouseenter={handleMouseEnter}
		on:mouseleave={handleMouseLeave}
	>
		{@render children()}
	</div>
{/if}

<style>
	.popover-container {
		position: fixed;
		z-index: 1000;
		min-width: 200px;
		max-width: 300px;
		background-color: var(--editor-bg-color);
		border: 1px solid var(--editor-linenum-color);
		border-radius: 4px;
		overflow: hidden;
		padding: 1em;
	}
</style>
