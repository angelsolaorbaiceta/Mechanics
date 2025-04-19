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

export async function hash(obj) {
	const str = JSON.stringify(obj, Object.keys(obj).sort())
	console.log(str)
	const encoder = new TextEncoder()
	const data = encoder.encode(str)

	const hashBuffer = await crypto.subtle.digest('SHA-256', data)

	return Array.from(new Uint8Array(hashBuffer))
		.map((b) => b.toString(16).padStart(2, '0'))
		.join('')
}
