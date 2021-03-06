from flask import request, json, jsonify
import os
from random import randint

from . import router, baseLocation, quizzesFileLocation, gamesFileLocation, questionFileLocation
from ..utils.file import readFile, writeFile


@router.route('/game', methods=['POST'])
def createGame():
    body = request.json

    quizzesData = readFile(questionFileLocation)

    for quiz in quizzesData["quizzes"]:
        if quiz["quiz-id"] == int(body["quiz-id"]):
            gameInfo = quiz
    
    gameInfo["game-pin"] = randint(100000,999999)
    gameInfo["user-list"] = []
    gameInfo["leaderboard"] = []

    gamesData ={
        "game-list":[]
    }    

    if os.path.exists(gamesFileLocation):
        gamesData = readFile(gamesFileLocation)
        gamesData["game-list"].append(gameInfo) 

        writeFile(gamesFileLocation, gamesData)

    return jsonify(gameInfo)

@router.route('/game/join', methods=['POST'])
def joinGame():
    body = request.json

    gamesData = readFile(gamesFileLocation)

    position = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == int(body["game-pin"]):
            if body["username"] not in game["user-list"]: # kalau usernamenya udah ada, jangan di append
                game["user-list"].append(body["username"])
                game["leaderboard"].append({
                    "username": body["username"],
                    "score": 0
                })

                gameInfo = game
                position = i
                break
            # todo : error kalau usernya udah dipake

        gamesData["game-list"][position] = gameInfo
        writeFile(gamesFileLocation, gamesData)

    return jsonify(request.json)

@router.route('/game/answer', methods=['POST'])
def submitAnswer():    
    isTrue = False
    body = request.json

    questionData = readFile(questionFileLocation)

    for question in questionData["questions"]:
        if question["quiz-id"] == int(body["quiz-id"]) and question["question-number"] == int(body["question-number"]):
            if question["answer"] == body["answer"]:
                isTrue = True

    gamesData = readFile(gamesFileLocation)
    
    gamePosition = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == int(body["game-pin"]):
            if isTrue:                
                userPosition = 0
                for j in range(len(game["leaderboard"])):
                    userData = game["leaderboard"][j]
                    
                    if userData["username"] == body["username"]:                        
                        userData["score"] += 100
                        
                        userInfo = userData
                        userPosition = j
                        break
                
                game["leaderboard"][userPosition] = userInfo
                gameInfo = game
                gamePosition = i
                break

    gamesData["game-list"][gamePosition] = gameInfo
    writeFile(gamesFileLocation, gamesData)
                
    return jsonify(request.json)

@router.route('/game/<gamePin>/leaderboard')
def getLeaderboard(gamePin):
   
    gamesData = readFile(gamesFileLocation)

    for game in gamesData["game-list"]:
        if game["game-pin"] == int(gamePin): #body["game-pin"]
            leaderboard = game["leaderboard"]
            break
    
    # todo: sorting dari score terbesar ke terkecil (selection sort)        
    for i in range(len(leaderboard)):
        largest = leaderboard[i]["score"]
        largestPosition = leaderboard[i]
        for j in range(i,len(leaderboard)):
            if leaderboard[j]["score"] >= largest:
                largest = leaderboard[j]["score"]
                largestPosition = leaderboard[j]
                positionCounter = j

        leaderboard[i], leaderboard[positionCounter] = largestPosition, leaderboard[i] # swap posisi pertama setiap looping dengan posisi largest

    return jsonify(leaderboard)

