#  https://www.codingame.com/ide/puzzle/hooch-clash

import sys,math

def getWert(d):
    return (4/3 * math.pi * (d/2)**3)

orbMin,orbMax=1,12
size1,size2=9,10

orbMin,orbMax=1,1000
size1,size2=90,492

orbMin,orbMax=1,3000
size1,size2=417,2962  # erg: 1290 2881


sum1 = getWert(size1) + getWert(size2)
print(sum1,file=sys.stderr)
wert1,wert2=0,0
ergList=[]
for i in range(orbMax,orbMin -1,-1):
    wert2 = getWert(i)
    if wert2 <= sum1:
        for j in range(orbMin,i):
            wert1 = getWert(j)
            if wert1 + wert2 <= sum1 + 0.001 and wert1 + wert2 >= sum1 - 0.001 :
                ergList.append([j,i])
print(ergList,file=sys.stderr)
noTreffer=True
for erg in ergList:
    if not erg[0] == size1 or not erg[1] == size2:
        print(str(erg[0])+" "+str(erg[1]))
        noTreffer=False
        break
if noTreffer:
    print("VALID")