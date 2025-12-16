import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(page_title="Resume Analysis Tool", layout="wide")

def get_gemini_response(formatted_prompt, api_key):
    """
    Initializes the Gemini model and returns the response.
    """
    if not api_key:
        raise ValueError("API Key is missing.")
    
    # Initialize the model with specific parameters for consistency
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", 
        google_api_key=api_key, 
        temperature=0.3
    )
    
    # specific invoke method for LangChain
    response = llm.invoke(formatted_prompt)
    return response.content

def extract_text_from_pdf(uploaded_file):
    """
    Helper function to extract raw text from a PDF file.
    """
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# System Prompt Template
SYSTEM_PROMPT = """
Act as a Technical Recruiter and ATS expert. 
Evaluate the following resume against the provided job description.

RESUME TEXT:
{resume_text}

JOB DESCRIPTION:
{jd_text}

REQUIREMENTS:
1. Calculate a Match Percentage (0-100%).
2. Identify Missing Keywords (Critical skills present in JD but absent in Resume).
3. Provide a concise Profile Summary and recommendations.

OUTPUT FORMAT (JSON String):
{{"Match": "XX%", "Missing": ["Skill1", "Skill2"], "Summary": "..."}}
"""

# --- Main Application Layout ---

st.title("ATS Resume Analyzer")
st.markdown("Optimize resume content for specific job descriptions using semantic matching.")

# Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Google API Key", type="password")
    st.info("Please provide a valid Google Gemini API key to proceed.")

# Input Section
col1, col2 = st.columns(2)

with col1:
    job_description = st.text_area("Job Description", height=300, placeholder="Paste the JD here...")

with col2:
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

# Action Button
if st.button("Analyze Resume"):
    if not api_key:
        st.error("Error: API Key is required.")
    elif not uploaded_resume or not job_description:
        st.error("Error: Please provide both a resume and a job description.")
    else:
        try:
            with st.spinner("Processing document..."):
                # 1. Extract Text
                resume_text = extract_text_from_pdf(uploaded_resume)
                
                # 2. Format Prompt
                formatted_prompt = SYSTEM_PROMPT.format(
                    resume_text=resume_text, 
                    jd_text=job_description
                )
                
                # 3. Get Response
                response = get_gemini_response(formatted_prompt, api_key)
                
                # 4. Display Results
                st.subheader("Analysis Report")
                st.write(response)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")