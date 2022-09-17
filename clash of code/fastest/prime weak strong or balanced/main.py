import sys
import math

'''
A prime is said to be weak if it smaller than the average of the two surrounding primes.
For example, 13 is a weak prime since it is less than the average of the two surrounding primes 11 and 17.
A prime is said to be balanced if it is the average of the two surrounding primes, i.e., it is at equal distance from previous prime and next prime.
Otherwise the prime is known as strong.
Input
13
Output
WEAK
'''

def getP(n,r):
    e = 0
    bis = 2 if r < 0 else n*n
    treffer = False
    for posP in range(n,bis,r):
        isPrime = True
        for num in range(2,posP):
            if posP %num == 0:
                isPrime=False
        e = posP
        if isPrime:
            break
    return e

n = 13
erg = 0

z1 = getP(13-1,-1)
z2 = getP(13+1,1)
erg = (z1 + z2) / 2

if n == erg:
    print("BALANCED")
elif n > erg:
    print("STRONG")
else:
    print("WEAK")

# 8 Minuten