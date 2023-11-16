#!/usr/bin/python3
"""This script contains the departments
endpoints"""

import re
from flask import abort, jsonify, request

from app.api.v1.views import api_v1
from app.models import db
from app.models.department import Department
from app.models.faculty import Faculty

# This will be used to convert our class instances into dict repr.
from app.utils.dict_cleanup import dict_cleanup


@api_v1.route("/departments", methods=["GET"], strict_slashes=False)
def get_all_departments():
    """This returns a json list of all
    departments in the db
    """
    # Instantiate a list that will contain all the
    # dict repr of the departments
    dept_list = []

    depts = Department.query.all()

    # Convert all department objects into dict repr. and add each to the list
    for d in depts:
        dict_repr = dict_cleanup(d)
        dept_list.append(dict_repr)
    return dept_list


@api_v1.route("departments/<int:id>", methods=["GET"], strict_slashes=False)
def get_one_dept(id):
    """This returns the department with
    specified id"""
    # Query the db for the faculty
    dept = Department.query.filter_by(id=id).first()

    # If the specified department is not found, return a 404 error
    if dept is None:
        abort(404)

    dict_repr = dict_cleanup(dept)
    return dict_repr


@api_v1.route(
    "/faculties/<int:id>/departments", methods=["GET"], strict_slashes=False
)
def get_depts_in_faculty(id):
    """This returns all of the departments
    that belong to the specified faculty
    """
    # get faculty with id specified
    fac = Faculty.query.filter_by(id=id).first()

    # Return a 404 error if no faculty with specified id is found
    if fac is None:
        abort(404)

    dept_list = []

    # get all the departments linked to the faculty
    depts = fac.departments

    # Convert all department objects to dict repr.
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
        return {"error": "Missing Name"}, 400
    if "hod" not in request.json.keys():
        return {"error": "Missing HOD"}, 400
    if "description" not in request.json.keys():
        return {"error": "Missing Description"}, 400

    # Store the request query parameters in a data variable
    data = request.json

    # Check to make sure that the department name and hod do not already exist
    hods = [d.hod for d in Department.query.all()]
    if data["hod"] in hods:
        return {"error": "HOD to another department"}, 400
    names = [d.name for d in Department.query.all()]
    if data["name"] in names:
        return {"error": "This department already exists"}, 400

    # Retrive faculty id specified from db
    fac = Faculty.query.filter_by(id=id).first()
    if fac is None:
        abort(404)

    # Create a new department with specified values
    dept = Department(**data)
    dict_repr = dict_cleanup(dept)

    # Add the created department to the faculty that was just
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

    # Store the request query parameters in a data variable
    data = request.json

    # Retrieve dept to be updated from db
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)

    # Check to make sure that the department name and hod do not already exist
    if "hod" in data.keys():
        # Retrieve the current hod value
        dept_hod = Department.query.filter_by(id=id).first().hod

        # Check if the hod is the same as the current hod value
        # before checking for duplicates
        if data.get("hod") != dept_hod and data.get("hod") is not None:
            hods = [d.hod for d in Department.query.all()]
            if data["hod"] in hods:
                return {"error": "HOD to another department"}, 400

    if "name" in data.keys():
        # Retrieve the current name value
        dept_name = Department.query.filter_by(id=id).first().name

        # Check if the hod is the same as the current hod value
        # before checking for duplicates
        if data.get("name") != dept_name and data.get("name") is not None:
            names = [d.name for d in Department.query.all()]
            if data["name"] in names:
                return {"error": "This department already exists"}, 400

    # Update the department with values specified
    for key, value in data.items():
        setattr(dept, key, value)

    # Save the changes to the db
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
    # Retrieve the department from the db
    dept = Department.query.filter_by(id=id).first()

    # Return a 404 error if it doesn't exist in the db
    if dept is None:
        abort(404)

    # Delete from the db and save changes
    db.session.delete(dept)
    db.session.commit()

    return {}, 200


@api_v1.route("/departments_search", methods=["POST"], strict_slashes=False)
def departments_search():
    """This function loads up departments from
    the db that match a particular pattern.
    IF no pattern is specified, it loads up
    all departments from the db"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")

    # Store the request query parameters in a data variable
    data = request.json
    dept_list = []

    # Check if a faculty id is specified.
    if data.get("faculty_id"):
        fac = Faculty.query.filter_by(id=data.get("faculty_id")).first()
        if fac is None:
            abort(404)
        depts = fac.departments
    else:
        depts = Department.query.all()

    # Convert all departments in dict repr. and append to list
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
