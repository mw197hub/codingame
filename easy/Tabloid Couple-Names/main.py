# https://www.codingame.com/training/easy/tabloid-couple-names
import sys,math

def sucheB(s1,s2):
    i1 = -1;gefunden=False
    tList1,tList2 = [],[]
    wortList = []
    ende = 0 if len(s1) == len(s2) and s1[0] == s2[0] else -1
    buchstabe=""
    for l in range(len(s1),0,-1):
        for i in range(len(s1)-l,ende,-1):
           # print(s1[i:i+l],file=sys.stderr)
            treffer = [k for k in range(len(s2)) if s2.startswith(s1[i:i+l], k)]
            if len(treffer) > 0:
                buchstabe=s1[i:i+l]
                treffer2 = [k for k in range(len(s1)) if s1.startswith(buchstabe, k)]
                for t in treffer:
                    wort = s2[:t+l-1] + s1[i+l-1:]
                    wort = wort[0].upper() + wort[1:].lower()
                    addWort(s1,s2,wort,wortList)
                
                    for y in treffer2:
                        wort = s1[:y+l-1] + s2[t+l-1:]
                        wort = wort[0].upper() + wort[1:].lower()
                        addWort(s2,s1,wort,wortList)
        if len(wortList) > 0:            
            break
    return wortList

def addWort(s1,s2,wort,wortList):
    print(wort,file=sys.stderr)
    if wort.lower() in s1.lower() or wort.lower() in s2.lower() or (len(wort) < len(s1) and len(wort) < len(s2)):
        a=0
    else:
        if not wort in wortList:
            wortList.append(wort)

coupleList=['Lois and Clark', 'Ben and Jennifer', 'Tarzan and Jane', 'Priscilla and Elvis', 'Simba and Nala', 'Mork and Mindy']
coupleList=['Brad and Angelina', 'Zac and Vanessa', 'Cory and Topanga from Boy Meets World', 'Harry and Markle of Montecito', 'Frida and Diego as in Frida Kahlo and Diego Rivera', 'Cam and Mitchell on Modern Family']
coupleList=['Mickey plus Minnie'] # = Minnickey Minniey
coupleList=['Alex plus Alexa']  # = Alexalex
coupleList=['Ben and Jennifer']
coupleList=['Tarzan plus Jane']
coupleList=['Fred plus Ethel']    # = Ethed Frel Frethel


for couple in coupleList:
    cList = couple.split(" ")
    ergA = "";ergList=[]
    ergList = sucheB(cList[0].lower(),cList[2].lower())    

    for e in sorted(ergList):
        ergA = ergA + " " + e
    ergA = ergA[1:] 
    if len(ergA) == 0:
        ergA = "NONE"
    print("{} plus {} = {}".format(cList[0],cList[2],ergA))