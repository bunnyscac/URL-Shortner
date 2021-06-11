from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .models import Link


shortner = Blueprint('shortner', __name__)


@shortner.route('/<short_url>')
def redirect_url_to(short_url):
    return ""


@shortner.route('/create_link', methods=["POST"])
def create_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_success.html',
                           new_url=link.short_url, original_url=link.original_url)


@shortner.route('/')
def index():
    return render_template("index.html")


@shortner.route('/analytics')
def analytics():
    return ""


@shortner.errorhandler(404)
def page_not_found():
    return '<h1>WOAPS! PAGE NOT FOUND</h1>', 404
