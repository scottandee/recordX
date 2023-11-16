#!/usr/bin/python3
"""This contains the configuration for
the application
"""

import os


class Config:
    """This contains configuration for the
    sqlalchemy db
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
