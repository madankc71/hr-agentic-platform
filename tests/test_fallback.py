from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.fallback_node import fallback_node


@patch("apps.hr_agent.nodes.fallback_node.OpenAI")
def test_fallback_node(mock_openai):
    mock_client = MagicMock()

    # Fake model output
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Sorry, I’m not sure. Can you clarify?"))]
    )

    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "???"}]
    }

    result = fallback_node(state)

    assert "fallback_answer" in result
    assert isinstance(result["fallback_answer"], str)
    assert "clarify" in result["fallback_answer"].lower()