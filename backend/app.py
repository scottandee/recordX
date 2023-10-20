#!/usr/bin/python3
"""This is the entry point into the backend"""

from flask import Flask
from backend.config import Config
from backend.models import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
