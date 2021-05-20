# text color constants
R = '\033[0;31m'  # red
BR = '\033[1;31m'  # bold red
G = '\033[0;32m'  # green
BG = '\033[1;32m'  # bold green
Y = '\033[0;33m'  # yellow
BY = '\033[1;33m'  # bold yellow
B = '\033[0;34m'  # blue
BB = '\033[1;34m'  # bold blue
P = '\033[0;35m'  # purple
BP = '\033[1;35m'  # bold purple
A = '\033[0;36m'  # aqua
BA = '\033[1;36m'  # bold aqua
X = '\033[0m'  # reset

import textwrap

# helper functions

def totalName(x):
    summmation = 0 
    letters = ['a','b','c','d','e','f','g','h','i', 'j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y', 'z']
    for char in x:
        if char in letters:
            summmation += (ord(char) - 96)
    return summmation
    
def eliminate_consonants(x):
    summmation = 0
    vowels= ['a','e','i','o','u']
    for char in x:
        if char in vowels:
            summmation += (ord(char) - 96)
    return summmation
    
def eliminate_vowels(x):
    summmation = 0
    total = 0
    consonants = ['b','c','d','f','g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for char in x:
        if char in consonants:
            summmation += (ord(char) - 96)
    return summmation


# creates a list of the strings broken at 70 characters - the paragraphs
def makeParagraph(text):
    text = textwrap.wrap(text, 70)
    for each in text:
        print(each)
    print()


def addDigits(totalSum):
        total = 0
        if totalSum == 11:
            return 11
        elif totalSum == 22:
            return 22
        while totalSum > 0:
            remainder = totalSum % 10
            total += remainder    
            totalSum //= 10
        if total == 11 or total == 22:
            totalSum = total
        elif total >= 10:
            remainder = total // 10
            remain = total % 10
            total = remainder + remain
        return total


def main():
    firstName = input(f'Enter your first name: ').lower()
    middleName = input(f'Enter your middle name: ').lower()
    lastName = input(f'Enter your last name: ').lower()
    birthMonth = eval(input(f'Enter the month you were born, as a number: '))
    birthDay = eval(input(f'Enter the day you were born: '))
    birthYear = eval(input(f'Enter the year you were born: '))
    
    # generate birth date values
    if birthDay == 11 or birthDay == 22:
        birthDayTotal = birthDay
    else:
        birthDayTotal = addDigits(birthDay)
    if addDigits(birthYear) == 11:
        birthYearTotal = 11
    elif addDigits(birthYear) == 22:
        birthYearTotal = 22
    else:
        birthYearTotal = addDigits(birthYear)
    if birthMonth == 11:
        birthMonthTotal = 11
    else:
        birthMonthTotal = addDigits(birthMonth)
    
    # generate soul dictionary
    soulDict = {}
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '22']
    f = open('soulUrge.txt', 'r')
    soulValues = f.read().split('\n')
    for i in range(len(keys)):
        soulDict[keys[i]] = soulValues[i]
    
    # generate personality dictionary
    personalityDict = {}
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '22']
    f = open('personality.txt', 'r')
    personalityValues = f.read().split('\n')
    for i in range(len(keys)):
        personalityDict[keys[i]] = personalityValues[i]
    
    # generate expression dictionary
    expressionDict = {}
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '22']
    f = open('expression.txt', 'r')
    expressionValues = f.read().split('\n')
    for i in range(len(keys)):
        expressionDict[keys[i]] = expressionValues[i]
        
    # generate life path dictionary
    lifePathDict = {}
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '22']
    f = open('lifePath.txt', 'r')
    lifePathValues = f.read().split('\n')
    for i in range(len(keys)):
        lifePathDict[keys[i]] = lifePathValues[i]
    
    
    # generate soul urge number
    soulUrge = sum([addDigits(eliminate_consonants(firstName)), addDigits(eliminate_consonants(middleName)), addDigits((eliminate_consonants(lastName)))])
    if soulUrge == 11 or soulUrge == 22:
        soulUrge = soulUrge
    else:
        soulUrge = sum([addDigits(eliminate_consonants(firstName)), addDigits(eliminate_consonants(middleName)), addDigits((eliminate_consonants(lastName)))])
    print(f'{G}Your Soul Urge number is: {addDigits(soulUrge)}{X}')
    
    # generate soul urge paragraph
    makeParagraph(soulDict[str(addDigits(soulUrge))])
    
    # generate personality number
    personalityNum = sum([addDigits(eliminate_vowels(firstName)), addDigits(eliminate_vowels(middleName)), addDigits(eliminate_vowels(lastName))])
    if personalityNum == 11 or personalityNum == 22:
        personalityNum = personalityNum
    else:
        personalityNum = sum([addDigits(eliminate_vowels(firstName)), addDigits(eliminate_vowels(middleName)), addDigits(eliminate_vowels(lastName))])
    print(f'{A}Your Personality Number is: {addDigits(personalityNum)}{X}')
    
    # generate personality paragraph
    makeParagraph(personalityDict[str(addDigits(personalityNum))])
    
    # generate expression number
    expressionNum = sum([addDigits(totalName(firstName)), addDigits(totalName(middleName)), addDigits(totalName(lastName))])
    if expressionNum == 11 or expressionNum == 22:
        expressionNum = expressionNum = sum([addDigits(totalName(firstName)), addDigits(totalName(middleName)), addDigits(totalName(lastName))])
    else:
        expressionNum 
    #print(totalSum)
    print(f'{B}Your Expression Number is: {addDigits(expressionNum)}{X}')
    
    # generate expression paragraph
    makeParagraph(expressionDict[str(addDigits(expressionNum))])
    
    # generate life path number
    lifePath = sum([birthDayTotal, birthMonthTotal, birthYearTotal])
    if lifePath == 11 or lifePath == 22:
        lifePath = lifePath
    else:
        lifePath = sum([birthDayTotal, birthMonthTotal, birthYearTotal])
    print(f'{P}Your Life Path Number is: {addDigits(lifePath)}{X}')
    
    # generate life path paragraph
    makeParagraph(lifePathDict[str(addDigits(lifePath))])
    
    
main()
