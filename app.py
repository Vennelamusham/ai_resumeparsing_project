from flask import Flask, jsonify
from resume_parser import extract_skills
from job_matcher import calculate_match

app = Flask(__name__)

@app.route("/analyze-file", methods=["GET"])
def analyze_from_file():
    # Read resume and job description from files
    resume_text = open("sample_data/resume.txt").read()
    job_text = open("sample_data/job_description.txt").read()

    skills = extract_skills(resume_text)
    match_score = calculate_match(resume_text, job_text)

    return jsonify({
        "extracted_skills": skills,
        "match_percentage": match_score
    })

if __name__ == "__main__":
    app.run(debug=True)


