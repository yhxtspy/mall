from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('/')
def index():
    print(323442433)
    return "ojbk"





