from flask import Blueprint
import json

home = Blueprint("home", __name__)


@home.route('/')
def get_home():
    return json.dumps({
        "message": "this is a home page"
    })
