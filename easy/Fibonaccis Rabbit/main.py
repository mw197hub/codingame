# https://www.codingame.com/ide/puzzle/fibonaccis-rabbit

import sys,math

'''
fi=1;vor=1
for i in range(1,10):
    wert=fi+vor
    vor=fi
    fi=wert
    print(fi,end=", ")
print("")
'''

f0,n,a,b=1,10,1,2   #1  = 89
f0,n,a,b=4,12,1,3   #2  = 3708

fiList=[f0]
for i in range(n):
    wert=0
    for g in range(a,b+1):
        if g <= len(fiList):
            wert+=fiList[-g]
    fiList.append(wert)
    #fiList.append(fiList[-1]+fiList[-2])
    print(fiList[-1],end=", ",file=sys.stderr)
print(" ",file=sys.stderr)
print(fiList[-1])

