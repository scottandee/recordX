#!/usr/bin/python3
"""This script contains the departments
endpoints"""

import re
from flask import abort, jsonify, request

from app.api.v1.views import api_v1
from app.utils.dict_cleanup import dict_cleanup
from app.models import db
from app.models.department import Department
from app.models.faculty import Faculty


@api_v1.route("/departments", methods=["GET"], strict_slashes=False)
def get_all_departments():
    """This returns a json list of all
    departments in the db
    """
    dept_list = []
    depts = Department.query.all()

    for d in depts:
        dict_repr = dict_cleanup(d)
        dept_list.append(dict_repr)
    return dept_list


@api_v1.route(
    "/faculties/<int:id>/departments", methods=["GET"], strict_slashes=False
)
def get_depts_in_faculty(id):
    """This returns all of the departments
    that belong to the specified faculty
    """
    # get faculty with id specified
    fac = Faculty.query.filter_by(id=id).first()
    if fac is None:
        abort(404)
    dept_list = []

    # get all the departments linked to the faculty
    depts = fac.departments

    for d in depts:
        dict_repr = dict_cleanup(d)
        dept_list.append(dict_repr)
    return dept_list


@api_v1.route(
    "/faculties/<int:id>/departments", methods=["POST"], strict_slashes=False)
def create_dept(id):
    """This creates a new department"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    if "name" not in request.json.keys():
        abort(400, "Missing name")
    if "hod" not in request.json.keys():
        abort(400, "Missing hod")
    if "description" not in request.json.keys():
        abort(400, "Missing description")
    data = request.json
    hods = [d.hod for d in Department.query.all()]
    names = [d.name for d in Department.query.all()]
    if data["hod"] in hods:
        abort(400, "Hod already exists")
    if data["name"] in names:
        abort(400, "name already exists")

    # retrive faculty id specified from db
    fac = Faculty.query.filter_by(id=id).first()
    if fac is None:
        abort(404)

    # create a new department with specified values
    dept = Department(**data)
    dict_repr = dict_cleanup(dept)

    # add the created department to the faculty that was just
    # retreived from the db
    fac.departments.append(dept)
    db.session.add(fac)
    db.session.add(dept)
    db.session.commit()

    return dict_repr, 201


@api_v1.route("/departments/<int:id>", methods=["PUT"], strict_slashes=False)
def update_dept(id):
    """This updates a department"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    data = request.json

    if "hod" in data.keys():
        hods = [d.hod for d in Department.query.all()]
        if data["hod"] in hods:
            abort(400, "Hod already exists")
    if "name" in data.keys():
        names = [d.name for d in Department.query.all()]
        if data["name"] in names:
            abort(400, "name already exists")

    # retrieve dept to be updated from db
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)

    # update the department with values specified
    for key, value in data.items():
        setattr(dept, key, value)

    dict_repr = dict_cleanup(dept)
    db.session.add(dept)
    db.session.commit()

    return dict_repr, 200


@api_v1.route(
    "/departments/<int:id>", methods=["DELETE"], strict_slashes=False
)
def delete_department(id):
    """This function deletes the specified
    department
    """
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)
    db.session.delete(dept)
    db.session.commit()
    return {}, 200


@api_v1.route("/departments_search", methods=["POST"], strict_slashes=False)
def departments_search():
    """This function loads up departments from
    the db that match a particular pattern.
    IF no pattern is specified, it loads up
    all departments from the db"""
    if not request.is_json:
        abort(400, "Not a JSON")

    data = request.json
    dept_list = []

    # check if a faculty id is specified.
    if data.get("faculty_id"):
        fac = Faculty.query.filter_by(id=data.get("faculty_id")).first()
        if fac is None:
            abort(404)
        depts = fac.departments
    else:
        depts = Department.query.all()

    for d in depts:
        dict_repr = dict_cleanup(d)
        dept_list.append(dict_repr)

    # check if there's a search pattern defined
    if data.get("pattern"):
        filtered = []
        search = "[a-zA-Z]*{}[a-zA-Z]*".format(data.get("pattern"))
        for d in dept_list:
            res = re.search(search, d["name"], re.IGNORECASE)
            if res is not None:
                filtered.append(d)
        return filtered
    else:
        return dept_list
