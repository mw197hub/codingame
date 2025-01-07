# 

import sys,math


def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def spielLogik(resources,num_travel_routes,travelDict,podList,buildList,tag,bauList):
    actions=[]
    if len(buildList) > 0:
        startDict={};zielDict={}
        verbindungsDict={}
        for build in buildList:
            bList = build.split()
            id = bList[1];pos=[bList[2],bList[3]]
            if bList[0] == '0':
                artDict={}                
                for i in range(5,int(bList[4])+5):
                    if bList[i] in artDict:
                        artDict[bList[i]]+=1
                    else:
                        artDict[bList[i]] = 1
                #print(artDict,file=sys.stderr)
                startDict[id] = [bList[0],pos,artDict]
            else:
                zielDict[id] = [bList[0],pos]
                if bList[0] in verbindungsDict:
                    vList = verbindungsDict[bList[0]]
                    vList.append(id)
                else:
                    verbindungsDict[bList[0]] = [id]
        print(verbindungsDict,file=sys.stderr)
        for id,iList in startDict.items():
          artDict = iList[2];start=iList[0];posS=iList[1]
          for ziel,anzahl in artDict.items():
              if not start+"-"+ziel in travelDict:
                  if not ziel+"-"+start in travelDict:
                      
                      kosten = distance(posS,)
                      actions.append('TUBE '+start+' '+ziel)
                    
    return actions




###

resources=2000;num_travel_routes=0
travelDict={}
podList=[]
buildList=['0 0 80 60 30 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2', '1 1 40 30', '2 2 120 30']
monat=1;tag=2


####

bauList=[]

####

actions = spielLogik(resources,num_travel_routes,travelDict,podList,buildList,tag,bauList)
print(';'.join(actions) if len(actions) > 0 else 'WAIT')