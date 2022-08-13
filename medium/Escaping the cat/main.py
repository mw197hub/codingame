import sys
import math

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def getKreis(r):
    rList = []
    for grad in range(360):
        x = int(r * math.cos(grad) + 0)
        y = int(r * math.sin(grad) + 0)
        rList.append([x,y])
        #print(distance([0,0],[x,y]),file=sys.stderr)
    return rList

def getZiel(abstand_Cat,rList,mList,cat_x,cat_y,mouse_x,mouse_y,abstand,fertig):
    zielX,zielY=0,0
    if abstand_Cat > abstand:
        zielA = 0
        for p in rList:
            if zielA < distance([cat_x,cat_y],p):
                zielA = distance([cat_x,cat_y],p)
                zielX,zielY = p[0],p[1]
        fertig = True
    else:
        zielA = 0
        for p in mList:
            if zielA < distance([cat_x,cat_y],p):
                zielA = distance([cat_x,cat_y],p)
                zielX,zielY = p[0],p[1]

    return zielX,zielY,fertig

mouse_x,mouse_y,mouse_speed = -430,0,10
cat_x,cat_y,cat_speed = -499,0,10  # 39
r = 501;cap=80;runde=0;abstand=620;zielX,zielY=0,0
#umfang = r *math.pi * 2
#print(umfang,file=sys.stderr) #3141
mouse_r = 130 # abstand zur Katze 610
rList = getKreis(r)
mList = getKreis(mouse_r)

fertig=False
# game loop
while True:    
    mouse_x, mouse_y, cat_x, cat_y = [int(i) for i in input().split()]
    print(str(mouse_x)+"-"+str(mouse_y)+"  abstand: " + str(distance([0,0],[mouse_x,mouse_y])),file=sys.stderr)
    runde += 1
    abstand_Cat = distance([mouse_x,mouse_y],[cat_x,cat_y])
    if not fertig:
        zielX,zielY,fertig = getZiel(abstand_Cat,rList,mList,cat_x,cat_y,mouse_x,mouse_y,abstand,fertig)
   
    print(str(zielX)+" "+str(zielY))