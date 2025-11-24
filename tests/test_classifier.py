from unittest.mock import patch, MagicMock
from apps.hr_agent.graph_setup import app

@patch("apps.hr_agent.nodes.classifier_node.OpenAI")
def test_classifier_runs(mock_openai):
    # Mock the OpenAI() return object
    mock_client = MagicMock()

    # Mock the API response structure
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="leave_request"))]
    )

    # When classifier_node.OpenAI() is called, return mock_client
    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "How many vacation days do I have?"}],
        "intent": None
    }

    result = app.invoke(state)

    assert "intent" in result
    assert result["intent"] == "leave_request"
