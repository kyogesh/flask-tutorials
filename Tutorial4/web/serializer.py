from flask_marshmallow import Marshmallow

ma = Marshmallow()


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
