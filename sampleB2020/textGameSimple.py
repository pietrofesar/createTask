import os
import time


# text color constants
G='\033[0;32m'    # green
Y='\033[0;33m'    # yellow
X='\033[0m'       # reset


def welcome():
    print(G)    # turn text green
    print('Welcome to Lee\'s Typing Game!')
    print('How to Play')
    print('* Read the highlighted sentence at the top.')
    print('* Type the sentence EXACTLY before the time runs out.')
    print('* Press Enter when you have typed the sentence correctly.')
    name = getName()
    resume = input('Press any key to START')
    os.system('clear')
    print(X)    # reset text color
    return name

def generateHighScores():
    highScores = []
    # open file and read the content in a list
    with open('highScoreFileSimple.txt', 'r') as filehandle:
        for line in filehandle:
            # split scores and names and store in a list inside the list
            score, name = line.strip().split()
            score = int(score.strip(', '))
            highScores.append([score, name])
    return highScores


def isHighScore(highScores, score):
    highScores.sort(reverse=True)
    if score >= highScores[-1][0]:
        return True
    else: 
        return False

def updateHighScore(highScores, score, playerName):
    highScores.append([score, playerName])
    highScores.sort(reverse=True)
    if len(highScores) > 10:
        highScores.pop()
    return highScores
   
    
def storeHighScores(highScores):
    with open('highScoreFileSimple.txt', 'w') as filehandle:
        for score in highScores:
            filehandle.write(f'{score[0]}, {score[1]}\n')
    
    
def getName():
    while True:
        playerName = input('Enter your name, single word no spaces:')
        if ' ' not in playerName:
            return playerName
        else:
            print('invalid entry')


def takeTurn(key):
    startTime = time.time()
    while True:
        print('Type the sentence and press Enter.')
        print(Y)    # turn text yellow
        print(key)
        print(X)    # reset text color
        entry = input()
        if entry == key:
            break
        else:
            print('Incorrect try again')
    elapsedTime = round(time.time() - startTime, 1)
    return elapsedTime


def printHighScores(highScores):
    print('---------High Scores----------')
    print('Rank   Score     Name')
    for i in range(len(highScores)):
        print(f'{i + 1:>3}.   {highScores[i][0]:<10}{highScores[i][1]:<10}')
    print()
    
def main():
    os.system('clear')
    key = 'Last night. I ate chicken, rice, and eggs.'
    highScores = generateHighScores()
    playerName = welcome()
    while True:
        elapsedTime = takeTurn(key)
        score = round(elapsedTime ** -1 * 10*100000)
        print(f'{elapsedTime} seconds, {score} points')
       
        if isHighScore(highScores, score):
            highScores = updateHighScore(highScores, score, playerName)
            print('New high score! :)')
        else:
            print('Sorry you didn\'t make the leaderboard :(')
       
        printHighScores(highScores)
       
        resume = input('press x to exit, any other key to try again: ')
        if resume == 'x':
            storeHighScores(highScores)
            break


main()
