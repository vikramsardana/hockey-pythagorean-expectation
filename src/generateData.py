'''
Created on Oct 22, 2018

@author: Vikram
'''
import random
import pandas as pd

goalsPerGame = 3.02
pythagExponent = goalsPerGame ** 0.458
goalieData = pd.read_csv("GoalieData.csv")

def getGoalieWinPercentages():
    goalieData["goalieExpectedWinGames"] = 0.0
    goalieData["goalieExpectedWinPercentage"] = 0.0
    goalieData["goalieActualWinPercentage"] = 0.0
    for index, row in goalieData.iterrows():
        goalsFor = row["oiGF"]
        numerator = goalsFor ** pythagExponent
        goalsAgainst = row["GA"]
        denominator = (goalsFor ** pythagExponent) + (goalsAgainst ** pythagExponent)
        pythagValue = float(numerator) / float(denominator)
        goalieData.loc[index, "goalieExpectedWinPercentage"] = pythagValue
        goalieData.loc[index, "goalieExpectedWinGames"] = pythagValue * row["GP"]
        goalieData.loc[index, "goalieActualWinPercentage"] = float(row["Wins"]) / float(row["GP"])


def getTeamWinPercentages():
    goalieData["teamExpectedWinGames"] = 0.0
    goalieData["teamExpectedWinPercentage"] = 0.0
    goalieData["teamActualWinPercentage"] = 0.0
    for index, row in goalieData.iterrows():
        goalsFor = row["TeamGF"]
        numerator = goalsFor ** pythagExponent
        goalsAgainst = row["TeamGA"]
        denominator = (goalsFor ** pythagExponent) + (goalsAgainst ** pythagExponent)
        pythagValue = float(numerator) / float(denominator)
        goalieData.loc[index, "teamExpectedWinPercentage"] = pythagValue
        goalieData.loc[index, "teamExpectedWinGames"] = pythagValue * row["TeamGP"]
        goalieData.loc[index, "teamActualWinPercentage"] = float(row["TeamW"]) / float(row["TeamGP"])


def getDifferences():
    goalieData["goalieExpectedMinusActualPercentage"] = goalieData['goalieExpectedWinPercentage'] - goalieData['goalieActualWinPercentage']
    goalieData["goalieExpectedMinusActualGames"] = goalieData['goalieExpectedWinGames'] - goalieData['Wins']
    goalieData["goalieExpectedMinusTeamPercentage"] = goalieData['goalieExpectedWinPercentage'] - goalieData['teamExpectedWinPercentage']
    goalieData["teamExpectedMinusActualPercentage"] = goalieData['teamExpectedWinPercentage'] - goalieData['teamActualWinPercentage']
    goalieData["teamExpectedMinusActualGames"] = goalieData['teamExpectedWinGames'] - goalieData['TeamW']
    

def sortByGoaliePercentDifference():
    goalieData2 = goalieData
    goalieData2 = goalieData2.sort_values('goalieExpectedMinusActualPercentage', ascending=False)
    goalieData2.to_csv("goaliePercentDifferenceOutput.csv")

def sortByGoalieWinDifference():
    goalieData2 = goalieData
    goalieData2 = goalieData2.sort_values('goalieExpectedMinusActualGames', ascending=False)
    goalieData2.to_csv("goalieWinDifferenceOutput.csv")

def sortByGoalieVsTeam():
    goalieData2 = goalieData
    goalieData2 = goalieData2.sort_values('goalieExpectedMinusTeamPercentage', ascending=False)
    goalieData2.to_csv("goalieVsTeamOutput.csv")
    
def sortByTeamPercentDifference():
    goalieData2 = goalieData
    goalieData2 = goalieData2.sort_values('teamExpectedMinusActualPercentage', ascending=False)
    goalieData2.to_csv("goalieTeamPercentDifferenceOutput.csv")
    
def sortByTeamWinDifference():
    goalieData2 = goalieData
    goalieData2 = goalieData2.sort_values('teamExpectedMinusActualGames', ascending=False)
    goalieData2.to_csv("goalieTeamWinDifferenceOutput.csv")
    


def getDataOutput():
    goalieData.to_csv("goalieDataOutput.csv")

if __name__ == '__main__':
    getGoalieWinPercentages()
    getTeamWinPercentages()
    getDifferences()
    sortByGoaliePercentDifference()
    sortByGoalieWinDifference()
    sortByGoalieVsTeam()
    sortByTeamPercentDifference()
    sortByTeamWinDifference()
    getDataOutput()
