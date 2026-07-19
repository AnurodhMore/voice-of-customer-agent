import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from services.story_generator import generate_user_stories
from services.analyzer import analyze_reviews
from services.ai_insights import generate_ai_insights

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Voice of Customer Dashboard",
    page_icon="💬",
    layout="wide"
)

# ---------------------------------------------------
# Load Custom CSS
# ---------------------------------------------------
css_path = Path("assets/css/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🤖 Voice of Customer")

st.sidebar.markdown("---")

st.sidebar.write("### AI Product Dashboard")

st.sidebar.info(
    """
Analyze customer feedback using AI.

### Features

- 📊 Review Analysis
- 📍 Pain Point Detection
- 💡 Feature Requests
- 📝 User Story Generation
- 📈 Priority Matrix
- 🤖 AI Product Insights
"""
)

st.sidebar.markdown("---")
st.sidebar.success("Portfolio Project")

st.sidebar.markdown("---")

st.sidebar.subheader("Tech Stack")

st.sidebar.markdown("""
- Python
- Streamlit
- Pandas
- Ollama
- Llama 3.2
""")

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------
st.title("💬 Voice of Customer")
st.caption("AI-powered Product Intelligence Dashboard")

## st.caption(
  ##  "AI-powered product analytics platform for discovering customer pain points, feature requests and product opportunities."
##)

