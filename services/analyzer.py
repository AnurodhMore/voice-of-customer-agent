import pandas as pd


# ---------------------------------------------------
# Issue Categories
# ---------------------------------------------------

ISSUE_CATEGORIES = {
    "OTP Issues": [
        "otp",
        "verification",
        "code"
    ],

    "App Crash": [
        "crash",
        "freeze",
        "stuck"
    ],

    "Performance": [
        "slow",
        "lag",
        "loading"
    ],

    "Payment": [
        "payment",
        "checkout",
        "failed"
    ]
}


# ---------------------------------------------------
# Business Impact Scores
# ---------------------------------------------------

BUSINESS_IMPACT = {
    "OTP Issues": 9,
    "Payment": 10,
    "App Crash": 8,
    "Performance": 7
}


# ---------------------------------------------------
# Analyze Reviews
# ---------------------------------------------------

def analyze_reviews(df):

    results = {}

    for issue, keywords in ISSUE_CATEGORIES.items():

        frequency = 0
        negative = 0

        for _, row in df.iterrows():

            review = str(row["review"]).lower()
            rating = row["rating"]

            if any(keyword in review for keyword in keywords):

                frequency += 1

                if rating <= 2:
                    negative += 1

        impact = BUSINESS_IMPACT.get(issue, 5)

        priority_score = (
            frequency * 0.4 +
            negative * 0.3 +
            impact * 0.3
        )

        results[issue] = {
            "frequency": frequency,
            "negative": negative,
            "impact": impact,
            "score": round(priority_score, 1)
        }

    return results