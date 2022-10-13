import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
abcDict={}
rows = int(input())
for i in range(rows):
    row = input().split(" ")
    for j in range(len(row)):
        abcDict[row[j]] = str(i)+str(j)
print(abcDict,file=sys.stderr)
message = input()
for m in message:
    print(abcDict[m],end="")
print("")
