# 🤖 AI Resume Analyser

An AI-powered Resume Analyser built using **Python**, **Streamlit**, and **Google Gemini API**. The application analyzes uploaded PDF resumes and provides an ATS-style evaluation, highlighting strengths, weaknesses, and actionable suggestions for improvement.

## 🌐 Live Demo

🔗 https://resume-reviewer-chatbot-2bya5lkjfioxuxezetnvak.streamlit.app

---

## 📌 Project Overview

Recruiters spend only a few seconds reviewing each resume. This project helps job seekers improve their resumes by providing AI-generated feedback instantly.

Users can upload a PDF resume and receive:

- ATS Score
- Resume Summary
- Strengths
- Weaknesses
- Improvement Suggestions
- Overall Feedback

---

## ✨ Features

- 📄 Upload PDF resumes
- 🤖 AI-powered resume analysis using Gemini
- 📊 ATS-style scoring
- 💡 Personalized improvement suggestions
- ⚡ Fast and interactive Streamlit interface
- 🌍 Deployed on Streamlit Cloud

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Application |
| Google Gemini API | AI Resume Analysis |
| PyMuPDF | PDF Text Extraction |
| dotenv | Environment Variables |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
AI-Resume-Analyser/
│
├── app.py
├── requirements.txt
├── services/
│   └── gemini_service.py
├── utils/
│   └── pdf_reader.py
├── screenshots/
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/nikhilagunturi/AI-Resume-Analyser.git
```

Move into the project

```bash
cd AI-Resume-Analyser
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Resume Analysis

![Resume Analysis](screenshots/analysis.png)

---

## 🚀 Future Enhancements

- Resume & Job Description Matching
- Skill Gap Analysis
- Downloadable PDF Reports
- Support for DOCX Files
- Multiple Resume Comparison
- User Authentication

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Python Development
- Prompt Engineering
- Google Gemini API
- Streamlit Application Development
- PDF Processing
- Git & GitHub
- Deploying Applications on Streamlit Cloud

---

## 👩‍💻 Author

**Nikhila Gunturi**

B.Tech CSE (AI & ML)

Mohan Babu University

GitHub:
https://github.com/nikhilagunturi

---

## ⭐ If you found this project useful, consider giving it a Star!