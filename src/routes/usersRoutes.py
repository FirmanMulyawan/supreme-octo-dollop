from flask import request, json, jsonify
import os
from pathlib import Path

from ..utils.crypt import encrypt, decrypt
from . import router, baseLocation

usersFileLocation = baseLocation / "data" / "users-file.json"




@router.route('/alaala')
def alaala():
    return "sampe"

@router.route('/users', methods=['POST'])
def registration():
    body = request.json
    body["password"] = encrypt(body["password"]) # encrypt dulu password sebelum masuk database
    
    userData = []

    if os.path.exists(usersFileLocation) and os.path.getsize(usersFileLocation) > 0:
        usersFile = open(usersFileLocation)
        userData = json.load(usersFile)     

    userData.append(body)

    usersFile = open(usersFileLocation, 'w')
    usersFile.write(str(json.dumps(userData)))

    return jsonify(userData)

@router.route('/users/login', methods=['POST'])
def login():
    body = request.json
    
    usersFile = open(usersFileLocation)
    usersData = json.load(usersFile)

    isLogin = False
    #password Matched = False
    for user in usersData:        
        if user["username"] == body["username"]:
            # userFound = True
            if decrypt(user["password"]) == body["password"]: # password di database di-decrypt dulu
                isLogin = True
                break
    body["status"] = isLogin
    if isLogin:
        body["message"] = "berhasil login"
    # if userFound and passwordMatched:
    else:
        body["message"] = "username atau password tidak sesuai"

    return jsonify(body)
    #     # result = "Selamat datang, " + body["username"]        
    # else:
    #     return jsonify("Username atau password tidak sesuai")
    #     # result = "Username atau password tidak sesuai"