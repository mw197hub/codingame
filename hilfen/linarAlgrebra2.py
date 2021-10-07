import sys
import math
from math import atan2, degrees
from math import acos, sqrt, pi

def length(v):
    return sqrt(v[0]**2+v[1]**2)
def dot_product(v,w):
   return v[0]*w[0]+v[1]*w[1]
def determinant(v,w):
   return v[0]*w[1]-v[1]*w[0]
def inner_angle(v,w):
   cosx=dot_product(v,w)/(length(v)*length(w))
   rad=acos(cosx) # in radians
   return rad*180/pi # returns degrees
def angle_clockwise(A, B):
    inner=inner_angle(A,B)
    det = determinant(A,B)
    if det<0: #this is a property of the det. If the det < 0 then B is clockwise of A
        return inner
    else: # if the det > 0 then A is immediately clockwise of B
        return 360-inner


def direction(p1,p2):
    return round(degrees(atan2(p2[1]-p1[1], p2[0]-p1[0])) % 180, 8) 

def neigung(p1, p2):
    div = p2[0] - p1[0]
    if p2[0] - p1[0] == 0:
        div = 1
    wert = (p2[1]  - p1[1] )*45.0 / ( div )
    factor = 1

    wert = wert * factor
    return wert

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def is_between(p1,p2,p3):
    return distance(p1,p3) + distance(p3,p2) == distance(p1,p2)

startPoint = [2500,2700]
#startPoint = [3,3]
zielPoint = [4750, 150]
#zielPoint = [5, 1]
ship = [0,2]

dist = distance(startPoint,zielPoint)
print(dist)
neig = neigung(startPoint,zielPoint)
print("Neigung: ",end="")
print(neig)
#direkt = direction(startPoint,zielPoint)
#print(direkt)

if is_between(startPoint,zielPoint,ship):
    print("auf der Linie")
else:
    print("Abstand: ?" )

print(math.atan2(8,5))
print(round(degrees(atan2(startPoint[0] - zielPoint[0], startPoint[1] - zielPoint[1] ))))