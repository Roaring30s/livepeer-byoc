# Reverse Text Microservice

This directory packages the Flask-based `reverse-server.py` app into a
container image that fits into the three-service BYOC layout
(`orchestrator`, `register_capability`, `reverse_text`).

## Build the image

From the repo root run:

```bash
docker build -t byoc_reverse_text ./reverse-text
```

## Run locally (optional)

```bash
docker run --rm -p 5000:5000 byoc_reverse_text
```

## Compose integration

Reference the image inside `docker-compose.yml`:

```yaml
  reverse_text:
    image: byoc_reverse_text
    container_name: byoc_reverse_text
    ports:
      - 5000:5000
    depends_on:
      - orchestrator
```


