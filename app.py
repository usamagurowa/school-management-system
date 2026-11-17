from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '3164',  # Replace with your MySQL root password
    'database': 'school_management_db'
}

# Test route to check if server is running
@app.route('/')
def home():
    return jsonify({"message": "School Management API is running!"})

# GET route: Fetch all students from MySQL
@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# POST route: Add a new student to MySQL
@app.route('/api/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        roll_number = data.get('roll_number')
        full_name = data.get('full_name')
        email = data.get('email')
        current_gpa = data.get('current_gpa', 0.00)

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO students (roll_number, full_name, email, current_gpa) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (roll_number, full_name, email, current_gpa))
        conn.commit()
        
        return jsonify({"message": "Student added successfully!", "student_id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
# GET route: Fetch all courses from MySQL
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        return jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# POST route: Add a new course to MySQL
@app.route('/api/courses', methods=['POST'])
def add_course():
    try:
        data = request.get_json()
        course_code = data.get('course_code')
        course_name = data.get('course_name')
        credits = data.get('credits', 3)

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO courses (course_code, course_name, credits) VALUES (%s, %s, %s)"
        cursor.execute(query, (course_code, course_name, credits))
        conn.commit()
        
        return jsonify({"message": "Course added successfully!", "course_id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
# POST route: Enroll a student in a course
@app.route('/api/enrollments', methods=['POST'])
def enroll_student():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        course_id = data.get('course_id')

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO student_enrollments (student_id, course_id) VALUES (%s, %s)"
        cursor.execute(query, (student_id, course_id))
        conn.commit()
        
        return jsonify({"message": "Student successfully enrolled in course!", "enrollment_id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
# GET route: Fetch all student enrollments with student and course details
@app.route('/api/enrollments', methods=['GET'])
def get_enrollments():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT se.enrollment_id, s.full_name, s.roll_number, c.course_code, c.course_name 
            FROM student_enrollments se
            JOIN students s ON se.student_id = s.student_id
            JOIN courses c ON se.course_id = c.course_id
        """
        cursor.execute(query)
        enrollments = cursor.fetchall()
        return jsonify(enrollments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
if __name__ == '__main__':
    app.run(debug=True, port=5000)