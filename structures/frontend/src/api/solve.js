// Use relative URL in production, localhost in development
const API_HOST = import.meta.env.PROD ? '' : 'http://localhost:8080'

export async function solveStructure(lines) {
	const response = await fetch(`${API_HOST}/solve`, {
		method: 'POST',
		headers: {
			'Content-Type': 'text/plain',
			Accept: 'application/json'
		},
		body: lines.join('\n')
	})
	const jsonData = await response.json()

	if (!response.ok) {
		const error = new Error(jsonData.message)
		error.cause = {
			status: response.status,
			statusText: response.statusText,
			url: response.url
		}

		throw error
	}

	return jsonData
}
