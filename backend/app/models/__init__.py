#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from app.models.faculty import Faculty
from app.models.course import Course
from app.models.student import Student
from app.models.student import student_course
from app.models.department import Department
