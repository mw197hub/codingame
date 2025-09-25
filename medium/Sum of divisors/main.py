# https://www.codingame.com/ide/puzzle/sum-of-divisors

import sys,math

n=4

total=0
for d in range(1,n+1):
    v=n//d
    total+=d*v

print(total)