<script>
	let { value = $bindable(), id, min, max, step } = $props()

	function oom(num) {
		if (num === 0) return 0

		const absNum = Math.abs(num)
		const exponent = Math.floor(Math.log10(absNum))

		return Math.pow(10, exponent)
	}

	function zoomIn() {
		value += oom(value)
	}

	function zoomOut() {
		value -= oom(value)
	}
</script>

<label for={id}>
	Scale:
	<div>
		<button aria-label="zoom out" onclick={zoomOut}>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				width="24px"
				height="24px"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="white"
				class="size-6"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607ZM13.5 10.5h-6"
				/>
			</svg>
		</button>

		<input type="number" {id} bind:value {min} {max} {step} />

		<button aria-label="zoom in" onclick={zoomIn}>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				width="24px"
				height="24px"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="white"
				class="size-6"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607ZM10.5 7.5v6m3-3h-6"
				/>
			</svg>
		</button>
	</div>
</label>

<style>
	label > div {
		display: flex;
		align-items: center;
	}

	button {
		background: none;
		border: none;
		cursor: pointer;
		display: inline-block;
	}
	input {
		height: 24px;
	}
</style>
