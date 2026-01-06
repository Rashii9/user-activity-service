from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_activity():
    response = client.post(
        "/activity",
        json={"user_id": "u1", "action": "login"}
    )
    assert response.status_code == 200
