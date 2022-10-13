from re import A
import sys
import math

abcDict={}
abcList=[['A', '41', '56'], ['B', '76', '85'], ['C', '8', '15'], ['D', '4', '7'], ['E', '69', '8'], ['F', '25', '75'], ['G', '35', '88'], ['H', '69', '3'], ['I', '10', '58'], ['J', '52', '80'], ['K', '24', '37'], ['L', '2', '56'], ['M', '91', '24'], ['N', '56', '92'], ['O', '52', '81'], ['P', '63', '94'], ['Q', '2', '32'], ['R', '41', '9'], ['S', '81', '85'], ['T', '46', '26'], ['U', '9', '92'], ['V', '80', '94'], ['W', '4', '32'], ['X', '37', '54'], ['Y', '92', '14'], ['Z', '81', '73']]

for aList in abcList:
    r=int(aList[1])
    c=int(aList[2])
    if r in abcDict:
        bList = abcDict[r]
        bList.append([c,aList[0]])
    else:
        abcDict[r] = [[c,aList[0]]]

print(abcDict,file=sys.stderr)
erg = "";gerade=True
for row in sorted(abcDict):
    aList=abcDict[row]
    aDict={}
    for bList in aList:
        aDict[bList[0]] = bList[1]
    if gerade:
        for b,name in sorted(aDict.items()):
            erg = erg + name + ","
    else:
        for b,name in sorted(aDict.items(),reverse=True):
            erg = erg + name + ","
    gerade = False if gerade else True

print(erg[:-1])


    #wert = 100-c if r%2 else c
    #if r%2:
    #    wert=100-c
    #else:
    #    wert=c
    #abcDict[r*100+wert] = aList[0]