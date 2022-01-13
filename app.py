import flask
from flask import request
import datetime
from pytz import timezone

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
    wordsList = words.replace('"', "").split(",")
    return wordsList

answers = loadAns()
validWords = loadWords()

# print(answers.index('favor')) -> 207
# start date = today - 207 days -> June 19, 2021
startDate = datetime.datetime(2021, 6, 19)
print(datetime.datetime.now()-startDate)
print(answers[207])

@app.route('/', methods=['GET'])
def root():
    return "hello world"


@app.route('/today', methods=['GET'])
def today():
    tz = timezone('EST')
    currDate = datetime.datetime.now(tz)
    ansIndex = (currDate - startDate).days
    return answers[ansIndex]

@app.route('/words', methods=['GET'])
def words():
    return validWords

@app.route('/day', methods=['GET'])
def day():
    tz = timezone('EST')
    currDate = datetime.datetime.now(tz)
    ansIndex = (currDate - startDate).days
    return "day " + ansIndex


