# resume_parser.py

import PyPDF2

def extract_skills(file):
    text = ""
    pdf = PyPDF2.PdfReader(file)
    for page in pdf.pages:
        if page.extract_skills():
            text += page.extract_skills()
    return text.lower()