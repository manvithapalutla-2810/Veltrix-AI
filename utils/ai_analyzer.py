from google import genai
import streamlit as st

# Use Streamlit Secrets when deployed, otherwise use local config.py
try:
    api_key = st.secrets["API_KEY"]
except Exception:
    import config
    api_key = config.API_KEY

client = genai.Client(api_key=api_key)


def analyze_resume(resume_text):

    prompt = f"""
You are a Senior Technical HR Recruiter with over 15 years of experience in hiring software engineers, AI engineers, data analysts, and data scientists.

Analyze the following resume professionally.

Return the result in **Markdown**.

Follow EXACTLY this structure.

# Executive Summary

Write a professional summary of the candidate in 3-4 lines.

# Overall Candidate Rating

Give a rating out of **10**.

# Experience Level

Choose ONE:
- Fresher
- Junior
- Mid-Level
- Senior

Explain briefly.

# Technical Skills

List all important technical skills found in the resume.

# Soft Skills

List important soft skills.

# Strengths

Mention at least 5 strengths.

# Weaknesses

Mention at least 5 weaknesses.

# Missing Skills

Mention important missing skills that would improve the candidate's profile.

# Recommended Job Roles

Suggest 3 suitable job roles.

# Hiring Decision

Choose ONE:
- Highly Recommended
- Recommended
- Needs Improvement
- Not Recommended

Explain your decision.

# Interview Questions

Generate 5 technical interview questions based on the candidate's resume.

# Resume Improvement Suggestions

Provide practical suggestions to improve the resume for better ATS performance and recruiter appeal.

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text