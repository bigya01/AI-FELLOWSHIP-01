from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_shorten_url():
    response = client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data
    assert data["short_url"].startswith("http://localhost:8000/")
