#!/usr/bin/python3
"""This script contains routes for the
faculties endpoints
"""

from app.models.faculty import Faculty
from flask import jsonify
from app.api.v1.views import api_v1


@api_v1.route("/faculties")
