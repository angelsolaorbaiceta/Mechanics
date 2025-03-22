struct.serve:
	poetry run python -m structures.server.main

docker.build:
	docker build -t hardcore-2dstructures:latest .
