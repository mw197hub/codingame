import sys
import math

s,m = 4,4

serviceList = [5, 10, 4, 3]
matList = [['20', '5', '10', '7'], ['25', '3', '14', '16'], ['15', '4', '20', '10']]
aktivList = [0 for i in range(m)]

print(serviceList,file=sys.stderr)
print(matList,file=sys.stderr)
#print(aktivList,file=sys.stderr)

for mList in matList:
    erg = ""
    for i in range(len(mList)):
        rest = int(mList[i]) % serviceList[i]
        anzahl = int(mList[i]) // serviceList[i]
        if rest > 0:
            anzahl += 1
        zuwachs = anzahl - aktivList[i]
        aktivList[i] = aktivList[i] + zuwachs
        erg = erg + str(zuwachs) + " "
    print(erg[:-1])