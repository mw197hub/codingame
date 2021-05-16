import sys
import math

class place():
    position = ""
    farbeWert = ""
    wertInfo = 0
    farbeInfo = ""
    def __init__(self, position):
        self.position = position
    def __str__(self):
        return (str(self.position) + ": " + self.farbeWert)

farben = ["WHITE","RED","GREEN","BLUE","YELLOW"]

def grundstellen(myPlayer,gegnerList,gegnerWert,gegnerFarbe,anzahlKarten):
    anzahlKarten = 35
    gegnerList = {}
    gegnerWert = {}
    gegnerFarbe = {}
    geg = {}
    for i in range(3):
        if not i == int(myPlayer):
            gegnerList[str(i)] = {}
            geg[str(i)] = 0
    for i in range(1,6):
        gegnerWert[str(i)] = geg.copy()
    for f in farben:
        gegnerFarbe[f] = geg.copy()
    return gegnerList,gegnerWert,gegnerFarbe,anzahlKarten

brettList = {"WHITE":0,"RED":0,"GREEN":0,"BLUE":0,"YELLOW":0}
playerList = {"A":["","",""],"B":["","",""],"C":["","",""],"D":["","",""],"E":["","",""]}
infoList = {"0":[],"1":[],"2":[]}
gegnerList = {"0":{},"2":{}}
gegnerWert = {"1":{"0":0,"2":0},"2":{"0":0,"2":0},"3":{"0":0,"2":0},"4":{"0":0,"2":0},"5":{"0":0,"2":0}}
gegnerFarbe = {"WHITE":{"0":0,"2":0},"RED":{"0":0,"2":0},"GREEN":{"0":0,"2":0},"BLUE":{"0":0,"2":0},"YELLOW":{"0":0,"2":0}}

remaining_possible_information = 2
anzahlKarten = 35
myPlayer = "0"
gegnerList,gegnerWert,gegnerFarbe,anzahlKarten = grundstellen(myPlayer,gegnerList,gegnerWert,gegnerFarbe,anzahlKarten)
#print(gegnerList)
#print(gegnerWert)
#print(gegnerFarbe)

f = open("C:\\Users\wiedm\Python\codingame\Practice AI\Fireworks\input.txt", "r")
for x in f:
    iList = x[:-1].split(":")
 # print(iList)
    if iList[1] == "CARD" and not iList[0] == myPlayer and not "?" in iList[3]:
        gegner = gegnerList[iList[0]]
        gegner[iList[2]] = iList[3].split("-")
        werte = iList[3].split("-")
        wert = gegnerWert[werte[1]]
        wert[iList[0]] += 1        
        farbe = gegnerFarbe[werte[0]]
        farbe[iList[0]] += 1

    if iList[1] == "CARD" and iList[0] == myPlayer:
        wert = iList[3].split("-")
        player = playerList[iList[2]] 
        if wert[0] == "?":
            player[1] = wert[1]
        else:
            player[0] = wert[0]
    if iList[1][:3] == "SAY":
        info = infoList[iList[2]]
        info.append(iList[1]+iList[3])
    if iList[1][:4] == "PLAY":
        werte = iList[3].split("-")
        brettList[werte[0]] = werte[1]


print(infoList,file=sys.stderr)

output = True
if output:
    for card, werte in playerList.items():
        if len(werte[0]) > 0 and len(werte[1]) > 0:
            gelegt = brettList[werte[0]]
            if int(gelegt) == int(werte[1]) - 1:
                print("PLAY:"+card)
                playerList[card] = ['','','']
                output = False
                break
    if output:
        nuller = 0
        for card, gelegt in brettList.items():
            if gelegt == 0:
                nuller += 1
        if nuller > 2:
            for card, werte in playerList.items():
                if werte[1] == '1':
                    print("PLAY:"+card)
                    playerList[card] = ['','','']
                    output = False
                    break

if output:
    if remaining_possible_information < 3:
        wCard = "A"

        for card, werte in playerList.items():
            if len(werte[0]) > 0 and len(werte[1]) > 0:
                gelegt = brettList[werte[0]]
                if int(gelegt) >= int(werte[1]):
                    wCard = card
                    break
        print("DISCARD:"+wCard)
        playerList[wCard] = ['','','']
        output = False

if output:
    for wert,gegList in gegnerWert.items():
        for geg,anzahl in gegList.items():
            infList = infoList[geg]
            print(infList)
            if not "SAYLEVEL"+wert in infList:
                print("SAY:"+geg+":"+wert)
                output = False
                break
        if not output:
            break
    
if output:
    for farbe,gegList in gegnerFarbe.items():
        for geg,anzahl in gegList.items():
            infList = infoList[geg]
            if "SAYCOLOR"+farbe not in infList:                    
                print("SAY:"+geg+":"+farbe)
                output = False
                break
        if not output:
            break


#print(infoList)
print(playerList)
#print(gegnerList)
#print("-----------")
#print(gegnerWert)
#print("-----------")
#print(gegnerFarbe)
print(brettList)
