from flask import Flask, request, jsonify
from resume_parser import extract_skills
from job_matcher import calculate_match

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Matcher Running"

@app.route("/match", methods=["POST"])
def match():
    resume_file = request.files['resume']
    job_file = request.files['job']

    resume_text = extract_skills(resume_file)
    job_text = extract_skills(job_file)

    score = calculate_match(resume_text, job_text)

    return jsonify({"match_score": score})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



