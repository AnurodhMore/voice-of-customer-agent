from services.local_llm import ask_llama


def detect_issues(reviews):
    prompt = f"""
You are a Senior Product Manager.

Read these customer reviews.

Identify the major issues customers are facing.

Group similar issues together.

Return ONLY a bullet list.

Reviews:

{reviews}
"""

    return ask_llama(prompt)