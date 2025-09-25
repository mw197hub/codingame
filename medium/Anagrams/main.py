# https://www.codingame.com/ide/puzzle/anagrams

import sys,math,string

phrase="ENID OL FNE" #1
#phrase="MOSTLY HARMLESS"
#phrase="MLSOHYTA RMLESS"


abc=string.ascii_uppercase
ausgabe=""
abc2List=[]
abc3List=[]
abc4List=[]
for i in range(len(abc)):
    if (i+1)%2 == 0:
        abc2List.append(abc[i])
    if (i+1)%3 == 0:
        abc3List.append(abc[i])
    if (i+1)%4 == 0:
        abc4List.append(abc[i])
a2List=[]
ausgabe=phrase     
#4
a2List.clear()
pList=ausgabe.split(" ")
phrase="";ausgabe=""
for p in pList:
    a2List.insert(0,len(p))
    phrase+=p
pos=0
for a in a2List:
    ausgabe+=phrase[pos:pos+a]
    ausgabe+=" "
    pos+=a
#3
phrase = ausgabe;ausgabe="";a2List.clear()
for p in phrase:    
    if p in abc4List:
        a2List.append(p)
if len(a2List) > 0:
    ab=a2List.pop()
    a2List.insert(0,ab)
for p in phrase:    
    if p in abc4List:
        ausgabe+=a2List.pop(0)
    else:
        ausgabe+=p   
#2        
phrase = ausgabe;ausgabe="";a2List.clear()
for p in phrase:    
    if p in abc3List:
        a2List.append(p)
if len(a2List) > 0:
    ab=a2List.pop(0)
    a2List.append(ab)
for p in phrase:    
    if p in abc3List:
        ausgabe+=a2List.pop(0)
    else:
        ausgabe+=p
#1
phrase=ausgabe;ausgabe=""
for p in phrase:    
    if p in abc2List:
        a2List.append(p)
for p in phrase:    
    if p in abc2List:
        ausgabe+=a2List.pop()
    else:
        ausgabe+=p
print(ausgabe[:-1])
