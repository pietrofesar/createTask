# Black Jack Game

import random
import os


# Making the deck of cards
def makeDeck():
    deckOfCards = []
    for suits in '♤♡♧♢': 
        for digit in range(2, 11):
            deckOfCards.append(f'{digit}{suits}')
    for suits in '♤♡♧♢':
        for face in 'JQKA':
            deckOfCards.append(f'{face}{suits}')
    random.shuffle(deckOfCards)
    return deckOfCards


# Using the number of players to deal the cards
def dealCards(numOfPlayers):
    numOfCards = 2 * numOfPlayers
    return numOfCards


# Defines the value of each hand based on the card value(s)
def handValue(hand):
    handValue = 0
    for card in hand:
        if card[0:2] == '10':
            handValue += 10
        elif card[0].isdigit():
             handValue += int(card[0])
        elif card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
            handValue += 10
        else:
            if handValue + 11 <= 21:
                handValue += 1
            else:
                handValue += 11
    return handValue

# Determines whether the dealer or the user/main player won the game of Blackjack
def winningValue(player, dealer):
    if handValue(dealer) > 21:
        return 'The dealer has busted!'
    elif handValue(player) > 21:
        return 'The player has busted!'
    elif handValue(dealer) == 21:
        return 'The dealer has blackjack and has won the game!'
    elif handValue(player) == 21:
        return 'The player has blackjack and has won the game!'
    elif handValue(dealer) > handValue(player):
        return 'The dealer is closer to 21 which means the dealer wins!'
    else:
        return 'The player is closer to 21 which means the player wins!'
        



# Main
def main():
    os.system('clear')
    deckOfCards = makeDeck()
    numOfPlayers = eval(input('Enter a number of players: '))
    playerHands = {}
    
   
    # numOfCards = dealCards(numOfPlayers)
    handList = []
    handList.append(deckOfCards.pop())
    handList.append(deckOfCards.pop())
    playerHands['dealer'] = handList.copy()
    
    
    for i in range(numOfPlayers):
        handList = []
        for j in range(2):
            handList.append(deckOfCards.pop())
        playerHands[f'player{i + 1}'] = handList.copy()
   
    for each in playerHands:
        if each == 'dealer':
            print(f"dealer {playerHands['dealer']} {handValue(playerHands['dealer'])}")
            print()
        else:
            print(f"{each} {playerHands[each]} {handValue(playerHands[each])}")
            print(winningValue(playerHands[each], playerHands['dealer']))
    

main()
