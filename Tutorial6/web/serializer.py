from flask_marshmallow import Marshmallow
from marshmallow import post_load

from .models import User

ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        load_only = ('password', )
    
    @post_load
    def create_user(self, data, **kwargs):
        return User(**data)
        


class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'house_num', 'street', 'locality', 'city',
                  'state', 'pincode', 'present')


user = UserSchema()
users = UserSchema(many=True)

address = AddressSchema()
addresses = AddressSchema(many=True)
