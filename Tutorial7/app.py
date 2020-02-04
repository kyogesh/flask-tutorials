# import os
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy_utils import PasswordType
#
# from Tutorial4.web.routes import init_routes
# from Tutorial4.web.models import User
#
#
# app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
#                                                                     'sample.db')
# db = SQLAlchemy(app)
#
# init_routes(app)
#
#
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True)
#     password = Column(PasswordType(
#         schemes=[
#             'pbkdf2_sha512',
#             'md5_crypt'
#         ],
#         deprecated=['md5_crypt']))
#
#
# class Address(db.Model):
#     __tablename__ = 'addresses'
#     user = ForeignKey('users', cascade='delete')
#     house_num = Column(Integer, primary_key=True)
#     street = Column(String)
#     locality = Column(String)
#     city = Column(String)
#     state = Column(String)
#     pincode = Column(Integer)
#     present = Column(Boolean)
