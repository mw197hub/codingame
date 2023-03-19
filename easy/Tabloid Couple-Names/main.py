# https://www.codingame.com/training/easy/tabloid-couple-names
import sys,math

def sucheB(s1,s2,laenge):
    i1 = -1;gefunden=False
    tList1,tList2 = [],[]
    wortList = []
    ende = 0 if len(s1) == len(s2) and s1[0] == s2[0] else -1

    for l in range(len(s1),0,-1):
        for i in range(len(s1)-l,ende,-1):
           # print(s1[i:i+l],file=sys.stderr)
            #treffer = s2.find(s1[i:i+l])
            treffer = [k for k in range(len(s2)) if s2.startswith(s1[i:i+l], k)]
            if len(treffer) > 0:
                for t in treffer:
                    wort = s2[:t+l-1] + s1[i+l-1:]
                    wort = wort[0].upper() + wort[1:].lower()
                    addWort(s1,s2,wort,wortList)
                gefunden=True
        if len(wortList) > 0 or l -1 < laenge:
            laenge = l
            break
    return wortList,laenge

def addWort(s1,s2,wort,wortList):
   # print(wort,file=sys.stderr)
    if wort.lower() in s1.lower() or wort.lower() in s2.lower() or (len(wort) < len(s1) and len(wort) < len(s2)):
        a=0
    else:
        wortList.append(wort)

coupleList=['Lois and Clark', 'Ben and Jennifer', 'Tarzan and Jane', 'Priscilla and Elvis', 'Simba and Nala', 'Mork and Mindy']
coupleList=['Brad and Angelina', 'Zac and Vanessa', 'Cory and Topanga from Boy Meets World', 'Harry and Markle of Montecito', 'Frida and Diego as in Frida Kahlo and Diego Rivera', 'Cam and Mitchell on Modern Family']
coupleList=['Mickey plus Minnie'] # = Minnickey Minniey
coupleList=['Alex plus Alexa']  # = Alexalex
#coupleList=['Ben and Jennifer']


for couple in coupleList:
    cList = couple.split(" ")
    ergA = "";erg="";ergList=[]
    laenge=0
    ergList1,laenge1 = sucheB(cList[0].lower(),cList[2].lower(),laenge)    
    ergList2,laenge = sucheB(cList[2].lower(),cList[0].lower(),laenge1)
    if laenge1 < laenge:
        ergList1.clear()
    ergList = []
    for erg in ergList1:
        if not erg in ergList:
            ergList.append(erg)
    for erg in ergList2:
        if not erg in ergList:
            ergList.append(erg)
    for e in sorted(ergList):
        ergA = ergA + " " + e
    ergA = ergA[1:] 
    if ergA == cList[0] or ergA == cList[2] or (len(ergA) < len(cList[0]) and len(ergA) < len(cList[2])):
        ergA = "NONE"
    print("{} plus {} = {}".format(cList[0],cList[2],ergA))