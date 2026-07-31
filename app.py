import streamlit as st
import re

from utils.report_generator import create_pdf_report
from utils.pdf_reader import extract_text_from_pdf
from services.gemini_service import review_resume


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.caption("Version: c3b39fc - UI updated")


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("AI Resume Analyzer")
st.caption("Professional ATS Evaluation and Recruiter Feedback")

st.divider()


# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully.")

    resume_text = extract_text_from_pdf(uploaded_file)

    # --------------------------------------------------
    # View Extracted Resume
    # --------------------------------------------------

    with st.expander("View Extracted Resume"):

        st.text_area(
            label="",
            value=resume_text,
            height=300
        )

    # --------------------------------------------------
    # Analyze Button
    # --------------------------------------------------

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume..."):

            review = review_resume(resume_text)

        # --------------------------------------------------
        # AI Service Error Handling
        # --------------------------------------------------

        if "AI Service Temporarily Unavailable" in review:

            st.error("AI Service Temporarily Unavailable")

            st.info(
                "The AI service is temporarily unavailable due to API usage limits "
                "or a temporary service issue. Please try again later."
            )

            st.markdown(review)

            st.stop()

        st.success("Analysis completed successfully.")

        # --------------------------------------------------
        # Detect Non-Resume Documents
        # --------------------------------------------------

        if "DOCUMENT_TYPE: OTHER" in review:

            st.warning(
                "The uploaded document does not appear to be a professional resume."
            )

            st.markdown(review)

        else:

            # --------------------------------------------------
            # Extract Scores
            # --------------------------------------------------

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
                    "Resume Score",
                    resume_score.group(1) + "/100"
                    if resume_score else "N/A"
                )

            with col2:

                st.metric(
                    "ATS Score",
                    ats_score.group(1) + "/100"
                    if ats_score else "N/A"
                )

            st.divider()

            # --------------------------------------------------
            # Resume Analysis Report
            # --------------------------------------------------

            st.subheader("Resume Analysis Report")

            clean_review = review.replace("DOCUMENT_TYPE: RESUME", "").strip()
            st.markdown(clean_review)

            st.divider()

            # --------------------------------------------------
            # Download PDF Report
            # --------------------------------------------------

            pdf_file = create_pdf_report(clean_review)

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name="AI_Resume_Analysis_Report.pdf",
                    mime="application/pdf"
                )