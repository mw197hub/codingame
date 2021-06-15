import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
erg = int(0)
for i in input().split():
    b = int(i)
    if b > l / 2:
        if b > erg:
            erg = b
    else:
        if erg < abs(l - b):
            erg = abs(l - b)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(erg))