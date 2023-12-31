#!/usr/bin/python3
"""This is script creates an instance of the
app and runs it"""

from app import create_app, db
from config import Config
from flask_cors import CORS


if __name__ == "__main__":
    app = create_app(Config)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
