import sys
import math
import pygame
from operator import itemgetter


def getInput(x0,y0,xAlt,yAlt,runde,xZiel,yZiel):    
    if runde == 0:
        return "UNKNOWN",0,0
    dist2 = distance(x0,y0,xZiel,yZiel) # neu
    dist1 = distance(xAlt,yAlt,xZiel,yZiel) # alt
    if dist1 == dist2:
        return "SAME",dist1,dist2
    if dist2 < dist1:
        return "WARMER",dist1,dist2
    return "COLDER",dist1,dist2

x0=3200;y0=2100;xAlt=6400;yAlt=6034
x0=280;y0=264;xAlt=421;yAlt=397
x0,y0,xAlt,yAlt=0,2,0,2
w0,h0=0,0
w=8000;h=8000
w=50;h=50;n=12

def erzeugeList(w0,h0,w,h):
    feldList = []
    for x in range(w0,w,1):
        for y in range(h0,h,1):
            feldList.append(str(x)+"-"+str(y))
    return feldList

def distance(xp1,yp1,xp2,yp2):
    return math.sqrt( ((xp1-xp2)**2)+((yp1-yp2)**2) )


def sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList,first):
    x1=x0;y1=y0
    newList={}
    for feld in sorted(feldList):
        xf,yf = feld.split("-")
        if first:
            newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
        else:
            dist1=distance(x0,y0,int(xf),int(yf))
            dist2=distance(xAlt,yAlt,int(xf),int(yf))
            if bomb_dir == "SAME" and dist1 == dist2:            
                newList[feld] = dist1
             #   newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
            if bomb_dir == "WARMER" and dist1 < dist2:
                newList[feld] = dist1
                #newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
            if bomb_dir == "COLDER" and dist1 > dist2:
                newList[feld] = dist1   # dist2
                #newList[feld] = int(x0) + int(y0) - (int(xf) + int(yf))
    
 #   for feld,laenge in newList.items():
 #       print(laenge,file=sys.stderr,end=" ")
 #       print(feld,file=sys.stderr)
   # print(sorted(newList),file=sys.stderr)
    if str(x0)+"-"+str(y0) in newList:
        newList.pop(str(x0)+"-"+str(y0))
    if len(newList) == 1:
        pos = 0
    else:
        pos = int(len(newList) /2)-1
    i = 0
    #pos = len(newList) -1
    newList = sorted(newList.items(), key=itemgetter(1))
    sortList = []
    for feld in newList:
        if i == pos:
            x1,y1 = feld[0].split("-")            
        i+=1;sortList.append(feld[0])

    return int(x1),int(y1),w0,h0,w,h,x0,y0,sortList



runde = 1;xZiel,yZiel=39,43
feldList = erzeugeList(w0,h0,w,h)
feldList1 = ['37-45', '38-44', '36-46', '39-43', '37-44', '38-43', '40-42', '39-42', '41-42','45-39'] #44-38
vektorList = {};summX=0;summY=0
for feld in feldList1:
    x1,y1 = feld.split("-");x0=int(x1);y0=int(y1)
    vektorList[feld] = str(xZiel-x0)+"-"+str(yZiel-y0)
    summX=summX+ xZiel-x0;summY=summY+yZiel-y0
print(vektorList,file=sys.stderr)
print("x-y: "+str(summX)+" "+str(summY)+"  diff:"+str(int(summX/len(feldList1)))+"  "+str(int(summY/len(feldList1))),file=sys.stderr)


for feld in feldList1:
    xZiel,yZiel=41,42
    x0,y0,xAlt,yAlt=39,43,33,42 #39,43,33,42
    feldList = ['37-45', '38-44', '36-46', '39-43', '37-44', '38-43', '40-42', '39-42', '41-42']
    x1,y1 = feld.split("-");x0=int(x1);y0=int(y1)
    print(str(x0)+" "+str(y0),file=sys.stderr)
    bomb_dir,dist1,dist2 = getInput(x0,y0,xAlt,yAlt,1,xZiel,yZiel)
    print(bomb_dir+"   alt:"+str((dist1))+"   neu:"+str((dist2)),file=sys.stderr)
    x0,y0,w0,h0,w,h,xAlt,yAlt,feldList = sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList,False)
    print(str(runde)+": rahmen: "+str(w0)+"-"+str(h0)+ " zu "+str(w)+"-"+str(h)+"  # alt: "+str(xAlt)+"-"+str(yAlt) + " feldList: " + str(len(feldList))+"  # x-y: " +str(x0)+" "+str(y0),file=sys.stderr)


#while True:
#    bomb_dir,dist1,dist2 = getInput(x0,y0,xAlt,yAlt,runde)

    #print(bomb_dir+"   alt:"+str((dist1))+"   neu:"+str((dist2)),file=sys.stderr)

    #if runde > 0:
    #    x0,y0,w0,h0,w,h,xAlt,yAlt,feldList = sucheList(bomb_dir,x0,y0,xAlt,yAlt,w0,h0,w,h,feldList)
    #    print(str(runde)+": rahmen: "+str(w0)+"-"+str(h0)+ " zu "+str(w)+"-"+str(h)+"  #  "+str(xAlt)+"-"+str(yAlt) + " feldList: " + str(len(feldList)),file=sys.stderr)
    #else:
    #    xAlt=x0;yAlt=y0
    #    x0,y0=0,0

    #print(str(x0)+" "+str(y0))

    #if x0 == xZiel and y0 == yZiel:
    #    print("erreicht",file=sys.stderr);break
    #runde+=1
    #if runde > n:
    #    print("versagt",file=sys.stderr)
    #    break

