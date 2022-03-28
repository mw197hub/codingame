import sys
import math

frame_pattern,h,w="#.",1,1
lineList = ['x']
frame_pattern,h,w="o",5,17
lineList = ['  ..@*@*', ' .@*  ..@*', '..@*    .@*', ' .@*  ..@*', '   .@*@*.........']

weite = w
h = h + len(frame_pattern) * 2 + 2
w = w + len(frame_pattern) * 2 + 2

for i in range(h):
    for j in range(w):
        pos = i if i < j else j
        end = h-i-1 if h-i-1  < w-j-1 else w-j-1
        if end < pos:
            pos = end
        z = " "
        if pos < len(frame_pattern):
            z = frame_pattern[pos]
        else:
            if i > len(frame_pattern) and i <= len(frame_pattern) + len(lineList):
                linie = lineList[i - len(frame_pattern)-1]
                if j > len(frame_pattern) and j <= len(frame_pattern) + weite and len(linie) > j-len(frame_pattern)-1:
                    z = linie[j-len(frame_pattern)-1]


        print(z,end="")
    print()