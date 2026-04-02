import random
from db import SessionLocal
from models import Student, Course

def create_courses():
    session = SessionLocal()
    titles = ["Math", "Physics", "Biology", "History", "Programming"]
    courses = [Course(title=t) for t in titles]
    session.add_all(courses)
    session.commit()
    session.close()

def seed_students():
    session = SessionLocal()
    courses = session.query(Course).all()

    for i in range(1, 21):
        s = Student(
            name=f"Student_{i}",
            age=random.randint(18, 25),
            courses=random.sample(courses, random.randint(1, 3)),
        )
        session.add(s)

    session.commit()
    session.close()

def add_student(name, age, course_title):
    session = SessionLocal()
    course = session.query(Course).filter_by(title=course_title).first()

    student = Student(name=name, age=age)
    student.courses.append(course)

    session.add(student)
    session.commit()
    session.close()

def get_all_students():
    session = SessionLocal()
    students = session.query(Student).all()
    session.close()
    return students

def get_students_by_course(title):
    session = SessionLocal()
    course = session.query(Course).filter_by(title=title).first()
    result = course.students if course else []
    session.close()
    return result

def update_student_age(name, new_age):
    session = SessionLocal()
    student = session.query(Student).filter_by(name=name).first()
    student.age = new_age
    session.commit()
    session.close()

def delete_student(name):
    session = SessionLocal()
    student = session.query(Student).filter_by(name=name).first()
    session.delete(student)
    session.commit()
    session.close()