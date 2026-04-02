from db import Base, engine
from services import (
    create_courses,
    seed_students,
    add_student,
    update_student_age,
    delete_student,
)

Base.metadata.create_all(engine)

create_courses()
seed_students()

add_student("New_Student", 22, "Math")
update_student_age("Student_1", 30)
delete_student("Student_2")