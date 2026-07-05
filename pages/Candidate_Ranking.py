import os
import pandas as pd
import plotly.express as px
import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.ml_matcher import calculate_match_score
from utils.ats_score import calculate_ats_score

st.set_page_config(
    page_title="Candidate Ranking",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Candidate Ranking")

st.write("Upload a Job Description and rank candidates automatically.")

st.markdown("---")

job = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "txt"]
)

resumes = st.file_uploader(
    "Upload Candidate Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if job:

    if job.name.endswith(".txt"):
        jd = job.read().decode("utf-8")
    else:
        jd = extract_text_from_pdf(job)

    if resumes:

        results = []

        for resume in resumes:

            resume_text = extract_text_from_pdf(resume)

            match = calculate_match_score(
                jd,
                resume_text
            )

            ats, matched, missing = calculate_ats_score(
                jd,
                resume_text
            )

            final_score = round(
                (match * 0.6) + (ats * 0.4),
                2
            )

            results.append({
                "Candidate": resume.name,
                "Resume Match": match,
                "ATS Score": ats,
                "Final Score": final_score
            })

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Final Score",
            ascending=False
        ).reset_index(drop=True)

        os.makedirs("data", exist_ok=True)

        df.to_csv(
            "data/candidate_rankings.csv",
            index=False
        )

        ranking_df = df.copy()
        ranking_df.index += 1

        st.success("✅ Candidates Ranked Successfully")

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "👥 Candidates",
                len(df)
            )

        with col2:
            st.metric(
                "📄 Avg Resume Match",
                f"{df['Resume Match'].mean():.2f}%"
            )

        with col3:
            st.metric(
                "⭐ Avg ATS Score",
                f"{df['ATS Score'].mean():.2f}"
            )

        st.markdown("---")

        st.subheader("📋 Candidate Ranking")

        st.dataframe(
            ranking_df,
            use_container_width=True
        )

        st.download_button(
            "📥 Download Ranking Report",
            df.to_csv(index=False),
            "candidate_rankings.csv",
            "text/csv"
        )

        st.markdown("---")

        winner = df.iloc[0]

        st.subheader("🥇 Best Candidate")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Candidate",
                winner["Candidate"]
            )

        with col2:
            st.metric(
                "Final Score",
                f"{winner['Final Score']}%"
            )

        st.success(
            f"🏆 {winner['Candidate']} is the best candidate with a Final Score of {winner['Final Score']}%."
        )

        st.markdown("---")

        st.subheader("📊 Final Score Comparison")

        fig = px.bar(
            df,
            x="Candidate",
            y="Final Score",
            color="Final Score",
            text="Final Score",
            title="Candidate Final Scores"
        )

        fig.update_traces(textposition="outside")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("⭐ ATS Score Distribution")

        fig2 = px.pie(
            df,
            values="ATS Score",
            names="Candidate",
            title="ATS Score Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )