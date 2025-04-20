<script>
	import { highlightLine } from '../services/code.js'
	import { fade } from 'svelte/transition'

	let { onClose } = $props()

	const exampleNodesLines = [
		'nodes',
		'# Fixed support at origin',
		'1: (0.0, 0.0) (xy)',
		'# Roller support: fixed in y, free in x',
		'2: (200.0, 0.0) (y)',
		'# No constraints, free node',
		'3: (400.0, 0.0) ()',
		'# Free node at top',
		'4: (200.0, 200.0) ()'
	]
	const exampleLoadsLines = [
		'loads',
		'# Downward force of 5000 units at node 3',
		'3 -> (0.0, -5000.0)',
		'# Combined horizontal and vertical force at node 4',
		'4 -> (2000.0, -3000.0)'
	]
	const exampleBarsLines = [
		'bars',
		'# Bar from node 1 to 2',
		'1: (1 -> 2) 25.0 20000000.0',
		'# Bar from node 2 to 3',
		'2: (2 -> 3) 25.0 20000000.0  ',
		'# Diagonal bar with larger cross-section',
		'3: (2 -> 4) 30.0 20000000.0  ',
		'# Bar from node 3 to 4',
		'4: (3 -> 4) 25.0 20000000.0  '
	]
	const completeExampleLines = [
		'nodes',
		'# Define the three vertices of our triangle',
		'# Fixed base point',
		'1: (0.0, 0.0) (xy)       ',
		'# Roller support',
		'2: (400.0, 0.0) (y)      ',
		'# Free top node',
		'3: (200.0, 200.0) ()     ',
		'',
		'loads',
		'# Apply vertical load to the top node',
		'# 10kN downward force',
		'3 -> (0.0, -10000.0)     ',
		'',
		'bars',
		'# Define the three sides of the triangle',
		'# Bottom bar (steel)  ',
		'1: (1 -> 2) 30.0 210000.0  ',
		'# Left diagonal bar',
		'2: (1 -> 3) 25.0 210000.0  ',
		'# Right diagonal bar',
		'3: (2 -> 3) 25.0 210000.0  '
	]
</script>

<div
	class="overlay"
	onclick={onClose}
	onkeydown={() => {}}
	role="dialog"
	tabindex="-1"
	in:fade={{ duration: 100 }}
	out:fade={{ duration: 75 }}
></div>

