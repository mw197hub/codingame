import sys
import math

def sumE(cardL):
    wert = 0;anz=0
    for c in cardL:
        if c in ['J','Q','K']:
            wert += 10
        elif c == 'A':
            anz+=1
        else:
            wert += int(c) 
    if anz > 0:
        if wert < 11 and anz == 1:
            wert += 11
        elif anz > 1 and wert < 10:
            wert += 12
        else:
            wert += 1 * anz
            
    return wert

bank_cards = ['8', '2', '2']
player_cards = ['7', '6']


bank = sumE(bank_cards)
player = sumE(player_cards)

if bank > 21 and player > 21:
    print("Bank")
elif (player == 21 and len(player_cards) == 2) and (bank == 21 and len(bank_cards)==2):
    print("Draw")
elif  (player == 21 and len(player_cards) == 2):
    print("Blackjack!")
elif bank > 21:
    print("Player")
elif player > 21:
    print("Bank")
elif player > bank:
    print("Player")
elif bank > player:
    print("Bank")
else:
    print("Draw")
