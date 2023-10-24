#!/usr/bin/python3
"""This script runs tests on the
 endpoints
"""

from app.models.department import Department


def test_get_all_department(client, app):
    """This tests the department get method"""
    r = client.get("/api/v1/departments")
    assert r.is_json
    assert r.status_code == 200

    with app.app_context():
        assert Department.query.count() == len(r.json)


def test_post_dept(client, app):
    """This tests the faculty post method"""
    with app.app_context():
        initial = Department.query.count()

    json = {"name": "Dept", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 201
    with app.app_context():
        assert Department.query.count() == initial + 1


def test_post_dept_no_name(client):
    """This tests the faculty post method"""
    json = {"description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 400


def test_post_dept_duplicate_name(client):
    """This tests the faculty post method"""
    json = {"name": "Dept", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    json = {"name": "Dept", "description": "dummy data2", "hod": "Labake2"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 400


def test_post_dept_no_descr(client):
    """This tests the faculty post method"""
    json = {"name": "Dept", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 400


def test_post_dept_no_hod(client):
    """This tests the faculty post method"""
    json = {"name": "Dept", "descripton": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 400


def test_post_dept_duplicate_hod(client):
    """This tests the faculty post method"""
    json = {"name": "Dept1", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    json = {"name": "Dept2", "description": "dummy data2", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)
    assert r.status_code == 400


def test_post_dept_invalid(client):
    """This tests the faculty post method"""
    json = {"name": "Dept", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/2/departments", json=json)
    assert r.status_code == 404


def test_update_dept(client, app):
    """This method tests the departments update method"""
    json = {"name": "Dept1", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    json = {"name": "Department", "description": "Testing...", "hod": "bro"}
    r = client.put("/api/v1/departments/1", json=json)

    assert r.status_code == 200
    with app.app_context():
        assert Department.query.filter_by(id=1).first().name == "Department"


def test_update_dept_invalid(client, app):
    """This method tests the departments update method"""
    json = {"name": "Department", "description": "Testing...", "hod": "bro"}
    r = client.put("/api/v1/departments/2", json=json)

    assert r.status_code == 404


def test_update_duplicate_hod_dept(client, app):
    """This method tests the departments update method"""
    json = {"name": "Dept1", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    json = {"name": "Dept13", "description": "dummy data", "hod": "Labake"}
    r = client.put("/api/v1/departments/1", json=json)

    assert r.status_code == 400


def test_update_duplicate_name_dept(client, app):
    """This method tests the departments update method"""
    json = {"name": "Dept1", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    json = {"name": "Dept1", "description": "dummy data", "hod": "LLabake"}
    r = client.put("/api/v1/departments/1", json=json)

    assert r.status_code == 400


def test_delete_department(client, app):
    """This tests the department delete method"""
    with app.app_context():
        initial = Department.query.count()
    json = {"name": "Dept1", "description": "dummy data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json)

    with app.app_context():
        assert Department.query.count() == initial + 1

    r = client.delete("/api/v1/departments/1")
    assert r.status_code == 200
    with app.app_context():
        assert Department.query.count() == 1


def test_delete_dept_invalid(client):
    """This tests the department delete method"""
    r = client.delete("/api/v1/departments/1000")
    assert r.status_code == 404


def test_dept_search_no_filter(client, app):
    """This tests the department search endpoint"""
    r = client.post("api/v1/departments_search", json={})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == 1


def test_department_search_filter(client, app):
    """This tests the department search endpoint"""
    json1 = {"name": "Dep", "description": "dummy data", "hod": "Labake"}
    json2 = {"name": "Dept1", "description": "dummy na data", "hod": "Labake"}
    json3 = {"name": "Dep1", "description": "dummy  ti data", "hod": "Labake"}
    r = client.post("/api/v1/faculties/1/departments", json=json1)
    r = client.post("/api/v1/faculties/1/departments", json=json2)
    r = client.post("/api/v1/faculties/1/departments", json=json3)

    r = client.post("api/v1/departments_search", json={"pattern": "dep"})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == Department.query.count()

    json = {"faculty_id": 1, "pattern": "dep"}
    r = client.post("api/v1/departments_search", json=json)
    assert r.status_code == 200
