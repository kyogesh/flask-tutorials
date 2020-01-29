import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import init_routes
from .models import User, Address


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sample.db')

db = SQLAlchemy(app)

init_routes(app)

@app.cli.command('db_drop')
def db_drop():
    with app.app_context():
        db.drop_all()
    print('DB Created!')


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('DB Dropped')


@app.cli.command('insert_data')
def insert_data():
    user1 = User(first_name='Some', last_name='One', email='someone@email.com', password='strongpass')
    user2 = User(first_name='Other', last_name='One', email='otherone@email.com', password='betterpass')

    db.session.add(user1)
    db.session.add(user2)
