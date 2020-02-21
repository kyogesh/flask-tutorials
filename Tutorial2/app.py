import os

from flask import Flask

app = Flask(__name__)

# app.config.from_object('Tutorial2.settings.Test')
app.config.from_envvar('FLASK_SETTINGS')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '')


@app.route('/')
def show_config():
    return f'{app.testing=}'
