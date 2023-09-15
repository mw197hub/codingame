import sys

connections=[[0, 2], [2, 4], [2, 1], [1, 3], [3, 4]]
#connections=[[2, 1], [0, 2], [0, 1]]
connections=[[9, 7], [6, 0], [5, 6], [9, 0], [2, 8], [4, 5], [6, 8], [3, 6], [9, 1]]
connections=[[8, 39], [46, 10], [4, 40], [44, 32], [3, 6], [22, 8], [18, 5], [17, 29], [41, 22], [41, 15], [3, 5], [19, 32], [29, 20], [5, 28], [8, 1], [5, 24], [30, 6], [29, 34], [45, 41], [13, 5], [32, 20], [41, 14], [32, 33], [46, 30], [20, 42], [28, 41], [41, 33], [4, 7], [24, 8], [41, 11], [5, 37], [8, 49], [32, 21], [41, 0], [41, 36], [8, 45], [32, 12], [46, 49], [45, 4], [46, 2], [41, 23], [38, 5], [32, 16], [27, 29], [43, 8], [47, 4], [26, 8], [41, 43], [8, 9], [8, 31], [25, 8], [7, 41], [42, 13], [41, 48], [8, 37], [10, 32], [32, 48], [46, 35], [46, 26], [10, 4], [32, 11], [41, 24]]


clock=set()
counter=set()
connDict={}
for conn in connections:
    c0 = str(conn[0])
    c1 = str(conn[1])
    if c0 in connDict:
        cSet = connDict[c0]
        if not c1 in cSet:
            cSet.append(c1)
    else:
        connDict[c0] = [c1]
    if c1 in connDict:
        cSet = connDict[c1]
        if not c0 in cSet:
            cSet.append(c0)
    else:
        connDict[c1] = [c0]

print(connDict,file=sys.stderr)


clockWise=1
posC=str(0)
erledigt=[];fehler=False
for i in range(len(connDict)):
    erledigt.append(posC)
    cSet = connDict[posC]
    if clockWise == 1:
        clock.add(posC)
    else:
        counter.add(posC)
    for c in cSet:
        if clockWise == 1:
            counter.add(c)
        else:
            clock.add(c)
    if i < len(connDict)-1:
        posC="-1"
        for c in counter:
            if not c in erledigt:
                posC = c;break
        clockWise=-1
        if posC in clock:
            fehler=True
        if posC == "-1":
            for c in clock:
                if not c in erledigt:
                    posC = c;break
            if posC in counter:
                fehler=True
            clockWise=1
ergL=[]
if fehler:
    ergL.append(-1);ergL.append(-1)
else:
    ergL.append(len(clock));ergL.append(len(counter))
print(ergL)