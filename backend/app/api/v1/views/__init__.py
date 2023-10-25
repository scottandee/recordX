#!/usr/bin/python3
from flask import Blueprint


api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1/")

from app.api.v1.views.index import *
from app.api.v1.views.faculties import *
from app.api.v1.views.departments import *
from app.api.v1.views.courses import *
from app.api.v1.views.students import *
from app.api.v1.views.enrollments import *
