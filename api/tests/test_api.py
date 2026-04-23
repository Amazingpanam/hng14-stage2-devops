from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200


def test_create_job():
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()


def test_get_job():
    res = client.get("/jobs/test-id")
    assert res.status_code in [200, 404]
