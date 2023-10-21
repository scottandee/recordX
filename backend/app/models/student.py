#!/usr/bin/python3
"""This contains the student class"""

from app.models import db


gender = ["Male", "Female"]
grades = ["A", "B", "C", "D", "E", "Nil"]


student_course = db.Table(
    "student_course",
    db.Column('student_id', db.Integer, db.ForeignKey("students.id")),
    db.Column('course_id', db.Integer, db.ForeignKey("courses.id")),
    db.Column("grade", db.Enum(*grades), default="Nil", nullable=False)
)


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
    courses = db.relationship(
        'Course', secondary="student_course", backref="students"
    )
