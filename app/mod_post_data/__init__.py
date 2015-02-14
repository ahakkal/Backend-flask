from flask import Blueprint

register = Blueprint('post', __name__)

from . import controllers