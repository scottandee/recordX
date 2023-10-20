#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from backend.models.faculty import Faculty
from backend.models.course import Course
from backend.models.student import Student
from backend.models.student import student_course
from backend.models.department import Department
