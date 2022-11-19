#  https://www.codingame.com/ide/puzzle/card-counting-when-easily-distracted

import sys,math,copy

cardList=['A','2','3','4','5','6','7','8','9','T','J','Q','K']

def gueltig(part):
    for p in part:
        if not p in cardList:
            return False
    return True

stream_of_consciousness='222.333.444.some distraction.555.5.678.678.678.678.another distraction.9999.TTTT.JJJJ.QQQQ.KKKK.AAAA'
bust_threshold=4

allList=['2', '2', '2','2', '3', '3', '3', '3', '4', '4','4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', 'A', 'A', 'A', 'A', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'T', 'T', 'T', 'T']

sList = stream_of_consciousness.split(".")
for s in sList:
    if gueltig(s):
        for t in s:
            if t in allList:
                allList.remove(t)
print(sorted(allList),file=sys.stderr)
wertList=[]
for a in allList:
    if a in ['T','J','K','Q']:
        wertList.append(10)
    elif a == "A":
        wertList.append(1)
    else:
        wertList.append(int(a))
print(wertList,file=sys.stderr)
anz=0
for w in wertList:
    if w < bust_threshold:
        anz+=1
erg=int(anz/len(wertList) *100 +0.5)
print(str(erg)+"%")