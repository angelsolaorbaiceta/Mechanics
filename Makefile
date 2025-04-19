struct.serve:
	DEV_MODE=true poetry run python -m structures.server.main

fe.serve:
	npm run dev

docker.build:
	docker build -t hardcore-2dstructures:latest .
