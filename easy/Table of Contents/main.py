# https://www.codingame.com/ide/puzzle/table-of-contents

import sys,math

lengthofline=40
entryList=['Title1 4', '>Subtitle1 5', '>>Subsubtitle1 5', '>Subtitle2 6', 'Title2 10']

lengthofline=50
entryList=['Sudamerica 1', '>Argentina 5', '>>BuenosAires 8', '>>Cordoba 10', '>Brasil 15', '>>SaoPaulo 20', '>>Fortaleza 25', 'Asia 30', '>Japan 32', '>>Yokohama 35', '>>Tokio 40', '>Iran 42', '>>Teheran 45']


lastPos=0
blank="    "
ebene=[]
for i in range(lengthofline):
    ebene.append(1)

for entry in entryList:
    teile = entry.split(" ")
    pos = teile[0].rfind('>') +1
    nr = ebene[pos]
    ebene[pos] +=1
    leer = lengthofline - (pos * 4) - len(entry) + pos  - len(str(nr))
    leerS=""
    for i in range(leer):
        leerS+="."
    zeile = blank*pos + str(nr)+" " + teile[0][pos:] +leerS+teile[1]
    print(zeile)
    if pos < lastPos:
        for i in range(pos+1,lengthofline):
            ebene[i] = 1
    lastPos = pos
