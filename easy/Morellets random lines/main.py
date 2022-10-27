import sys
import math

# Linie - formel:   ax + by + c = 0

def formel(a,b,c,x,y):
    return a*x + b * y + c 
def formelY(a,b,c,x):
    if b == 0:
        return 0
    return (-(a*x) -c)/b

xyList=[[1, 1], [0, 0]]
abcList=[[1, 2, 3]]

xyList=[[3, 2], [-2, -2]]
abcList=[[1, 2, 3], [1, 1, 1]]

#xyList=[[-1, 0], [-2, 0]]
#abcList=[[1, 1, 1]]

xyList=[[0, 0], [1, 1]]
abcList=[[1, 1, -1], [-1, -1, 1]]

onLine=False;ergList=[]
for xy in xyList:
    fList=set();farbe=False
    for abc in abcList:
        e = formel(abc[0],abc[1],abc[2],xy[0],xy[1])
        if e == 0:
            onLine=True
            break
        fList.add(formelY(abc[0],abc[1],abc[2],xy[0]))
    #print(fList,file=sys.stderr)
    for f in fList:
        if f < xy[1]:
            farbe = not farbe
    ergList.append(farbe)
    
#print(ergList)
if onLine:
    print("ON A LINE")
elif ergList[0] == ergList[1]:
    print("YES")
else:
    print("NO")