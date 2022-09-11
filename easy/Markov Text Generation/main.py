import sys
import math
import copy

def randS(anz,rSeed):
    rSeed += 7
    return rSeed%anz,rSeed

tList = ['one', 'fish', 'is', 'good', 'and', 'no', 'fish', 'is', 'bad', 'and', 'that', 'is', 'it']
d,l=2,4
sList= ['fish', 'is']

tList = ['stop', 'there', 'once', 'was', 'a', 'girl', 'named', 'dorothy', 'stop', 'dorothy', 'had', 'a', 'dog', 'named', 'toto', 'stop', 'dorothy', 'lived', 'with', 'her', 'aunt', 'and', 'uncle', 'with', 'her', 'dog', 'named', 'toto', 'stop', 'she', 'was', 'a', 'girl', 'of', 'who', 'dreamed', 'of', 'traveling', 'stop']
d,l=2,10
sList=['dorothy', 'was', 'a'] # dorothy was a girl named dorothy stop dorothy had a


rSeed = 0
ergList = [];anzahl = len(sList)
ergList = copy.deepcopy(sList)
while anzahl < l:
    newList = []
    for i in range(len(tList)-d+1):
        if tList[i:i+d] == ergList[-d:]:
            if i+1 < len(tList):
                newList.append(tList[i+d])                
                    
    anzahl+=1
    r,rSeed =randS(len(newList),rSeed)
    ergList.append(newList[r])
print(*ergList)
