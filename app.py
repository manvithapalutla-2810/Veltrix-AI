import streamlit as st

st.set_page_config(
    page_title="Veltrix AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# Load CSS
# ==========================

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================
# Hero Section
# ==========================

st.markdown("""
<div class="hero">
    <h1>🚀 Veltrix AI</h1>
    <p>AI-Powered Recruitment Intelligence Platform</p>
    <p>Analyze • Match • Rank • Hire Better Talent</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# Platform Overview
# ==========================

st.markdown("<div class='section-title'>Platform Overview</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Resume Analysis", "AI Powered")

with col2:
    st.metric("ATS Engine", "Enabled")

with col3:
    st.metric("Candidate Ranking", "Ready")

with col4:
    st.metric("Gemini AI", "Integrated")

st.markdown("---")

# ==========================
# Feature Cards
# ==========================

st.markdown("<div class='section-title'>Core Features</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="card">
<h3>📄 Resume Screening</h3>
<p>Automatically extract resume information, calculate ATS score and evaluate candidate quality.</p>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<h3>🏆 Candidate Ranking</h3>
<p>Rank applicants intelligently using Resume Match, ATS Score and Final Score.</p>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<h3>🤖 AI Resume Review</h3>
<p>Google Gemini generates recruiter-style feedback, interview questions and improvement tips.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
<div class="card">
<h3>📊 Recruiter Dashboard</h3>
<p>Interactive charts, KPIs and hiring insights for recruiters.</p>
</div>
""", unsafe_allow_html=True)

with c5:
    st.markdown("""
<div class="card">
<h3>📄 PDF Reports</h3>
<p>Generate downloadable AI-powered recruitment reports for every candidate.</p>
</div>
""", unsafe_allow_html=True)

with c6:
    st.markdown("""
<div class="card">
<h3>📧 Email Automation</h3>
<p>Send interview invitations and hiring updates directly from the platform.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================
# How It Works
# ==========================

st.markdown("<div class='section-title'>How Veltrix AI Works</div>", unsafe_allow_html=True)

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.info("📂\n\nUpload Job Description")

with step2:
    st.info("📄\n\nUpload Candidate Resumes")

with step3:
    st.info("🤖\n\nAI analyzes every resume")

with step4:
    st.info("🏆\n\nRank & Hire the Best Candidate")

st.markdown("---")

# ==========================
# Technology Stack
# ==========================

st.markdown("<div class='section-title'>Technology Stack</div>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("🐍 Python")

with t2:
    st.success("⚡ Streamlit")

with t3:
    st.success("🧠 Gemini AI")

with t4:
    st.success("📊 Plotly")

st.markdown("---")

# ==========================
# Footer
# ==========================

st.caption("© 2026 Veltrix AI • Intelligent Recruitment Platform")