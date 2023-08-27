# https://www.codingame.com/ide/puzzle/duo-combinations

import sys,math


symbolList=['*', '#']
#symbolList=['0', '1','2']
symbolList=['^', '@', '$']
#symbolList=['*', '&', '^', '%']

l=len(symbolList)

wert=""
pos=0;start=0
for k in range(l-1):
    for j in range(start,2**l):
        binary = "{0:b}".format(j)
        s=binary
        if len(binary) < l:
            s = "0000000"[:l-len(binary)] + binary        
       # print("    "+s,file=sys.stderr)
        for i in range(l):
            if s[i] == "0":
                wert+=symbolList[pos]
            else:
                wert+=symbolList[pos+1]
        print(wert)
        wert=""
    pos+=1
    start=1
