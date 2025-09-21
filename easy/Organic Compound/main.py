#https://www.codingame.com/ide/puzzle/organic-compound

import math,sys

formula="C2H6"
#formula="CH3CH2CH2CH2CH2CH2OH"
formula="CH3COC8H17"
#formula="CH3COOCH2CH3"
formula="HOCH2CH2OH"
formula="CH3CH2CH2COCH3"


####
carDict={1:"meth",2:'eth',3:'prop',4:'but',5:'pent',6:'hex',7:'hept',8:'oct',9:'non',10:'dec'}

# -ane, -ene, -anol, -anoic acid, -anal, -anone, OTHERS

atomList=""
anzahlList=[];ending="OTHERS"
for atom in ['C','H','O']:
    anzahl=0;atomList=""
    for i in range(len(formula)):
        if not formula[i].isdigit():
            atomList+=formula[i]
        if formula[i] == atom:
            if i+1 < len(formula) and formula[i+1].isdigit():
                if i+2 < len(formula) and formula[i+2].isdigit():
                    anzahl += int(formula[i+1:i+3])
                else:
                    anzahl += int(formula[i+1])
            else:
                anzahl+=1  
    anzahlList.append(anzahl)
print(anzahlList,file=sys.stderr)

if anzahlList[2] == 0:
    if anzahlList[0]*2+2 == anzahlList[1]:
        ending = "ane"
    elif anzahlList[0]*2 == anzahlList[1]:
        ending = "ene"
elif anzahlList[0]*2+2 == anzahlList[1] and atomList[-2:] == "OH" and anzahlList[2] == 1:
    ending = "anol"
elif atomList[-4:] == "COOH" and anzahlList[0]*2 == anzahlList[1] and anzahlList[2] == 2:
    ending = "anoic acid"
elif atomList[-3:] == "CHO" and anzahlList[0]*2 == anzahlList[1] and anzahlList[2] == 1:
    ending = "anal"
elif anzahlList[0]*2 == anzahlList[1] and anzahlList[2] == 1:    
    treffer = atomList[1:-1].find("CO")
    if treffer != -1:
        ending = "anone"

if ending == "OTHERS":
    print(ending)
else:
    print(carDict[anzahlList[0]]+ending)



