#  https://www.codingame.com/ide/puzzle/popularity-of-each-activity

import sys,math

def ausgabe(anz,gesamt):
    if anz == 0:
        return "__0%"
    e=str(int(round((anz/gesamt)*100,0)))
    if len(e) ==1:
        return "__"+e+"%"
    if len(e) ==2:
        return "_"+e+"%"
    return "100%"

rowList=[[' ', ' ', '*', ':', ' ', ' ', ' ', ':', ' ', ' '], [' ', ' ', ' ', ':', ' ', ' ', ' ', ':', ' ', ' '], ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-'], [' ', ' ', ' ', ':', '*', ' ', ' ', ':', ' ', ' '], [' ', ' ', ' ', ':', ' ', ' ', ' ', ':', ' ', ' '], [' ', ' ', ' ', ':', ' ', '*', ' ', ':', ' ', ' '], ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-'], [' ', ' ', ' ', ':', ' ', ' ', ' ', ':', ' ', ' '], [' ', ' ', ' ', ':', ' ', '*', ' ', ':', ' ', ' '], [' ', ' ', ' ', ':', ' ', ' ', ' ', ':', ' ', ' ']]


anzahl=0
ergList=[0,0,0,0,0,0,0,0,0]
x,y=0,0
for row in rowList:
    x=0
    if row[0] == '-':
        x=0;y+=1
    else:
        for r in row:
            if r == ':':
                x+=1
            if r == "*":
                anzahl+=1
                pos=x+(y*3)
                ergList[pos] +=1
#print("{}  {}".format(ergList,anzahl))

print("{} attendees".format(anzahl))
for y in range(3):
    out=""
    for x in range(3):
        pos=x+y*3
        out = out + ausgabe(ergList[pos],anzahl) +" "
    print(out[:-1])
