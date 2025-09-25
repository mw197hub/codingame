# https://www.codingame.com/ide/puzzle/magic-stones

import sys,math,copy

levelList=[1, 1]
levelList=[1, 1, 5]
levelList=[1, 1, 1, 2, 2, 3, 3, 4, 4]

###
erg=0
levelDict={}
for level in levelList:
    if level in levelDict:
        levelDict[level] +=1
    else:
        levelDict[level] = 1
print(levelDict,file=sys.stderr)
while True:
    ende=True
    levelN=copy.deepcopy(levelDict)
    for level,wert in levelDict.items():
        if wert > 1:
            ende=False
            wertN=wert//2
            levelN[level] = wert-wertN*2
            if level+1 in levelDict:
                levelN[level+1]+=wertN
            else:
                levelN[level+1]=wertN
            break
    levelDict=copy.deepcopy(levelN)
    print(levelDict,file=sys.stderr)
    if ende:
        break
for level,wert in levelDict.items():
    if wert > 0:
        erg+=1
print(erg)