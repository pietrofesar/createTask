import random
import os
import time


def wordSelection(file):
    words = []
    with open(file, 'r') as filehandle:
        for word in filehandle:
            words.append(word.strip())
    random.shuffle(words)
    return words


def gameSetup(words):
    random.shuffle(words)
    word = words.pop()
    splitWord = word.split(",")
    return splitWord


def hintCreator(word):
    dashWord = []
    for each in word[0]:
        dashWord.append('_')
    hint = word[1]
    return word[0], dashWord, hint


def replaceDash(guess, word, dashWord):
    for i in range(len(word)):
        if guess == word[i]:
            dashWord[i] = guess
    return dashWord

#Function to meet APCSP requirements.
def checkWord(guess, word):
  for each in word:
    if guess in word:
      return True
    else:
      return False

def outputClear(userName):
    os.system('clear')
    print(f'Hello {userName}, welcome to this word guessing game. The instructions are fairly simple.\n')
    print('First, you will be prompted to guess a letter of the word. If it is in the word, then it will show up as correct. If not, it will result as incorrect and count as a strike.\n')
    print('As each turn goes by, you will be asked if you want to solve the word. If you do, type yes, and if you do not, then type no.\n')
    print('You can have as many mistakes for how long the word is plus 3 freebies. Alright, let\'s get to it! Good luck!\n')
    print('Guess the word!')


  
def main():
    # initialize overall game variables
    words = wordSelection('wordBank.txt')
    userName = input('What is your name? ')

    # initialize turn
    while True:
        word = gameSetup(words)
        word, dashWord, hint = hintCreator(word)
        numWrong = 0
        # guessing sequence per turn
        while True:
            outputClear(userName)
            print(' '.join(dashWord))
            print(f'The hint is {hint}')
            guess = input('Guess your letter: ')
            # not a letter
            # repeat of a guessed letter
            if guess in dashWord:
                print('You have already guessed that letter.')
                time.sleep(2)
                continue
            if not guess.isalpha():
                print('That is not a letter.')
                time.sleep(1)
                continue
            else:  
              result = checkWord(guess, word)
              if result == True:
                print ('You guessed a letter!')
                dashWord = replaceDash(guess, word, dashWord)
                print(' '.join(dashWord))
                # solve the word
                solveWord = input('Would you like to solve the word? Enter y to accept. ')
                if solveWord == 'y':
                    wordGuess = input('What do you think the word is? ')
                    if wordGuess == word:
                        print('Congrats! You have guessed the word!')
                        break
                    else:
                        print('Your guess did not match with the selected word.')
                        time.sleep(1)
                        continue
                else:
                  continue
            # repeat of a guessed letter
            if guess in dashWord:
                print('You have already guessed that letter.')
                time.sleep(2)
                continue
            # guessed incorrectly    
            else:
                print('That letter is not in the word.')
                numWrong += 1
                time.sleep(2)
            # checking if game is over
            # ran out of attempts
            if numWrong == len(word) + 3:
                print(f'Unfortunately, you have used up all of your available guesses and lost the game. The word was {word}.'
                )
                break
            # guessed the word
            elif word == ''.join(dashWord):
                print(f'Congrats! You\'ve guessed the randomly selected word! The word was {word}. ')
                break
            # take another turn
            else:
                #print(dashWord) # debug
                continue

        resume = input('Press "y" to play again and "n" to exit: ')
        if resume == 'y':
            continue
        else:
            print(f'Alrighty then. Thanks for playing my game, {userName}.')
        break


main()
