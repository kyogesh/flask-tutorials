from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy_utils import PasswordType

from ..database import db


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
    present = Column(Boolean, default=True)
