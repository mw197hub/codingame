# https://www.codingame.com/ide/puzzle/solar-shadow-hunter

import sys,math


k=2;rowList=['.P.', '.P.', '.P.', '.1.', '...']#1
k=3;rowList=['P', 'P', 'P', '.', '.', '2'] #3
k=2;rowList=['PPPPPPPPPP', '..........', '..........', '123456789.'] #4


newList=[]
for row in rowList:
    new=[]
    for r in row:
        new.append(r)
    newList.append(new[:])
for y in range(len(newList)):
    for x in range(len(newList[0])):
        if newList[y][x] in "123456789":
            schatten = int(newList[y][x]) * k
            for i in range(schatten):
                yN = y - i - 1
                if yN >= 0:
                    newList[yN][x] = "S"

anzahl=0
for row in newList:
    for r in row:
        if r == "P":
            anzahl+=1
print(anzahl*100)