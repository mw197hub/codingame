from random import randrange, random
import math,copy


#for _ in range(20):
#    print(randrange(2))

def kreisgleichung(xM,yM,r,grad):
    xA = r * math.cos(grad) + xM
    xA = xA +0.5 if xA > 0 else xA - 0.5
    yA = r * math.sin(grad) + yM
    yA = yA +0.5 if yA > 0 else yA - 0.5
    return int(xA),int(yA)

#print(flaeche(4.8))
#print(umfang(5))
punktDict=[]

for r in range(100,1000,100):
    for i in range(0,360,15):
        punktDict.append((kreisgleichung(0,0,r,math.radians(i))))
print(punktDict)
print(len(punktDict))
