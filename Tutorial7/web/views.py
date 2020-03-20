from flask import render_template, redirect, url_for
from flask.views import MethodView

from .forms import UserForm
from .models import User
from .serializer import user, users
from ..database import db


class Greet(MethodView):
    def get(self, name=None):
        return render_template('home.html', name=name)


class UsersListView(MethodView):
    def get(self):
        users_list = User.query.all()
        serializer = users.dump(users_list)
        return render_template('user_list.html', users=serializer)


class UserCreateView(MethodView):
    def get(self):
        form = UserForm()
        return render_template('user_create.html', form=form)

    def post(self):
        form = UserForm()
        if form.validate_on_submit():
            print(form.data)
            user_ = User(first_name=form.first_name.data,
                         last_name=form.last_name.data,
                         email=form.email.data, password=form.password.data)
            db.session.add(user_)
            db.session.commit()
            return redirect(url_for('web.user_detail', id=user_.id))
        return render_template('user_create.html', form=form)


class UserDetailView(MethodView):

    def get(self, id):
        user_ = User.query.filter_by(id=id).first_or_404()
        serializer = user.dump(user_)
        return render_template('user_detail.html', user=serializer)
