# resume_parser.py

import PyPDF2

def extract_text(file):
    text = ""
    pdf = PyPDF2.PdfReader(file)
    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()