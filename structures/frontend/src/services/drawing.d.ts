export function structureSVGSizes(
	structure: any,
	solution: any,
	{
		margin,
		scale,
		loadsScale,
		solutionScale,
		reactionsScale
	}: {
		margin?: number
		scale?: number
		loadsScale?: number
		solutionScale?: number
		reactionsScale?: number
	}
):
	| {
			width: number
			height: number
			top: number
			left: number
			margin: number
			x?: undefined
			y?: undefined
	  }
	| {
			width: number
			height: number
			left: number
			top: number
			margin: number
			x: any[]
			y: any[]
	  }
export function displacedNodePos(
	node: any,
	scale: any
): {
	x: any
	y: any
}
export function calculateLabelTransform(
	startPos: any,
	endPos: any,
	separation?: number
): {
	transform: string
	cx: number
	cy: number
}
