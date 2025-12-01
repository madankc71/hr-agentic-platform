# tests/test_api.py

from fastapi.testclient import TestClient
from apps.hr_agent.api import api

client = TestClient(api)


def test_api_chat_endpoint():
    payload = {"message": "How many vacation days do I have?"}
    response = client.post("/hr/chat", json=payload)

    assert response.status_code == 200
    body = response.json()

    assert "intent" in body
    assert "answer" in body
    assert "raw_state" in body
