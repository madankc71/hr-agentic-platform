from typing import Dict
from openai import OpenAI

client = OpenAI()

ALLOWED_INTENTS = [
    "policy_question",
    "ticket_request",
    "benefits_question",
    "payroll_question",
    "leave_request",
    "other"
]


def classifier_agent(state: Dict) -> Dict:
    """
    Placeholder classifier node.
    This will be implemented in the next step.
    """
    # TODO: implement logic
    messages = state.get("messages", [])
    user_message = messages[-1]["content"] if messages else ""

    system_prompt = f"""
    You are an HR intent classifier.
    Your job is to categorize employee HR questions into EXACTLY one of the following:

    - policy_question
    - ticket_request
    - benefits_question
    - payroll_question
    - leave_request
    - other

    Return ONLY the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=4,
        temperature=0
    )

    intent = response.choices[0].message.content.strip()

    if intent not in ALLOWED_INTENTS:
        intent = "other"

    print(f"[classifier_agent] User message: {user_message}")
    print(f"[classifier_agent] Classified intent: {intent}")

    return {"intent": intent}
