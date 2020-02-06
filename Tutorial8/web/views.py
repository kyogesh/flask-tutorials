from flask import jsonify, request, render_template, redirect, url_for
from flask.views import MethodView

from ..database import db
from .models import User
from .serializer import user, users, address, addresses


class Greet(MethodView):
    def get(self, name=None):
        return render_template('home.html', name=name)


class UsersListView(MethodView):

    def get(self):
        users_list = User.query.all()
        serializer = users.dump(users_list)
        return render_template('user_list.html', users=serializer)


class UserDetailView(MethodView):

    def get(self, id):
        user_ = User.query.filter_by(id=id).first_or_404()
        serializer = user.dump(user_)
        return render_template('user_detail.html', user=serializer)

    def post(self):
        user_obj = user.load(request.json)
        db.session.add(user_obj)
        db.session.commit()
        serializer = user.dump(user_obj)
        return redirect(url_for('web.user_detail', id=serializer['id']))
