FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m workeruser
USER workeruser

HEALTHCHECK CMD python -c "import redis; redis.Redis(host='redis', port=6379).ping()" || exit 1

CMD ["python", "worker.py"]
