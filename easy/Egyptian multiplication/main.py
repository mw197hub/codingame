# https://www.codingame.com/ide/puzzle/egyptian-multiplication

import sys,math,copy


a=3;b=12 #1
a=20;b=2 #2


###
wert=a;multi=b;reste=[]
if a < b:
    wert=b;multi=a
print("{} * {}".format(wert,multi))
while multi > 0:
    nMulti=multi//2
    nRest=multi%2
    if nRest > 0:
        reste.append(wert)    
    rest=""
    for r in reste:
        rest = rest + " + " + str(r)
    if not multi-nRest == multi:
        print("= {} * {}{}".format(wert,multi-nRest,rest))
    
    wert=wert*2
    multi=nMulti
    if multi == 0:
        break
    print("= {} * {}{}".format(wert,multi,rest))

print("= {}".format(a*b))