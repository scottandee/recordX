#!/usr/bin/python3
"""This script contains tests for the
emrollment endpoints
"""

from app.models import Enrollment


def test_get_student_courses(client, app):
    """This tests the get student courses
    route
    """
    r = client.get("api/v1/students/1/courses")
    assert r.status_code == 200
    with app.app_context():
        assert len(r.json) == 1


def test_post_enrollment(client, app):
    """This tests the create enrollments
    route
    """
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"grade": "A"}
    r = client.post("api/v1/students/1/courses/2", json=json)
    assert r.status_code == 201

    with app.app_context():
        e = Enrollment.query.filter_by(student_id=1, course_id=2).first()
        assert e.grade == "A"


def test_post_enrollment_no_grade(client, app):
    """This tests the create enrollments
    route
    """
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {}
    r = client.post("api/v1/students/1/courses/2", json=json)
    assert r.status_code == 201

    with app.app_context():
        e = Enrollment.query.filter_by(student_id=1, course_id=2).first()
        assert e.grade == "Nil"


def test_post_enrollment_invalid(client):
    """This tests the create enrollments
    route
    """
    json = {}
    r = client.post("api/v1/students/1/courses/89", json=json)
    assert r.status_code == 404

    r = client.post("api/v1/students/62/courses/1", json=json)
    assert r.status_code == 404


def test_put_enrollment(client, app):
    """This function tests the update enrollment
    route
    """
    json = {"grade": "B"}
    r = client.put("api/v1/students/1/courses/1", json=json)
    assert r.status_code == 200

    with app.app_context():
        e = Enrollment.query.filter_by(student_id=1, course_id=1).first()
        assert e.grade == "B"


def test_put_enrollment_no_grade(client, app):
    """This function tests the update enrollment
    route
    """
    json = {}
    r = client.put("api/v1/students/1/courses/1", json=json)
    assert r.status_code == 400


def test_put_enrollment_invalid(client, app):
    """This function tests the update enrollment
    route
    """
    json = {"grade": "B"}
    r = client.put("api/v1/students/1/courses/82", json=json)
    assert r.status_code == 404


def test_delete_enrollment(client, app):
    """This function tests the delete enrollment
    route
    """
    r = client.delete("api/v1/students/1/courses/1")
    assert r.status_code == 200

    with app.app_context():
        e = Enrollment.query.all()
        assert len(e) == 0


def test_delete_enrollment_invalid(client, app):
    """This function tests the delete enrollment
    route
    """
    r = client.delete("api/v1/students/5/courses/1")
    assert r.status_code == 404
