import random
import logging
from db import SessionLocal
from models import Student, Course

logger = logging.getLogger(__name__)

def create_courses():
    session = SessionLocal()
    titles = ["Math", "Physics", "Biology", "History", "Programming"]
    courses = [Course(title=t) for t in titles]
    session.add_all(courses)
    session.commit()
    logger.info(f"Created {len(titles)} courses.")
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
    logger.info("Seeded 20 students.")
    session.close()

def add_student(name, age, course_title):
    session = SessionLocal()
    course = session.query(Course).filter_by(title=course_title).first()
    student = Student(name=name, age=age)
    student.courses.append(course)
    session.add(student)
    session.commit()
    logger.info(f"Added student {name} to {course_title}.")
    session.close()

def update_student_age(name, new_age):
    session = SessionLocal()
    student = session.query(Student).filter_by(name=name).first()
    if student:
        student.age = new_age
        session.commit()
        logger.info(f"Updated {name}'s age to {new_age}.")
    session.close()

def delete_student(name):
    session = SessionLocal()
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        logger.info(f"Deleted student {name}.")
    session.close()