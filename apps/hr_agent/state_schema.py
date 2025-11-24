from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class HRState(TypedDict):
    messages: Annotated[List[dict], add_messages]
    intent: str | None
