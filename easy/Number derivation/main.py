import sys
import math

def berechnen(n):
    res = 0
    cpy = n
    p = 2
    while p <= cpy:
        while cpy % p == 0:
            cpy =(cpy / p)
            res = res + (n/p)
        p += 1
    return res

n = 42 # 41
n =  7 # 1
n = 81 # 108

res = berechnen(n)
print("{0:.0f}".format(res))