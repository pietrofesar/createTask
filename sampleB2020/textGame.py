import os
import time


# text color constants
R='\033[0;31m'    # red
BR='\033[1;31m'   # bold red
G='\033[0;32m'    # green
BG='\033[1;32m'   # bold green
Y='\033[0;33m'    # yellow
BY='\033[1;33m'   # bold yellow
B='\033[0;34m'    # blue
BB='\033[1;34m'   # bold blue
P='\033[0;35m'    # purple
BP='\033[1;35m'   # bold purple
A='\033[0;36m'    # aqua
BA='\033[1;36m'   # bold aqua
X='\033[0m'       # reset


def welcome():
    print(f'{BY}Welcome to Lee\'s Typing Game!{X}')
    print('How to Play')
    print(f'{G}* Read the highlighted sentence at the top.{X}')
    print(f'{G}* Type the sentence EXACTLY before the time runs out.{X}')
    print(f'{G}* Press Enter when you have typed the sentence correctly.{X}')
    name = getName()
    resume = input(f'{BY}press any key to {BG}START{X}')
    os.system('clear')
    return name

def generateHighScores():
    highScores = []
    # open file and read the content in a list
    with open('highScoreFile.txt', 'r') as filehandle:
        for line in filehandle:
            # split scores and names and store in a list inside the list
            elapsedTime, score, name = line.strip().split()
            elapsedTime = float(elapsedTime.strip(', '))
            score = int(score.strip(', '))
            highScores.append([elapsedTime, score, name])
    return highScores


def isHighScore(highScores, score):
    highScores.sort(reverse=True)
    if score >= highScores[-1][0]:
        return True
    else: 
        return False

def updateHighScore(highScores, elapsedTime, score, playerName):
    highScores.append([elapsedTime, score, playerName])
    highScores.sort()
    if len(highScores) > 10:
        highScores.pop()
    return highScores
   
    
def storeHighScores(highScores):
    with open('highScoreFile.txt', 'w') as filehandle:
        for score in highScores:
            filehandle.write(f'{score[0]}, {score[1]}, {score[2]}\n')
    
    
def getName():
    while True:
        playerName = input(f'{Y}Enter your name{X}, single word no spaces:')
        if ' ' not in playerName:
            return playerName
        else:
            print('invalid entry')


def takeTurn(key):
    startTime = time.time()
    while True:
        print(f'{Y}Type the sentence and press Enter.{X}')
        print(f'{BR}{key}{X}')
        entry = input()
        if entry == key:
            break
        else:
            print('Incorrect try again')
    elapsedTime = round(time.time() - startTime, 1)
    return elapsedTime

'''
def printHighScores(highScores):
    message = f'{BA}High Scores\n{X}'.center(50)
    message += f'{"Rank":>6}{"Time":<6}{"Score":<9}{"Name":<10}\n'
    for i in range(len(highScores)):
        message += f'{i + 1:>4}. {highScores[i][0]:<6}{highScores[i][1]:<9}{highScores[i][2]:<10}\n'
    return message
'''

def printHighScores(highScores):
    colors = [R, BR, G, BG, Y, BY, B, BB, P, BP, A, BA]
    print(f'{BA}High Scores{X}'.center(40))
    print(f'{"Rank":<6}{"Time":<6}{"Score":<9}{"Name":<10}')
    color = 0
    for i in range(len(highScores)):
        if color > len(colors) - 1:
            color = 0
        print(colors[color], end='')
        print(f'{i + 1:>3}.  {highScores[i][0]:<6}{highScores[i][1]:<9}{highScores[i][2]:<10}')
        color += 1
    print(f'{X}')
    
        

def main():
    os.system('clear')
    highScores = generateHighScores()
    key = 'Last night. I ate chicken, rice, and eggs.'
    playerName = welcome()
    while True:
        elapsedTime = takeTurn(key)
        score = round(elapsedTime ** -1 * 10*100000)
        print(f'{BY}{elapsedTime} seconds, {Y}{score} points{X}')
       
        if isHighScore(highScores, score):
            highScores = updateHighScore(highScores, elapsedTime, score, playerName)
            print(f'{BG}New high score! :){X}')
        else:
            print(f'{R}Sorry you didn\'t make the leaderboard :({X}')
       
        printHighScores(highScores)
       
        resume = input('press x to exit, any other key to try again')
        if resume == 'x':
            storeHighScores(highScores)
            break


main()
