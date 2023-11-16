#!/usr/bin/python3
"""This script contains functions to aid enrollments"""

from app.models import Student, Course, Enrollment, db


def link_course_to_student(student_id, course_id, grade):
    """This function links a student to a course and
    sets the grade if one is specified
    """
    # Retreive the specified student and course from the db
    student = Student.query.filter_by(id=student_id).first()
    if student is None:
        return -1
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return -1

    # check if the course id already linked to the student
    existing_enrollment = Enrollment.query.filter_by(
        student_id=student_id, course_id=course_id
    ).first()

    if existing_enrollment:
        existing_enrollment.grade = grade
    else:
        if grade is not "Nil":
            e = Enrollment(grade=grade)
        else:
            e = Enrollment()
        e.course = course
        student.courses.append(e)
        db.session.add(e)
        db.session.add(course)
        db.session.add(student)
        db.session.commit()
    return 0
