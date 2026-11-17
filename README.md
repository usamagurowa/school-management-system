# 🏫 Full-Stack School Management System

A production-grade, full-stack web application designed to manage students, courses, and relational academic enrollments. Built as part of an Industrial Training capstone project to demonstrate proficiency in backend API design, database modeling, and frontend integration.

---

## 🚀 Tech Stack

* **Frontend:** HTML5, CSS3 (Dark-Mode & Neon Glow UI), Asynchronous JavaScript (`Fetch API`)
* **Backend:** Python, Flask, Flask-CORS
* **Database:** MySQL, Relational Database Design (`mysql-connector-python`)

---

## ✨ Features

* **Complete CRUD Operations:** Add, view, and manage student records and academic courses dynamically.
* **Relational Database Modeling:** Enforces foreign key constraints across `students`, `courses`, and `student_enrollments` tables.
* **Advanced SQL Joins:** Custom backend endpoints utilizing SQL `JOIN` queries to fetch cross-table relational records.
* **Responsive Dark-Mode Interface:** A custom slate-themed UI designed with modern developer aesthetic standards.

---

## 🛠️ Getting Started Locally

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/usamagurowa/school-management-system.git
cd school-management-system
\`\`\`

### 2. Set Up the Python Virtual Environment
\`\`\`bash
python -m venv venv
# On Windows:
venv\Scripts\activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install flask flask-cors mysql-connector-python requests
\`\`\`

### 4. Configure MySQL Database
Run your MySQL schema script to create the database and tables (`students`, `courses`, `student_enrollments`), and update your local credentials in `app.py`.

### 5. Run the Application
Start the Flask backend server:
\`\`\`bash
python app.py
\`\`\`
Then, open **`index.html`** in your browser to launch the live dashboard!

---

## 👤 Author
**Usama Hassan**  
* Computer Science Major & Software Developer  
* GitHub: [@usamagurowa](https://github.com/usamagurowa)