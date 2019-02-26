from flask import json

def writeFile(fileLocation, data):
    theFile = open(fileLocation, "w")
    theFile.write(str(json.dumps(data)))    

def readFile(fileLocation):
    theFile = open(fileLocation)
    data = json.load(theFile)
    return data
    
def checkFile():

    return "checkFile"