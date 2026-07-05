import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="Email Center",
    page_icon="📧",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📧 Email Center")
st.write("Send interview invitations or rejection emails to candidates.")

st.markdown("---")

candidate_name = st.text_input("Candidate Name")
candidate_email = st.text_input("Candidate Email")

email_type = st.selectbox(
    "Select Email Type",
    [
        "Interview Invitation",
        "Rejection Email"
    ]
)

st.markdown("---")

if st.button("📨 Send Email"):

    sender_email = st.secrets["EMAIL"]
sender_password = st.secrets["APP_PASSWORD"]

    if email_type == "Interview Invitation":

        subject = "Interview Invitation | Veltrix AI"

        body = f"""
Dear {candidate_name},

Congratulations!

Based on our AI-powered recruitment process, you have been shortlisted for the interview round.

Our HR team will contact you shortly.

Best Regards,
HR Team
Veltrix AI
"""

    else:

        subject = "Application Update | Veltrix AI"

        body = f"""
Dear {candidate_name},

Thank you for applying.

After careful evaluation, we have decided to move forward with other candidates.

We appreciate your interest and wish you success.

Regards,
HR Team
Veltrix AI
"""

    try:

        msg = MIMEMultipart()

        msg["From"] = sender_email
        msg["To"] = candidate_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.send_message(msg)

        server.quit()

        st.success("✅ Email Sent Successfully!")

    except Exception as e:

        st.error(f"Error: {e}")