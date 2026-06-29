"""Smoke tests for the FastAPI app."""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health() -> None:
    """The health endpoint should return a JSON OK response."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "SMS Surface"


def test_sms_inbound_stub() -> None:
    """The inbound SMS endpoint should return a TwiML response."""
    payload = {"From": "+14155551234", "Body": "Hello"}
    response = client.post("/sms/inbound", data=payload)
    assert response.status_code == 200
    assert "<Response>" in response.text
    assert "<Message>" in response.text
