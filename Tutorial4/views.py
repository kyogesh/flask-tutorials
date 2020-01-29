import jsonify

from flask import current_app

from .models import User, Address


def home():
    return '<h1> Hello World!</h1>'


def greet(name):
    return f'<h1> Hello {name.title()}!</h1>'


def users():
    users = User.query.all()
    return jsonify(users)
