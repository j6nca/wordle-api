import flask
from flask import request
from datetime import datetime as dt
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # arg = request.args['arg1']
    return "hello world"


