#!/usr/bin/python3
"""This script contains the faculty class"""

from app.models import db


class Faculty(db.Model):
    """This contains the column declarations for
    faculties table
    """

    __tablename__ = "faculties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    departments = db.relationship("Department", backref="faculty")
