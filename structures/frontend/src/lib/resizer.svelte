<script>
	/**
	 * The position is the percentage from the left where the resizer is at.
	 * It should be between 25 and 75 at all times.
	 */
	let positon = $state(50)
</script>

<div class="resizer"></div>

<style>
	.resizer {
		width: 6px;
		height: 100%;
		background-color: #ccc;
		cursor: col-resize;
		position: relative;
	}
	.resizer:hover,
	.resizer.active {
		background-color: #999;
	}
	.resizer::after {
		content: '';
		position: absolute;
		top: 0;
		left: 50%;
		height: 100%;
		border-left: 2px dashed #666;
		transform: translateX(-50%);
		opacity: 0;
		transition: opacity 0.2s;
	}
	.resizer:hover::after,
	.resizer.active::after {
		opacity: 1;
	}
</style>
