#!/usr/bin/python3
"""This script contains the students
endpoints"""

import re
from flask import abort, jsonify, request
from datetime import datetime

from app.api.v1.views import api_v1
from app.utils.dict_cleanup import dict_cleanup
from app.utils.enrollments import link_course_to_student
from app.models import db
from app.models.student import Student
from app.models.department import Department


@api_v1.route(
    "/departments/<int:id>/students", methods=["GET"], strict_slashes=False
)
def get_students_in_department(id):
    """This returns all of the students
    that belong to the specified department
    """
    # get dept with id specified
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)
    student_list = []

    # get all the students linked to the dept
    students = dept.students

    for s in students:
        dict_repr = dict_cleanup(s)
        student_list.append(dict_repr)
    return student_list


@api_v1.route(
    "/departments/<int:id>/students", methods=["POST"], strict_slashes=False)
def create_student(id):
    """This creates a new student"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")

    requirements = [
        "first_name", "last_name", "email", "gender", "matric_number", "dob"
    ]
    for r in requirements:
        if r not in request.json.keys():
            abort(400, f"Missing {r}")

    data = request.json
    matrics = [c.matric_number for c in Student.query.all()]
    emails = [c.email for c in Student.query.all()]
    if data["matric_number"] in matrics:
        abort(400, "matric number already exists")
    if data["email"] in emails:
        abort(400, "email already exists")

    # retrive department id specified from db
    dept = Department.query.filter_by(id=id).first()
    if dept is None:
        abort(404)

    data["dob"] = datetime.strptime(data["dob"], '%Y-%m-%d')

    # Filter out all specified enrollments
    enrollments = {}
    for key, value in data.items():
        try:
            k = int(key)
            enrollments[key] = value
        except ValueError:
            continue

    # cleanse the data dict of all enrollmens
    for key in enrollments.keys():
        del data[key]

    # create a new student with specified data
    student = Student(**data)
    dict_repr = dict_cleanup(student)

    # add the created student to the department that was just
    # retreived from the db
    dept.students.append(student)
    db.session.add(student)
    db.session.add(dept)
    db.session.commit()

    # add all course enrollments to the student
    student = Student.query.filter_by(email=dict_repr["email"]).first()
    for key, value in enrollments.items():
        e = link_course_to_student(student.id, int(key), value)
        if e == -1:
            abort(400, "error in grades")

    return dict_repr, 201


@api_v1.route("/students/<int:id>", methods=["PUT"], strict_slashes=False)
def update_student(id):
    """This updates a student"""
    # error checking
    if not request.is_json:
        abort(400, "Not a JSON")
    data = request.json

    if "matric_number" in data.keys():
        matrics = [c.matric_number for c in Student.query.all()]
        if data["matric_number"] in matrics:
            abort(400, "matric number already exists")

    if "email" in data.keys():
        emails = [c.email for c in Student.query.all()]
        if data["email"] in emails:
            abort(400, "email already exists")

    # retrieve student to be updated from db
    student = Student.query.filter_by(id=id).first()
    if student is None:
        abort(404)

    # update the student with values specified
    for key, value in data.items():
        setattr(student, key, value)

    dict_repr = dict_cleanup(student)
    db.session.add(student)
    db.session.commit()

    return dict_repr, 200


@api_v1.route("/students/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_student(id):
    """This function deletes the specified
    student
    """
    student = Student.query.filter_by(id=id).first()
    if student is None:
        abort(404)
    db.session.delete(student)
    db.session.commit()
    return {}, 200


@api_v1.route("/students_search", methods=["POST"], strict_slashes=False)
def students_search():
    """This function loads up students from
    the db that match a particular pattern.
    IF no pattern is specified, it loads up
    all students from the db
    """
    if not request.is_json:
        abort(400, "Not a JSON")

    data = request.json
    student_list = []
    students = None

    # check if a department id is specified.
    if data.get("department_id"):
        dept = Department.query.filter_by(id=data.get("department_id")).first()
        if dept is None:
            abort(404)
        if data.get("course_id"):
            courses = dept.courses
            cse = None
            for c in courses:
                if c.id == data.get("course_id"):
                    cse = c
                    break
            if cse is not None:
                students = cse.students
            else:
                abort(404)
        else:
            students = dept.students
    else:
        students = Student.query.all()

    for s in students:
        dict_repr = dict_cleanup(s)
        student_list.append(dict_repr)

    # check if there's a search pattern defined
    if data.get("pattern"):
        filtered = []
        search = "[a-zA-Z]*{}[a-zA-Z]*".format(data.get("pattern"))

        for s in student_list:
            res = re.search(search, s["first_name"], re.IGNORECASE)
            if res is not None:
                filtered.append(s)
                continue
            res = re.search(search, s["last_name"], re.IGNORECASE)
            if res is not None:
                filtered.append(s)

        return filtered
    else:
        return student_list
