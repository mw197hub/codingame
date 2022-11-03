#  https://www.codingame.com/ide/puzzle/genetics-and-computers---part-1

import sys,math,string


parent_1='RRYY'
parent_2='RRYY'
ratioList=['RRYY', 'rryy']

parent_1='TtYy'
parent_2='Ttyy'
ratioList=['TTYy', 'Ttyy', 'ttYy', 'ttyy', 'TtYy', 'TTyy']


aList=[];bList=[]
for i in range(2):
    for j in range(2,4):
        aList.append(parent_1[i]+parent_1[j])
        bList.append(parent_2[i]+parent_2[j])
genList=[]
for a in aList:
    for b in bList:
        g1 = b[0]+a[0] if a[0] in string.ascii_lowercase and b[0] in string.ascii_uppercase else a[0]+b[0]
        g2 = b[1]+a[1] if a[1] in string.ascii_lowercase and b[1] in string.ascii_uppercase else a[1]+b[1]
        genList.append(g1+g2)
print(genList,file=sys.stderr)

erg=""
anzList=[]
for ratio in ratioList:
    anz = 0
    for gen in genList:
        if gen == ratio:
            anz+=1
    anzList.append(anz)
print(anzList,file=sys.stderr)
div=1
for d in [16,8,4,2]:
    fertig=True
    for anz in anzList:
        if not anz % d == 0:            
            fertig=False
    if fertig:
        div = d
        break
for anz in anzList:
    erg = erg + str(int(anz/div))+":"

print(erg[:-1])