#!/usr/bin/python3
"""This script runs tests on the
faculty endpoints
"""

from app.models.faculty import Faculty


def test_get_all_faculty(client, app):
    """This tests the faculty get method"""
    r = client.get("/api/v1/faculties")
    assert r.is_json
    assert r.status_code == 200

    with app.app_context():
        assert Faculty.query.count() == len(r.json)


def test_get_faculty_invalid(client, app):
    """This tests the faculty get method"""
    r = client.get("/api/v1/faculties/50")
    assert r.status_code == 404


def test_post_faculty(client, app):
    """This tests the faculty post method"""
    with app.app_context():
        initial = Faculty.query.count()
    r = client.post("/api/v1/faculties", json={"name": "Agric",
                                               "description": "Farm house"})
    assert r.status_code == 201
    with app.app_context():
        assert Faculty.query.count() == initial + 1


def test_post_faculty_not_json(client):
    """This tests the faculty post method"""
    r = client.post("/api/v1/faculties", data={"name": "Agric",
                                               "description": "Farm house"})
    assert r.status_code == 400


def test_post_faculty_no_name(client):
    """This tests the faculty post method"""
    r = client.post("/api/v1/faculties", json={"description": "Farm house"})
    assert r.status_code == 400


def test_get_one_faculty(client, app):
    """This tests the faculty get method"""
    data = {"name": "agric", "description": "farm house"}
    r = client.post("/api/v1/faculties", json=data)
    r = client.get("/api/v1/faculties/1")
    assert r.is_json
    assert r.status_code == 200


def test_delete_faculty(client, app):
    """This tests the faculty delete method"""
    with app.app_context():
        initial = Faculty.query.count()
    r = client.post("/api/v1/faculties", json={"name": "Agric",
                                               "description": "Farm house"})
    assert r.status_code == 201
    with app.app_context():
        assert Faculty.query.count() == initial + 1

    r = client.delete("/api/v1/faculties/1")
    assert r.status_code == 200
    with app.app_context():
        assert Faculty.query.count() == 0


def test_delete_faculty_invalid(client):
    """This tests the faculty delete method"""
    r = client.delete("/api/v1/faculties/1000")
    assert r.status_code == 404


def test_update_faculty(client, app):
    """This tests the faculty update method"""
    with app.app_context():
        initial = Faculty.query.count()
    r = client.post("/api/v1/faculties", json={"name": "Agric",
                                               "description": "Farm house"})
    assert r.status_code == 201
    with app.app_context():
        assert Faculty.query.count() == initial + 1

    r = client.put("/api/v1/faculties/1", json={"name": "Agricultural"})
    assert r.status_code == 200
    with app.app_context():
        fac = Faculty.query.filter_by(id=1).first()
        assert fac.name == "Agricultural"


def test_update_faculty_invalid(client):
    """This tests the faculty delete method"""
    r = client.put("/api/v1/faculties/1000", json={"name": "hahha"})
    assert r.status_code == 404


def test_update_faculty_not_json(client):
    """This tests the faculty post method"""
    r = client.put("/api/v1/faculties/1", data={"name": "Agric"})
    assert r.status_code == 400


def test_faculty_search_no_filter(client, app):
    """This tests the faculty search endpoint"""
    r = client.post("api/v1/faculties_search", json={})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == Faculty.query.count()


def test_faculty_search_filter(client, app):
    """This tests the faculty search endpoint"""
    data1 = {"name": "agric", "description": "farm house1"}
    data2 = {"name": "agri", "description": "farm house2"}
    data3 = {"name": "agr", "description": "farm house3"}
    r = client.post("/api/v1/faculties", json=data1)
    r = client.post("/api/v1/faculties", json=data2)
    r = client.post("/api/v1/faculties", json=data3)

    r = client.post("api/v1/faculties_search", json={"pattern": "agr"})
    assert r.status_code == 200

    with app.app_context():
        assert len(r.json) == Faculty.query.count()
