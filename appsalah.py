from flask import Flask, request, json, jsonify

import requests
import os
app = Flask(__name__)

@app.route('/quiz', methods=['POST'])
def createQuiz():

    body = json.dumps(request.json)

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes":[]
    }

    if os.path.exists('./quizzes-file.json'):
        quizzesFile = open('./quizzes-file.json', 'r')
        quizData = json.load(quizzesFile)

    else:
        quizzesFile = open('quizzes-file.json', 'x')
        print("file ga ada")

    quizzesFile = open('./quizzes-file.json', 'w')
    quizData["quizzes"].append(body)
    quizzesFile.write(str(json.dumps(quizData)))



    return str(quizData)

# /quiz/<quiz-id
#

@app.route('/question', methods=['POST'])
def createQuestion():
    body = json.dumps(request.json)

    questionData = {
        "questions":[]
    }

    if os.path.exists('./question-file.json'):
        questionFile = open('./question-file.json', 'r')
        print("File ada")
        questionData = json.load(questionFile)

    else:
        questionFile = open('question-file.json', 'x')
        print("file ga ada")

    questionFile = open('./question-file.json', 'w')
    questionData["questions"].append(body)
    questionFile.write(str(json.dumps(questionData)))



    return str(questionData)

@app.route('/quizzes/<quizId>')
def getQuiz(quizId):
    quizzesFile = open('./quizzes-file.json')
    quizzesData = json.load(quizzesFile)

    for quiz in quizData["quizzes"]:
        quiz = json.loads(quiz)
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    questionFile = open('./question-file.json')
    questionsData = json.load(questionsFile)
   

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

@app.route('/quizzes/<quizId>/questions/<questionNumber>')
def getThatQuestion(quizId, questionNumber):
    quizData = getQuiz(int(quizId)).json

    for question in quizData["question-list"]:
        if question["question-number"] == int(questionNumber):
            return jsonify(question)



# /quiz/<quiz-id
#
@app.route('/questions/<questionNumber>')
def getQuestion(questionNumber):
    questionFile = open('./question-file.json')
    questionData = json.load(questionFile)
    print(type(questionData))

    for question in questionData["questions"]:
        question = json.loads(question)
        if question["question-number"] == int(questionNumber):
            return str(question)

    return "gak ketemu soalnya"

historyUser=[]


@app.route('/codewars/history') 
def getSeachHistory():
    historyFile = open("history-user", 'r')
    return historyFile.read()

@app.route('/codewars/<username>')
def getUserInfo(username):
    historyFile = open("history-users", "a")
    historyFile.write(username)
    historyUser.append(username)

    data = requests.get("https://www.codewars.com/api/v1/users/%s" % username)
    # score = requests.get("https://www.codewars.com/api/v1/users/%s" % honor)
    theName = data.json()["name"]
    theHonor = data.json()["honor"]

    result =  "Saya yang bernama %s mempunyai nilai %s" % (theName,theHonor)
    return result


   



@app.route('/') #example = google.com
def home():
    return "<h1>Pulang Kuuyyy</h1>"

@app.route('/jam-pulang')
def jamPulang():
    return "Sekarang sudah saatnya"

@app.route('/kalkulator-sederhana/<numb1>/<numb2>')
def summation(numb1, numb2):
    numb1 = int(numb1)
    numb2 = int(numb2)

    result = numb1 + numb2
    return str(result)

@app.route('/kalkulator-sederhana')
def pengurangan():
    numb1 = request.args.get('numb1')
    numb2 = request.args.get('numb2')

    numb1 = int(numb1)
    numb2 = int(numb2)

    result = numb1 - numb2
    return str(result)

