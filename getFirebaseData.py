from firebase import firebase
from firebaseKey import *
import json
import numpy as np

def updateUserScore(user, amt):  # get the first sheet of the spreadsheet
    location = "Users/" + str(user)
    currentScore = getCurrentScore(location)
    if currentScore is None:
        newScore = amt
    else:
        newScore = amt + currentScore
    firebase.put(location, "totalScore", newScore)
    firebase.put(location, "mostRecentGame", amt)
    updateGamesPlayed(location)

def getCurrentScore(loc):
    return firebase.get(loc, "totalScore")

def getGamesPlayed(loc):
    return firebase.get(loc, "gamesPlayed")

def updateGamesPlayed(loc):
    if getGamesPlayed(loc) is None:
        games = 1
    else:
        games = getGamesPlayed(loc) + 1
    firebase.put(loc, "gamesPlayed", games)
def sortPlayerOrder():
    playerNames = []
    playerNum = []
    playerScores = []
    playerData = []
    result = firebase.get("Users", None)
    for key, value in result.items():
        playerData.append([key,result[key]['totalScore']])

    #sort based on high score
    print (playerData)
    playerData =sorted(playerData, key=lambda x:x[1], reverse = True)
    print (playerData)
    return playerData

#updateUserScore("medina", 17)
sortPlayerOrder()