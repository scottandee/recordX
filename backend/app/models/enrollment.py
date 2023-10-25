#!/usr/bin/python3
"""This contains the enrollment class"""

from app.models import db


grades = ["A", "B", "C", "D", "E", "Nil"]


class Enrollment(db.Model):
    """This contains the columns declaration for the
    enrollment class
    """
    __tablename__ = "enrollments"
    student_id = db.Column(
        db.Integer, db.ForeignKey("students.id"), primary_key=True
    )
    course_id = db.Column(
        db.Integer, db.ForeignKey("courses.id"), primary_key=True
    )
    grade = db.Column(db.Enum(*grades), default="Nil", nullable=False)
    course = db.relationship('Course', back_populates='students')
    student = db.relationship('Student', back_populates='courses')
