# https://www.codingame.com/ide/puzzle/bouncing-simulator

import math,sys

w=7;h=3;n=2
w=4;h=3;n=4


####

feldList=[]
for y in range(h):
    yList=[]
    for x in range(w):
        yList.append(0)
    feldList.append(yList)
print(feldList,file=sys.stderr)
ball=[0,0]
richtung=[1,1]
while True:
    feldList[ball[0]][ball[1]]+=1   
    ball[0]+=richtung[0];ball[1]+=richtung[1]
    mod=0
    if ball[0] < 0:
        ball[0]-=richtung[0]
        mod=1;richtung[0]=1;ball[0]+=richtung[0]
    if ball[0] >= h:
        ball[0]-=richtung[0]
        mod=1;richtung[0]=-1;ball[0]+=richtung[0]
    if ball[1] < 0:
        ball[1]-=richtung[1]
        mod=1;richtung[1]=1;ball[1]+=richtung[1]
    if ball[1] >= w:
        ball[1]-=richtung[1]
        mod=1;richtung[1]=-1;ball[1]+=richtung[1]
    
    n-=mod
    if n <= 0:
        break

rahmen='#'*(w+2)
print(rahmen)
for feld in feldList:
    zeile="#"
    for f in feld:
        if f == 0:
            zeile+=" "
        else:
            zeile+=str(f)
    print(zeile+"#")
print(rahmen)