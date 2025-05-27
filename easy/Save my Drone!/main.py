# https://www.codingame.com/ide/puzzle/save-my-drone

import sys,math

r=0;rowList=['.@.', '+§+', '^.^']  #1
r=1;rowList=['^#^', '+§+', '#@#']  #2


nameDict={'#':'Block','^':'Thruster','@':'Gyroscope','+':'Fuel','§':'Core'}
akt="";wert=0
ausgabe=""
rowL = ''.join(rowList)


for row in rowL:
    if row in nameDict:
        if akt == nameDict[row]:
            wert+=1
        else:
            if len(akt) > 0:
                if wert > 1:
                    akt = akt+"s"
                if r == 0:
                    ausgabe+=str(wert) + " " + akt + ", "
                else:
                    ausgabe=str(wert) + " " + akt + ", " + ausgabe
            wert=1
            akt= nameDict[row]
if wert > 1:
    akt = akt+"s"
if r == 0:
    ausgabe+=str(wert) + " " + akt + ", "
else:
    ausgabe=str(wert) + " " + akt + ", " + ausgabe
if len(akt) == 0:
    print("Nothing")
else:
    print(ausgabe[:-2])
