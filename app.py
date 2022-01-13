import flask
from flask import request
from datetime import datetime as dt
app = flask.Flask(__name__)

def loadAns():
    ansFile = open("answers", "r")
    ans = ansFile.read()
    ansFile.close()
    ansList = ans.replace('"', "").split(",")
    return ansList

def loadWords():
    wordsFile = open("answers", "r")
    words = wordsFile.read()
    wordsFile.close()
    return words

answers = loadAns()
valid_words = loadWords()

@app.route('/', methods=['GET'])
def root():
    return "hello world"


@app.route('/today', methods=['GET'])
def today():
    return "hello world"

@app.route('/words', methods=['GET'])
def words():
    return valid_words

