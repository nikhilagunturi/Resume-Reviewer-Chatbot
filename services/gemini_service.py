import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

# Load .env (for local development)
load_dotenv()

# Read API key from .env first, then Streamlit Secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY", None)

# Create Gemini client
client = genai.Client(api_key=api_key)


def review_resume(resume_text):

    # -------------------------------
    # STEP 1: Document Type Detection
    # -------------------------------

    check_prompt = f"""
You are a document classifier.

Analyze the uploaded document and classify it.

Reply with ONLY one word from these options:

RESUME
ACADEMIC_TRANSCRIPT
OTHER

Document:
{resume_text}
"""

    try:
        check_response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=check_prompt
        )

        document_type = check_response.text.strip().upper()

    except ClientError:
        return """
## AI Service Temporarily Unavailable

The AI Resume Analyzer is temporarily unavailable.

This may happen because:

• The Gemini API usage limit has been reached.
• The AI service is temporarily unavailable.
• There is a temporary connection issue.

Please try again after some time.

Thank you for your patience.
"""

    except Exception:
        return """
## AI Service Temporarily Unavailable

An unexpected error occurred while connecting to the AI service.

Please try again later.
"""

    # -------------------------------
    # STEP 2: Reject Non-Resume Files
    # -------------------------------

    if document_type != "RESUME":

        return f"""
# ⚠ Document Type Detection

TYPE: {document_type}

# Message

This document is not a professional resume.

Please upload a proper resume containing:

- Contact Information
- Professional Summary
- Technical Skills
- Projects
- Experience
- Education
"""

    # -------------------------------
    # STEP 3: Resume Analysis
    # -------------------------------

    prompt = f"""
    ...
    """   # Keep your existing prompt exactly as it is.

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except ClientError:
        return """
## AI Service Temporarily Unavailable

The AI Resume Analyzer is temporarily unavailable.

This may happen because:

• The Gemini API usage limit has been reached.
• The AI service is temporarily unavailable.
• There is a temporary connection issue.

Please try again after some time.

Thank you for your patience.
"""

    except Exception:
        return """
## AI Service Temporarily Unavailable

An unexpected error occurred while generating the resume analysis.

Please try again later.
"""