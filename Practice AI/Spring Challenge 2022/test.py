import sys
import math
from collections import namedtuple

class figur:
    def __init__(self,id,wert):
        self.id=id;self.wert=wert

def distance(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

x1=0;y1=0;x2=17630;y2=9000  # 1,9588
#gesamtlänge 19794
windrange=2200;baseRange=300
# 2200*3+300=6500   # windPos(0,0)=5750,2935   windPos(17630,9000) = 11800,6065
print(distance(x1,y1,4315,3089))

figurList=[]
figurList.append(figur(0,10))
figurList.append(figur(1,8))
figurList.append(figur(2,5))

#for f in sorted(figurList,key=lambda figur: figur.wert):
#    print(f.id)

xList=[[11890,12200,12600,13300,12600,12200],[6760,6660,6500,6300,6500,6660],[1200,1700,2000,2300,1800,1700]]
yList=[[7200,6700,6400,5600,6400,6700],[700,1200,1700,2000,1700,1200],[6350,6200,5850,5300,5850,6200]]
xNew=[]
yNew=[]
zaehler=0
for i in range(6):
    x = xList[0][zaehler]
    y = yList[0][zaehler]
    xNew.append(17630-x)
    yNew.append(9000-y)
    zaehler=0 if zaehler > 4 else zaehler+1
print(xNew)
print(yNew)

