from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_reviews(reviews):

    prompt = f"""
You are an experienced Product Manager.

Analyze these customer reviews.

Return ONLY JSON.

Reviews:

{reviews}

Return this format:

{{
"sentiment_summary":"",
"pain_points":[],
"feature_requests":[],
"user_stories":[]
}}

"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content