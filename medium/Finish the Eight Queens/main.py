# https://www.codingame.com/ide/puzzle/finish-the-eight-queens

import sys,math

def testLauf(fertig,ergList,posList,yList,xList):
    for y in yList:
        for x in xList:
            yNList= yList[:];yNList.remove(y)
            xNList= xList[:];xNList.remove(x)
            ergList.append([y,x])
            fertig = testLauf(fertig,ergList,posList,yNList,xNList)
    #print(ergList)
    if len(ergList) + len(posList) == 8:
    #    if [7,2] in ergList and [6,4] in ergList and [3,5] in ergList and [1,6] in ergList:
    #        a=0
        testList= ergList[:] + posList[:]
        okay=True
        for i in range(7):
            tP=testList[i]
            for j in range(7):
                for yN,xN in [[1,1],[1,-1],[-1,1],[-1,-1]]:
                    yN=tP[0]+yN;xN=tP[1]+xN
                    if [yN,xN] in testList:
                        okay=False
            #for j in range(i+1,8):
            #    tN=testList[j]
            #    if tP[0] == tN[0] or tP[1] == tN[1]:
            #        okay=False
        if okay:
            fertig1=ergList[:] + posList[:]
            fertig1=sorted(fertig1)
            if not fertig1 in fertig:
                fertig.append(fertig1[:])
    if len(ergList) > 0:
        ergList.pop()
    return fertig

####
rowList=['Q.......', '........', '...Q....', '........', '.......Q', '.Q......', '........', '........']
rowList=['........', '..Q.....', '....Q...', '......Q.', '........', '........', '........', '........']
#rowList=['........', '........', '.......Q', 'Q.......', '........', '......Q.', '....Q...', '........']
rowList=['...Q....', '........', '........', '........', '......Q.', '........', '........', '....Q...']

#####
ergList=[];fertig=[]
posList=[];yList=[];xList=[]
for i in range(8):
    yList.append(i);xList.append(i)
for y in range(8):
    for x in range(8):
        if rowList[y][x] == "Q":
            posList.append([y,x])
            yList.remove(y);xList.remove(x)
print(posList,file=sys.stderr)
print("yList={}     xList={}".format(yList,xList),file=sys.stderr)

fertig = testLauf(fertig,ergList,posList,yList,xList)
for f in fertig:
    for y in range(8):
        erg=""
        for x in range(8):
            if [y,x] in posList or [y,x] in f:
                erg+="Q"
            else:
                erg+="."
        print(erg)
    print("----")
print(len(fertig),file=sys.stderr)