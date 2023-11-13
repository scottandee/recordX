#!/usr/bin/python3
"""This script contains the department class"""

from app.models import db


class Department(db.Model):
    """This contains the column declarations for
    the departments table"""

    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    hod = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey("faculties.id"))
    students = db.relationship("Student", backref="department")
    courses = db.relationship("Course", backref="department")
