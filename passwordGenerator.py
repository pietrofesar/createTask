import random


def genListFromFile(file):
    lines = []
    with open(file, 'r') as filehandle:
        for line in filehandle:
            lines.append(line.strip())
    return lines


def addSpecialChar(password):
    if 's' in password:
        password = password.replace('s', '$')
    elif 'i'in password:
        password = password.replace('i', '!')
    else: # 'a'in password:
        password = password.replace('a', '@')
    if '$' not in password and '!' not in password and '@' not in password:
        return '&' + password
    else:
        return password


def addDigit(password):
    if 'o' in password:
        password = password.replace('o', '0')
    elif 'e'in password:
        password = password.replace('e', '3')
    else: #'l' in password:
        password = password.replace('l', '1')
    
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    if digit:
        return password
    else:
        return password + '69'
    

def main():
    while True:
        firstWord = genListFromFile('descriptiveWord.txt')
        secondWord = genListFromFile('thingWord.txt')
        password = f'{random.choice(firstWord).capitalize()}{random.choice(secondWord).capitalize()}'
        password = addSpecialChar(password)
        password = addDigit(password)
        print(password)
        resume = input('press x to exit, any other key to generate another: ')
        if resume == 'x':
            break
        
main()
