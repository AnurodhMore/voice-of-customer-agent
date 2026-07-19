from services.gemini_service import ask_ai


def generate_ai_insights(df):

    reviews = "\n".join(df["review"].astype(str).tolist())

    prompt = f"""
You are a Senior Product Manager.

Analyze the customer reviews below.

Provide:

1. Top 3 customer issues
2. Root causes
3. Product improvement recommendations

Keep the response under 200 words.

Reviews:

{reviews}
"""

    return ask_ai(prompt)