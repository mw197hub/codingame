import sys
import math
import copy

def istUngerade(nr):
    if nr % 2:
        return True
    return False

geradeList = []
coinList = {}
inputList = []
erg = ""
#n, t = [int(i) for i in input().split()]
#for i in range(t):
#    inputList.append(list(input().split()))
#print(inputList,file=sys.stderr)
n = 2;inputList = [['4', '2'], ['2', '4'], ['4', '3']]
n = 3;inputList = [['3', '1', '6'], ['4', '1', '6']]

for i in range(1,n*2 + 1,2):
    geradeList.append(i+1)
for i in range(1,n*2 + 1,2):
    coinList[i] = copy.deepcopy(geradeList)

for iList in inputList:
    unList = [];geList = []
    for zahl in iList:
        if (istUngerade(int(zahl))):
            unList.append(zahl)
        else:
            geList.append(zahl)
    for uZahl in unList:
        cList = coinList[int(uZahl)]
        for gZahl in geList:
            if int(gZahl) in cList:
                cList.remove(int(gZahl))
        if len(cList) == 1:
            dWert = cList[0]
            for c,gL in coinList.items():
                if len(gL) > 1 and dWert in gL:
                    gL.remove(dWert)

print(coinList,file=sys.stderr)
while True:
    abbruch = True
    for c,gL in coinList.items():
        if len(gL) == 1:
            dWert = gL[0]
            for c1,gL1 in coinList.items():
                if len(gL1) > 1 and dWert in gL1:
                    gL1.remove(dWert)
                    abbruch = False
    if abbruch:
        break

for zahl in sorted(coinList):
    wert = coinList[zahl]
    erg = erg + str(wert[0]) + " "
print(erg[:-1])