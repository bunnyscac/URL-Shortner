from flask import Blueprint

shortner = Blueprint('shortner', __name__)


@shortner.route('/<short_url>')
def redirect_url_to(short_url):
    return ""
