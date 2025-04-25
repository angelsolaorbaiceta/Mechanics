struct.serve:
	DEV_MODE=true poetry run python -m structures.server.main

fe.serve:
	cd structures/frontend && npm run dev

fe.build:
	cd structures/frontend && npm run build

docker.build:
	docker build -t asolaor/hardcore-2dstructures:0.2 .
