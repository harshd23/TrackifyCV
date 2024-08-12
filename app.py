import os
import streamlit as st

# from PIL import Image
# import pdf2image

import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# import base64
# import io

import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def getModelResponse(input):
    model = GoogleGenerativeAI(model='models/gemini-1.5-pro')
    response = model.invoke(input)
    return response


def inputPDFSetup(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


st.set_page_config(page_title="TrackifyCV")
st.header("TrackifyCV 📑🔍")
job_description = st.text_area(label="Job Description", placeholder="PLease provide Job Description here...", height=10, key="input")
uploaded_file = st.file_uploader("Upload your Resume in PDF format...", type=["pdf"], help="Please upload a PDF file")


if uploaded_file is not None:
    st.write("Resume Uploaded Successfully!!!✅")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("What are the Keywords That are Missing")
submit4 = st.button("Percentage match")


input_prompt1 = PromptTemplate.from_template(
    """
    As an experienced Technical Human Resource Manager,your task is to evaluate the provided resume against the job description.
    Please provide a professional assessment of how well the candidate's profile aligns with the role. 
    Specifically, highlight the strengths and weaknesses of the applicant in relation to the job requirements outlined.
    Resume:{text}
    Job Description: {job_description}
    
    Response:
""")

input_prompt2 = PromptTemplate.from_template(
    """
    As a Technical Human Resource Manager with expertise in data science, your role is to review the resume in the context of the provided job description.
    Please provide your insights on the candidate's suitability for the role from an HR perspective. 
    Additionally, offer recommendations for enhancing the candidate’s skills and identify areas where improvement is needed.
    Resume:{text}
    Job Description: {job_description}
    
    Response:
""")
 
input_prompt3 = PromptTemplate.from_template(
    """
    As a skilled ATS (Applicant Tracking System) scanner with expertise in data science and ATS functionality, your task is to evaluate the resume against the provided job description.
    Assess the compatibility of the resume with the role from a Human Resource perspective. 
    Identify any missing keywords and provide recommendations for enhancing the candidate's skills. 
    Additionally, highlight areas where further development is needed.
    Resume: {text}
    Job Description: {job_description}
    
    Response:
""")

input_prompt4 = PromptTemplate.from_template(
    """
    As a skilled ATS (Applicant Tracking System) scanner with deep expertise in data science and ATS functionality,  your task is to evaluate the resume against the provided job description.
    First, provide the percentage match between the resume and the job description. 
    Next, list any missing keywords. Finally, offer your overall assessment and final thoughts on the resume’s suitability for the role.
    Resume: {text}
    Job Description: {job_description}
    
    Response:
""")


if submit1:
    if uploaded_file is not None:
        text = inputPDFSetup(uploaded_file)
        response = getModelResponse(input_prompt1.format(text=text, job_description=job_description))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        text = inputPDFSetup(uploaded_file)
        response = getModelResponse(input_prompt2.format(text=text, job_description=job_description))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        text = inputPDFSetup(uploaded_file)
        response = getModelResponse(input_prompt3.format(text=text, job_description=job_description))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        text = inputPDFSetup(uploaded_file)
        response = getModelResponse(input_prompt4.format(text=text, job_description=job_description))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")