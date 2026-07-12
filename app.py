import streamlit as st
import pandas as pd
from services.story_generator import generate_user_stories
from services.analyzer import analyze_reviews
from services.ai_insights import generate_ai_insights
# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Voice of Customer AI Agent",
    page_icon="💬",
    layout="wide"
)

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------
st.title("💬 Voice of Customer AI Agent")
st.markdown("""
Transform raw customer feedback into **actionable product insights**.

This AI-powered dashboard helps Product Managers:
- 📊 Analyze customer sentiment
- 🚨 Detect recurring issues
- 💡 Extract feature requests
- 📝 Generate Agile user stories
- 🤖 Receive AI-powered product recommendations
""")


# ---------------------------------------------------
# File Upload
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload your reviews",
    type=["csv", "xlsx"]
)

# ===================================================
# MAIN APPLICATION
# ===================================================
if uploaded_file is not None:

    # ------------------------------------------------
    # Read Uploaded File
    # ------------------------------------------------
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # ------------------------------------------------
    # Validate Required Columns
    # ------------------------------------------------
    required_columns = ["review", "rating"]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        st.error(f"Missing required columns: {missing_columns}")
        st.stop()
    # ------------------------------------------------
    # Analyze Reviews
    # ------------------------------------------------
    analysis = analyze_reviews(df)
    ai_summary = generate_ai_insights(df)
    # ------------------------------------------------
    # Review Summary
    # ------------------------------------------------
    total_reviews = len(df)

    positive = (df["rating"] >= 4).sum()
    neutral = (df["rating"] == 3).sum()
    negative = (df["rating"] <= 2).sum()

    positive_pct = round((positive / total_reviews) * 100)
    neutral_pct = round((neutral / total_reviews) * 100)
    negative_pct = round((negative / total_reviews) * 100)

    # ------------------------------------------------
    # Detect Feature Requests
    # ------------------------------------------------
    feature_keywords = [
        "add",
        "feature",
        "need",
        "please",
        "would like",
        "login",
        "dark mode",
        "biometric"
    ]

    feature_requests = []

    for review in df["review"]:

        review_lower = str(review).lower()

        if any(keyword in review_lower for keyword in feature_keywords):
            feature_requests.append(review)
    # ------------------------------------------------
    # Generate User Stories
    # ------------------------------------------------

    feature_requests = list(set(feature_requests))

    if feature_requests:
        stories_df = generate_user_stories(feature_requests)
    else:
        stories_df = pd.DataFrame(
           columns=["User Story", "Acceptance Criteria"]
    )
    # ------------------------------------------------
    

    

    # ------------------------------------------------
    # # Dynamic Priority Matrix
    # ------------------------------------------------
    priority_matrix = pd.DataFrame([
    {
        "Issue": issue,
        "Frequency": details["frequency"],
        "Business Priority": details["score"]
    }
        for issue, details in analysis.items()
    ])

    priority_matrix = priority_matrix.sort_values(
        by="Score",
        ascending=False
    )

    # ------------------------------------------------
    # KPI Cards
    # ------------------------------------------------
    

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Reviews", total_reviews)

    col2.metric(
    "🚨 Critical Issues",
    len([i for i in analysis.values() if i["frequency"] > 0])
)

    col3.metric("💡 Features", len(feature_requests))

    col4.metric("📝 Stories", len(stories_df))

    st.divider()

    # ------------------------------------------------
    # Dashboard Layout
    # ------------------------------------------------
    left, right = st.columns(2)

    # ================= LEFT =================
    with left:

        st.subheader("📊 Review Summary")

        st.metric("😊 Positive Reviews", f"{positive_pct}%")

        st.metric("😐 Neutral Reviews", f"{neutral_pct}%")

        st.metric("😞 Negative Reviews", f"{negative_pct}%")

        st.subheader("💡 Feature Requests")

        if feature_requests:

            for request in feature_requests:
                st.info(request)

        else:
            st.write("No feature requests detected.")

    # ================= RIGHT =================
    with right:

        st.subheader("🔥 Top Pain Points")

        sorted_issues = sorted(
           analysis.items(),
           key=lambda x: x[1]["score"],
           reverse=True
)

        medals = ["🥇", "🥈", "🥉"]

for i, (issue, details) in enumerate(sorted_issues[:3]):

    st.markdown(
        f"{medals[i]} **{issue}**  \n"
        f"Mentions: **{details['frequency']}**  \n"
        f"Priority Score: **{details['score']}**"
    )
    

        

        st.subheader("📈 Priority Matrix")

        st.dataframe(
            priority_matrix,
            use_container_width=True,
            hide_index=True
        )

    st.divider()
    st.subheader(f"📝 Generated User Stories ({len(stories_df)})")

    st.dataframe(
        stories_df,
        use_container_width=True,
        hide_index=True
    )
    st.divider()

    st.divider()

    with st.expander(
        "🤖 AI Product Manager Insights",
        expanded=True
    ):

    st.markdown(ai_summary)
    # ------------------------------------------------
    # Export
    # ------------------------------------------------
    st.subheader("📤 Export")

    csv = stories_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Export User Stories",
        data=csv,
        file_name="user_stories.csv",
        mime="text/csv"
    )
    st.divider()

    st.caption(
    "Built using Python • Streamlit • Pandas • Ollama • Llama 3.2"
    )