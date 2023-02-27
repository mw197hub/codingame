import sys,math,time

mapDict={}
def initMap():
    eingabe = open('C:\\Users\\marku\\Python\\codingame\\Practice AI\\Ghost in the cell\\input1.txt','r')
    i=0
    for zeile in eingabe:
        if not zeile[0] == "*":
            z=zeile.split(",")
            mapDict[i] = [z[0],z[1],z[2],z[3],z[4],z[5],z[6][:-1]]
            i+=1
    eingabe.close()
def getInput(i):
    z = mapDict[i]
    return z[0],z[1],z[2],z[3],z[4],z[5],z[6]

#######################################################
#######################################################
#######################################################
def setSZ(s,z):
    return str(s)+"-"+str(z)

def getSZ(wert):
    w = wert.split("-")
    return int(w[0]),int(w[1])


def sucheWeg(weg,t1Dict,factory_count,dauer,graph,wegePrioDict):    
    suchList=[]
    start,ziel = getSZ(weg);schwellwert=60
    #visited=[];visited.append(start)    
    for such1,d in graph[start].items():
        if d < schwellwert and d <= dauer:
            queue=[];aktDauer=d
            queue.append(start);queue.append(such1)
            if such1 == ziel:
                queue.insert(0,aktDauer)
                suchList.append(queue[:]);queue.pop(0)
            else:
                for such2,d2 in graph[such1].items():
                    if d2 < schwellwert and not such2 in queue and aktDauer+d2 < dauer:
                        queue.append(such2);aktDauer+=d2
                        if such2 == ziel:
                            queue.insert(0,aktDauer)
                            suchList.append(queue[:]);queue.pop(0)
                        else:
                            for such3,d3 in graph[such2].items():
                                if d3 < schwellwert and not such3 in queue and aktDauer+d3 < dauer:
                                    queue.append(such3);aktDauer+=d3
                                    if such3 == ziel:
                                        queue.insert(0,aktDauer)
                                        suchList.append(queue[:]);queue.pop(0)                                    
                                    else:
                                        for such4,d4 in graph[such3].items():
                                            if d4 < schwellwert and not such4 in queue and aktDauer+d4 < dauer:
                                                queue.append(such4);aktDauer+=d4
                                                if such4 == ziel:
                                                    queue.insert(0,aktDauer)
                                                    suchList.append(queue[:]);queue.pop(0)
                                                else:
                                                    for such5,d5 in graph[such4].items():
                                                        if d5 < schwellwert and not such5 in queue and aktDauer+d5 < dauer:
                                                            queue.append(such5);aktDauer+=d5
                                                            if such5 == ziel:
                                                                queue.insert(0,aktDauer)
                                                                suchList.append(queue[:]);queue.pop(0)
                                                            else:
                                                                for such6,d6 in graph[such5].items():
                                                                    if d6 < schwellwert and not such6 in queue and aktDauer+d6 < dauer:
                                                                        queue.append(such6);aktDauer+=d6
                                                                        if such6 == ziel:
                                                                            queue.insert(0,aktDauer)
                                                                            suchList.append(queue[:]);queue.pop(0)
                                                                        else:
                                                                            for such7,d7 in graph[such6].items():
                                                                                if d7 < schwellwert and not such7 in queue and aktDauer+d7 < dauer:
                                                                                    queue.append(such7);aktDauer+=d7
                                                                                    if such7 == ziel:
                                                                                        queue.insert(0,aktDauer)
                                                                                        suchList.append(queue[:]);queue.pop(0)
                                                                                #    else:
                                                                                #        for such8,d8 in graph[such7].items():
                                                                                #            if d8 < schwellwert and not such8 in queue and aktDauer+d8 < dauer:
                                                                                #                queue.append(such8);aktDauer+=d8
                                                                                #                if such8 == ziel:
                                                                                #                    queue.insert(0,aktDauer)
                                                                                #                    suchList.append(queue[:]);queue.pop(0)
                                                                                #                queue.pop();aktDauer-=d8
                                                                                    queue.pop();aktDauer-=d7
                                                                        queue.pop();aktDauer-=d6
                                                            queue.pop();aktDauer-=d5
                                                queue.pop();aktDauer-=d4
                                    queue.pop();aktDauer-=d3
                        queue.pop();aktDauer-=d2
            queue.pop();aktDauer-=d
  #  print(weg,file=sys.stderr,end="  ")
  #  print(suchList,file=sys.stderr)    
    e=[];d=999
    for such in suchList:
        if such[0] < d:
            d = such[0];e=such[:]
        if such[0] == d and len(such[:]) < len(e):
            e=such[:]
    wertL=[];wertL.append(e[0])
    for i in range(len(e[1:-1])):
        wert = setSZ(e[i+1],e[i+2]);wertL.append(wert)
    t1Dict[weg] = wertL[:]
    #drehen
    wertLD=[]
    for i in range(len(wertL)):
        if i == 0:
            wertLD.append(wertL[i])
        else:
            s1,z1=getSZ(wertL[i]);wertLD.insert(1,(setSZ(z1,s1)))

    t1Dict[setSZ(ziel,start)] = wertLD[:]

    for e in wertL[1:]:
        e1,e2 = getSZ(e);wegePrioDict[e1]+=1;wegePrioDict[e2]+=1 
   # if weg == "7-8":
   #     print(weg,file=sys.stderr,end=":  ")
   #     print(wertL,file=sys.stderr)
   #     print(wertLD,file=sys.stderr)

