from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student CRUD API")


class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


students = []


@app.get("/")
def home():
    return {"message": "Welcome to Student CRUD API"}


@app.post("/students")
def create_student(student: Student):

    for s in students:
        if s.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student)

    return {
        "message": "Student added successfully",
        "student": student
    }


@app.get("/students")
def get_all_students():
    return {
        "total_students": len(students),
        "students": students
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):

    for index, student in enumerate(students):

        if student.id == student_id:
            students[index] = updated_student

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "deleted_student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )