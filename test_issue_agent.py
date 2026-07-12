from agents.issue_agent import detect_issues

reviews = """
OTP takes too long.
Payment fails often.
App crashes while paying.
Dark mode should be added.
"""

print(detect_issues(reviews))