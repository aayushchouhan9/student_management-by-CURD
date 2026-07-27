# 🎓 Student CRUD API

<p align="center">
  <strong>A FastAPI-based REST API for managing student records.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Uvicorn-ASGI-orange" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063" alt="Pydantic">
  <img src="https://img.shields.io/github/license/YOUR_USERNAME/student-crud-fastapi" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/student-crud-fastapi?style=social" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/YOUR_USERNAME/student-crud-fastapi?style=social" alt="GitHub Forks">
</p>

---

## 🚀 Project Overview

**Student CRUD API** is a beginner-friendly REST API built using **Python, FastAPI and Pydantic**.

It allows you to:

```text
➕ CREATE   → Add a student
📖 READ     → View students
✏️ UPDATE   → Modify student information
🗑️ DELETE   → Remove a student
```

The project currently uses a Python list as a temporary in-memory database.

---

# 🌐 Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-crud-fastapi.git
```

### 2️⃣ Enter Project

```bash
cd student-crud-fastapi
```

### 3️⃣ Install Dependencies

```bash
py -m pip install fastapi uvicorn
```

### 4️⃣ Start Server

```bash
py -m uvicorn main:app --reload
```

---

# 🔗 Quick Links

Once the server is running:

| Page          | Link                                       |
| ------------- | ------------------------------------------ |
| 🌐 API Home   | [Open API](http://127.0.0.1:8000/)         |
| 📚 Swagger UI | [Open Swagger](http://127.0.0.1:8000/docs) |
| 📖 ReDoc      | [Open ReDoc](http://127.0.0.1:8000/redoc)  |

> ⚠️ The links above work when your FastAPI server is running locally.

---

# ⚡ API Endpoints

|    Method    | Endpoint                 | Function         |
| :----------: | ------------------------ | ---------------- |
|   🏠 `GET`   | `/`                      | API Home         |
|   ➕ `POST`   | `/students`              | Create Student   |
|   📋 `GET`   | `/students`              | Get All Students |
|   🔍 `GET`   | `/students/{student_id}` | Get Student      |
|   ✏️ `PUT`   | `/students/{student_id}` | Update Student   |
| 🗑️ `DELETE` | `/students/{student_id}` | Delete Student   |

---

# 🧪 API Examples

## ➕ Create Student

```http
POST /students
```

```json
{
    "id": 1,
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}
```

### Response

```json
{
    "message": "Student added successfully",
    "student": {
        "id": 1,
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    }
}
```

---

## 📋 Get All Students

```http
GET /students
```

Example:

```json
{
    "total_students": 1,
    "students": [
        {
            "id": 1,
            "name": "Rahul",
            "age": 21,
            "course": "Python"
        }
    ]
}
```

---

## 🔍 Get Student

```http
GET /students/1
```

---

## ✏️ Update Student

```http
PUT /students/1
```

```json
{
    "id": 1,
    "name": "Rahul Sharma",
    "age": 22,
    "course": "FastAPI"
}
```

---

## 🗑️ Delete Student

```http
DELETE /students/1
```

---

# 📚 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

**Try every API directly from your browser:**

👉 http://127.0.0.1:8000/docs

### ReDoc

Alternative API documentation:

👉 http://127.0.0.1:8000/redoc

---

# 🛠️ Tech Stack

```text
🐍 Python
⚡ FastAPI
📦 Pydantic
🚀 Uvicorn
📚 Swagger UI
🔧 Git & GitHub
```

---

# 📁 Project Structure

```text
student-crud-fastapi/
│
├── main.py
├── .gitignore
└── README.md
```

---

# 💡 Features

* ✅ REST API architecture
* ✅ Complete CRUD operations
* ✅ Pydantic request validation
* ✅ Duplicate ID checking
* ✅ HTTP 404 error handling
* ✅ HTTP 400 error handling
* ✅ Swagger documentation
* ✅ ReDoc documentation
* ✅ Easy local setup
* ✅ Beginner-friendly code

---

# 🔮 Future Improvements

```text
🗄️ MySQL / PostgreSQL Database
🔐 JWT Authentication
👤 User Login & Registration
🔎 Search Students
📊 Filtering & Pagination
🧪 Automated Testing
🎨 React Frontend
☁️ Cloud Deployment
```

---

# 📊 CRUD Flow

```text
                 Student CRUD API
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
     CREATE           READ            UPDATE
     POST              GET              PUT
        │               │               │
        └───────────────┼───────────────┘
                        ↓
                      DELETE
                        │
                       🗑️
```

---

# 👨‍💻 Author

## AAYUSHMAN CHOUHAN

**Python | FastAPI | REST API | Web Development**

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.

<p align="center">
  <strong>Made with ❤️ using Python & FastAPI</strong>
</p>
