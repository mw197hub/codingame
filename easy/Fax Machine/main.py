import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = 8
h = 3
t = [int(v) for v in "10 10 4".split(" ")]
print(t,file=sys.stderr)
print(sum(t),file=sys.stderr)
black = True
anzahl = 0
for zahl in t:
    for i in range(zahl):
        if anzahl == 0:
            print("|",end="")
        if black:
            print("*",end="")
        else:
            print(" ",end="")
        anzahl += 1
        if anzahl == w:
            print("|")
            anzahl = 0
    black = False if black else True
