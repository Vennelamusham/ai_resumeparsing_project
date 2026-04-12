# AI Resume Analyzer (MLOps Project)

## 🔹 Description

This project analyzes a resume and compares it with a job description to extract skills and calculate match percentage.

## 🔹 Features

* Extracts skills from resume
* Matches with job description
* Returns match percentage
* Built using Flask API

## 🔹 Tech Stack

* Python
* Flask
* NLP (basic processing)
* Git & GitHub

## 🔹 API Endpoint

GET /analyze-file

## 🔹 Output Example

{
"extracted_skills": ["java", "sql"],
"match_percentage": 20.66
}

## 🔹 How to Run

1. pip install -r requirements.txt
2. python app.py
3. Open: http://127.0.0.1:5000/analyze-file
