"""Smoke tests for the FastAPI app."""

from unittest.mock import AsyncMock, patch

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


def test_message_inbound_stub() -> None:
    """The inbound message endpoint should acknowledge a BlueBubbles payload."""
    payload = {
        "text": "Hello",
        "handle": "+14155551234",
        "chatGuid": "iMessage;+;chat123",
    }
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        response = client.post("/message/inbound", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "delivered"
    assert "Hello" in data["reply"]
    mock_post.assert_called_once()