def setWege(zwDict,factory_count):
    wegeDict={};zw2Dict={};wegePrioDict={};graph={}
    for i in range(factory_count):
        wegePrioDict[i] = 0
    for weg,dauer in zwDict.items():
        zw2Dict[weg] = dauer;s,z = getSZ(weg);zw2Dict[setSZ(z,s)]=dauer
        if s in graph:
            dic = graph[s];dic[z]=dauer
            graph[s] = dic
        else:
            dic ={};dic[z]=dauer;graph[s]=dic
        if z in graph:
            dic = graph[z];dic[s]=dauer
            graph[z] = dic
        else:
            dic ={};dic[s]=dauer;graph[z]=dic
            
    #print(graph,file=sys.stderr)
  #  for g in graph:
  #      print(g,file=sys.stderr,end=": ")
  #      print(graph[g],file=sys.stderr)
    for weg,dauer in zwDict.items():        
        sucheWeg(weg,wegeDict,factory_count,dauer,graph,wegePrioDict)
 #   print(wegeDict,file=sys.stderr)
 #   print(wegePrioDict,file=sys.stderr)
    tDict={}
    for w in sorted(wegePrioDict,key=wegePrioDict.get, reverse=True):
        tDict[w] = wegePrioDict[w]
#
    moeglicheWegeDict={}
    for id in range(factory_count):
        moeglicheWegeDict[id] = []
    for weg,wList in wegeDict.items():
        s,z = getSZ(weg);s1,z1 = getSZ(wList[1])
        mList = moeglicheWegeDict[s]
        if not z1 in mList:
            mList.append(z1)

    return wegeDict,tDict,zw2Dict,moeglicheWegeDict

