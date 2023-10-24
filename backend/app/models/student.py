#!/usr/bin/python3
"""This contains the student class"""

from app.models import db


gender = ["Male", "Female"]


class Student(db.Model):
    """This contains columns declaration for the
    students table"""

    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    matric_number = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.Enum(*gender), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    courses = db.relationship("Enrollment", back_populates="student")
