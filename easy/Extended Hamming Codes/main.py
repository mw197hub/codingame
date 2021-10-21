import sys
import math
import copy

def summeE(wertL,bitList):
    summe = 0
    for i in wertL:
        summe = summe + bitList[i]
    return geradeP(summe)

def geradeP(wert):
    if wert % 2:
        return False
    return True

def printBit(bList):
    ausgabe = ""
    for b in bList:
        ausgabe = ausgabe + str(b)
    print(ausgabe)

b = [1,3,5,7,9,11,13,15]
c = [2,3,6,7,10,11,14,15]
e = [4,5,6,7,12,13,14,15]
i = [8,9,10,11,12,13,14,15]

bits = "1100101010110110"
#bits = "1100101011110110"
#
# bits = "0111010001101111"

bitList = [int(a) for a in bits]
print(bitList,file=sys.stderr)
bitList2 = copy.deepcopy(bitList)

sumBool = geradeP(sum(bitList2))
bBool = summeE(b,bitList2)
cBool = summeE(c,bitList2)
eBool = summeE(e,bitList2)
iBool = summeE(i,bitList2)


if sumBool and (not bBool or not cBool or not eBool or not iBool):
    print('TWO ERRORS')
else:
    bitList2 = copy.deepcopy(bitList)
    for j in range(16):        
        if sumBool and bBool and cBool and eBool and iBool:
            printBit(bitList2)
            break
        bitList2 = copy.deepcopy(bitList)
        if bitList[j] == 0:
            bitList2[j] = 1
        else:
            bitList2[j] = 0
        sumBool = geradeP(sum(bitList2))
        bBool = summeE(b,bitList2)
        cBool = summeE(c,bitList2)
        eBool = summeE(e,bitList2)
        iBool = summeE(i,bitList2)
