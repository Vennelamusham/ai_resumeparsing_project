# job_matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity_score = cosine_similarity(vectors[0], vectors[1])

    return round(similarity_score[0][0] * 100, 2)
