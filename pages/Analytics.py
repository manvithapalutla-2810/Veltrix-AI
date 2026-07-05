import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Veltrix AI Analytics")
st.subheader("Recruitment Insights & Hiring Analytics")

st.markdown("---")

csv_path = "data/candidate_rankings.csv"

if not os.path.exists(csv_path):
    st.warning("⚠️ Please run Candidate Ranking first.")
    st.stop()

df = pd.read_csv(csv_path)

# =========================
# KPI Cards
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Candidates", len(df))

with col2:
    st.metric(
        "⭐ Avg ATS",
        f"{df['ATS Score'].mean():.2f}"
    )

with col3:
    st.metric(
        "🎯 Avg Match",
        f"{df['Resume Match'].mean():.2f}%"
    )

with col4:
    st.metric(
        "🏆 Highest Score",
        f"{df['Final Score'].max():.2f}%"
    )

st.markdown("---")

# =========================
# Final Score Histogram
# =========================

st.subheader("🏆 Final Score Distribution")

fig = px.histogram(
    df,
    x="Final Score",
    nbins=10,
    color="Final Score"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# ATS vs Resume Match
# =========================

st.subheader("⭐ ATS Score vs Resume Match")

fig2 = px.scatter(
    df,
    x="ATS Score",
    y="Resume Match",
    color="Final Score",
    size="Final Score",
    hover_name="Candidate"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# =========================
# Final Score Pie
# =========================

col1, col2 = st.columns(2)

with col1:

    fig3 = px.pie(
        df,
        values="Final Score",
        names="Candidate",
        title="Candidate Contribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

with col2:

    fig4 = px.bar(
        df,
        x="Candidate",
        y="Final Score",
        color="Final Score",
        text="Final Score",
        title="Final Candidate Scores"
    )

    fig4.update_traces(textposition="outside")

    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# =========================
# Resume Match Trend
# =========================

st.subheader("📄 Resume Match Trend")

fig5 = px.line(
    df,
    x="Candidate",
    y="Resume Match",
    markers=True
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# =========================
# ATS Trend
# =========================

st.subheader("⭐ ATS Score Trend")

fig6 = px.line(
    df,
    x="Candidate",
    y="ATS Score",
    markers=True
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# =========================
# Recruiter Insights
# =========================

st.subheader("💡 Recruiter Insights")

best = df.iloc[0]

st.success(f"""
🏆 Top Candidate: **{best['Candidate']}**

⭐ Final Score: **{best['Final Score']}%**

🎯 Resume Match: **{best['Resume Match']}%**

📄 ATS Score: **{best['ATS Score']}**
""")

st.info(f"""
Average ATS Score: **{df['ATS Score'].mean():.2f}**

Average Resume Match: **{df['Resume Match'].mean():.2f}%**

Total Candidates Screened: **{len(df)}**
""")

st.markdown("---")

st.download_button(
    "📥 Download Analytics Report",
    data=df.to_csv(index=False),
    file_name="Veltrix_AI_Analytics.csv",
    mime="text/csv"
)