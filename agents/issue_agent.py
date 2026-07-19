from services.gemini_service import ask_ai


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

    return ask_ai(prompt)