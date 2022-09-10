import sys
import math

#n = 157285
#n = 25747
n =338066

erg = "Normal";teile=0
for i in range(1,10):
    mList=[]
    for w in str(n):
        mList.append(int(w)%i)
    print(mList)
    bisher = mList.pop(0);anz=1
    for m in mList:
        if not bisher == m:
            anz+=1;bisher=m
    if anz < teile:
        erg = i;break
    else:
        teile = anz


print(erg)