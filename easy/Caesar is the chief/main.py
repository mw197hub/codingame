import sys
import math
import string


def pruefe(w,abcDict,zahlDict,cList):
    versatz=0
    neuList=[];buch=w[0]
    for i in w[1:]:
        wert = abcDict[i] - abcDict[buch]
        neuList.append(wert)
        buch = i
    if cList == neuList:
        return neuList,True
    return neuList,False

def decode(w,zahlDict,versatz,abcDict):
    v = versatz + abcDict[w]
    if v > 25:
        v = v - 26
    elif v < 0:
        v = v + 26
    return zahlDict[v]

t = "HELLO"  #1
t = "CHIEF"  #2
t = "DIJFG JT XSPOH" #3

abcDict = {}
zahlDict = {}
chiefList= []
for i in range(len(string.ascii_uppercase)):
    abcDict[string.ascii_uppercase[i]] = i
    zahlDict[i] = string.ascii_uppercase[i]
#print(abcDict,file=sys.stderr)

chiefList,chief = pruefe("CHIEF",abcDict,zahlDict,[])
#print(chiefList,file=sys.stderr)

erg="WRONG MESSAGE "

wList = t.split(" ")
chief=False;versatz=0
for w in wList:
    if len(w) == 5:
        versatzList,chief=pruefe(w,abcDict,zahlDict,chiefList)
    if chief:
        versatz = abcDict['H'] - abcDict[w[1]]
        break

if chief:
    erg = ""
    for wort in wList:
        for w in wort:
            erg = erg + decode(w,zahlDict,versatz,abcDict)
        erg = erg + " "
print(erg[:-1])
