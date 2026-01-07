# Production image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps (curl helps healthcheck; optional)
RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Copy and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ ./app/

EXPOSE 5000

# Healthcheck (tries /api/health)
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -fsS http://127.0.0.1:5000/api/health || exit 1

# Gunicorn entrypoint
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app", "--workers", "2", "--timeout", "30"]
