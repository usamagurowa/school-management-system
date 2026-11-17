import requests

url = "http://127.0.0.1:5000/api/enrollments"
payload = {
    "student_id": 1,
    "course_id": 1
}

response = requests.post(url, json=payload)
print("Enrollment Status:", response.status_code)
print("Enrollment Response:", response.json())