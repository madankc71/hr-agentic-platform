from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.leave_node import leave_node


@patch("apps.hr_agent.nodes.leave_node.OpenAI")
def test_leave_node(mock_openai):
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="You have 15 days of PTO per year."))]
    )
    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "How many vacation days do I have?"}]
    }

    result = leave_node(state)

    assert "messages" in result
    assert isinstance(result["messages"], list)
    assert result["messages"][-1]["role"] == "assistant"
    assert "15 days" in result["messages"][-1]["content"]
