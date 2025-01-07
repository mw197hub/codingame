# https://www.codingame.com/ide/puzzle/pachinko-jackpot

import sys,math,copy,itertools

height=5;iList=['0', '12', '012', '0120', '12012'];pList=[900, 600, 300, 500, 700, 800]

datei = open('C:\\Users\\marku\\Python\\codingame\\easy\\Pachinko Jackpot\\input.txt','r')
i=0
iList.clear();pList.clear()
for zeile in datei:
    if i == 0:
        height=int(zeile)
    else:
        if i <= height:
            iList.append(zeile[:-1])
        else:
            pList.append(int(zeile[:-1]))
    i+=1        
##

height=5;iList=['0', '12', '012', '0120', '12012'];pList=[900, 600, 300, 500, 700, 800]
#height=5;iList=['1', '00', '000', '0000', '00000'];pList=[900, 600, 300, 500, 700, 800]

###
erg=0
ergList=[int(iList[0])]

for i in range(1,len(iList)):
    tList = list(iList[i])
    zwList=[]
    for j in range(len(tList)):
        wert = int(tList[j])
        if j-1 >= 0:
            links=ergList[j-1]+wert
        else:
            links=-1
        if j < len(ergList):
            rechts=ergList[j]+wert
        else:
            rechts=-1
        zwList.append(max(links,rechts))
    ergList=zwList[:]
       
print(ergList,file=sys.stderr)


for i in range(len(pList)):
    wert=pList[i]
    if i-1 >= 0:
        links=ergList[i-1]*wert
    else:
        links=-1
    if i < len(ergList):
        rechts=ergList[i]*wert
    else:
        rechts=-1
    erg=max(erg,links,rechts)

print(erg)

###
datei.close()


