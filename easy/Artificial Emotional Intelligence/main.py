#  https://www.codingame.com/ide/puzzle/artificial-emotional-intelligence

import sys,math,string

name='Frankie'
name='Meg Eagleton'
#name='Sir A$AP the 2nd'


z1='It\'s so nice to meet you, my dear '
z2='I sense you are both ' #  and [14th word in adjList].'
z3='May our future together have much more '

adj='Adaptable Adventurous Affectionate Courageous Creative Dependable Determined Diplomatic Giving Gregarious Hardworking Helpful Hilarious Honest Non-judgmental Observant Passionate Sensible Sensitive Sincere'
good='Love, Forgiveness, Friendship, Inspiration, Epic Transformations, Wins'
bad='Crime, Disappointment, Disasters, Illness, Injury, Investment Loss'

adjList=adj.split(" ")
goodList=good.split(",")
badList=bad.split(",")
adjDict,goodDict,badDict={},{},{}
for i in range(len(adjList)):
    adjDict[i] = adjList[i]
for i in range(len(goodList)):
    goodDict[i] = goodList[i].strip()
    badDict[i] = badList[i].strip()

consonants='bcdfghjklmnpqrstvwxz'
vowels='aeiouy'


vList,cList=[],[]
for i in range(len(name)):
    if name[i].lower() in vowels:
        print(name[i],file=sys.stderr,end=", ")
        for j in range(len(vowels)):
            if vowels[j] == name[i].lower(): # and not j in vList:
                vList.append(j)
                break
    if name[i].lower() in consonants:
        for j in range(len(consonants)):
            if consonants[j] == name[i].lower() and not j in cList:
                cList.append(j)
                break
print("",file=sys.stderr)
print(vList,file=sys.stderr)

e1=adjDict[cList[0]].lower()
e2=adjDict[cList[1]].lower()
e3=adjDict[cList[2]].lower()
e4=goodDict[vList[0]].lower()
e5=badDict[vList[1]].lower()

print(z1+e1+" "+name+".")
print(z2+e2+" and "+e3+".")
print(z3+e4+" than "+e5+".")
