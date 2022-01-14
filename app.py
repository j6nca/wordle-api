import flask
import datetime
import pytz
import random

app = flask.Flask(__name__)

def loadAns():
    ansFile = open("answers", "r")
    ans = ansFile.read()
    ansFile.close()
    ansList = ans.replace('"', "").split(",")
    return ansList

def loadWords():
    wordsFile = open("words", "r")
    words = wordsFile.read()
    wordsFile.close()
    return words

def getAnsIndex():
    tz = pytz.timezone('EST')
    startDateTZ = tz.localize(startDate)
    currDate = datetime.datetime.now(tz)
    return (currDate - startDateTZ).days

answers = loadAns()
validWords = loadWords()

# print(answers.index('favor')) -> 207
# start date = today - 207 days -> June 19, 2021
startDate = datetime.datetime(2021, 6, 19)
# tz = pytz.timezone("EST")
# startDate = tz.localize(startDate)
# print(datetime.datetime.now(tz)-startDate)
# print(answers[207])

@app.route('/', methods=['GET'])
def root():
    return 'api for wordle, view <a href=https://github.com/jngbot/wordle-api>repo</a> for usage'


# Dailies

@app.route('/answer', methods=['GET'])
def answer():
    return answers[getAnsIndex()]

@app.route('/day', methods=['GET'])
def day():
    return str(getAnsIndex())

# Misc

@app.route('/words', methods=['GET'])
def words():
    return validWords

# Games?
@app.route('/random', methods=['GET'])
def randAnswer():
    return random.choice(answers)

@app.route('/random2', methods=['GET'])
def randWords():
    return random.choice(validWords)


