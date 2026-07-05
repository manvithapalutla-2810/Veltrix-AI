from utils.pdf_report import generate_pdf
from utils.ai_analyzer import analyze_resume
from utils.ats_score import calculate_ats_score
from utils.ml_matcher import calculate_match_score
from utils.pdf_reader import extract_text_from_pdf
import streamlit as st

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analysis")

st.write("Upload a Job Description and Candidate Resume(s).")

st.markdown("---")

# Upload Job Description
job_description = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "txt"]
)

# Upload Resume(s)
resumes = st.file_uploader(
    "Upload Candidate Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)

st.markdown("---")

job_description_text = ""

# Read Job Description
if job_description:

    if job_description.name.endswith(".txt"):
        job_description_text = job_description.read().decode("utf-8")
    else:
        job_description_text = extract_text_from_pdf(job_description)

    st.success("✅ Job Description Uploaded Successfully!")

# Read Resume(s)
if resumes:

    st.success(f"✅ {len(resumes)} Resume(s) Uploaded Successfully!")

    for resume in resumes:

        resume_text = extract_text_from_pdf(resume)

        with st.expander(f"📄 {resume.name}"):

            st.text_area(
                "Extracted Resume",
                resume_text,
                height=250
            )

# Resume Analysis
if job_description_text and resumes:

    st.markdown("---")
    st.header("🎯 Resume Analysis Results")

    for resume in resumes:

        resume_text = extract_text_from_pdf(resume)

        # Resume Match
        match_score = calculate_match_score(
            job_description_text,
            resume_text
        )

        # ATS Score
        ats_score, matched_skills, missing_skills = calculate_ats_score(
            job_description_text,
            resume_text
        )

        st.subheader(f"📄 {resume.name}")

        st.progress(match_score / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🎯 Resume Match",
                f"{match_score}%"
            )

        with col2:
            st.metric(
                "⭐ ATS Score",
                f"{ats_score}/100"
            )

        st.markdown("### ✅ Matched Skills")

        if matched_skills:
            st.success(", ".join(matched_skills))
        else:
            st.warning("No matched skills found.")

        st.markdown("### ❌ Missing Skills")

        if missing_skills:
            st.error(", ".join(missing_skills))
        else:
            st.success("No missing skills!")

        st.markdown("### 💼 Hiring Recommendation")

        if ats_score >= 80:
            recommendation = "Highly Recommended"
            st.success("⭐ Excellent Candidate — Highly Recommended")

        elif ats_score >= 60:
            recommendation = "Recommended"
            st.info("👍 Good Candidate — Consider for Interview")

        elif ats_score >= 40:
            recommendation = "Needs Improvement"
            st.warning("⚠ Average Candidate — Needs Skill Improvement")

        else:
            recommendation = "Not Recommended"
            st.error("❌ Not Recommended")

        st.markdown("---")

        # AI Resume Review
        st.subheader("🤖 AI Resume Review")

        analysis = ""

        with st.spinner("Gemini AI is analyzing the resume..."):

            try:
                analysis = analyze_resume(resume_text)
                st.markdown(analysis)

            except Exception as e:
                st.error(f"AI Analysis Failed: {e}")

        st.markdown("---")

        # Generate PDF Report
        pdf_file = f"{resume.name}_Report.pdf"

        try:

            generate_pdf(
                pdf_file,
                resume.name,
                match_score,
                ats_score,
                recommendation,
                matched_skills,
                missing_skills,
                analysis
            )

            with open(pdf_file, "rb") as pdf:

                st.download_button(
                    label="📄 Download AI Report",
                    data=pdf,
                    file_name=pdf_file,
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"PDF Generation Failed: {e}")

        st.markdown("---")