<article in:fade={{ duration: 100 }} out:fade={{ duration: 75 }}>
	<nav>
		<button aria-label="close" onclick={onClose} tabindex="0">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				width="24px"
				height="24px"
				stroke-width="1.5"
				stroke="white"
				class="size-6"
			>
				<path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
			</svg></button
		>
	</nav>

	<h1>2D Truss Structure Definition Language</h1>

	<h2>Language Structure</h2>

	<p>A structure definition consists of three main sections:</p>
	<ul>
		<li>
			<code class="codeh header">nodes</code>: Defines points in 2D space and their constraints
		</li>
		<li><code class="codeh header">loads</code>: Specifies forces applied to nodes</li>
		<li>
			<code class="codeh header">bars</code>: Defines connections between nodes with material
			properties
		</li>
	</ul>
	<p>
		Comments can be added using the <code class="codeh comment">#</code> symbol at the beginning of a
		line. Everything after this symbol on a line is ignored.
	</p>
	<p>
		Use consistent units throughout. If you decide to use meters to define the coordinates of the
		nodes, you should also use meters to define the cross sectional area of a bar.
	</p>

	<h2>Nodes Section</h2>

	<div class="example">
		<code class="code">
			<div class="codeh header">nodes</div>
			<div>
				<span class="codeh id">&lt;id&gt;</span>: (<span class="codeh xdir">&lt;x_pos&gt;</span>,
				<span class="codeh ydir">&lt;y_pos&gt;</span>) (&lt;external_constraints&gt;)
			</div>
		</code>
	</div>

	<ul>
		<li><code class="codeh id">id</code>: A unique identifier for the node (integer)</li>
		<li>
			<code class="codeh xdir">x_pos</code>, <code class="codeh ydir">y_pos</code>: Position
			coordinates (floating-point numbers)
		</li>
		<li>
			<code>external_constraints</code>: Optional directional constraints:
			<ul>
				<li><code>(xy)</code>: Fixed in both x and y directions (completely immobile)</li>
				<li><code>(x)</code>: Fixed only in x direction (can move vertically)</li>
				<li><code>(y)</code>: Fixed only in y direction (can move horizontally)</li>
				<li><code>()</code>: No constraints (free to move in any direction)</li>
			</ul>
		</li>
	</ul>

	<h3>Example</h3>

	<div class="example">
		<code>
			{#each exampleNodesLines as line}
				<div>{@html highlightLine(line)}</div>
			{/each}
		</code>
	</div>

	<h2>Loads Section</h2>

	<div class="example">
		<code class="code">
			<div class="codeh header">loads</div>
			<div>
				<span class="codeh id">&lt;node_id&gt;</span> -> (<span class="codeh xdir">&lt;fx&gt;</span
				>, <span class="codeh ydir">&lt;fy&gt;</span>)
			</div>
		</code>
	</div>

	<ul>
		<li><code class="codeh id">node_id</code>: ID of the node where the load is applied</li>
		<li><code class="codeh xdir">fx</code>: Force component in x-direction (positive = right)</li>
		<li><code class="codeh ydir">fy</code>: Force component in y-direction (positive = up)</li>
	</ul>

	<h3>Example</h3>

	<div class="example">
		<code>
			{#each exampleLoadsLines as line}
				<div>{@html highlightLine(line)}</div>
			{/each}
		</code>
	</div>

	<h2>Bars Section</h2>

	<div class="example">
		<code>
			<div class="codeh header">bars</div>
			<span class="codeh id">&lt;id&gt;</span>: (<span class="codeh id">&lt;start_node_id&gt;</span>
			-> <span class="codeh id">&lt;end_node_id&gt;</span>) &lt;section_area&gt;
			&lt;young_modulus&gt;
		</code>
	</div>

	<ul>
		<li><code class="codeh id">id</code>: Unique identifier for the bar (integer)</li>
		<li>
			<code class="codeh id">start_node_id</code>, <code class="codeh id">end_node_id</code>: IDs of
			nodes connected by this bar
		</li>
		<li><code>section_area</code>: Cross-sectional area of the bar (determines strength)</li>
		<li><code>young_modulus</code>: Young's modulus (elasticity) of the bar material</li>
	</ul>

	<h3>Example</h3>

	<div class="example">
		<code>
			{#each exampleBarsLines as line}
				<div>{@html highlightLine(line)}</div>
			{/each}
		</code>
	</div>

	<h2>Complete Example</h2>
	<p>Let's define a simple triangular truss with three nodes and three bars:</p>

	<div class="example">
		<code>
			{#each completeExampleLines as line}
				<div>{@html highlightLine(line)}</div>
			{/each}
		</code>
	</div>

	<p>
		This defines a triangular truss with a fixed support at the left bottom, a roller support at the
		right bottom, and a vertical load applied at the top.
	</p>

	<h2>Best Practices</h2>
	<ol>
		<li>Use consistent units throughout your definition</li>
		<li>Number nodes and bars sequentially for readability</li>
		<li>Group related components with comments</li>
		<li>For large structures, organize nodes by layers or functional groups</li>
		<li>Include material constants in separate comments for clarity</li>
	</ol>
</article>

<style>
	.overlay {
		position: fixed;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background-color: black;
		opacity: 0.85;
		z-index: 99999;
		cursor: pointer;
	}

	article {
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -75%);
		width: 80vh;
		min-width: 300px;
		height: 50vh;
		min-height: 200px;
		padding: 2em;
		z-index: 999999;
		background: var(--canvas-bg-color);
		overflow-y: auto;
		border-radius: 12px;

		> nav {
			text-align: right;
			position: sticky;
			top: 0;

			> button {
				cursor: pointer;
				background: none;
				border: none;
			}
		}
	}
	.example {
		background-color: var(--editor-bg-color);
		padding: 1em 2em;
		margin: 20px 0;
		> code {
			line-height: 1.5;
		}
	}
	.code {
		line-height: 1.5;
	}
</style>
