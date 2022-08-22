import sys
import math
import copy



def move(l,lineList,h,w,ih,iw,moveDict):
    m=[]
    if lineList[ih][iw] == ">":
        m = [0,1]
    if lineList[ih][iw] == "<":
        m = [0,-1]
    if lineList[ih][iw] == "v":
        m = [1,0]
    if lineList[ih][iw] == "^":
        m = [-1,0]
        
    nh = ih + m[0];nw = iw + m[1]       
    if nh >= h:
        nh = 0
    if nh < 0:
        nh = h-1
    if nw >= w:
        nw = 0
    if nw < 0:
        nw = w -1 
    if str(nh)+"-"+str(nw) in moveDict:
        moveDict[str(nh)+"-"+str(nw)] = "x"
    else:
        moveDict[str(nh)+"-"+str(nw)] = lineList[ih][iw]

    lineList[ih][iw] = "."

def bewegen(lineList,h,w):   
    moveDict={}
    for ih in range(h):
        line = lineList[ih]
        for iw in range(w):
            l = line[iw]
            if l in "><v^":
                move(l,lineList,h,w,ih,iw,moveDict)
    anzahl = 0

    for m,feld in moveDict.items():
        m1,m2=m.split("-")
        if not feld == "x":
            lineList[int(m1)][int(m2)] = feld
            anzahl +=1
    return anzahl

h,w = 5,5
lineList2 = ['.....', '..v..', '.>.<.', '..^..', '.....']

h,w=5,6
lineList2 = ['>.....', '......', '......', '......', '.....^']


lineList = []
for line in lineList2:
    lineList.append(list(line))

runde = 0
while True:
    anzahl = 0
    anzahl = bewegen(lineList,h,w)
    runde += 1
    print(runde,file=sys.stderr)
    print(lineList)
    if anzahl == 0:
        break
print(runde)