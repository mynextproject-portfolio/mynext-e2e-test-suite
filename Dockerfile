FROM python:3.12-slim AS base
WORKDIR /app

FROM base AS test
COPY pyproject.toml ./
RUN pip install -e ".[test]"
COPY . .
CMD ["pytest", "-v"]

FROM base AS production
COPY . .
CMD ["python", "src/main.py"]

