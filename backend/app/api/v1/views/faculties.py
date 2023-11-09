#!/usr/bin/python3
"""This script contains routes for the
faculties endpoints
"""

import re
from app.models.faculty import Faculty
from app.models import db
from flask import jsonify, abort, request
from app.api.v1.views import api_v1
from app.utils.dict_cleanup import dict_cleanup


@api_v1.route("/faculties", methods=["GET"], strict_slashes=False)
def get_all_faculties():
    """This returns a json list of all
    faculties in the db
    """
    fac_list = []
    faculties = Faculty.query.all()

    for f in faculties:
        dict_repr = dict_cleanup(f)
        fac_list.append(dict_repr)
    return fac_list


@api_v1.route("faculties/<int:id>", methods=["GET"], strict_slashes=False)
def get_one_faculty(id):
    """This returns the faculty with
    specified id"""
    faculty = Faculty.query.filter_by(id=id).first()
    if faculty is None:
        abort(404)
    dict_repr = dict_cleanup(faculty)
    return dict_repr


@api_v1.route("/faculties", methods=["POST"], strict_slashes=False)
def create_faculty():
    """This creates a new faculty"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    if "name" not in request.json.keys():
        abort(400, "Missing name")
        return {"error": "Missing Name"}, 400

    data = request.json
    names = [f.name for f in Faculty.query.all()]
    if data["name"] in names:
        return {"error": "Faculty name already exists"}, 400

    faculty = Faculty(**data)
    dict_repr = dict_cleanup(faculty)
    db.session.add(faculty)
    db.session.commit()
    return dict_repr, 201


@api_v1.route("/faculties/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_faculty(id):
    """This function deletes the specified
    faculty
    """
    faculty = Faculty.query.filter_by(id=id).first()
    if faculty is None:
        abort(404)
    db.session.delete(faculty)
    db.session.commit()
    return {}, 200


@api_v1.route("/faculties/<int:id>", methods=["PUT"], strict_slashes=False)
def update_faculty(id):
    """This function updates the specified
    faculty
    """
    if not request.is_json:
        abort(400, "Not a JSON")

    faculty = Faculty.query.filter_by(id=id).first()
    if faculty is None:
        abort(404)

    data = request.json
    if data["name"] != Faculty.query.filter_by(id=id).first().name:
        names = [f.name for f in Faculty.query.all()]
        if data["name"] in names:
            return {"error": "Faculty name already exists"}, 400
    for key, value in data.items():
        setattr(faculty, key, value)
    dict_repr = dict_cleanup(faculty)
    db.session.add(faculty)
    db.session.commit()

    return dict_repr, 200


@api_v1.route("/faculties_search", methods=["POST"], strict_slashes=False)
def faculties_search():
    """This function loads up faculties from
    the db that match a particular pattern.
    IF no pattern is specified, it loads up
    all faculties from the db"""
    if not request.is_json:
        abort(400, "Not a JSON")

    request_data = request.json
    fac_list = []
    faculties = Faculty.query.all()

    for f in faculties:
        dict_repr = dict_cleanup(f)
        fac_list.append(dict_repr)

    if request_data == {}:
        return fac_list
    if request_data.get("pattern"):
        filtered = []
        search = "[a-zA-Z]*{}[a-zA-Z]*".format(request_data.get("pattern"))
        for fac in fac_list:
            res = re.search(search, fac["name"], re.IGNORECASE)
            if res is not None:
                filtered.append(fac)
        return filtered
    else:
        return fac_list
