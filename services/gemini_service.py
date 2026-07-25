import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def review_resume(resume_text):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume and provide:

1. Overall Summary
2. Strengths
3. Weaknesses
4. Suggestions for Improvement

Resume:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text