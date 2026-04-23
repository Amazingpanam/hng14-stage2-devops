import redis
import time
import os
import signal

# Environment variables
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD")

sleep_time = int(os.getenv("WORKER_SLEEP", 2))

# Redis connection
r = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True
)

# Graceful shutdown control
running = True

def shutdown(signum, frame):
    global running
    print("Shutting down worker...")
    running = False

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

# Health check (for Docker later)
def health_check():
    try:
        r.ping()
        return True
    except Exception:
        return False

# Job processing
def process_job(job_id):
    try:
        print(f"Processing job {job_id}")
        time.sleep(sleep_time)
        r.hset(f"job:{job_id}", "status", "completed")
        print(f"Done: {job_id}")
    except Exception as e:
        print(f"Failed job {job_id}: {e}")

# Main worker loop
while running:
    try:
        job = r.brpop("job", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id)
    except Exception as e:
        print(f"Worker error: {e}")
        time.sleep(2)
