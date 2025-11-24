from apps.hr-agent.graph_setup import app

def test_classifier_runs():
    state = {
        "messages": [{"role": "user", "content": "Hello"}],
        "intent": None
    }

    result = app.invoke(state)
    assert "intent" in result
