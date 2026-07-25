import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Reviewer")
st.subheader("Built with Python + Streamlit + Gemini")

st.write("Upload your resume and receive AI-powered feedback.")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )