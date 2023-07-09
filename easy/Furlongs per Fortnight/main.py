# https://www.codingame.com/ide/puzzle/furlongs-per-fortnight

import sys,math

a_speed="790 furlongs per fortnight CONVERT TO chains per week"  #1
a_speed="430 miles per day CONVERT TO feet per day" #2
a_speed="938 feet per day CONVERT TO chains per hour" #4

wortList=a_speed.split(" ")
#print(wortList)
erg=0.18
verhDist=0
verhTime=0
distDict={"mile":["furlong",8],"furlong":["chain",10],"chain":["yard",22],"yard":["feet",3],"foot":["inch",12]}
distToInch={"mile":63360,"furlong":7920,"chain":792,"yard":36,"foot":12,"feet":12,"inch":1}
timeToSek={"fortnight":1209600,"week":604800,"day":86400,"hour":3600,"minute":60,"second":1}

key1,key2="",""
for key in distToInch:
    if key in wortList[1]:
        key1 = key
    if key in wortList[6]:
        key2 = key
verhDist=distToInch[key1] / distToInch[key2]
for key in timeToSek:
    if key in wortList[3]:
        key1 = key
    if key in wortList[8]:
        key2 = key
verhTime=timeToSek[key1] / timeToSek[key2]
        

print(verhDist/verhTime,file=sys.stderr)
erg = int(wortList[0]) * (verhDist/verhTime)
erg=round(erg,1)
print("{} {} per {}".format(erg,wortList[6],wortList[8]))