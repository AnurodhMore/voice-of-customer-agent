import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_ai(prompt):
    """
    Sends a prompt to Google Gemini Flash and returns the response.
    """
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text