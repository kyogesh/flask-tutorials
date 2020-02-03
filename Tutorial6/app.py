from flask import Flask, request


app = Flask(__name__)


def before():
    print('Run before request')


def after(req):
    print('Run after request')
    return req


app.before_request(before)
app.after_request(after)


@app.route('/')
def index():
    print('Inside Request')
    # headers = list([header for header in request.headers])
    return f"{request.query_string} ======== {request}"
