from typing import Dict
from openai import OpenAI


def fallback_node(state: Dict) -> Dict:
    """
    Handles unknown or unsupported HR intents.
    Returns a generic helpful HR message.
    """

    client = OpenAI()

    messages = state.get("messages", [])
    user_message = messages[-1]["content"] if messages else ""

    system_prompt = """
    You are an HR fallback assistant.

    When the system cannot determine the correct HR category,
    you provide a polite, safe, and helpful generic HR response.

    Your tone must be:
    - Friendly
    - Supportive
    - Not overly confident (avoid hallucinations)
    - Encourage the user to clarify their question if needed.

    Respond with a short answer (2–3 sentences).
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=120,
        temperature=0.2
    )

    answer = response.choices[0].message.content.strip()

    print(f"[fallback_node] User message: {user_message}")
    print(f"[fallback_node] Response: {answer}")

    return {"fallback_answer": answer}