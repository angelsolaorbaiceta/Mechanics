FROM node:20-slim AS frontend-builder

WORKDIR /frontend

COPY structures/frontend/package*.json ./
RUN npm ci

COPY structures/frontend/ ./
RUN npm run build

FROM python:3.12-slim

WORKDIR /app

RUN pip install uv
COPY pyproject.toml requirements.txt ./
RUN uv pip install -r requirements.txt

COPY structures/ ./structures/
RUN find ./structures -type d \( -name tests -o -name __pycache__ \) -exec rm -rf {} +

# Copy the built Svelte app into the static directory
COPY --from=frontend-builder /frontend/build/ ./structures/server/static/

COPY geom2d/ ./geom2d/
RUN find ./geom2d -type d \( -name tests -o -name __pycache__ \) -exec rm -rf {} +

COPY eqs/ ./eqs/
RUN find ./eqs -type d \( -name tests -o -name __pycache__ \) -exec rm -rf {} +

COPY utils/ ./utils/
RUN find ./utils -type d -name __pycache__ -exec rm -rf {} +

EXPOSE 8080

CMD ["python", "-m", "structures.server.main"]