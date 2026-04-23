from fastapi import FastAPI
import redis
import uuid
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD")

r = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True
)

@app.post("/jobs")
def create_job():
    try:
        job_id = str(uuid.uuid4())
        r.lpush("job", job_id)
        r.hset(f"job:{job_id}", "status", "queued")
        return {"job_id": job_id}
    except Exception as e:
        return {"error": str(e)}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    try:
        status = r.hget(f"job:{job_id}", "status")
        if not status:
            return {"error": "not found"}
        return {"job_id": job_id, "status": status}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    try:
        r.ping()
        return {"status": "healthy"}
    except:
        return {"status": "unhealthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
