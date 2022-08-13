import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
erg = 0;max=0;min=99
n = int(input())
for i in input().split():           # 3 2 4 2 1 5
    v = int(i)
    if v > max:
        max = v;min = v
    if v < min:
        min = v
    if min - max < erg:
        erg = min - max

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(erg))
