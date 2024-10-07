# https://www.codingame.com/ide/puzzle/number-of-digits

import sys,math

n=219
k=5   # 42

n=4218
k=4    # 1461

n=248919
k=7     # 119682

zahlDict={999999999:900000000,99999999:80000000,9999999:7000000,999999:600000,99999:50000,9999:4000,999:300,99:20,9:1}

erg=0
for i in range(n+1):
    zahl=str(i)
    for z in zahl:
        if z == str(k):
            erg+=1
print(erg)

###
n=248919

erg, start = 0, 1
while start <= n:
    high, cur, low = n // (start * 10), (n // start) % 10, n % start
    wert1=0;wert2=0
    if cur == k:
        wert1 = 1
    elif cur > k:
        wert2 =1
    erg += high * start + wert1 * (low + 1) + wert2 * start
    start *= 10
print(erg)

