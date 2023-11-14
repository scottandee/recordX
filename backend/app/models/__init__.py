#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy

# Instantiation of an SQLAlchemy instance
db = SQLAlchemy()

from app.models.faculty import Faculty
from app.models.enrollment import Enrollment
from app.models.student import Student
from app.models.course import Course
from app.models.department import Department
