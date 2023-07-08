# https://www.codingame.com/ide/puzzle/the-leaking-bathtub

import sys,math

#   1 Liter = 1000 cm³

def defWert(zahl):
    wert = str(zahl)
    if len(wert) == 1:
        return "0"+wert
    return wert

#1    01:14:08
s,h,flow=12750,60,12
leakList=[[20, 1], [45, 3]]

#4    01:00:00
#s,h,flow=8000,90,12
#leakList=[]

#5     88:14:20
s,h,flow=12500000,300,2800

sekProCm= 60 / (flow*1000 / s)
print(sekProCm,file=sys.stderr)
leakSum=0;zeit=0
for i in range(h):
    for leak in leakList:
        if i == leak[0]:
            leakSum+=leak[1]
    if leakSum >= flow:
        print("Impossible, {} cm.".format(i))
        break   
    zeit = zeit + (60 / ((flow - leakSum)*1000 / s))

sek = defWert(int(zeit%60))
min = defWert(int(zeit/60%60))
std = defWert(int(zeit/3600))
print("{}:{}:{}".format(std,min,sek))