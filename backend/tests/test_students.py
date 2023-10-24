#!/usr/bin/python3
"""This script runs tests on the student
 endpoints
"""

from app.models.student import Student
from datetime import datetime


dob_string = '2004-03-03'


def test_post_student(client, app):
    """This tests the student post method"""
    with app.app_context():
        initial = Student.query.count()

    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)
    assert r.status_code == 201
    with app.app_context():
        assert Student.query.count() == initial + 1


def test_post_student_missing_value(client):
    """This tests the student post method"""
    json = {"last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)
    assert r.status_code == 400


def test_post_student_duplicate_matric(client):
    """This tests the student post method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00878", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)
    assert r.status_code == 400


def test_post_student_duplicate_email(client):
    """This tests the student post method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "sc@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)
    assert r.status_code == 400


def test_post_student_invalid(client):
    """This tests the faculty post method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/2/students", json=json)
    assert r.status_code == 404


def test_update_student(client, app):
    """This method tests the students update method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)

    json = {"first_name": "Honeys", "last_name": "Badgers"}
    r = client.put("/api/v1/students/2", json=json)

    assert r.status_code == 200
    with app.app_context():
        assert Student.query.filter_by(id=2).first().first_name == "Honeys"


def test_update_student_invalid(client, app):
    """This method tests the students update method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00888", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.put("/api/v1/students/10", json=json)

    assert r.status_code == 404


def test_update_duplicate_matric_student(client, app):
    """This method tests the students update method"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00878", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.put("/api/v1/students/1", json=json)

    assert r.status_code == 400


def test_update_duplicate_email_student(client, app):
    """This method tests the students update method"""
    json = {"email": "sc@gmail.com"}
    r = client.post("/api/v1/departments/1/students", json=json)

    assert r.status_code == 400


def test_delete_student(client, app):
    """This tests the student delete method"""
    with app.app_context():
        initial = Student.query.count()

    r = client.delete("/api/v1/students/1")
    assert r.status_code == 200
    with app.app_context():
        assert Student.query.count() == 0


def test_delete_student_invalid(client):
    """This tests the student delete method"""
    r = client.delete("/api/v1/students/1000")
    assert r.status_code == 404


def test_dept_search_no_filter(client, app):
    """This tests the department search endpoint"""
    json = {"first_name": "Honey", "last_name": "Badger",
            "matric_number": "20/58EC/00858", "gender": "Male",
            "email": "scott@gmail.com", "address": "76, Kings street",
            "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json)

    r = client.post("api/v1/students_search", json={})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 2


def test_department_search_filter(client, app):
    """This tests the department search endpoint"""
    json2 = {"first_name": "Honey", "last_name": "Badger",
             "matric_number": "20/58EC/00458", "gender": "Male",
             "email": "scott@gmail.com", "address": "76, Kings street",
             "dob": dob_string}
    json1 = {"first_name": "Honey", "last_name": "Badger",
             "matric_number": "20/58EC/00058", "gender": "Male",
             "email": "sct@gmail.com", "address": "76, Kings street",
             "dob": dob_string}
    json3 = {"first_name": "Honey", "last_name": "Badger",
             "matric_number": "20/58EC/00858", "gender": "Male",
             "email": "scot@gmail.com", "address": "76, Kings street",
             "dob": dob_string}
    r = client.post("/api/v1/departments/1/students", json=json1)
    r = client.post("/api/v1/departments/1/students", json=json2)
    r = client.post("/api/v1/departments/1/students", json=json3)

    r = client.post("api/v1/students_search", json={"pattern": "hon"})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 3

    r = client.post("api/v1/students_search", json={"pattern": "bad"})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 3

    json = {"department_id": 1, "pattern": "bad"}
    r = client.post("api/v1/students_search", json=json)
    assert r.status_code == 200
