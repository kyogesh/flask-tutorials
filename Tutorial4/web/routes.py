from flask import Blueprint

from . import views

web_routes = Blueprint('web', __name__)


web_routes.add_url_rule('/', 'home', views.home)
web_routes.add_url_rule('/user/<int:id>/', 'user', views.get_user)
web_routes.add_url_rule('/users/', 'users', views.get_users)
web_routes.add_url_rule('/<string:name>/', 'greet', views.greet)
