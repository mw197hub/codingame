# https://www.codingame.com/ide/puzzle/sandpile-addition

import sys,math

n=3;rowList=['121', '202', '121', '020', '202', '020']

ergList=[]
for i in range(n):
    row = rowList[i]
    erg=[]
    for r in row:
        erg.append(int(r))
    ergList.append(erg[:])
for i in range(n):
    row = rowList[i+n]
    erg=ergList[i]
    for j in range(len(row)):
        r = int(row[j])
        erg[j]=erg[j]+r

while True:
    ende=True
    for i in range(len(ergList)):
        erg=ergList[i]
        for j in range(len(erg)):
            e = erg[j]
            if e >= 4:
                ende = False
                e-=4
                ergList[i][j] = e
                for xy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    y=i+xy[0];x=j+xy[1]
                    if y < 0 or x < 0 or y >=len(ergList) or x >= len(erg):
                        continue
                    else:
                        ergList[y][x] +=1
    if ende:
        break

for erg in ergList:
    ausgabe=""
    for e in erg:
        ausgabe+=str(e)
    print(ausgabe)