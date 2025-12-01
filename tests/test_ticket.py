# tests/test_ticket.py

from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.ticket_node import ticket_node


@patch("apps.hr_agent.nodes.ticket_node.OpenAI")
def test_ticket_node(mock_openai):
    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Ticket created"))]
    )

    mock_openai.return_value = mock_client

    state = {
        "messages": [{"content": "I need to reset my password", "role": "user"}]
    }

    result = ticket_node(state)

    assert "answer" in result
    assert result["answer"] == "Ticket created"
