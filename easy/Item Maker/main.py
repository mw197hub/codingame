# https://www.codingame.com/ide/puzzle/item-maker

import sys,math

def zentriert(wort,outLen,rahmen,first):
    ra = "##"
    if rahmen in ["Epic","Legendary"]:
        ra ="||"
        if first and rahmen == "Legendary":
            ra = "[]"
    if outLen > len(wort):
        unterschied = outLen - len(wort)
        vorne = int(unterschied//2)
        hinten = vorne
        if not unterschied == vorne*2:
            vorne+=1
        wort = " "*vorne + wort + " "*hinten
    print(ra[0]+" "+wort +" "+ra[1])        



###########

data="Wooden Sword,Common,Damage:20"
data="Iron Pickaxe,Rare,Speed:5,Damage:5,Crit. Chance:1.2%"
data="Draconic Sword,Epic,Skill:Dragon Cry,Damage:100,Critical Damage:150%"
data="Sword of Everything,Legendary,Skill:Annihilation,Skill:Creation,Damage:500,Critical Chance:3.5%,Critical Damage:300%,Speed:2"
data="Elucidator,Legendary,Skill:Dual Blades,Damage:150,Speed:15,Critical Chance:5.1%,Critical Damage:450%"


####

dataList=data.split(",")
#print(dataList,file=sys.stderr)
outLen=len(dataList[0])+2
for data in dataList:
    if len(data) > outLen:
        outLen = len(data)

rahmen = "#"
if dataList[1] in ["Epic","Legendary"]:
    rahmen = "|"
    if dataList[1] == "Epic":
        print("/"+"-"*(outLen+2)+"\\")
    else:
        if (outLen//2)*2 == outLen:
            print("X"+"-"*((outLen//2)-1)+"\\__/"+"-"*((outLen//2)-1)+"X")
        else:
            print("X"+"-"*((outLen//2))+"\\_/"+"-"*((outLen//2))+"X")
else:
    if dataList[1] == "Rare":
        print("/"+"#"*(outLen+2)+"\\")
    else:
        print("#"*(outLen+4))

zentriert("-"+dataList[0]+"-",outLen,dataList[1],True)
zentriert(dataList[1],outLen,dataList[1],False)

for i in range(2,len(dataList)):
    wort = dataList[i].replace(":"," ")
    unterschied = outLen - len(wort)
    print(rahmen+" "+wort+" "*unterschied+" "+rahmen)

if dataList[1] in ["Epic","Legendary"]:
    if dataList[1] == "Epic":
        print("\\"+"_"*(outLen+2)+"/")
    else:
        print("X"+"_"*(outLen+2)+"X")
else:
    if dataList[1] == "Rare":
        print("\\"+"#"*(outLen+2)+"/")
    else:
        print("#"*(outLen+4))