from . import views


def init_routes(app):
    if app:
        app.add_url_rule('/', 'home', views.home)
        app.add_url_rule('/<string:name>', 'greet', views.greet)

