# apps/hr_agent/api.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any

from langchain_core.messages import HumanMessage
from apps.hr_agent.graph_setup import app as hr_workflow


api = FastAPI(
    title="HR Agentic Platform API",
    version="0.1.0",
    description="HTTP interface for the HR LangGraph workflow.",
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    intent: str
    answer: str
    raw_state: Optional[Dict[str, Any]] = None


@api.post("/hr/chat", response_model=ChatResponse)
def hr_chat(req: ChatRequest) -> ChatResponse:
    """
    Entrypoint for HR questions.

    - Wraps the user message as a HumanMessage
    - Invokes the LangGraph HR workflow
    - Extracts intent + answer from the resulting state
    """

    # Build initial state expected by your HRState / graph
    state = {
        "messages": [HumanMessage(content=req.message)],
        "intent": None,
    }

    result_state = hr_workflow.invoke(state)

    intent = result_state.get("intent", "other")

    # All your handler nodes (policy, leave, benefits, payroll, fallback)
    # should be setting something like `answer` in the state.
    answer = result_state.get("answer", "Sorry, I could not generate an answer.")

    return ChatResponse(
        intent=intent,
        answer=answer,
        raw_state=result_state,  # helpful for debugging in early stages
    )