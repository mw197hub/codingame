import sys
import time,math


nameList = ['test1.txt','test2.txt','test3.txt','test4.txt',
'test5.txt','test6.txt','test7.txt','test8.txt']

time_1 = time.time()

#name = "test1.txt"
#datei = open(name,'r')
#for zeile in datei:
#    print(zeile[:-1])

class Point():
    x,y = 0,0
    def __init__(self, x=0, y=0):self.x = x; self.y = y
    def __repr__(self) -> str:return (str(self.x) + " # " + str(self.y))
def distance(p1,p2):
    return math.sqrt( ((p1.x-p2.x)**2)+((p1.y-p2.y)**2) )
def gehe(p1,p2,move):
    dist = distance(p1,p2)
    if dist <= move:
        return p2
    p1.x = p1.x + int((p2.x - p1.x) / dist * move)
    p1.y = p1.y + int((p2.y - p1.y) / dist * move)
    return p1

p = gehe(Point(707,707),Point(9000,9000),1000)
print(str(p.x) + " " + str(p.y))