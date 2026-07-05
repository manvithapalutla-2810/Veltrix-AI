import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Veltrix AI Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🚀 Veltrix AI Dashboard")
st.subheader("AI-Powered Recruitment Analytics Platform")

st.markdown("---")

csv_path = "data/candidate_rankings.csv"

# =========================
# Top Buttons
# =========================

col1, col2 = st.columns([1, 1])

with col1:

    if st.button("🔄 Refresh Dashboard"):
        st.rerun()

with col2:

    if st.button("🗑️ Clear Previous Results"):

        if os.path.exists(csv_path):
            os.remove(csv_path)

        st.success("✅ Previous candidate results cleared successfully.")

        st.rerun()

# =========================
# Check CSV
# =========================

if not os.path.exists(csv_path):

    st.warning("⚠️ No candidate ranking data found.")

    st.info("👉 Please go to **Candidate Ranking** and rank candidates first.")

    st.stop()

# =========================
# Read CSV
# =========================

df = pd.read_csv(csv_path)

st.success("✅ Candidate Ranking Loaded Successfully")

st.markdown("---")

# =========================
# KPI Cards
# =========================

st.header("📈 Recruitment Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Candidates",
        len(df)
    )

with col2:
    st.metric(
        "🎯 Average Resume Match",
        f"{df['Resume Match'].mean():.2f}%"
    )

with col3:
    st.metric(
        "⭐ Average ATS Score",
        f"{df['ATS Score'].mean():.2f}"
    )

with col4:
    st.metric(
        "🏆 Highest Final Score",
        f"{df['Final Score'].max():.2f}%"
    )

st.markdown("---")

# =========================
# Best Candidate
# =========================

winner = df.iloc[0]

st.header("🥇 Best Candidate")

st.success(f"""
### 🎉 {winner['Candidate']}

🎯 **Resume Match:** {winner['Resume Match']}%

⭐ **ATS Score:** {winner['ATS Score']}

🏆 **Final Score:** {winner['Final Score']}%
""")

st.markdown("---")

# =========================
# Leaderboard
# =========================

st.header("🏅 Candidate Leaderboard")

leaderboard = df.copy()
leaderboard.index += 1

st.dataframe(
    leaderboard,
    use_container_width=True
)

st.markdown("---")

# =========================
# Charts
# =========================

col1, col2 = st.columns(2)

with col1:

    fig1 = px.bar(
        df,
        x="Candidate",
        y="Final Score",
        color="Final Score",
        text="Final Score",
        title="🏆 Final Candidate Scores"
    )

    fig1.update_traces(textposition="outside")

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.pie(
        df,
        values="ATS Score",
        names="Candidate",
        title="⭐ ATS Score Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    fig3 = px.bar(
        df,
        x="Candidate",
        y="Resume Match",
        color="Resume Match",
        text="Resume Match",
        title="📄 Resume Match Comparison"
    )

    fig3.update_traces(textposition="outside")

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col4:

    fig4 = px.bar(
        df,
        x="Candidate",
        y="ATS Score",
        color="ATS Score",
        text="ATS Score",
        title="⭐ ATS Score Comparison"
    )

    fig4.update_traces(textposition="outside")

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.markdown("---")

# =========================
# Final Score Trend
# =========================

st.header("📈 Final Score Trend")

fig5 = px.line(
    df,
    x="Candidate",
    y="Final Score",
    markers=True,
    title="Candidate Performance Trend"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# =========================
# Top Candidates
# =========================

st.header("🥇 Top 3 Candidates")

st.table(df.head(3))

st.markdown("---")

# =========================
# Download Report
# =========================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Candidate Ranking Report",
    data=csv,
    file_name="Veltrix_AI_Candidate_Ranking.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption("🚀 Veltrix AI | AI-Powered Recruitment Intelligence Platform")