<script>
	let { children, widthPercentage } = $props()
</script>

<section style={`width: ${widthPercentage}%`}>
	{@render children?.()}
</section>

<style>
	section {
		overflow: auto;
		box-sizing: border-box;
		min-width: 25%;
	}
</style>
