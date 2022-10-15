import sys
import math

def ermitteln(gList):
    runde=1;punkte=0;zaehler=1;bisher=[];vorher=0
    for g in gList:
        if g == "X":
            punkte-=20
            if len(bisher) > 0 and bisher[-1] == "X":
                punkte-=10
                if len(bisher) > 1 and bisher[-2] == 'X':
                    punkte = 0
        elif '*' in g:
            punkte = punkte + (int(g[0])*int(g[2:]))
        else:
            punkte+= int(g)
        if punkte>101:
            zaehler=3
            punkte=vorher
        if punkte == 101:
            break
        if zaehler == 3:
            runde+=1;zaehler=1;bisher=[];vorher=punkte
        else:
            zaehler+=1;bisher.append(g)

    return runde

plDict={0: ['Hugo', '10 5 3*18 15 5 4 8'], 1: ['Guillaume', '5 5 10 2*19 5 6 2*5 1 20 1']}
plDict={0: ['Fred', '10 6 3*18 X 19 X 2*25 2'], 1: ['Charles', '5 5 10 2*19 5 6 2*5 1 20 1']}
plDict={0: ['Eric', '6 2 7 15 2*10 8 2 3 6 15 2 1 3 11'], 1: ['Delphine', '4 3 2 1 1 1 X X 10 2 3 5'], 2: ['Patricia', 'X X X X X X X X X 2*25 3*17'], 3: ['Yan', '3*15 2*10 3*5 2*12 2*7 2*7 3*15']}


name="";runden=999
for nr,sList in plDict.items():
    runde=ermitteln(sList[1].split(" "))
    sList.append(runde)
    plDict[nr] = sList
    if runde < runden:
        runden=runde;name=sList[0]

print(plDict,file=sys.stderr)
print(name)