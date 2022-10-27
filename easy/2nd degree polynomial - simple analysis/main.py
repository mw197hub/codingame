import sys
import math

def getY(a,b,c,x):
    return a*x**2+b*x+c

def getDelta(a,b,c):
    return b**2-4*a*c

def getX(a,b,c):
    x1 = (-b + math.sqrt(getDelta(a,b,c)))/(2*a)
    x2 = (-b - math.sqrt(getDelta(a,b,c)))/(2*a)
    return x1,x2

a,b,c=1,0,1
#a,b,c=1,0,-1
#a,b,c=0,0,0
#a,b,c=1,-2,1
a,b,c=3,0,-0.75


if a == 0 and b == 0 and c == 0:
    print("(0,0)")
else:
    if a == 0 and b == 0:
        print("(0,"+str(round(c,2))+")")
    else:
        xyDict={}
        xyDict[0] = [0,c]
        if a == 0:
            xyDict[(-c/b)] = [(-c/b),0]
        else:
            delta = getDelta(a,b,c)
            if delta == 0:
                xyDict[-b/(2*a)] = [-b/(2*a),0]
            elif delta > 0:
                x1,x2 = getX(a,b,c)
                xyDict[x1] = [x1,0]
                xyDict[x2] = [x2,0]
        erg = ""
        for xI in sorted(xyDict):
            xy = xyDict[xI]
            x,y=0,0
            if xy[0] == int(xy[0]):
                x = int(xy[0])
            else:
                x = round(xy[0],2)
            if xy[1] == int(xy[1]):
                y = int(xy[1])
            else:
                y = round(xy[1],2)
            erg = erg + "("+str(x)+","+str(y)+")"+","
        print(erg[:-1])
#else:
#    erg=""
#    x=-2
#    while x < 3:        
#        y = getY(a,b,c,x)
#        if x == 0 or y == 0:
#            if y == int(y):
#                y = int(y)
#            else:
#                y = round(y,2)
#            if x == int(x):
#                x = int(x)        
#            erg = erg + "("+str(x)+","+str(y)+")"+","
#        x+=0.5
#    print(erg[:-1])