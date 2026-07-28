import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from services.gemini_service import review_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption("Get ATS Score, Resume Score & Recruiter Feedback")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    with st.expander("📄 View Extracted Resume"):
        st.text_area(
            "",
            resume_text,
            height=300
        )

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            review = review_resume(resume_text)

        st.success("Analysis Complete ✅")

        st.markdown(review)