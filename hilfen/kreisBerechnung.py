import sys
import math

def direction(p1,p2):
    return round(math.degrees(math.atan2(p2[1]-p1[1], p2[0]-p1[0])) % 180, 8)    

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def is_between(p1,p2,p3):
    return distance(p1,p3) + distance(p3,p2) == distance(p1,p2)

def flaeche(r):
    return math.pi * r**2
def umfang(r):
    return math.pi * r * 2

def kreisgleichung(xM,yM,r,grad):
    xA = r * math.cos(grad) + xM
    xA = xA +0.5 if xA > 0 else xA - 0.5
    yA = r * math.sin(grad) + yM
    yA = yA +0.5 if yA > 0 else yA - 0.5
    return int(xA),int(yA)

#print(flaeche(4.8))
#print(umfang(5))

for i in range(0,360,15):
    print("Grad: " + str(i),end="   ")
    print(kreisgleichung(0,0,15,math.radians(i)))


