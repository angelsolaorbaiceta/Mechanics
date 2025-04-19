import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		// Using adapter-static to build a static site
		// that will be served from our Python server
		adapter: adapter({
			// Output directory matches the directory referenced in Dockerfile
			// where static files will be copied from
			fallback: 'index.html'
		})
	}
};

export default config;
