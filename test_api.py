import requests

url = "http://127.0.0.1:5000/analyze"

data = {
    "resume": "Python, data structures, machine learning",
    "job": "Looking for Python engineer with DSA and ML"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
