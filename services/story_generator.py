import pandas as pd


def generate_user_stories(feature_requests):

    stories = []

    for feature in feature_requests:

        feature_lower = feature.lower()

        if "dark" in feature_lower:

            story = (
                "As a user, "
                "I want Dark Mode "
                "so that I can comfortably use the app at night."
            )

        elif "login" in feature_lower or "biometric" in feature_lower:

            story = (
                "As a user, "
                "I want Biometric Login "
                "so that I can securely log in faster."
            )

        else:

            story = (
                "As a user, "
                "I want this feature "
                "so that my experience improves."
            )

        stories.append(story)

    return pd.DataFrame({
        "User Story": stories
    })