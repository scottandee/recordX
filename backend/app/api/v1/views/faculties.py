#!/usr/bin/python3
"""This script contains controllers for the
faculties endpoints
"""

import re
from app.models.faculty import Faculty
from app.models import db
from flask import abort, request
from app.api.v1.views import api_v1

# This will be used to convert our class instances into dict repr.
from app.utils.dict_cleanup import dict_cleanup


@api_v1.route("/faculties", methods=["GET"], strict_slashes=False)
def get_all_faculties():
    """This returns a json list of all
    faculties in the db
    """
    # Instantiate a list that will contain all the
    # dict repr. of the faculties
    fac_list = []

    faculties = Faculty.query.all()

    # Convert faculties to dict repr. and then append
    for f in faculties:
        dict_repr = dict_cleanup(f)
        fac_list.append(dict_repr)

    return fac_list


@api_v1.route("faculties/<int:id>", methods=["GET"], strict_slashes=False)
def get_one_faculty(id):
    """This returns the faculty with
    specified id
    """
    # Query the db for the faculty
    faculty = Faculty.query.filter_by(id=id).first()

    # Check if the faculty is in the db
    if faculty is None:
        abort(404)

    # Create a dictionary representation of the faculty
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

    # Save the request into a data variable
    data = request.json

    # Check if the faculty name provided is not one that already exists
    names = [f.name for f in Faculty.query.all()]
    if data["name"] in names:
        return {"error": "Faculty name already exists"}, 400

    # Create a new faculty and save to the db
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
    # Query the db for the specified faculty
    faculty = Faculty.query.filter_by(id=id).first()

    # Return not found if the faculty doesn't exist
    if faculty is None:
        abort(404)

    # Delete the faculty and save changes to the db
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

    # Query the db for the specified faculty
    faculty = Faculty.query.filter_by(id=id).first()

    # Return not found if the faculty doesn't exist
    if faculty is None:
        abort(404)

    # Save the request into a data variable
    data = request.json

    # Check if the faculty name provided is not one that already exists
    if data["name"] != Faculty.query.filter_by(id=id).first().name:
        names = [f.name for f in Faculty.query.all()]
        if data["name"] in names:
            return {"error": "Faculty name already exists"}, 400

    # Update the faculty with all of the specifies data and save to db
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

    # Save the request into a data variable
    request_data = request.json

    # declare a list that will contain the dict repr. of all faculties
    fac_list = []

    # Get all the faculties from the db
    faculties = Faculty.query.all()

    # Convert all of the faculties into dict repr. and appent to fac_list
    for f in faculties:
        dict_repr = dict_cleanup(f)
        fac_list.append(dict_repr)

    # Check if a pattern is specified
    if request_data == {}:
        return fac_list

    # Check if a search pattern is specified
    if request_data.get("pattern"):
        # Declare a list that will contain all faculties that match the pattern
        filtered = []

        # Create the search pattern with the data provided
        search = "[a-zA-Z]*{}[a-zA-Z]*".format(request_data.get("pattern"))

        # Check for a matches all throughout the fac_list
        for fac in fac_list:
            res = re.search(search, fac["name"], re.IGNORECASE)

            # If it's a match, add to filtered list
            if res is not None:
                filtered.append(fac)
        return filtered
    else:
        return fac_list
