import requests

url = "http://127.0.0.1:5000/api/students"
payload = {
    "roll_number": "CS/2026/001",
    "full_name": "Usama Hassan",
    "email": "usama@example.com",
    "current_gpa": 4.80
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())