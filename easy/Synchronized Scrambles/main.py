# https://www.codingame.com/ide/puzzle/synchronized-scrambles

import sys,math

def berechnen(h,m,offset):
    if offset[0] == "-":
        h = h - int(offset[1:3])
        m = m - int(offset[3:5])
    else:
        h = h + int(offset[1:3])
        m = m + int(offset[3:5])
    if m < 0:
        h = h -1
        m = 60 + m
    if m > 59:
        h = h + 1
        m = m - 60
    if h < 0:
        h = 24 + h
    if h > 23:
        h = h - 24
    return str(int(str(h).zfill(2)+str(m).zfill(2))).zfill(4)


offset1="-0930";offset2="-0044"
offset1="+0545";offset2="-0100"
offset1="+0451";offset2="+0730"


outList=[]
for h in range(24):
    for m in range(60):
       # print(str(h)+":"+str(m))
        if h == 20 and m == 4:
            a = 1
        time1 = berechnen(h,m,offset1)
        time2 = berechnen(h,m,offset2)
        if sorted(str(time1)) == sorted(str(time2)):
            outList.append(time1+", "+time2)
            #print("{}, {}".format(time1,time2))

for out in sorted(outList):
    print(out)
