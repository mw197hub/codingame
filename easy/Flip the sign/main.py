import sys
import math


zahlList=[]
wertList=['12', '-1', '4', '-21', '3', '8', '99', '4', '96', '-92', '1', '-31', '18', '-69', '-15', '26', '23', '7', '-77', '-73']
xList=['X', 'X', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

for i in range(len(xList)):
    x = xList[i]
    w = wertList[i]
    if x == "X":
        zahlList.append(int(w))
print(zahlList,file=sys.stderr)
erg = "true"
if len(zahlList) > 0:
    positiv = True if zahlList.pop(0) > 0 else False
    for z in zahlList:
        if positiv and z < 0:
            positiv = False
        elif not positiv and z > 0:
            positiv = True
        else:
            erg = "false"
            break


print(erg)
