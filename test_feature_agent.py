from agents.feature_agent import detect_features

reviews = """
Please add dark mode.
Biometric login would be useful.
OTP takes too long.
Payment keeps failing.
"""

print(detect_features(reviews))