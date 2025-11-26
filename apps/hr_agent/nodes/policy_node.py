from typing import Dict
from openai import OpenAI


def policy_node(state: Dict) -> Dict:
    """
    Handles HR policy questions.
    Returns a structured dictionary with the answer.
    """

    client = OpenAI()

    messages = state.get("messages", [])
    user_message = messages[-1].content if messages else ""

    system_prompt = """
    You are an HR Policy assistant.
    Answer employee questions strictly based on common HR policy standards.
    Be factual, concise, and professional.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=200,
        temperature=0.2
    )

    answer = response.choices[0].message.content.strip()

    print(f"[policy_node] User message: {user_message}")
    print(f"[policy_node] Response: {answer}")

    return {"answer": answer}
