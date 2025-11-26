from typing import Dict
from openai import OpenAI

def payroll_node(state: Dict) -> Dict:
    """
    Handles payroll-related HR questions.
    Returns a structured dictionary with the answer.
    """

    client = OpenAI()

    messages = state.get("messages", [])
    # Handle both dict and LangGraph HumanMessage
    last_msg = messages[-1]
    user_message = last_msg["content"] if isinstance(last_msg, dict) else last_msg.content

    system_prompt = """
    You are an HR payroll specialist. 
    Answer employee payroll-related questions clearly and accurately.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content.strip()

    print("[payroll_node] User message:", user_message)
    print("[payroll_node] Answer:", answer)

    return {"answer": answer}