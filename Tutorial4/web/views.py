from flask import jsonify

from Tutorial4.database import db
from .models import User


def home():
    return '<h1> Hello World!</h1>'


def greet(name):
    return f'<h1> Hello {name.title()}!</h1>'


def get_users():
    users = db.session.query(User)
    return jsonify({'messages': 'There should be a list of users here!',
                    'users': [users]})
