# https://www.codingame.com/ide/puzzle/kangaroo-words

import sys,math

def pruefung(kangaroo,joey):
    pos=0
    treffer=False
    if len(joey) >= len(kangaroo):
        return False
    for p in kangaroo:        
        if joey[pos] == p:                      
           pos = pos+1
           treffer = True
        if pos == len(joey):
            return True
    return False



lineList=['detect, examine, inspect, note, see, observe', 'bag, box, can, container, tank, tin']
lineList=['educator, instructor, lecturer, mentor, teacher, tutor', 'absorbing, amusing, captivating, enjoyable, entertaining, fun, funny, lively, pleasant']


ergDict={}
for line in lineList:

    inList=line.split(",")
    for i in range(len(inList)):
        inList[i] = inList[i].strip()
    #print(inList,file=sys.stderr)

    

    for i in range(len(inList)):
        kangaroo=inList[i]
        a =0
        for j in range(len(inList)):
            if i != j:
                joey=inList[j]
                if pruefung(kangaroo,joey):
                    if kangaroo in ergDict:
                        eList = ergDict[kangaroo]
                        eList.append(joey)
                        ergDict[kangaroo] = eList
                    else:
                        ergDict[kangaroo] = [joey]

for eList in sorted(ergDict):
    outP=eList+": "
    for e in sorted(ergDict[eList]):
        outP+= e+", "
    print(outP[:-2])
