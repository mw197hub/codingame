import sys
import math

n = 36
start = 1
erg = 0
while n > 0:
    if n == 1:
        erg = erg + start
    else:
        erg = erg + start + (start + (n -1)) + (start + (n - 1) *2) + (start + (n-1) *3)
    anzahl = n + n + n -2 + n -2
    start = start + anzahl
    n -= 2
    #print("n: " + str(n) + "  start: " + str(start))


print(str(erg))