# https://www.codingame.com/ide/puzzle/text-alignment

import sys,math

alignment="LEFT";textList=['Never gonna give you up, never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry, never gonna say goodbye', 'Never gonna tell a lie and hurt you']
alignment="JUSTIFY";textList=['Never gonna give you up, never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry, never gonna say goodbye', 'Never gonna tell a lie and hurt you']



laenge=0
for text in textList:
    if len(text) > laenge:
        laenge = len(text)

for text in textList:
    if alignment == "LEFT":
        print(text)
    elif alignment == "RIGHT":
        leerAnzahl = laenge - len(text) 
        leer =""
        for i in range(leerAnzahl):
            leer+=" "
        print(leer + text)
    elif alignment == "CENTER":
        leerAnzahl = (laenge - len(text))//2 
        leer =""
        for i in range(leerAnzahl):
            leer+=" "
        print(leer + text)
    else:
        textL = text.split(" ")
        leerAnzahl = laenge - len(text) + len(textL) -1
        minL = leerAnzahl // (len(textL) -1)
        leer = ""
        for i in range(minL):
            leer+=" "
        rest = leerAnzahl % (len(textL) -1)
        ausgabe=textL[0]
        for i in range(len(textL)-1):
            ausgabe+=leer
            if i > len(textL) - rest:
                ausgabe+=" "
            ausgabe+=textL[i+1]

        print(ausgabe)


