from services.local_llm import ask_llama


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

    return ask_llama(prompt)