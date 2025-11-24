from langgraph.graph import StateGraph, START, END
from .state_schema import HRState
from .nodes.classifier_node import classifier_agent

workflow = StateGraph(HRState)

workflow.add_node("classifier", classifier_agent)
workflow.add_edge(START, "classifier")
workflow.add_edge("classifier", END)

app = workflow.compile()
