import math

class Point():
    x = 0
    y = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
 
def distance(p1,p2):
    return math.sqrt( ((p1.x-p2.x)**2)+((p1.y-p2.y)**2) )

def is_between(p1,p2,p3):
    return distance(p1,p3) + distance(p3,p2) == distance(p1,p2)

def GetLinePara(line):
    line.a = line.p1.y - line.p2.y; line.b = line.p2.x - line.p1.x
    line.c = line.p1.x * line.p2.y - line.p2.x * line.p1.y
 
def GetCrossPoint(l1,l2):
    GetLinePara(l1);  GetLinePara(l2)
    d = l1.a * l2.b - l2.a * l1.b; p = Point()
    p.x = (l1.b * l2.c - l2.b * l1.c)*1.0 / d
    p.y = (l1.c * l2.a - l2.c * l1.a)*1.0 / d
    return is_between(l2.p1,l2.p2,p), p
 
landList = [[0, 1000], [300, 1500], 
[350, 1400], [500, 2000],
 [800, 1800], [1000, 2500], 
 [1200, 2100], [1500, 2400],
  [2000, 1000], [2200, 500], 
  [2500, 100], [2900, 800],
   [3000, 500], [3200, 1000],
    [3500, 2000], [3800, 800],
     [4000, 200], [5000, 200], 
     [5500, 1500], [6999, 2800]]
p1 = Point(1,1)
p2 = Point(3,3)
line1 = Line(p1,p2)
 
p3 = Point(0, 2)
p4 = Point(5, 2)
line2 = Line(p3,p4)
treffer, Pc = GetCrossPoint(line1,line2)
if treffer:
    print("Cross point:", Pc.x, Pc.y)
else:
    print("keine Kreuzung")

startP = Point(500,2700)
zielP = Point(4500,200)
schnittPunkt = False
landP1 = landList[0]
for i in range(1,len(landList)):
    landP2 = landList[i]
    if (startP.x < zielP.x and landP1[0] >= startP.x and landP2[0] >= startP.x and landP1[0] <= zielP.x and landP2[0] <= zielP.x) or (startP.x > zielP.x and landP1[0] <= startP.x and landP2[0] <= startP.x and landP1[0] >= zielP.x and landP2[0] >= zielP.x):
        cross,pCross = GetCrossPoint(Line(startP,zielP),Line(Point(landP1[0],landP1[1]),Point(landP2[0],landP2[1])))
        if cross:
            print("Schnittpunkt  " + str(i), end=" ")
            print(landP1,end="  -  ")
            print(landP2)
    landP1 = landList[i]    