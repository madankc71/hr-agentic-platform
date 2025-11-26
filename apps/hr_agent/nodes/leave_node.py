from typing import Dict
from openai import OpenAI


def leave_node(state: Dict) -> Dict:
    """
    Handles leave / PTO questions.
    Returns a structured dictionary with the assistant's answer.
    """

    client = OpenAI()

    messages = state.get("messages", [])
    # Support both LangGraph HumanMessage and simple dicts
    if messages:
        last = messages[-1]
        user_message = getattr(last, "content", last.get("content", ""))
    else:
        user_message = ""

    system_prompt = """
    You are an HR assistant specializing in leave / vacation / PTO questions.
    - Answer only HR leave-related questions.
    - If the question is not about leave, say you only handle leave/absence queries.
    - Use clear, concise language an employee can understand.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
        max_tokens=256,
    )

    answer = response.choices[0].message.content.strip()

    print(f"[leave_node] User message: {user_message}")
    print(f"[leave_node] Leave answer: {answer}")

    # Append answer to messages so downstream nodes have full conversation
    updated_messages = list(messages) + [
        {"role": "assistant", "content": answer}
    ]

    return {"messages": updated_messages}