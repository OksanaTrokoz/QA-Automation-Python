from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

DATABASE_URL = "postgresql://user:1@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship("Student", secondary=student_course, back_populates="courses")

Base.metadata.create_all(engine)
session = Session()

titles = ["Math", "Physics", "Biology", "History", "Programming"]
courses = [Course(title=t) for t in titles]
session.add_all(courses)
session.commit()


for i in range(1, 21):
    s = Student(
        name=f"Student_{i}",
        age=random.randint(18, 25),
        courses=random.sample(courses, random.randint(1, 3)),
    )
    session.add(s)
session.commit()


course = session.query(Course).filter_by(title="Math").first()
new_student = Student(name="New_Student", age=22)
new_student.courses.append(course)
session.add(new_student)
session.commit()


student = session.query(Student).filter_by(name="Student_1").first()
student.age = 30
session.commit()


student_to_delete = session.query(Student).filter_by(name="Student_2").first()
session.delete(student_to_delete)
session.commit()