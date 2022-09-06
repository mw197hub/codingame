import sys
import math

n,m=6,3
xList=[1, 3, 7, 10, 10, 12]
n,m=26,5
xList=[0, 0, 2, 3, 8, 10, 16, 22, 23, 25, 26, 27, 33, 35, 38, 49, 58, 59, 61, 61, 67, 68, 68, 90, 97, 97]

xList = sorted(xList)
print(xList)
erg=9999

for i in range(n-m+1):
    if xList[i+m-1] - xList[i] < erg:
        erg = xList[i+m-1] - xList[i]

print(erg)