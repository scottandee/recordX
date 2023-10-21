#!/usr/bin/python3
"""This tests the index view"""


def test_status(client):
    """This tests the status of the API"""
    response = client.get("/api/v1/status")
    assert response.is_json
    assert response.status_code == 200
    assert b"OK" in response.data


def test_stats(client):
    """This tests if the stats are of correct format"""
    response = client.get("/api/v1/stats")
    assert response.is_json
    assert response.status_code == 200
