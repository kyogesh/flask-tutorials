from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    from . import database
    database.db.init_app(app)
    db = database.db

    migrate = Migrate(app, db)

    from .web.routes import web_routes
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
        from .web.models import User
        user1 = User(first_name='Some', last_name='One', email='someone@email.com',
                     password='strongpass')
        user2 = User(first_name='Other', last_name='One',
                     email='otherone@email.com', password='betterpass')

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        print('data inserted!')
    return app
