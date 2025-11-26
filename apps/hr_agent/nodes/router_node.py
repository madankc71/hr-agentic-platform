from typing import Dict

def router_node(state:Dict) -> str:
    """
    Router node decides which next node to run based on the classified intent.
    It returns the name of the next node in the LangGraph workflow.
    """

    intent = state.get("intent", "other")

    routing_table = {
        "policy_question": "policy_node",
        "ticket_request": "ticket_node",
        "benefits_question": "benefits_node",
        "payroll_question": "payroll_node",
        "leave_request": "leave_node",
        "other": "fallback_node"
    }

    next_node = routing_table.get(intent, "fallback_node")

    print(f"[router_node] Intent received: {intent}")
    print(f"[router_node] Routing to: {next_node}")

    # return next_node        
    return {"next_node": next_node}