def setMeineZiele(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict,verteidigungsDict,myBots,enemyBots):
    incZiele = setIncZiele(zw2Dict,wegeDict,myFactoryList,enemyFactoryList,factoryDict,bombZielList)
    bewertungsDict,entferungsDict,zielBewertung={},{},{}
    for id in range(factory_count):
        bewertungsDict[id]=0;entferungsDict[id]=0;zielBewertung[id]=0
    meineZiele=[];enemyZiele=[];myID,enemyID=0,0
    for id,elem in factoryDict.items():
        myEntfernung,enemyEntfernung=0,0
        for mElem in myFactoryList:
            if not id == mElem.id:
                myEntfernung+=wegeDict[setSZ(id,mElem.id)][0]
        for eElem in enemyFactoryList:
            if not id == eElem.id:
                enemyEntfernung+=wegeDict[setSZ(id,eElem.id)][0]
        entferungsDict[id]=enemyEntfernung-myEntfernung
    keinZiel=set()
    for elem in myFactoryList:
        for ziel,zielE in factoryDict.items():
            if zielE.arg_1 < 1:
                bewertung = entferungsDict[ziel]
                entfernung = zw2Dict[setSZ(elem.id,zielE.id)]
                bombCome=False
                for myBomb in myBombList:
                    if myBomb.arg_3 == zielE.id and entfernung <= myBomb.arg_4:
                        bombCome=True
                if bombCome:
                    keinZiel.add(zielE.id)
                else:
                    bewertung -= zielE.troopDict[entfernung]          
                    if zielE.arg_1 == -1:
                        bewertung +=2
                        bewertung +=  ((10-entfernung)* zielE.arg_3) - (zielE.arg_2 * entfernung)
                    else: 
                        bewertung +=  ((10-entfernung)* zielE.arg_3) - zielE.arg_2
                    zielBewertung[zielE.id] += bewertung                
            else:
                zielBewertung[zielE.id] += 3 - zielE.arg_3  + zielE.arg_4# + entfernung gegner
                if zielE.arg_2 >= 10 and zielE.arg_3 < 3:
                    zielBewertung[zielE.id] += 2
    for idN in keinZiel:
        if idN in zielBewertung:
            zielBewertung.pop(idN)
    zielBewertungRest={}
    for zID in zielBewertung:
        zielE = factoryDict[zID]
        zielBewertungRest[zID] = zielBewertung[zID]
       # if zielE.arg_3 == 3 and zielE.arg_1 == 0:
        if zielE.arg_1 == 0:
            anzahl=0
            for troop in myTroopList:
                if troop.arg_3 == zID:
                    anzahl+= troop.arg_4
            if anzahl > zielE.arg_2 and zielE.arg_3 == 3:
                zielBewertungRest.pop(zID)
            elif anzahl > zielE.arg_2:
                zielBewertungRest[zID] = 3 - zielE.arg_3
        if zielE.arg_1 == 1 and zielE.arg_3 == 3 and zielE.arg_4 == 0:
            zielBewertungRest.pop(zID)
    zielList = sorted(zielBewertungRest,key=zielBewertungRest.get, reverse=True)

   # print(meineZiele,file=sys.stderr)
    return zielList,zielBewertungRest

def setIncZiele(zw2Dict,wegeDict,myFactoryList,enemyFactoryList,factoryDict,bombZielList):
    incZiele = [];bewertungDict={}
    for elem in myFactoryList:
        if elem.arg_3 < 3:
            bZiel=False
            for bID,bombZList in bombZielList.items():
                if elem.id in bombZList:
                    bZiel=True
            if not bZiel:
                bewertungDict[elem.id] = elem.arg_2 + elem.arg_3
    for id in sorted(bewertungDict,key=bewertungDict.get, reverse=True):
        incZiele.append(id)
    return incZiele

def setmoeglicheActions(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict):
    moeglicheActions={}
    for elem in myFactoryList:
        noBomb=setNoBomb(elem,bombZielList)
        actionList=[]
        if elem.arg_3 < 3 and noBomb:
            actionList.append("INC")
        for ziel in elem.zielDict:
            actionList.append(str(ziel))
        moeglicheActions[elem.id] = actionList[:]
    return moeglicheActions

class Element:
    def __init__(self,id,type,arg_1,arg_2,arg_3,arg_4,arg_5):
        self.id=id;self.type=type;self.arg_1=arg_1;self.arg_2=arg_2;self.arg_3=arg_3;self.arg_4=arg_4;self.arg_5=arg_5
        self.troopDict={};self.enemyTroopDict={};self.bombAnkunft=[];self.zielDict={}
