# 🚀 Smart ATS: Resume Optimizer using Gemini Pro

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini API](https://img.shields.io/badge/Gemini%20Pro-LLM-green)
![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

📋 Overview
The **Smart ATS (Applicant Tracking System) Optimizer** is an intelligent career tool designed to help job seekers crack the automated resume screening process.

Built using **Google's Gemini Pro LLM** and **LangChain**, this application acts as a personalized Technical Recruiter. It evaluates your resume against any Job Description (JD) to provide a precise match percentage, identifies missing technical keywords, and generates a tailored profile summary to boost your interview chances.

🌟 Key Features
* **Semantic Analysis:** Goes beyond simple keyword matching by using the Gemini Pro LLM to understand the context of your experience.
* **Instant ATS Score:** Provides a percentage match (0-100%) indicating how well your profile fits the specific role.
* **Skill Gap Analysis:** Clearly lists the critical skills and keywords missing from your resume that the JD demands.
* **Profile Summarization:** Generates a professional, keyword-optimized summary to add to the top of your resume.
* **PDF Support:** Seamlessly parses text from PDF resumes.

🛠️ Tech Stack
* **LLM:** Google Gemini 1.5 Pro (via `langchain-google-genai`)
* **Framework:** Streamlit (for the Web UI)
* **Orchestration:** LangChain
* **File Handling:** PyPDF2
* **Environment:** Python-dotenv

⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/smart-ats-optimizer.git](https://github.com/your-username/smart-ats-optimizer.git)
cd smart-ats-optimizer
