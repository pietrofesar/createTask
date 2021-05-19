# my 2 partners and I worked together on this program.

import random 
import time

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


def askQuestion(question):
    
    print(question.pop(0))
    answerKey = question[0]
    random.shuffle(question)
    for each in question:
        print(each, end=', ')
        
    response = input('\nType your answer here: ')
    if response == answerKey:
        print('correct!')
        return True
    else:
        print(f'Wrong...The correct answer is {answerKey}')
        return False
            
            
def main():
    
    f = open('questions.csv', 'r')
    questions = f.read().split('\n')
    random.shuffle(questions)
    f.close()
    
    total = len(questions)
    correct = 0
    # 3bii this is where the list is utilized
    for each in range(len(questions)):
        if askQuestion(questions.pop(0).split(',')):
            correct += 1
    percentCorrect = correct/total * 100
    
    print(f'You got {percentCorrect:.2f}% of the questions correct.')
    
    playAgain = input(f'{R}Do you want to play again? (y / n) {X}')
    if playAgain == 'y':
        main()
    else:
        quit()
        
        
main()