#####2####
def setzeWerte(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,bombZielList,moeglicheWegeDict):
    myProduktion,neutralProduktion,enemyProduktion=0,0,0
    troopRange=25
    for elem in enemyBombList:
        if elem.id in bombAktiv:
            elem.arg_5 = bombAktiv[elem.id]
    for bomb,ab in bombAktiv.items():
        if ab == runde -1:
            mZiele=[]
            for elem in myFactoryList:
                mZiele.append(elem.id)
            bombZielList[bomb] = mZiele[:]

    zielDict2=[]
    for elem in enemyFactoryList:
        enemyProduktion += elem.arg_3
        for i in range(troopRange):
            if i >= elem.arg_4:
                elem.troopDict[i] = elem.arg_3 
            else:
                elem.troopDict[i] = 0
        zielDict2.append(elem.id) 
    for elem in neutralFactoryList:
        neutralProduktion += elem.arg_3
        for i in range(troopRange):
            elem.troopDict[i] = 0
            elem.enemyTroopDict[i] = 0
        zielDict2.append(elem.id) 

    for elem in myFactoryList:
        myProduktion += elem.arg_3 
        for i in range(troopRange):
            if i >= elem.arg_4:
                elem.troopDict[i] = elem.arg_3 
            else:
                elem.troopDict[i] = 0
        for bomb in enemyBombList:
            weg = setSZ(elem.id, bomb.arg_2)
            if weg in zw2Dict:
                flug = zw2Dict[weg]
                unterwegs = runde - bomb.arg_5
                if unterwegs < flug:
                    elem.bombAnkunft.append(flug - unterwegs)
        indirektZiel=set()
        for idFremd in zielDict2:
            s,z = getSZ(wegeDict[setSZ(elem.id,idFremd)][1])
            indirektZiel.add(z)
        hilfsDict={}
        for idFremd in indirektZiel:
            hilfsDict[idFremd] = wegeDict[setSZ(elem.id,idFremd)][0]
        for idH in sorted(hilfsDict,key=hilfsDict.get, reverse=False):
            elem.zielDict[idH] = hilfsDict[idH]

    for elem in myTroopList:
        zielE = factoryDict[elem.arg_3]
        if zielE.arg_1 == 1:
            zielE.troopDict[elem.arg_5] += elem.arg_4
        else:
            zielE.troopDict[elem.arg_5] -= elem.arg_4


    for elem in enemyTroopList:
        zielE = factoryDict[elem.arg_3]
        if zielE.arg_1 == -1:
            zielE.troopDict[elem.arg_5] += elem.arg_4
        elif zielE.arg_1 == 1:
            zielE.troopDict[elem.arg_5] -= elem.arg_4
        else:
            zielE.enemyTroopDict[elem.arg_5] -= elem.arg_4

    actions.append('MSG {} | {} | {}'.format(myProduktion,neutralProduktion,enemyProduktion))

##########################
def setVerteidigung(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict):    
    verteidigungsDict={};myBots,enemyBots=0,0
    for elem in myFactoryList:
        nachschub={}
        for r,anz in elem.troopDict.items():
            if anz < 0:
                nachschub[r] = anz
        if len(nachschub) > 0:
            verteidigungsDict[elem.id] = nachschub
        myBots+=elem.arg_2+elem.arg_3
    for elem in myTroopList:
        myBots += elem.arg_4
    for elem in enemyFactoryList:
        enemyBots+=elem.arg_2+elem.arg_3
    for elem in enemyTroopList:
        enemyBots+=elem.arg_4

    return verteidigungsDict,myBots,enemyBots

def setNoBomb(elem,bombZielList):
    for id,zielList in bombZielList.items():
        if elem.id in zielList:
            return False

    return True

