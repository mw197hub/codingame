# https://www.codingame.com/ide/puzzle/the-descent---part-2

import sys,math

def ermittleDiff(y,x,a,b,mList,t):
    if y == 4 and x == 1:
        xxx=0
    wertList=[];xyList=[];diff=t+10
    for yN in range(y,y+a):
        for xN in range(x,x+b):
            if yN < len(mList) and xN < len(mList[0]):
                wertList.append(mList[yN][xN])
                xyList.append([yN,xN])
    if len(wertList) == a*b:
        minWert = min(wertList)
        sumWert = sum(wertList)
        diff = sumWert - (minWert*len(wertList))
    if not a == b:
        wertList.clear();xyList.clear()
        for yN in range(y,y+b):
            for xN in range(x,x+a):
                if yN < len(mList) and xN < len(mList[0]):
                    wertList.append(mList[yN][xN])
        if len(wertList) == a*b:
            minWert = min(wertList)
            sumWert = sum(wertList)
            diff1 = sumWert - (minWert*len(wertList))
            if diff1 < diff:
                diff = diff1
    if diff <= t:
        return diff
    return t+10


##########
#1
a=2;b=2;t=10;mList=[[2, 2, 3, 4], [4, 5, 6, 4], [5, 5, 5, 4], [4, 4, 4, 4]]
#2
a=4;b=3;t=28;mList=[[15, 14, 16, 18, 17, 19, 15, 14], [13, 14, 15, 16, 15, 14, 11, 12], [15, 14, 9, 2, 15, 14, 16, 15], [11, 12, 13, 14, 15, 16, 17, 18], [18, 17, 16, 15, 14, 13, 12, 11], [15, 15, 15, 15, 14, 14, 16, 18], [18, 17, 18, 17, 15, 12, 11, 8]]


#8
#a=2;b=3;t=15;mList=[[13, 14, 15, 17, 18, 22], [23, 23, 22, 21, 23, 21], [23, 23, 23, 17, 19, 12], [24, 25, 24, 21, 24, 23], [29, 28, 26, 24, 24, 24], [27, 28, 24, 27, 24, 24], [19, 18, 17, 26, 24, 24]]
#10
#a=13;b=14;t=1520;mList=[[21, 23, 24, 25, 26, 21, 27, 28, 29, 28, 30, 31, 32], [22, 26, 25, 28, 27, 24, 25, 26, 23, 30, 31, 20, 19], [22, 23, 21, 30, 31, 34, 32, 28, 27, 29, 25, 20, 19], [24, 25, 26, 27, 28, 24, 21, 23, 20, 19, 31, 32, 34], [21, 23, 24, 25, 26, 21, 27, 28, 29, 28, 30, 31, 32], [22, 26, 25, 28, 27, 24, 25, 26, 23, 30, 31, 20, 19], [22, 23, 21, 30, 31, 34, 32, 28, 27, 29, 25, 20, 19], [24, 28, 25, 26, 21, 23, 24, 31, 34, 35, 38, 37, 34], [31, 32, 34, 35, 36, 37, 30, 29, 28, 31, 34, 35, 36], [22, 26, 25, 28, 27, 24, 25, 26, 23, 30, 31, 20, 19], [22, 23, 21, 30, 31, 34, 32, 28, 27, 29, 25, 20, 19], [24, 28, 25, 26, 21, 23, 24, 31, 34, 35, 38, 37, 34], [31, 32, 34, 35, 36, 37, 30, 29, 28, 31, 34, 35, 36], [24, 28, 25, 26, 21, 23, 24, 31, 34, 35, 38, 37, 34], [31, 32, 34, 35, 36, 37, 30, 29, 28, 31, 34, 35, 36]]



ergMin=t+10
rand=min(a,b)-1
for y in range(len(mList)-rand):
    for x in range(len(mList[0])-rand):
        wert=ermittleDiff(y,x,a,b,mList,t)
        if wert < ergMin:
            ergMin = wert

if ergMin <= t:
    print(ergMin)
else:
    print("Not Possible")