#!/usr/bin/python3
"""This contains general views for the app"""

from app.api.v1.views import api_v1
from flask import jsonify
import app.models as m


models = {
        "faculties": m.Faculty, "departments": m.Department,
        "courses": m.Course, "students": m.Student
    }


@api_v1.route("/status", strict_slashes=False)
def status():
    """Test api connection"""
    return {"status": "OK"}


@api_v1.route("/stats", strict_slashes=False)
def stats():
    """This returns the count of all resources"""
    stats = {}
    for model in models.keys():
        count = models[model].query.count()
        stats[model] = count
    return stats
