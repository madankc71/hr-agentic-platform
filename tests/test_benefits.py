from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.benefits_node import benefits_node


@patch("apps.hr_agent.nodes.benefits_node.OpenAI")
def test_benefits_node(mock_openai):
    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Here is your benefits information"))]
    )

    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "Do we have dental insurance?"}]
    }

    result = benefits_node(state)

    assert "benefits_answer" in result
    assert result["benefits_answer"] == "Here is your benefits information"
