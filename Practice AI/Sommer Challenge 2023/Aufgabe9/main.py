# https://ide.codingame.com/21609455?id=67159074dfed33eeaec99fa6e7420adaa0162c2

import sys,math,copy
import binascii,codecs
import string


def defeat(enemy):
    newE=[];loeschen=[]
    for i1 in range(len(enemy)-1):
        for i2 in range(1,len(enemy)):
            if enemy[i1] in loeschen or enemy[i2] in loeschen or i1 == i2:
                a=0
            else:
                if enemy[i1] == enemy[i2]:
                    if not enemy[i1] in loeschen:
                        loeschen.append(enemy[i1])
                    if not enemy[i2] in loeschen:
                        loeschen.append(enemy[i2])
    for e in enemy:
        if not e in loeschen:
            newE.append(e)
    return newE[:]

def moveEnemy(eMove,enemy,my):
    for eny in enemy:
        xdist=eny[0]-my[0]
        ydist=eny[1]-my[1]
        if xdist > 0:
            eny[0] -= 1
        if xdist < 0:
            eny[0] += 1
        if ydist > 0:
            eny[1] -= 1
        if ydist < 0:
            eny[1] += 1            
        if eny == my:
            return ("gefangen")
    return ""


def versuchWert(versuch,enemy,my,mMove,paar):    
    if versuch == 0:
        if len(paar) < 3:
            return "LEFT"
        i1,i2 = paar.split("#")
        e1=enemy[int(i1)];e2=enemy[int(i2)]
        x=e1[0]-e2[0]
        y=e1[1]-e2[1]    
        if abs(x) < abs(y):  # left or right
            x1 = my[0]-e1[0]
            x2 = my[0]-e1[0]
            if abs(x1) > abs(x2):
                if x1 < 0:
                    return "LEFT"
                else:
                    return "RIGHT"
        else:
            y1 = my[1]-e1[1]
            y2 = my[1]-e1[1]
            if abs(y1) > abs(y2):
                if y1 < 0:
                    return "DOWN"
                else:
                    return "UP"



    if versuch == 1:
        return "UP"
    if versuch == 2:
        return "DOWN"
    if versuch == 3:
        return "LEFT"
    if versuch == 4:
        return "RIGHT"
    if versuch == 5:
        e1 = enemy[0];e2=enemy[1]
        if len(enemy) > 2:
            if e1[0] < e2[0]:
                return "RIGHT"
            if e1[0] > e2[0]:
                return "LEFT"        
            if e1[1] < e2[1]:
                return "UP"
            if e1[1] > e2[1]:
                return "DOWN"
        else:
            if e1[1] < e2[1]:
                return "RIGHT"
            if e1[1] > e2[1]:
                return "LEFT"        
            if e1[0] < e2[0]:
                return "UP"
            if e1[0] > e2[0]:
                return "DOWN"


    distList=[];xMax,yMax=0,0
    for eny in enemy:
        xdist=eny[0]-my[0];ydist=eny[1]-my[1]
        distList.append([xdist,ydist])
        if abs(xdist) > abs(xMax):
            xMax=xdist
        if abs(ydist) > abs(yMax):
            yMax=ydist
    #print(distList,file=sys.stderr)
    befehl = "LEFT"
    if abs(xMax) > abs(yMax):
        if xMax > 0:
            befehl="LEFT"
        else:
            befehl="RIGHT"
    else:
        if yMax > 0:
            befehl="DOWN"
        else:
            befehl="UP"
    return befehl

def moveMy(eMove,enemy,my,mMove,versuch,paar):
    
    befehl = versuchWert(versuch,enemy,my,mMove,paar)       
    bef = mMove[befehl]
    my[0] += bef[0]
    my[1] += bef[1]

    return befehl

