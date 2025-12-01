# apps/hr_agent/nodes/ticket_node.py

from typing import Dict
from openai import OpenAI


def ticket_node(state: Dict) -> Dict:
    """
    Handles employee ticket requests such as:
    - Creating IT tickets
    - HR support requests
    - Access issues
    """

    client = OpenAI()

    messages = state.get("messages", [])
    user_message = ""

    # Handle both dict messages and HumanMessage objects
    if messages:
        last = messages[-1]
        if isinstance(last, dict):
            user_message = last.get("content", "")
        else:
            user_message = getattr(last, "content", "")

    system_prompt = """
    You are a corporate HR/IT ticket assistant.
    Identify if the user is requesting creation of a support ticket.
    Respond with a short confirmation message — NOT the intent class.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=50,
        temperature=0
    )

    ticket_text = response.choices[0].message.content.strip()

    return {
        "answer": ticket_text,
        "intent": state.get("intent", "ticket_request"),
    }