#####
def setActions(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict):
    # MOVE von nach anz    
    verteidigungsDict,myBots,enemyBots = setVerteidigung(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict)                
    for vID,vDict in verteidigungsDict.items():
        elem = factoryDict[vID]
        ab,wert=99,0
        for nr,anz in vDict.items():
            ab = nr if ab == 99 else ab
            wert+=anz    
        if (wert * -1) >= elem.arg_2:
            wert=wert+elem.arg_2;elem.arg_2=0
        else:
            elem.arg_2 = elem.arg_2 + wert;wert=0
            myDist,enDist=99,99
            for fID, fElem in factoryDict.items():
                if fElem.arg_1 == 1 and not elem.id == fElem.id:
                    wDist = zw2Dict[setSZ(elem.id,fElem.id)]
                    myDist = wDist if wDist < myDist else myDist
                elif fElem.arg_1 == -1:
                    wDist = zw2Dict[setSZ(elem.id,fElem.id)]
                    enDist = wDist if wDist < enDist else enDist
            if myDist >= enDist:
                elem.arg_2=0 if elem.arg_2 <= 6 else elem.arg_2 -6
        if elem.arg_2 >= 10 and elem.arg_3 < 3:
            actions.append("INC {}".format(elem.id))
            elem.arg_2 -= 10
        if not ab == 99 and elem.arg_3 > 0:
            nahDict={}
            for fElem in myFactoryList:
                if not elem.id == fElem.id and not fElem.id in verteidigungsDict:
                    nahDict[fElem.id] = zw2Dict[setSZ(elem.id,fElem.id)]
            nahList = sorted(nahDict,key=nahDict.get, reverse=False)
            wert = wert * -1
            for nID in nahList:
                nElem = factoryDict[nID]
                entfernung = nahDict[nElem.id]
                if nElem.arg_2 > 0:
                    wert = wert if entfernung > ab else wert + (elem.arg_3 * (entfernung -ab))
                    if wert > 0:
                        if nElem.arg_2 > wert:
                            actions.append("MOVE {} {} {}".format(nElem.id,elem.id,wert))
                            wert = 0;nElem.arg_2 -= wert;break
                        else:
                            actions.append("MOVE {} {} {}".format(nElem.id,elem.id,nElem.arg_2))
                            wert -= nElem.arg_2;nElem.arg_2 =0
                    else:
                        break

   # for elem in myFactoryList:
        #if elem.arg_2 >= 10 and elem.arg_3 < 3 and runde > 1:
   #     if elem.arg_2 >= 10 and elem.arg_3 < 3:
   #         actions.append("INC {}".format(elem.id))
   #         elem.arg_2 -= 10;elem.arg_3+=1

    meineZiele,meineDict = setMeineZiele(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict,verteidigungsDict,myBots,enemyBots)        
    moeglicheActions=setmoeglicheActions(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict)

    bisherList=[]
    for i in range(len(meineZiele)):
        zID = meineZiele[i]
        zElem = factoryDict[zID]
        anzahl = zElem.arg_2
        if zElem.arg_1 < 1:
            anzahl+=1
            if zElem.arg_1 == -1:
                anzahl+=4
        entfDict={};restTroop=0
        for elem in myFactoryList:
            restTroop+=elem.arg_2
            if not elem.id == zID and elem.arg_2 > 0:
                entfDict[elem.id] = wegeDict[setSZ(elem.id,zID)][0]
            #if elem.id == zID and elem.arg_2 >= 10 and elem.arg_3 < 3:
            if elem.id == zID:
                entfDict[elem.id] = 0
        if restTroop == 0:
            break
        entfList = sorted(entfDict,key=entfDict.get, reverse=False)  
        if len(entfList) > 0:      
            anzahl+=zElem.troopDict[entfDict[entfList[0]]]
        for eID in entfList:
            eElem = factoryDict[eID]  
            if eID == zID:       
                if eElem.arg_2 >= 10 and eElem.arg_3 < 3:
                    actions.append("INC {}".format(eElem.id))
                    eElem.arg_2 -= 10;eElem.arg_3+=1   
                elif eElem.arg_3 < 3:
                    eElem.arg_2 = 0
            else:
                weg = wegeDict[setSZ(eElem.id,zID)]
                s,z = getSZ(weg[1]);alle=False    
                if i > len(meineZiele) -1:
                    if factoryDict[meineZiele[i+1]].arg_3 == 0 and factoryDict[z].arg_3 < 3:
                        alle=True
                if anzahl > eElem.arg_2 or anzahl <= 0 or alle:
                    if eElem.arg_2 > anzahl + 10 and eElem.arg_3 < 3 and eElem.arg_2 >= 10:
                        actions.append("INC {}".format(eElem.id))
                        eElem.arg_2 -= 10
                    if not zElem.arg_1 == 0:
                        actions.append("MOVE {} {} {}".format(eElem.id,z,eElem.arg_2))
                        eElem.arg_2 = 0;anzahl-=eElem.arg_2
                else:            
                    if zElem.arg_1 == -1:
                        actions.append("MOVE {} {} {}".format(eElem.id,z,eElem.arg_2))
                        eElem.arg_2 = 0
                    else:    
                        actions.append("MOVE {} {} {}".format(eElem.id,z,anzahl))
                        eElem.arg_2 -= (anzahl)
                bisherList.append(z)

