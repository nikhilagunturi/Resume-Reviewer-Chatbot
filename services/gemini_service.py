import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


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

    check_response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=check_prompt
    )

    document_type = check_response.text.strip().upper()


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

- Contact information
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
You are a Senior HR Recruiter, ATS Expert, and Technical Hiring Manager with over 15 years of experience.

Analyze the following resume professionally.

IMPORTANT RULES:
- Keep the response under 350 words.
- Do NOT rewrite the resume.
- Give concise recruiter-style feedback.
- Use bullet points wherever possible.
- Return ONLY the given format.

Resume:
{resume_text}


# 📊 Overall Resume Score
Score: XX/100


# 🤖 ATS Score
Score: XX/100


# 💻 Skills Identified
- Skill 1
- Skill 2
- Skill 3


# 🚀 Missing Skills
- Skill 1
- Skill 2
- Skill 3


# 💪 Strengths
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5


# ⚠ Weaknesses
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5


# 🔑 ATS Keyword Match

Matched Keywords:
- Keyword 1
- Keyword 2

Missing Keywords:
- Keyword 1
- Keyword 2

Keyword Match: XX%


# 📑 Section Ratings

Professional Summary: X/10

Technical Skills: X/10

Projects: X/10

Experience: X/10

Education: X/10


# 📝 Grammar & Formatting

Grammar Score: X/10

Formatting Score: X/10


Formatting Issues:
- Issue 1
- Issue 2


Grammar Issues:
- Issue 1
- Issue 2


# 👨‍💼 Recruiter Verdict

Choose ONLY one:

- Hire
- Shortlist
- Maybe
- Reject


# 🎯 Top 5 Improvements

1.
2.
3.
4.
5.
"""


    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text