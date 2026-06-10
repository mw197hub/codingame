# https://www.codingame.com/ide/puzzle/snap

import sys,math

p1Deck=['5S', '6D', '5D', '10D'];p2Deck=['3H', '7S', '5C', 'KH'] #1
p1Deck=['3S', '5D', 'KC', '3C', '4H'];p2Deck=['JH', '9C', 'KS', '8H', 'JC'] #2



wertDict={'A':14,'K':13,'Q':12,'B':11,'1':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
farbenDict={'S':4,'H':3,'D':2,'C':1}
pileList=[]
while True:
    if len(p1Deck) == 0 or len(p2Deck) == 0:
        break
    p1 = p1Deck.pop(0)    
    # vergleich mit pile
    if len(pileList) > 0:
        pile=pileList[-1]
        if p1[0] == pile[0] or p1[1] == pile[1]:
            pileList.append(p1)
            if p1[0] == pile[0]:
                if farbenDict[p1[-1]] > farbenDict[pile[-1]]:
                    while True:
                        p1Deck.append(pileList.pop(0))
                        if len(pileList) == 0:
                            break
                else:
                    while True:
                        p2Deck.append(pileList.pop(0))
                        if len(pileList) == 0:
                            break
        else:            
            pileList.append(p1)
    else:
        pileList.append(p1)
   # if len(p1Deck) == 0 or len(p2Deck) == 0:
   #     break

    ### player 2
    p2 = p2Deck.pop(0)
    if len(pileList) > 0:
        pile=pileList[-1]
        if p2[0] == pile[0] or p2[1] == pile[1]:
            pileList.append(p2)
            if p2[0] == pile[0]:
                if farbenDict[p2[-1]] > farbenDict[pile[-1]]:
                    while True:
                        p2Deck.append(pileList.pop(0))
                        if len(pileList) == 0:
                            break
                else:
                    while True:
                        p1Deck.append(pileList.pop(0))
                        if len(pileList) == 0:
                            break
        else:
            pileList.append(p2)
    else:
        pileList.append(p2)




if len(p1Deck) == 0:
    print("Winner: Player 2")
    print(len(p2Deck))
else:
    print("Winner: Player 1")
    print(len(p1Deck))