# https://www.codingame.com/ide/puzzle/diagonal-achoo

import sys,math

def ausbreitung(rowL):
    neuer=False
    while True:
        for y in range(len(rowL)):
            row = rowL[y]
            for x in range(len(row)):
                if row[x] == "C":
                    for yV,xV in [[1,1],[1,-1],[-1,1],[-1,-1]]:
                        xN=x+xV;yN=y+yV
                        if xN<0 or yN <0 or xN>= len(row) or yN>= len(rowL):
                            continue
                        else:
                            if rowL[yN][xN] == ".":
                                neuer=True;rowL[yN][xN] = "C"
        if not neuer:
            break    
        neuer=False    


####
rowList=[[['.', 'H', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', 'H', '.', 'C', '.'], ['.', '.', 'H', '.', '.'], ['.', '.', '.', '.', '.']], [['.', '.', '.', '.', '.'], ['.', '.', 'C', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]]



####
pos=0;ergList=[];anzahl=0
for i in range(len(rowList)):    
    summe=0
    rowL=rowList[i]
    ausbreitung(rowL)
    for row in rowL:
        for r in row:
            if r == "C":
                summe+=1
    if summe > anzahl:
        anzahl=summe;pos=i
        ergList=rowL[:]
    
print(pos)
for ergL in ergList:
    erg=""
    for e in ergL:
        erg+=e
    print(erg)