#  actions.append("INC {}".format(elem.id))



    # BOMB von nach
    if myBomb > 0: 
        zielID3,zielID2=99,99
        for elem in enemyFactoryList:
            neuZ=True
            for myB in myBombList:
                if myB.arg_3 == elem.id:
                    neuZ=False
            if neuZ and ((elem.arg_3 == 3 and elem.arg_4 == 0) or (elem.arg_3 == 2 and elem.arg_4 == 0 and runde > 2+(len(factoryDict)//2))):
                ab=0;dist=999
                for my in myFactoryList:
                    dist2 = wegeDict[setSZ(elem.id,my.id)][0]
                    if dist2 < dist:
                        dist=dist2;ab=my.id
                        if elem.arg_3 == 3:
                            zielID3 = elem.id
                        else:
                            zielID2 = elem.id
       # print("bomb {} {}".format(zielID3,zielID2),file=sys.stderr)
        if zielID3 < 99:
            actions.append("BOMB {} {}".format(ab,zielID3))
            myBomb-=1
        elif zielID2 < 99:
            actions.append("BOMB {} {}".format(ab,zielID2))
            myBomb-=1

    return myBomb

##############################
##############################
start = time.time()
factory_count=7
zwDict ={'0-1': 3, '0-2': 3, '0-3': 6, '0-4': 6, '0-5': 3, '0-6': 3, '1-2': 8, '1-3': 1, '1-4': 11, '1-5': 2, '1-6': 7, '2-3': 11, '2-4': 1, '2-5': 7, '2-6': 2, '3-4': 14, '3-5': 3, '3-6': 10, '4-5': 10, '4-6': 3, '5-6': 8}

initMap()
#####

wegeDict,wegePrioDict,zw2Dict,moeglicheWegeDict = setWege(zwDict,factory_count)

# game loop
runde = 7
bombAktiv={}
bombZielList={}
myBomb=0
while True:    
    elementList=[];myFactoryList=[];enemyFactoryList=[];myBombList=[];enemyBombList=[]
    myTroopList=[];enemyTroopList=[];neutralFactoryList=[];factoryDict={}
    #entity_count = int(input())  
    for i in range(len(mapDict)):
        inputs = getInput(i)
        element = Element(int(inputs[0]),inputs[1],int(inputs[2]),int(inputs[3]),int(inputs[4]),int(inputs[5]),int(inputs[6]))
        elementList.append(element)
        if inputs[1] == "FACTORY":
            factoryDict[int(inputs[0])] = element
            if int(inputs[2]) == 1:
                myFactoryList.append(element)
            elif int(inputs[2]) == -1:
                enemyFactoryList.append(element)
            else:
                neutralFactoryList.append(element)
        if inputs[1] == "TROOP":
            if int(inputs[2]) == 1:
                myTroopList.append(element)
            elif int(inputs[2]) == -1:
                enemyTroopList.append(element)
        if inputs[1] == "BOMB":
            if int(inputs[2]) == 1:
                myBombList.append(element)
            elif int(inputs[2]) == -1:
                enemyBombList.append(element)
                if not int(inputs[0]) in bombAktiv:
                    bombAktiv[int(inputs[0])] = runde

    actions=[]
        
    setzeWerte(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,bombZielList,moeglicheWegeDict)
    
    myBomb = setActions(runde,wegeDict,wegePrioDict,elementList,myFactoryList,enemyFactoryList,myBombList,enemyBombList,myTroopList,enemyTroopList,neutralFactoryList,actions,factoryDict,bombAktiv,zw2Dict,factory_count,myBomb,bombZielList,moeglicheWegeDict)


    print(';'.join(actions) if len(actions) > 0 else 'WAIT')
    runde+=1

    break




print(time.time() - start,file=sys.stderr)