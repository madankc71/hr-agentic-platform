from apps.hr_agent.nodes.router_node import router_node

def test_router_policy():
    state = {"intent": "policy_question"}
    # assert router_node(state) == "policy_node"
    assert router_node(state) == {"next_node": "policy_node"}


def test_router_unknown_intent():
    state = {"intent": "xyz_unknown"}
    # assert router_node(state) == "fallback_node"
    assert router_node(state) == {"next_node": "fallback_node"}
