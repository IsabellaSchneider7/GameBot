from firebase import firebase
from firebaseKey import *

def updateUserScore(user, amt):  # get the first sheet of the spreadsheet
    location = "Users/" + str(user)
    currentScore = getCurrentScore(location)
    if currentScore is None:
        newScore = amt
    else:
        newScore = amt + currentScore
    firebase.put(location, "totalScore", newScore)
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

updateUserScore("medina", 17)
