# https://www.codingame.com/ide/puzzle/ascii-worms

import sys,math

thickness=2;length=5;turns=4
thickness=1;length=2;turns=2
thickness=1;length=15;turns=15



breite=(turns+1)*thickness+turns+2
querList = [0,breite-1]
start=0
oben=[]
unten=[]
yOben=True
for i in range(turns+1):
    start=start+thickness+1
    querList.append(start)
    if yOben:
        unten.append(start)
    else:
        oben.append(start)
    if yOben:
        yOben=False
    else:
        yOben=True
ungerade=True
if turns//2 == turns/2:
    ungerade=False


for y in range(length+1):
    for x in range(breite):
        if x in querList:
            if y > 0:
                if y == 1 and x in oben:
                    if ungerade and x == breite -1:
                        print("|",end="")
                    else:
                        print(" ",end="")
                elif  y == length and x in unten and x < breite-1:
                    if y == length:
                        print("_",end="")
                    else:
                        print(" ",end="")
                else:                    
                    print("|",end="")
            else: 
                if x in oben:
                    if x == breite -1 and y == 0 and ungerade:
                        a=0
                    else:
                        print("_",end="")               
                else:
                    if y == 0 and x == breite -1:
                        a=0
                    else:
                        print(" ",end="")
        else:
            if y == 0 or y == length:
                print("_",end="")
            else:
                print(" ",end="")
    print("")