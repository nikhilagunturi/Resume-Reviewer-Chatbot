import streamlit as st
import re

from utils.report_generator import create_pdf_report
from utils.pdf_reader import extract_text_from_pdf
from services.gemini_service import review_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("📄 AI Resume Analyzer")
st.caption(
    "AI-powered ATS evaluation and recruiter feedback using Gemini"
)

st.divider()


# -----------------------------
# Upload Resume
# -----------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Your Resume (PDF)",
    type=["pdf"]
)


if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)


    # Show extracted text

    with st.expander("📄 View Extracted Resume Text"):

        st.text_area(
            "",
            resume_text,
            height=300
        )


    if st.button("🚀 Analyze Resume"):


        with st.spinner("🤖 AI is reviewing your resume..."):

            review = review_resume(resume_text)


        st.success("✅ Analysis Completed!")


        # -----------------------------
        # Detect Non-Resume Documents
        # -----------------------------

        if "Document Type Detection" in review:

            st.warning(
                "⚠️ This does not appear to be a professional resume."
            )

            st.markdown(review)


        else:


            # -----------------------------
            # Extract Scores
            # -----------------------------

            resume_score = re.search(
                r"Overall Resume Score.*?(\d+)/100",
                review,
                re.S
            )


            ats_score = re.search(
                r"ATS Score.*?(\d+)/100",
                review,
                re.S
            )


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "📊 Resume Score",
                    resume_score.group(1) + "/100"
                    if resume_score else "N/A"
                )


            with col2:

                st.metric(
                    "🤖 ATS Score",
                    ats_score.group(1) + "/100"
                    if ats_score else "N/A"
                )


            st.divider()


            # -----------------------------
            # Display AI Analysis
            # -----------------------------

            st.markdown(review)


            # -----------------------------
            # Generate PDF Report
            # -----------------------------

            pdf_file = create_pdf_report(review)


            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📥 Download AI Report PDF",
                    data=file,
                    file_name="AI_Resume_Analysis_Report.pdf",
                    mime="application/pdf"
                )