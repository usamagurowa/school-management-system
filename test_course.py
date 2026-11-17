import requests

# Test adding a new course
url = "http://127.0.0.1:5000/api/courses"
payload = {
    "course_code": "CSC301",
    "course_name": "Software Engineering",
    "credits": 3
}

response = requests.post(url, json=payload)
print("Add Course Status:", response.status_code)
print("Add Course Response:", response.json())

# Test fetching all courses
get_response = requests.get(url)
print("Get Courses Response:", get_response.json())