# https://www.codingame.com/ide/puzzle/cards-castle

import sys,math

sList=['.../\\...', '../\\/\\..', './\\/\\/\\.', '/\\/\\/\\/\\']
sList=['.../\\.\\/', '\\./\\/\\./', './\\/\\/\\.', '/\\/\\/\\/\\'] #9

#for s in sList:
#    print(s)
richtig=True
for i in range(len(sList)):
    satz = sList[i]
    offen=False
    for s in range(len(satz)):
        if satz[s] == "/":
            offen=True
            if s+1 < len(satz):
                if not satz[s+1] == "\\":
                    richtig=False
            else:
                richtig=False
            if i < len(sList)-1:
                uSatz=sList[i+1]
                if not uSatz[s-1] == "/":
                    richtig=False
                if not uSatz[s] == "\\":
                    richtig=False
        if satz[s] == "\\":
            if not offen:
                richtig=False
            offen=False
            if i < len(sList)-1:
                uSatz=sList[i+1]
                if not uSatz[s-1] == "\\":
                    richtig=False
                if not uSatz[s] == "/":
                    richtig=False
        


    if offen:
        richtig=False

if richtig:
    print("STABLE")
else:
    print("UNSTABLE")
