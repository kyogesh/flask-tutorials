from flask import jsonify

from Tutorial4.database import db
from .models import User
from .serializer import user, users, address, addresses

def home():
    return '<h1> Hello World!</h1>'


def greet(name):
    return f'<h1> Hello {name.title()}!</h1>'


def get_users():
    users_list = User.query.all()
    serializer = users.dump(users_list)
    return jsonify({'messages': 'There should be a list of users here!',
                    'users': serializer})
