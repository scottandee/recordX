#!/usr/bin/python3
"""This is script creates an instance of the
app and runs it"""

from app import create_app, db
from config import Config


if __name__ == "__main__":
    app = create_app(Config)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