def simulation(s1,versuch):
    sList=s1.split(" ")
    my=[int(sList[-2]),int(sList[-1])]
    enemy=[]
    for e in range(0,len(sList)-2,2):
        enemy.append([int(sList[e]),int(sList[e+1])])

    erg=True
    runde=0
    befehlList=[]
    while enemy:
        enemy = defeat(enemy)

        paar = bildePaare(my,enemy)
        info  = moveEnemy(eMove,enemy,my)
        if len(info) > 0:
            print("gefangen");erg=False
            break
        
        befehl = moveMy(eMove,enemy,my,mMove,versuch,paar)
        befehlList.append(befehl)
        #print(befehl,file=sys.stderr,end="    ")
        #print("{}  {}".format(enemy,my),file=sys.stderr)
        #print(moveT[befehl])
        
        if runde >= 300:
            print("abgelaufen",file=sys.stderr);erg=False
            break
        runde+=1    
    return erg,befehlList

def bildePaare(my,enemy):
    paare=[];reste=copy.deepcopy(enemy)
    abstaende={}
    while reste:
        abstand=1000
        for i2 in range(1,len(reste)):
            x=reste[0][0]-reste[i2][0]
            y=reste[0][1]-reste[i2][1]            
            if abs(x) > abs(y):
                if abs(x) < abstand:
                    abstaende[0] = str(i2)+"#x#"+str(x)
                    abstand = abs(x)
            else:
                if abs(y) < abstand:
                    abstaende[0] = str(i2)+"#y#"+str(y)
                    abstand = abs(y)
        ergL=abstaende[0].split("#")
        paare.append([abs(int(ergL[2])),reste[0],reste[int(ergL[0])]])
        reste.pop(int(ergL[0]))
        reste.pop(0)        
    #print("{}  ###  {}".format(paare,enemy),file=sys.stderr)
    abstand=1000;treffer=-1
    paar=""
    for i in range(len(paare)):
        if paare[i][0] < abstand:
            treffer=i;abstand=paare[i][0]
            i1,i2=0,0
            for k in range(len(enemy)):
                if enemy[k] == paare[i][1]:
                    i1 = k
                if enemy[k] == paare[i][2]:
                    i2 = k
            paar = str(i1)+"#"+str(i2)
    #print(paar,file=sys.stderr)
    return paar


s1="37 21 37 27 16 29"  #1
s2="6 10 16 10 84 35 84 42 11 38"  #2
s3="-42 191 184 -15 184 -19 185 -19 186 -15 -42 190 92 93" #3
s4="42 34 33 118 -3 178 151 29 42 59 0 178 106 29 33 65 149 87"
s5="100 108 114 64 114 63 50 61 74 68 76 68 58 108 50 64 69 92"
s6="184 -20 184 -22 185 -27 185 -28 158 166 -17 -18 -17 -20 160 154 160 -32 -30 166 93 105"
s7="-126 -107 -111 249 227 -83 265 260 265 263 235 245 251 233 236 245 227 229 -110 244 251 236 -110 240 -126 257 -111 -99 85 43"
s8="190 -29 190 165 190 163 80 97"
s9="193 -26 193 -25 91 125 70 125 193 167 74 131"
s10="56 111 18 51 106 51 51 95 97 111 18 120 51 59 52 51 51 58 77 88 55 111 75 88 71 79"  #10

inputList=[]
inputList.append(s1);inputList.append(s2);inputList.append(s3);inputList.append(s4)
inputList.append(s5);inputList.append(s6);inputList.append(s7);inputList.append(s8)
inputList.append(s9);inputList.append(s10)

mMove={'UP':[0,1],'DOWN':[0,-1],'LEFT':[-1,0],'RIGHT':[1,0]}
#mMove=[[0,-1],[0,1],[-1,0],[1,0]]
eMove=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]   
moveS={'RB':'UP','KLUO':'DOWN','TYHPF':'RIGHT','EQXF':'LEFT'}
moveT={'UP':'RB','DOWN':'KLUO','RIGHT':'TYHPF','LEFT':'EQXF'}

#for i in range(len(inputList)):
for i in range(3,4):
    weg=-1    
    for versuch in range(1):        
        erg,befehlList = simulation(inputList[i],versuch)
        if erg == True:
            weg = versuch;break
    print("Test: {}  Weg: {}   befehle: {}".format(i+1,weg,befehlList),file=sys.stderr)
