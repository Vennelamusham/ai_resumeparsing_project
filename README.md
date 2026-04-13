# AI Resume Matcher

A web application that matches a resume with a job description using Natural Language Processing (NLP) and Machine Learning techniques.

## Features

- Upload Resume (PDF)
- Upload Job Description (TXT)
- Extract text from documents
- Calculate similarity score
- Display match percentage instantly

## Tech Stack

- Python
- Flask
- Scikit-learn
- PyPDF2
- HTML, CSS, JavaScript
- Render (Deployment)

## How It Works

1. Extract text from resume PDF using PyPDF2  
2. Extract text from job description  
3. Convert both texts into vectors using TF-IDF  
4. Compute similarity using cosine similarity  
5. Return match score as percentage  

## Screenshots
### UI


### Result Output
![Result](screenshots/result.png)

## Live Demo
- 🔗 API: https://ai-resumeparsing-project-6.onrender.com

## 📂 Project Structure
