import sys
import math

def einsOben(dice):
    while not verschieben(dice):
        dice = schieben(dice)
        #print(dice)
    ausgabe(dice)

def ausgabe(dice):
    if dice[0:3] == '123':
        print("right-handed")
    else:
        print("left-handed")

def verschieben(dice):
    if (dice[1] == '3' and dice[2] == '2') or (dice[1] == '2' and dice[2] == '3'):
        return True
    return False

def schieben(dice):
    return dice[0]+dice[2:5]+dice[1]+dice[5]

def dreheEins(dice):
    return dice[2]+dice[1]+dice[5]+dice[3]+dice[0]+dice[4]

def sucheEins(dice):
    while not schiebeEins(dice):
        dice = schieben(dice)
    return dice

def schiebeEins(dice):
    if dice[2] == '1':
        return True
    return False


## Wuerfel in einen String bringen:
#  1
# 2354
#  6

dice='123546'
dice="465123"
dice="536412"
dice="632451"
dice="645321"
#dice="154236"

if not int(dice[0]) + int(dice[5]) == 7 or not int(dice[1]) + int(dice[3]) == 7 or not int(dice[2]) + int(dice[4]) == 7:
    print("degenerate")
else:
    if dice[0] == '1':
        einsOben(dice)
    else:
        if dice[5] == '1':            
            dice = dreheEins(dice)
            dice = dreheEins(dice)
            einsOben(dice)
        else:
            dice = sucheEins(dice)
            dice = dreheEins(dice)
            einsOben(dice)