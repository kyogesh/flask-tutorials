from flask import jsonify, request


def before():
    print('Run Before Request')
    if 'Authorization' not in request.headers:
        return jsonify({'message': "Unauthorized Access"}), 401


def after(req):
    print('Run after request')
    return req


def init_middlewares(app):
    app.before_request_funcs = {'greet': [before, ]}
    app.after_request(after)
