import sys
import math
import copy

def setze(p,rowList,mList):
    ast='*';til='~'
    tList = mList[int(p)]
    for t in tList:
        y,x = t.split('-')
        if rowList[int(y)][int(x)] == "*":
            rowList[int(y)][int(x)] = til
        else:
            rowList[int(y)][int(x)] = ast



rowList = [['~', '*', '~'], ['~', '~', '~'], ['~', '*', '~']]
pList = ['8', '8', '4']

rowList = [['~', '~', '*'], ['*', '*', '~'], ['*', '*', '~']]
pList = ['4', '5']


erg = 0;ast='*';til='~'
ergList = [['*', '*', '*'], ['*', '~', '*'], ['*', '*', '*']]
mList = {1:['0-0','0-1','1-0','1-1'],3:['0-1','0-2','1-1','1-2'],
7:['1-0','1-1','2-0','2-1'],9:['1-1','1-2','2-1','2-2'],5:['1-1','0-1','1-0','1-2','2-1'],
2:['0-0','0-1','0-2'],4:['0-0','1-0','2-0'],
6:['0-2','1-2','2-2'],8:['2-0','2-1','2-2']}
print(rowList,file=sys.stderr)

for p in pList:
    setze(p,rowList,mList)
    #print(rowList,file=sys.stderr)
for i in range(1,10):
    testList = copy.deepcopy(rowList)
    setze(i,testList,mList)
    if testList == ergList:
        #print(rowList,file=sys.stderr)
        erg = i;break



print(erg)