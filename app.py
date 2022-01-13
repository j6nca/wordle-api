import flask
import datetime
import pytz

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



@app.route('/answer', methods=['GET'])
def answer():
    tz = pytz.timezone('EST')
    startDateTZ = tz.localize(startDate)
    currDate = datetime.datetime.now(tz)
    ansIndex = (currDate - startDateTZ).days
    return answers[ansIndex]

@app.route('/words', methods=['GET'])
def words():
    return validWords

@app.route('/day', methods=['GET'])
def day():
    tz = pytz.timezone('EST')
    startDateTZ = tz.localize(startDate)
    currDate = datetime.datetime.now(tz)
    ansIndex = (currDate - startDateTZ).days
    return str(ansIndex)


