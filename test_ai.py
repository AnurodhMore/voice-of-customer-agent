from services.ai_service import analyze_reviews

reviews = """
OTP never arrives.

Please add dark mode.

App crashes while paying.

Need biometric login.
"""

response = analyze_reviews(reviews)

print(response)