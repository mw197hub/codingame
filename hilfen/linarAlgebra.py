import sys
import math
import binascii
import numpy as np
import matplotlib
import numpy as np 
from matplotlib import path
from math import atan2, degrees

def slope(p1, p2):
    if p2[0] - p1[0] == 0:
        return 0
    return (p2[1]  - p1[1] )*1.0 / ( p2[0] - p1[0] )

def direction(p1,p2):
    return round(degrees(atan2(p2[1]-p1[1], p2[0]-p1[0])) % 180, 8)    

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def is_between(p1,p2,p3):
    return distance(p1,p3) + distance(p3,p2) == distance(p1,p2)

def is_inside_polygon(pList,p):
    pos,neg = 0,0
    if p in pList:
        return True
    for i in range(len(pList)):
        x1 = pList[i][0]
        y1 = pList[i][1]
        i2 = 0
        if i < len(pList) -1:
            i2 = i + 1
        x2 = pList[i2][0]
        y2 = pList[i2][1]
        x,y = p[0],p[1]

        d = (x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)
        if d > 0:
            pos += 1
        if d < 0:
            neg += 1
        if pos > 0 and neg > 0:
            return False
    return True

# point in polygon  mit matplotlib
p = path.Path([[0, 0], [100, 0], [150, 50], [100, 100], [0, 100]]) 
result = p.contains_points([(125, 76)])
print(result)

# punkt auf Linie
print(is_between([0,0],[100,100],[1,1]))

print("-----")
# entfernung von punkten
pList = [[0, 0], [100, 0], [150, 50], [100, 100], [0, 100]]
p = [150,0]
print(is_inside_polygon(pList,p))
