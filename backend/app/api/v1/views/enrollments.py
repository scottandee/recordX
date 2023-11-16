#!/usr/bin/python3
"""This script contains the enrollments
endpoints
"""
from flask import request, abort

from app.api.v1.views import api_v1
from app import db
from app.models import Enrollment
from app.models import Student
from app.models import Course
from app.utils.dict_cleanup import dict_cleanup


@api_v1.route("/students/<int:student_id>/courses", strict_slashes=False)
def get_all_courses_for_student(student_id):
    """This method returns a list of all
    courses a student is enrolled in
    """
    # Declare a list that will contain all the dict repr. of the
    # student's courses
    sc_list = []

    # Retreive the student object from the db
    student = Student.query.filter_by(id=student_id).first()
    if student is None:
        abort(404)

    # Retrive the courses the student is enrolled in
    enrollments = student.courses

    # Convert all course objects into dict repr, add corresponding
    # grade and append to student's courses list
    for e in enrollments:
        data = {}
        data["course"] = dict_cleanup(e.course)
        data["grade"] = e.grade
        sc_list.append(data)
    return sc_list


@api_v1.route(
    "students/<int:student_id>/courses/<int:course_id>",
    methods=["POST"], strict_slashes=False
)
def link_course_to_student(student_id, course_id):
    """This function links a student to a course and
    sets the grade if one is specified
    """
    # Error Checking
    if not request.is_json:
        return abort(400, "Not a JSON")

    # Retrieve student object from db
    student = Student.query.filter_by(id=student_id).first()

    # Return 404 if it doesn't exist
    if student is None:
        abort(404)

    # Retrieve the course object that is to be
    course = Course.query.filter_by(id=course_id).first()
    # Return 404 if it doesn't exist
    if course is None:
        abort(404)
    course_dict_repr = dict_cleanup(course)

    # check if the course id already linked to the student
    existing_enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    # Send a return code of 200 if it already exists.
    # If not, add the course and set the return code to 201
    if existing_enrollment:
        return_code = 200
    else:
        data = request.json
        if data.get("grade"):
            e = Enrollment(grade=data.get("grade"))
        else:
            e = Enrollment()
        e.course = course
        student.courses.append(e)
        db.session.add(e)
        db.session.add(course)
        db.session.add(student)
        db.session.commit()
        return_code = 201

    return course_dict_repr, return_code


@api_v1.route(
    "students/<int:student_id>/courses/<course_id>",
    methods=["PUT"], strict_slashes=False
)
def update_enrollment_grade(student_id, course_id):
    """This function updates the grade of
    an enrollment
    """
    # Error checking
    if not request.is_json:
        return abort(400, "Not a JSON")

    # Retreive the enrollment from the db
    existing_enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    # If the enrollment is not found, return a 404 error
    if not existing_enrollment:
        abort(404)

    # Store the request query parameters in a data variable
    data = request.json
    if not data.get("grade"):
        abort(400, "Grade is missing")

    # Set the grade and save to the db
    existing_enrollment.grade = data.get("grade")
    dict_repr = dict_cleanup(existing_enrollment)

    db.session.add(existing_enrollment)
    db.session.commit()
    return dict_repr, 200


@api_v1.route(
    "students/<int:student_id>/courses/<course_id>",
    methods=["DELETE"], strict_slashes=False
)
def delete_enrollment(student_id, course_id):
    """This function deletes the enrollment with
    the specified course and student id
    """
    # Retrieve the enrollment from the db
    enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    # Return a 404 error if it is not found
    if not enrollment:
        abort(404)
    db.session.delete(enrollment)
    db.session.commit()
    return {}, 200
