#!/usr/bin/python3
"""This script contains the courses
endpoints"""

import re
from flask import abort, jsonify, request

from app.api.v1.views import api_v1
from app.utils.dict_cleanup import dict_cleanup
from app.models import db
from app.models.course import Course
from app.models.department import Department


@api_v1.route(
    "/departments/<int:id>/courses", methods=["GET"], strict_slashes=False
)
def get_courses_in_department(id):
    """This returns all of the courses
    that belong to the specified department
    """
    # get dept with id specified
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)
    course_list = []

    # get all the courses linked to the dept
    courses = dept.courses

    for c in courses:
        dict_repr = dict_cleanup(c)
        course_list.append(dict_repr)
    return course_list


@api_v1.route(
    "/departments/<int:id>/courses", methods=["POST"], strict_slashes=False)
def create_course(id):
    """This creates a new course"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    if "title" not in request.json.keys():
        abort(400, "Missing title")
    if "instructor" not in request.json.keys():
        abort(400, "Missing instructor")
    if "code" not in request.json.keys():
        abort(400, "Missing code")
    if "description" not in request.json.keys():
        abort(400, "Missing description")
    data = request.json
    titles = [c.title for c in Course.query.all()]
    codes = [c.code for c in Course.query.all()]
    if data["title"] in titles:
        abort(400, "title already exists")
    if data["code"] in codes:
        abort(400, "title already exists")

    # retrive department id specified from db
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)

    # create a new course with specified values
    course = Course(**data)
    dict_repr = dict_cleanup(course)

    # add the created course to the department that was just
    # retreived from the db
    dept.courses.append(course)
    db.session.add(course)
    db.session.add(dept)
    db.session.commit()

    return dict_repr, 201


@api_v1.route("/courses/<int:id>", methods=["PUT"], strict_slashes=False)
def update_course(id):
    """This updates a course"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    data = request.json

    if "title" in data.keys():
        titles = [c.title for c in Course.query.all()]
        if data["title"] in titles:
            abort(400, "Title already exists")

    if "code" in data.keys():
        codes = [c.code for c in Course.query.all()]
        if data["code"] in codes:
            abort(400, "Code already exists")

    # retrieve course to be updated from db
    course = Course.query.filter_by(id=id).first()
    if course is None:
        abort(404)

    # update the course with values specified
    for key, value in data.items():
        setattr(course, key, value)

    dict_repr = dict_cleanup(course)
    db.session.add(course)
    db.session.commit()

    return dict_repr, 200


@api_v1.route("/courses/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_course(id):
    """This function deletes the specified
    course
    """
    course = Course.query.filter_by(id=id).first()
    if course is None:
        abort(404)
    db.session.delete(course)
    db.session.commit()
    return {}, 200


@api_v1.route("/courses_search", methods=["POST"], strict_slashes=False)
def courses_search():
    """This function loads up courses from
    the db that match a particular pattern.
    IF no pattern is specified, it loads up
    all courses from the db
    """
    if not request.is_json:
        abort(400, "Not a JSON")

    data = request.json
    course_list = []

    # check if a department id is specified.
    if data.get("department_id"):
        dept = Department.query.filter_by(id=data.get("department_id")).first()
        if dept is None:
            abort(404)
        courses = dept.courses
    else:
        courses = Course.query.all()

    for c in courses:
        dict_repr = dict_cleanup(c)
        course_list.append(dict_repr)

    # check if there's a search pattern defined
    if data.get("pattern"):
        filtered = []
        search = "[a-zA-Z]*{}[a-zA-Z]*".format(data.get("pattern"))
        for c in course_list:
            res = re.search(search, c["title"], re.IGNORECASE)
            if res is not None:
                filtered.append(c)
        return filtered
    else:
        return course_list
