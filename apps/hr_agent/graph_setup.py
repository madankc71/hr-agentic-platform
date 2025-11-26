from langgraph.graph import StateGraph
from .state_schema import HRState
from .nodes.classifier_node import classifier_agent
from .nodes.router_node import router_node
from .nodes.policy_node import policy_node

workflow = StateGraph(HRState)

workflow.add_node("classifier", classifier_agent)
workflow.add_node("router", router_node)
workflow.add_node("policy_node", policy_node)

workflow.add_edge("classifier", "router")

workflow.set_entry_point("classifier")

app = workflow.compile()