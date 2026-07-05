import streamlit as st

st.set_page_config(
    page_title="About Veltrix AI",
    page_icon="ℹ️",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>🚀 About Veltrix AI</h1>
    <p>AI-Powered Recruitment Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:

    st.header("🎯 Our Mission")

    st.write("""
Veltrix AI is an intelligent recruitment platform designed to simplify and automate the hiring process.

It enables recruiters to analyze resumes, calculate ATS scores, rank candidates, generate AI-powered hiring insights, and communicate with applicants—all from one platform.
""")

    st.header("✨ Key Features")

    st.markdown("""
- 📄 AI Resume Analysis
- ⭐ ATS Score Calculation
- 🎯 Resume Matching
- 🏆 Candidate Ranking
- 📊 Interactive Dashboard
- 📈 Recruitment Analytics
- 🤖 Google Gemini AI Integration
- 📧 Email Automation
- 📄 PDF Report Generation
- 📥 CSV Report Export
""")

with col2:

    st.info("""
### 📦 Version

**Veltrix AI v1.0**

---

### 🤖 AI Model

Google Gemini 2.5 Flash

---

### 💻 Framework

Streamlit

---

### 📊 Machine Learning

TF-IDF

Cosine Similarity

Scikit-learn

---

### 📄 Reports

PDF

CSV
""")

st.markdown("---")

st.header("🛠 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("""
🐍 Python

Streamlit

Pandas
""")

with tech2:
    st.success("""
🤖 AI

Google Gemini

Prompt Engineering
""")

with tech3:
    st.success("""
📊 ML

TF-IDF

Cosine Similarity

Scikit-learn
""")

with tech4:
    st.success("""
📈 Visualization

Plotly

ReportLab

SMTP Email
""")

st.markdown("---")

st.header("🚀 Future Enhancements")

st.markdown("""
- 🔐 Recruiter Login System

- 👥 Candidate Portal

- 📅 Interview Scheduling

- ☁️ Cloud Database

- 🎥 Video Interview Analysis

- 📱 Mobile Responsive UI

- 🌍 Multi-language Support

- 🧠 AI Candidate Recommendation
""")

st.markdown("---")

st.success("""
### 💙 Developed using Python, Streamlit, Machine Learning, and Google Gemini AI.

**Veltrix AI** aims to make recruitment faster, smarter, and more efficient.
""")