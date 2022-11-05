#  https://www.codingame.com/ide/puzzle/ww2-mortar-warfare

import sys,math

n='-+500+--'
#n='+777+--'
#n='300'

wert=""
for i in range(len(n)):    
    if n[i].isdigit():
        wert+=n[i]
m=int(wert)
if m > 1800:
    print("OUT OF RANGE")
else:
    d1=(math.asin((m*9.8)/(158*158)))/2
    d2 = math.pi / 2 - d1
    deg1 = math.degrees(math.pi/2 - d1)
    deg2 = math.degrees(math.pi/2 - d2)
    if (deg1 < 40 and deg2 < 40) or (deg1 > 85 and deg2 > 85) or (deg1 < 40 and deg2 > 85) or (deg1 > 85 and deg2 < 40):
        print("OUT OF RANGE")
    else:   
        deg = deg1
        if deg1 < 40 or deg1 > 85:
            deg = deg2
        s=(2*158*math.sin(d2))/9.8


        deg = round(deg,1)
        sek = round(s,1)
        print(str(deg) + " degrees")
        print(str(sek) + " seconds")