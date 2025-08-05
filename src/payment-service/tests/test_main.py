from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_payment():
    response = client.post("/payments", json={
        "amount": 150.5,
        "currency": "USD",
        "recipient": "test@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["payment"]["amount"] == 150.5
