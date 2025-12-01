from langgraph.graph import StateGraph
from .state_schema import HRState
from .nodes.classifier_node import classifier_agent
from .nodes.router_node import router_node
from .nodes.policy_node import policy_node
from .nodes.leave_node import leave_node
from .nodes.benefits_node import benefits_node
from .nodes.payroll_node import payroll_node
from .nodes.fallback_node import fallback_node


workflow = StateGraph(HRState)

workflow.add_node("classifier", classifier_agent)
workflow.add_node("router", router_node)
workflow.add_node("policy_node", policy_node)

workflow.add_node("leave_node", leave_node)
workflow.add_node("benefits_node", benefits_node)
workflow.add_node("payroll_node", payroll_node)
workflow.add_node("fallback_node", fallback_node)
# workflow.add_node("ticket_node", ticket_node)


workflow.add_edge("classifier", "router")

workflow.set_entry_point("classifier")

app = workflow.compile()