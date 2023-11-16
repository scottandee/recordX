#!/usr/bin/python3
"""This script runs tests on the course
 endpoints
"""

from app.models.course import Course


def test_post_course(client, app):
    """This tests the course post method"""
    with app.app_context():
        initial = Course.query.count()

    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 201
    with app.app_context():
        assert Course.query.count() == initial + 1


def test_post_course_no_title(client):
    """This tests the course post method"""
    json = {"description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 400


def test_post_course_duplicate_title(client):
    """This tests the course post method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"title": "intro", "description": "This is for testing3", "code":
            "ECE5093", "instructor": "Babajide3"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 400


def test_post_course_no_descr(client):
    """This tests the course post method"""
    json = {"title": "intro", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 400


def test_post_course_no_instuctor(client):
    """This tests the course post method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 400


def test_post_course_duplicate_code(client):
    """This tests the course post method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"title": "intro", "description": "This is for testing3", "code":
            "ECE509", "instructor": "Babajide3"}
    r = client.post("/api/v1/departments/1/courses", json=json)
    assert r.status_code == 400


def test_post_course_invalid(client):
    """This tests the faculty post method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/2/courses", json=json)
    assert r.status_code == 404


def test_update_course(client, app):
    """This method tests the courses update method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"title": "introsj", "description": "This is for testings", "code":
            "ECE508", "instructor": "Babajidee"}
    r = client.put("/api/v1/courses/2", json=json)

    assert r.status_code == 200
    with app.app_context():
        assert Course.query.filter_by(id=2).first().title == "introsj"


def test_update_course_invalid(client, app):
    """This method tests the courses update method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.put("/api/v1/courses/10", json=json)

    assert r.status_code == 404


def test_update_duplicate_code_course(client, app):
    """This method tests the courses update method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"title": "introsj", "description": "This is for testings", "code":
            "ECE509", "instructor": "Babajidee"}
    r = client.put("/api/v1/courses/2", json=json)

    assert r.status_code == 200


def test_update_duplicate_title_course(client, app):
    """This method tests the courses update method"""
    json = {"title": "intro", "description": "This is for testing", "code":
            "ECE509", "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json)

    json = {"title": "intro"}
    r = client.put("/api/v1/courses/2", json=json)

    assert r.status_code == 200


def test_delete_course(client, app):
    """This tests the course delete method"""
    with app.app_context():
        initial = Course.query.count()

    r = client.delete("/api/v1/courses/1")
    assert r.status_code == 200
    with app.app_context():
        assert Course.query.count() == 0


def test_delete_course_invalid(client):
    """This tests the course delete method"""
    r = client.delete("/api/v1/courses/1000")
    assert r.status_code == 404


def test_dept_search_no_filter(client, app):
    """This tests the department search endpoint"""
    r = client.post("api/v1/courses_search", json={})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 1


def test_department_search_filter(client, app):
    """This tests the department search endpoint"""
    json1 = {
        "title": "introduction",
        "description": "This is for testing",
        "code": "ECE509",
        "instructor": "Babajide"}
    json2 = {"title": "intro", "description": "This is for testing", "code":
             "ECE505", "instructor": "Babajide"}
    json3 = {
        "title": "introduce",
        "description": "This is for testing",
        "code": "ECE506",
        "instructor": "Babajide"}
    r = client.post("/api/v1/departments/1/courses", json=json1)
    r = client.post("/api/v1/departments/1/courses", json=json2)
    r = client.post("/api/v1/departments/1/courses", json=json3)

    r = client.post("api/v1/courses_search", json={"pattern": "intr"})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 3

    json = {"department_id": 1, "pattern": "intr"}
    r = client.post("api/v1/courses_search", json=json)
    assert r.status_code == 200
