from flask import Blueprint, Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy_utils import PasswordType


ma = Marshmallow()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

db.init_app(app)


def home():
    return '<h1> Hello World!</h1>'


def greet(name):
    return f'<h1> Hello {name.title()}!</h1>'


def get_users():
    users_list = User.query.all()
    serializer = users.dump(users_list)
    return jsonify({'messages': 'There should be a list of users here!',
                    'users': serializer})


web_routes = Blueprint('web', __name__)

web_routes.add_url_rule('/', 'home', home)
web_routes.add_url_rule('/<string:name>/', 'greet', greet)
web_routes.add_url_rule('/users/', 'users', get_users)

app.register_blueprint(web_routes)


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('DB Dropped!')


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('DB Created')


@app.cli.command('insert_data')
def insert_data():
    user1 = User(first_name='Some', last_name='One', email='someone@email.com',
                    password='strongpass')
    user2 = User(first_name='Other', last_name='One',
                    email='otherone@email.com', password='betterpass')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print('data inserted!')


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        load_only = ('password', )
        

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'house_num', 'street', 'locality', 'city',
                  'state', 'pincode', 'present')


user = UserSchema()
users = UserSchema(many=True)

address = AddressSchema()
addresses = AddressSchema(many=True)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(length=100, convert_unicode=True))
    last_name = Column(String(length=100, convert_unicode=True))
    email = Column(String(length=255, convert_unicode=True), unique=True)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']))


class Address(db.Model):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user = ForeignKey('users', cascade='delete')
    house_num = Column(Integer)
    street = Column(String(length=100, convert_unicode=True))
    locality = Column(String(length=100, convert_unicode=True))
    city = Column(String(length=100, convert_unicode=True))
    state = Column(String(length=100, convert_unicode=True))
    pincode = Column(Integer)
    present = Column(Boolean)
