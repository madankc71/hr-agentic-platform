from typing import Dict
from openai import OpenAI


def benefits_node(state: Dict) -> Dict:
    """
    Handles HR benefits-related questions.
    Returns a dictionary containing the LLM-generated answer.
    """

    client = OpenAI()

    messages = state.get("messages", [])
    user_message = messages[-1].get("content", "") if messages else ""

    system_prompt = """
    You are an HR Benefits Specialist AI.
    Your task is to answer employee questions related to:

    - health insurance
    - medical coverage
    - dental/vision benefits
    - retirement plans
    - wellness programs
    - insurance eligibility

    Provide clear, accurate answers.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        max_tokens=200,
        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    print(f"[benefits_node] User message: {user_message}")
    print(f"[benefits_node] Answer: {answer}")

    # LangGraph node output must be a dict
    return {"benefits_answer": answer}
