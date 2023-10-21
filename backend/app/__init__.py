#!/usr/bin/python3
"""Declaration of factory method"""

from flask import Flask
from app.models import db
from app.api.v1.views import api_v1


def create_app(config):
    """This function creates a new app"""
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(api_v1)
    return app
