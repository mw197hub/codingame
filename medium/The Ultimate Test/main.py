# https://www.codingame.com/ide/puzzle/the-ultimate-test

import sys,math
import itertools

n="123";k=6
#n="123987654";k=200
#n="1234789";k=45
#n="89765421";k=65

###
nList=[int(n)]
ergList=[]
for i in range(2,len(n)+1):
    zahlenList=[] 
    if i == len(n):
        zList=[]
        for teil in n:
            zList.append(int(teil))
        zahlenList.append(zList[:])
    else:
        zahlenList=[]
        posList=[]
        for anz in range(1,len(n)):
            posList.append([anz])
        for j in range(1,i):
            newList=[]
            for pList in posList:
                for anz in range(1,len(n)):
                    nList=pList[:]
                    nList.append(anz)
                    newList.append(nList[:])
            posList=newList[:]            
        #print(posList,file=sys.stderr)
        for pList in posList:
            if sum(pList) == len(n):
                zList=[];pos=0
                for p in pList:
                    zList.append(int(n[pos:pos+p]))
                    pos+=p
                zahlenList.append(zList[:])


    pmList=[]
    for z in range(i-1):
        pmList.append("+")
        pmList.append("-")
    perm = itertools.combinations(pmList,i-1)
    rechenzeichenList=[]
    for p in perm:
        if not p in rechenzeichenList:
            rechenzeichenList.append(p)
    #print(rechenzeichenList,file=sys.stderr)
    for zahlen in zahlenList:
        for rechen in rechenzeichenList:
            erg=str(zahlen[0]);summe=zahlen[0];pos=0
            for z in range(1,len(zahlen)):
                if rechen[pos] == "+":
                    summe+=zahlen[z]
                    erg+="+"
                else:
                    summe-=zahlen[z]
                    erg+="-"
                erg+=str(zahlen[z])
                pos+=1
            if summe == k:
                ergList.append(erg)



for erg in sorted(ergList):
    print(erg)
print("------",file=sys.stderr)
#ä#### Loesung

l = {0: '', 1: '+', 2: '-'}
n = n
mindex = 3 ** (len(n) - 1)
t = k

for i in range(mindex):
    ops = [l[(i // (3 ** j)) % 3] for j in range(len(n) - 1)][::-1]
    # n.chars -> list(n)
    # [n.chars] + [ops + ['']] -> [list(n), ops + ['']]
    expr = ''.join(a + b for a, b in zip(n, ops + ['']))
    if eval(expr) == t:
        print(expr)

