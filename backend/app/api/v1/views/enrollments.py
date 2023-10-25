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
    sc_list = []
    student = Student.query.filter_by(id=student_id).first()
    if student is None:
        abort(404)
    enrollments = student.courses
    for e in enrollments:
        data = {}
        data["course"] = dict_cleanup(e.course)
        data["grade"] = e.grade
        sc_list.append(data)
    return sc_list


@api_v1.route(
    "students/<int:student_id>/courses/<course_id>",
    methods=["POST"], strict_slashes=False
)
def link_course_to_student(student_id, course_id):
    """This function links a student to a course and
    sets the grade if one is specified
    """
    if not request.is_json:
        return abort(400, "Not a JSON")
    student = Student.query.filter_by(id=student_id).first()
    if student is None:
        abort(404)
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        abort(404)
    course_dict_repr = dict_cleanup(course)

    # check if the course id already linked to the student
    existing_enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

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
    if not request.is_json:
        return abort(400, "Not a JSON")

    existing_enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    if not existing_enrollment:
        abort(404)
    data = request.json
    if not data.get("grade"):
        abort(400, "Grade is missing")
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
    enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    if not enrollment:
        abort(404)
    db.session.delete(enrollment)
    db.session.commit()
    return {}, 200
