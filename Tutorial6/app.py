from flask import Flask, request, jsonify, Blueprint, url_for


app = Flask(__name__)


def before():
    print('Run Before Request')
    if 'Authorization' not in request.headers:
        return jsonify({'message': "Unauthorized Access"}), 401


def after(req):
    print('Run after request')
    return req


bp = Blueprint('web', __name__)
bp2 = Blueprint('greet', __name__)


def index():
    print('Inside Request')
    # headers = list([header for header in request.headers])
    return f"{request.query_string} ======== {request}"


def greet(name=None):
    if not name:
        return '<h1> Hello World! </h1>'
    return f'<h1> Hello {name.title()}! </h1>'

bp.add_url_rule('/', 'index', index)

bp2.add_url_rule('/greet/', 'greet', greet)
bp2.add_url_rule('/greet/<string:name>', 'greet_user', greet)

app.register_blueprint(bp)
app.register_blueprint(bp2)
app.before_request_funcs = {'web': [before, ]}
app.after_request(after)
