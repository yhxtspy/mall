from flask import Blueprint

import factory

user = Blueprint('user', __name__)

from . import views
