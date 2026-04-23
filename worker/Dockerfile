FROM python:3.11-slim

WORKDIR /app

# system dependencies (optional but safe)
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# non-root user
RUN useradd -m workeruser
USER workeruser

ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import redis; r=redis.Redis(host='redis', port=6379); r.ping()" || exit 1

CMD ["python", "worker.py"]
