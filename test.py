import random 


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
    for each in range(len(questions)):
        if askQuestion(questions.pop(0).split(',')):
            correct += 1
    percentCorrect = correct/total * 100
    
    print(f'You got {percentCorrect:.2f}% of the questions correct.')
    
    playAgain = input(f'Do you want to play again? (y / n)')
    if playAgain == 'y':
        main()
    else:
        quit()
        
        
main()
