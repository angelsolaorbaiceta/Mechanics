export function debounce(fn, milliseconds) {
	let timeout

	return function (...args) {
		const context = this

		clearTimeout(timeout)

		timeout = setTimeout(function () {
			fn.apply(context, args)
		}, milliseconds)
	}
}