st.markdown(
    """
Transform customer feedback into **prioritized product opportunities** using AI.

Designed for **Product Managers**, **Product Owners**, and **Founders** to quickly identify customer pain points, prioritize features, and generate actionable user stories.
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("Sentiment Analysis")

with col2:
    st.success("Pain Point Detection")

with col3:
    st.success("Feature Requests")

with col4:
    st.success("AI User Stories")
st.markdown("<br>", unsafe_allow_html=True)
# ---------------------------------------------------
# File Upload
# ---------------------------------------------------
st.markdown("### 📂 Upload Customer Reviews")
st.caption("Upload a CSV or Excel file to begin AI-powered analysis.")
uploaded_file = st.file_uploader(
    "Upload Customer Reviews Dataset",
    type=["csv", "xlsx"]
)
# ---------------------------------------------------
# Download Demo Dataset
# ---------------------------------------------------

with open("data/customer_reviews_sample.csv", "rb") as f:
    st.download_button(
        label="📥 Download Demo Dataset",
        data=f,
        file_name="data/customer_reviews_sample.csv",
        mime="text/csv"
    )
# ===================================================
# MAIN APPLICATION
# ===================================================
if uploaded_file is not None:

    # ------------------------------------------------
    # Read File
    # ------------------------------------------------
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success(f"✅ {len(df)} customer reviews analyzed successfully!")

    # ------------------------------------------------
    # Validate Columns
    # ------------------------------------------------
    required_columns = ["review", "rating"]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        st.error(f"Missing required columns: {missing_columns}")
        st.stop()

    st.divider()

    st.subheader("🎛 Dashboard Filters")

    minimum_rating = st.slider(
        "Show reviews with rating",
        min_value=1,
        max_value=5,
        value=1
    )

    filtered_df = df[df["rating"] >= minimum_rating]
    if filtered_df.empty:
        st.warning("No reviews match the selected filter.")
        st.stop()
    # ------------------------------------------------
    # Analyze Reviews
    # ------------------------------------------------
    analysis = analyze_reviews(filtered_df)
    ai_summary = generate_ai_insights(filtered_df)

    # ------------------------------------------------
    # Review Summary
    # ------------------------------------------------
    total_reviews = len(filtered_df)

    positive = (filtered_df["rating"] >= 4).sum()
    neutral = (filtered_df["rating"] == 3).sum()
    negative = (filtered_df["rating"] <= 2).sum()

 
    sentiment_df = pd.DataFrame({
        "Sentiment": [
          "Positive",
          "Neutral",
          "Negative"
        ],
        "Reviews": [
          positive,
          neutral,
         negative
        ]
}) 
    pie_chart = px.pie(
      sentiment_df,
      names="Sentiment",
      values="Reviews",
      hole=0.45,
      title="Customer Sentiment"
    )

    pie_chart.update_layout(
      paper_bgcolor="#0E1117",
      plot_bgcolor="#0E1117",
      font_color="white",
      title_x=0.5
    )
    # ------------------------------------------------
    # Feature Request Detection
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

    for review in filtered_df["review"]:
        review_lower = str(review).lower()

        if any(keyword in review_lower for keyword in feature_keywords):
            feature_requests.append(review)

    feature_requests = list(set(feature_requests))

    # ------------------------------------------------
    # User Stories
    # ------------------------------------------------
    if feature_requests:
        stories_df = generate_user_stories(feature_requests)
    else:
        stories_df = pd.DataFrame(
            columns=["User Story", "Acceptance Criteria"]
        )

    # ------------------------------------------------
    # Priority Matrix
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
        by="Business Priority",
        ascending=False
    )
    critical_count = sum(
    details["frequency"]
    for details in analysis.values()
)
    # ------------------------------------------------
    # KPI Cards
    # ------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="
            background:#1E1E1E;
            padding:20px;
            border-radius:12px;
            border:1px solid #30363d;
            text-align:center;
        ">
            <div style="font-size:28px;">📄</div>
            <div style="font-size:32px;font-weight:bold;">{len(filtered_df)}</div>
            <div style="color:#9CA3AF;">Total Reviews</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            background:#1E1E1E;
            padding:20px;
            border-radius:12px;
            border:1px solid #30363d;
            text-align:center;
        ">
            <div style="font-size:28px;">🚨</div>
            <div style="font-size:32px;font-weight:bold;">{critical_count}</div>
            <div style="color:#9CA3AF;">Critical Issues</div>
        </div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
            background:#1E1E1E;
            padding:20px;
            border-radius:12px;
            border:1px solid #30363d;
            text-align:center;
        ">
            <div style="font-size:28px;">💡</div>
            <div style="font-size:32px;font-weight:bold;">{len(feature_requests)}</div>
            <div style="color:#9CA3AF;">Feature Requests</div>
        </div>
    """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="
            background:#1E1E1E;
            padding:20px;
            border-radius:12px;
            border:1px solid #30363d;
            text-align:center;
        ">
            <div style="font-size:28px;">📝</div>
            <div style="font-size:32px;font-weight:bold;">{len(stories_df)}</div>
            <div style="color:#9CA3AF;">AI User Stories</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.info(
    """
    The dashboard automatically identifies customer pain points,
    feature requests and converts them into prioritized
    product opportunities.
    """
    )
    # ------------------------------------------------
    # Dashboard Layout
    # ------------------------------------------------
    left, right = st.columns(2)

    # ================= LEFT =================
    with left:

        st.subheader("📊 Customer Sentiment")

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("💡 Feature Requests")

        if feature_requests:

            for request in feature_requests:
                st.info(request)

        else:
            st.info("No feature requests detected.")

    # ================= RIGHT =================
    with right:

        st.subheader("📍 Highest Impact Issues")

        sorted_issues = sorted(
           [
                (issue, details)
                for issue, details in analysis.items()
                if details["frequency"] > 0
            ],
            key=lambda x: x[1]["score"],
            reverse=True
        )

        for i, (issue, details) in enumerate(sorted_issues[:3], start=1):

            st.write(
                f"**{i}. {issue}** — {details['frequency']} mentions"
            )

        st.markdown("---")

        st.subheader("📈 Business Priority Score")

        fig = px.bar(
            priority_matrix,
            x="Business Priority",
            y="Issue",
            orientation="h",
            text="Business Priority",
            height=300
        )

        fig.update_layout(
            yaxis=dict(categoryorder="total ascending"),
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ------------------------------------------------
    # User Stories
    # ------------------------------------------------
    st.divider()

    st.subheader(
        f"📝 AI Generated User Stories({len(stories_df)})"
    )

    st.dataframe(
        stories_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🔍 Customer Review Explorer")

    search = st.text_input(
        "Search customer reviews",
        placeholder="Search by keyword..."
    )

    review_df = filtered_df.copy()

    if search:
        review_df = review_df[
            review_df["review"].str.contains(
                search,
                case=False,
                na=False
            )    
        ]

    st.dataframe(
        review_df,
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------------
    # AI Insights
    # ------------------------------------------------
    st.divider()

    with st.expander(
        "🤖 Executive Product Summary",
        expanded=True
    ):

        st.markdown(ai_summary)

    # ------------------------------------------------
    # Export
    # ------------------------------------------------
    st.divider()

    st.subheader("📤 Export")

    csv = stories_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download User Stories (.csv)",
        data=csv,
        file_name="user_stories.csv",
        mime="text/csv"
    )

    st.divider()

    st.caption(
        "Built with Python • Streamlit • Ollama • Llama 3.2 • Plotly")
    
    st.caption("AI Product Management Portfolio Project") 
    st.caption("Designed & Built by Anurodh More")
       
    