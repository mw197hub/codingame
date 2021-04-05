import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t1List = {}
t2List = {}
t3List = {}
output = []
outZeile = ""
w, h, t1, t2, t3 = [int(i) for i in input().split()]
print(str(w) + " " + str(h) + " : " + str(t1) + " "+ str(t2) + " " + str(t3),file=sys.stderr)
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    zeile = ""
    for j in range(w):
        zeile = zeile + "."
        t = first_picture_row[j:j+1]
        if not t == ".":
            t1List[t] = [i,j]
    for j in range(w):
        t = second_picture_row[j:j+1]
        if not t == ".":
            t2List[t] = [i,j]
    outZeile = zeile
    output.append(zeile)
print(t1List,file=sys.stderr)
print(t2List,file=sys.stderr)

for buch,koor1 in sorted(t1List.items()):
    koor2 = t2List[buch]
    w1 = (koor2[0] - koor1[0]) / (t2 - t1) * (t3 - t2)
    h1 = (koor2[1] - koor1[1]) / (t2 - t1) * (t3 - t2)
    w1 = (math.floor(w1 + koor2[0]))
    h1 = (math.floor(h1+ koor2[1]))
    t3List[buch] = [w1 ,h1]
    if w1 >= 0 and h1 >= 0 and w1 <= w and h1 <= h:
        out2 = output[w1]
        if out2[h1:h1+1] == ".":
            out2 = out2[:h1]  + buch + out2[h1+1:] 
            output[w1] = out2

print(t3List,file=sys.stderr)
for out in output:
    print(out)