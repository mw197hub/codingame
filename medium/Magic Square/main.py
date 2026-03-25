# https://www.codingame.com/ide/puzzle/magic-square

import sys,math

cubeList=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
#cubeList=[[5]]

richtig=True
# row, column, diagonal  # alle anders
# row
zahlList=[]
for y in range(len(cubeList)):
    for x in range(len(cubeList)):
        zahlList.append(cubeList[y][x])
for i in range(len(zahlList)):
    if not i+1 in zahlList:
        richtig=False

summe=sum(cubeList[0])
setList=set(cubeList[0])
for y in range(1,len(cubeList)):
    if not summe == sum(cubeList[y]):
        richtig=False
    if not len(setList) == len(set(cubeList[y])):
        richtig=False
#column
summe=0
for x in range(len(cubeList)):
    sum2=0;setList=set()
    for y in range(len(cubeList)):
        if x == 0:
            summe+=cubeList[y][x]
        else:
            sum2+=cubeList[y][x]
        setList.add(cubeList[y][x])
    if not summe == sum2 and x > 0:
        richtig=False
    if not len(setList) == len(cubeList):
        richtig=False
# diagonal
wert1=0;wert2=0;set1=set();set2=set();x1,y1,x2,y2=0,0,len(cubeList)-1,0
for y in range(len(cubeList)):
    wert1+=cubeList[y1][x1]
    set1.add(cubeList[y1][x1])
    x1+=1;y1+=1
    wert2+=cubeList[y2][x2]
    set2.add(cubeList[y2][x2])
    x2-=1;y2+=1


if not wert1 == wert2:
    richtig=False
if not len(set1) == len(cubeList):
    richtig=False
if not len(set2) == len(cubeList):
    richtig=False    
if richtig:
    print("MAGIC")
else:
    print("MUGGLE")