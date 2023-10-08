# https://www.codingame.com/ide/puzzle/score-a-bridge-deal

import sys,math

def compute(vulnerable, level, suit, doubled, redoubled, tricks):
    if tricks < level + 6:
        undertricks = level + 6 - tricks
        if not doubled and not redoubled:
            return undertricks * -50 * (2 if vulnerable else 1)
        penalty = undertricks * -300
        if vulnerable:
            return (penalty + 100) * (2 if redoubled else 1)
        penalty += 200
        penalty += 100 * min(undertricks - 1, 2)
        return penalty * (2 if redoubled else 1)
    trick_value = 20 if suit in 'CD' else 30
    contracted = level * trick_value
    if suit == 'NT':
        contracted += 10
    contracted *= 4 if redoubled else (2 if doubled else 1)
    score = contracted
    if score >= 100:
        score += 500 if vulnerable else 300
    else:
        score += 50
    if level == 6:
        score += 750 if vulnerable else 500
    elif level == 7:
        score += 1500 if vulnerable else 1000
    if not doubled and not redoubled:
        return score + (tricks - level - 6) * trick_value
    score += 100 if redoubled else 50
    overtrick_value = 200 if vulnerable else 100
    if redoubled:
        overtrick_value *= 2
    return score + (tricks - level - 6) * overtrick_value



dealList=[['V', '4S', '11']]

for deal in dealList:
    if deal[1] == "Pass":
        print(0)
    else:
        vulnerable = deal[0] == "V"
        contract = deal[1]
        tricks = int(deal[2])
        level = int(deal[1][0])
        suit = contract[1]
        if not contract[1] in "CDHS":
           suit = "NT" 
        doubled, redoubled = False, False
        if contract[-2:] == 'XX':
            redoubled = True
        elif contract[-1] == 'X':
            doubled = True
        print(compute(vulnerable, level, suit, doubled, redoubled, tricks))        