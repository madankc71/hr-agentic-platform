from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.policy_node import policy_node


@patch("apps.hr_agent.nodes.policy_node.OpenAI")
def test_policy_node(mock_openai):
    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Here is the policy answer"))]
    )

    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "What is the vacation policy?"}]
    }

    result = policy_node(state)

    assert "answer" in result
    assert result["answer"] == "Here is the policy answer"