#!/usr/bin/python3

import pytest
from datetime import date
from app import create_app, db
from app.models.faculty import Faculty
from app.models.department import Department
from app.models.course import Course
from app.models.student import Student
from app.models.enrollment import Enrollment


class TestConfig():
    """Configurations for test database"""
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture()
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
    with app.app_context():
        # Create a dummy faculty
        faculty = Faculty(
            name='Dummy Faculty',
            description='This is a dummy faculty'
        )
        db.session.add(faculty)

        # Create a dummy department associated with the faculty
        department = Department(
            name='Dummy Department',
            hod='Dr. John Doe',
            description='This is a dummy department',
        )
        department.faculty = faculty
        db.session.add(department)

        course = Course(
            title='Dummy Course',
            code='DUMMY101',
            instructor='Dr. Jane Smith',
            description='This is a dummy course',
        )
        course.department = department
        db.session.add(course)

        student = Student(
            first_name="Maddock", last_name="James",
            matric_number="20/58EC/00878",
            gender="Male", email="sc@gmail.com",
            address="73, Kings street",
            dob=date(2004, 3, 3)
        )
        student.department = department
        db.session.add(student)
        e = Enrollment(grade="A")
        e.course = course
        student.courses.append(e)
        db.session.add(e)
        db.session.add(student)
        db.session.add(course)
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
