from flask import Flask, request, jsonify, Blueprint, url_for


app = Flask(__name__)


def before():
    if 'Authorization' not in request.headers:
        return jsonify({'message': "Unauthorized Access"}), 401


def after(req):
    print('Run after request')
    return req


bp = Blueprint('web', __name__)


def index():
    print('Inside Request')
    # headers = list([header for header in request.headers])
    return f"{request.query_string} ======== {request}"


bp.add_url_rule('/', 'index', index)

app.register_blueprint(bp)
app.before_request_funcs = {None: [before, ]}
app.after_request(after)
