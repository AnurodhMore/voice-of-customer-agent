from services.gemini_service import ask_ai


def detect_features(reviews):
    prompt = f"""
You are a Senior Product Manager.

Read the customer reviews.

Identify ONLY feature requests.

Ignore bugs.

Return ONLY bullet points.

Reviews:

{reviews}
"""

    return ask_ai(prompt)