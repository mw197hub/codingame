# https://www.codingame.com/ide/puzzle/compiler-cg86-easy-version

import sys,math

expression="1 + 2 + 2 + 2 + 2 - 3" #1


expList=expression.split(" ")
print(expList,file=sys.stderr)
ergList=[];wdhDict={};rechDict={'+':'ADD','-':'SUB'}
rechenzeichen="+"
for exp in expList:
    if exp == "+" or exp == "-":
        rechenzeichen = exp
    else:
        ausdruck=rechDict[rechenzeichen]+" cgx "+exp
        if ausdruck in wdhDict:
            wdhDict[ausdruck]+=1
        else:
            wdhDict[ausdruck]=1
            ergList.append(ausdruck)

for erg in ergList:
    anzahl=wdhDict[erg]
    if anzahl > 1:
        print("REPEAT "+str(anzahl))
    print(erg)
print("EXIT")
#print(ergList,file=sys.stderr)
#print(wdhDict,file=sys.stderr)
    
