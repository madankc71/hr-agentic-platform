from unittest.mock import patch, MagicMock
from apps.hr_agent.nodes.payroll_node import payroll_node

@patch("apps.hr_agent.nodes.payroll_node.OpenAI")
def test_payroll_node(mock_openai):
    mock_client = MagicMock()

    # Fake response content
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Your next pay date is Feb 28th."))]
    )

    mock_openai.return_value = mock_client

    state = {
        "messages": [{"role": "user", "content": "When is the next pay date?"}]
    }

    result = payroll_node(state)

    assert "answer" in result
    assert "Feb" in result["answer"]
