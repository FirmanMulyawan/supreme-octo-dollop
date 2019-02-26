from flask import Flask, request, json, jsonify
import requests
import os

from src.routes import router

app = Flask(__name__)
app.register_blueprint(router)

# quizzesFilePath = './quizzes-file.json'
# questionsFilePath = './question-file.json'
# gamesFilePath = './games-file.json'
# usersFilePath = './users-file.json'

if __name__ == "__main__":
    app.run(debug=True, port=1989)