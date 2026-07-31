import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key from .env first, then Streamlit Secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

# Create Gemini client
client = genai.Client(api_key=api_key)


def review_resume(resume_text):

    prompt = f"""
You are a Senior HR Recruiter, ATS Expert, and Technical Hiring Manager with over 15 years of experience.

FIRST TASK:

Determine whether the uploaded document is a professional resume.

A professional resume normally contains:
- Contact Information
- Professional Summary
- Skills
- Projects
- Experience
- Education

If the uploaded document is NOT a professional resume
(for example: academic transcript, marks memo, certificate,
question paper, ID card, invoice, or any other document),

respond ONLY with:

DOCUMENT_TYPE: OTHER

This document is not a professional resume.

Please upload a valid professional resume.

----------------------------------------------------

If the uploaded document IS a professional resume,

start your response with:

DOCUMENT_TYPE: RESUME

Then continue with the complete resume analysis exactly in the format below.

IMPORTANT RULES:

- Keep the response under 300 words.
- Do NOT rewrite the resume.
- Give concise recruiter-style feedback.
- Use bullet points wherever possible.
- Return the report in plain text.
- Do NOT use emojis.
- Do NOT use Markdown headings.
- Use bold text ONLY for section titles.

Resume:
{resume_text}


**Overall Resume Score**
Score: XX/100

**ATS Score**
Score: XX/100

**Professional Summary**
(2-3 lines)

**Skills Identified**
- Skill 1
- Skill 2
- Skill 3

**Missing Skills**
- Skill 1
- Skill 2
- Skill 3

**Strengths**
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

**Areas for Improvement**
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

**ATS Keyword Analysis**

Matched Keywords:
- Keyword 1
- Keyword 2

Missing Keywords:
- Keyword 1
- Keyword 2

Keyword Match: XX%

**Section Evaluation**

Professional Summary: X/10

Technical Skills: X/10

Projects: X/10

Experience: X/10

Education: X/10

**Grammar and Formatting**

Grammar Score: X/10

Formatting Score: X/10

Formatting Issues:
- Issue 1
- Issue 2

Grammar Issues:
- Issue 1
- Issue 2

**Recruiter Recommendation**

Choose ONLY one:

- Hire
- Shortlist
- Maybe
- Reject

**Recommended Improvements**

1.
2.
3.
4.
5.

**Final Verdict**
One concise paragraph.
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:

        error = str(e)

        if (
            "RESOURCE_EXHAUSTED" in error
            or "429" in error
            or "quota" in error.lower()
        ):
            return """
AI Service Temporarily Unavailable

The AI Resume Analyzer has reached today's API usage limit.

Please try again later.

Thank you for your patience.
"""

        return f"""
AI Service Temporarily Unavailable

An unexpected error occurred.

Error:
{error}
"""