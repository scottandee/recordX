#!/usr/bin/python3
"""This contains course class"""

from app.models import db


class Course(db.Model):
    """This contains the columns declaration for the
    courses table"""

    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    instructor = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    students = db.relationship(
        "Enrollment", back_populates="course", cascade='all, delete-orphan'
    )
