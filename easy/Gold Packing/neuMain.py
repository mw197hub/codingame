import sys
import math
import time

def barsOfBin(reversedBin,bars):
    bars1 = []
    for i in range(0,len(reversedBin)):
        if reversedBin[i] == 1:
            bars1.append(bars[i])
    #print("erg: " + str(bars1))
    return bars1

def barsOfCombinationId(i,bars):
    bin = dec2bin(i,bars)
    #print(bin,file=sys.stderr)
    return barsOfBin((bin),bars)

def dec2bin(dec,bars):
    if dec == 0:
        return [0]
    stack = []
    num = dec
    while num > 0:
        stack.append(num % 2)
        num = int(num/2)
    result = []
    for i in range(0,len(bars) - len(stack)):
        result.append(0)
    while stack:
        result.append(stack.pop())
    return result

def process(m,bars):
    c = int(math.pow(2,len(bars)))
    validLengths = []
    for i in range(0,c):
        barSet = barsOfCombinationId(i,bars)
        #print(barSet,file=sys.stderr)
        if sum(barSet) <= m:
            validLengths.append([sum(barSet),len(barSet),i,barSet])
    #print(sorted(validLengths),file=sys.stderr)
    newErg = []
    newErg.append(sorted(validLengths).pop())
    for e in sorted(validLengths):
        if e[0] == newErg[0][0]:
            newErg.append(e)
    newErg1 = []
    laenge = 99
    for e in newErg:
        if e[1] < laenge:
            laenge = e[1]
    for e in newErg:
        if e[1] == laenge:
            newErg1.append(e)
    print(newErg1,file=sys.stderr)
    ind1 = 0
    for e in newErg1:
        if e[2] > ind1:
            ind1 = e[2]
    for e in newErg1:
        if ind1 == e[2]:
            erg = e
    ergStr = ""
    for e in erg[3]:
        ergStr = ergStr + " " + str(e)
    return ergStr[1:]


m = 1489
n = 19
# 3 6 10 21 28 45 55 66 78 91 105 120 136 153 171 190 210
barList = [3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]

m = 113
n = 10
barList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

m = 46
n = 7
barList = [1, 3, 5, 7, 9, 11, 13]

#m = 6
#n = 3
#barList = [1, 2, 4]

startTime = time.time()

resultE = process(m,barList)
print(resultE)

print('{:5.3f}s'.format(time.time()-startTime))