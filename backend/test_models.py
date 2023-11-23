#!/usr/bin/python3
"""This runs a test to ensure that all
models have been created properly"""

from app import create_app
from app.models import *
from datetime import date


class TestConfig():
    """Configurations for test database"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = create_app(TestConfig)
# Create all Tables
with app.app_context():
    db.drop_all()
    db.create_all()

# Create some faculties
faculty1 = Faculty(
    name="Engineering",
    description="Engineering the best students")
faculty2 = Faculty(name="Sciences", description="Taking sciences by storm")

with app.app_context():
    db.session.add_all([faculty1, faculty2])


# Create some departments
dept1 = Department(name="ECE", description="Electrical Engineering",
                   hod="Dr Lambe")
dept2 = Department(name="MSE", description="Materials Science Engineering",
                   hod="Dr Kabir")
dept3 = Department(name="MCB", description="Microbiology",
                   hod="Dr Awodele")
dept4 = Department(name="BCH", description="Biochemistry",
                   hod="Dr Kamal")

with app.app_context():
    db.session.add_all([dept1, dept2, dept3, dept4])

faculty1.departments.append(dept1)
faculty1.departments.append(dept2)
print("faculty1 depts:", faculty1.departments)
print(dept1.faculty)

# Create Some students
s1 = Student(
    first_name="Maddock",
    last_name="James",
    matric_number="20/58EC/00878",
    gender="Male",
    email="sc@gmail.com",
    address="73, Kings street",
    dob=date(
        2004,
        3,
        3))
s2 = Student(
    first_name="Jane",
    last_name="Johnson",
    matric_number="20/58EC/00888",
    gender="Female",
    email="jj@gmail.com",
    address="14, maya street",
    dob=date(
        2005,
        12,
        2))
s3 = Student(
    first_name="Willow",
    last_name="Aurthur",
    matric_number="20/58EC/00978",
    gender="Male",
    email="yu@gmail.com",
    address="73, Magic street",
    dob=date(
        2010,
        7,
        7))
s4 = Student(first_name="Han", last_name="Wu", matric_number="20/58EC/00808",
             gender="Male", email="wu@gmail.com", address="72, Kings street",
             dob=date(2002, 5, 11))

with app.app_context():
    db.session.add_all([s1, s2, s3, s4])
print("dept1 depts:", dept1.students)

dept1.students.append(s1)
dept1.students.append(s3)
dept2.students.append(s2)
dept2.students.append(s4)

print("dept 1 students", dept1.students)
print("dept 2 students", dept2.students)


# Create Some Courses
c1 = Course(
    title="Applied Electricity I",
    instructor="Balogun",
    description="Intro to circuits",
    code="GET201")

c2 = Course(
    title="Fluid Mechanics",
    instructor="Awilorem",
    description="Intro to fluids",
    code="GET241")
c3 = Course(title="Applied Electricity II", instructor="Balogun",
            description="Advanced circuit analysis", code="GET202")

with app.app_context():
    db.session.add_all([c1, c2, c3])

# Test the many to many relationship

e = Enrollment(grade="A")
e.course = c1
s1.courses.append(e)
e2 = Enrollment(grade="A")
e2.course = c3
s1.courses.append(e2)
print(s1.courses)
print(c1.students)

with app.app_context():
    db.session.add_all([faculty1, faculty2])
    db.session.add_all([dept1, dept2, dept3, dept4])
    db.session.add_all([s1, s2, s3, s4])
    db.session.add_all([c1, c2, c3])
    db.session.commit()

with app.app_context():
    faculties = Faculty.query.all()


print("All Faculties")
for fac in faculties:
    print(fac.name)
print("---------------------")

with app.app_context():
    depts = Department.query.all()

print("All Departments")
for d in depts:
    print(d.name)
print("---------------------")

with app.app_context():
    studs = Student.query.all()

print("All Students")
for s in studs:
    print(s.last_name, s.first_name)
print("---------------------")

with app.app_context():
    cs = Course.query.all()

print("All Students")
for c in cs:
    print(c.title, c.code)
